import pandas as pd
import numpy as np
from sklearn.compose import ColumnTransformer
from sklearn.pipeline import Pipeline
from sklearn.impute import SimpleImputer
from sklearn.preprocessing import OneHotEncoder
from xgboost import XGBRegressor
from sklearn.model_selection import RandomizedSearchCV
from sklearn.metrics import r2_score
from sklearn.metrics import mean_squared_error
from sklearn.model_selection import train_test_split
#from google.colab import files -> for colab environment

x_train_path=list(files.upload().keys())[0] #for colab environment
# x_train_path= /data/train.csv
x_train_full=pd.read_csv(x_train_path)

y=x_train_full["SalePrice"]
x_train_full.drop(axis=1,columns=["SalePrice"],inplace=True)
x_train, x_valid, y_train, y_valid = train_test_split(x_train_full, y, train_size=0.8, test_size=0.2)


cat_columns=[col for col in x_train_full.columns if x_train_full[col].dtypes=="object" and x_train_full[col].nunique()<15]
num_columns=[col for col in x_train_full.columns if x_train_full[col].dtypes in ["float64","int64"]]
cols=cat_columns+num_columns

x_train=x_train[cols]
x_valid=x_valid[cols]

numerical_transformer = SimpleImputer(strategy='median')
categorical_transformer = Pipeline(steps=[('imputer', SimpleImputer(strategy='constant')),
                                          ('onehot', OneHotEncoder(handle_unknown='ignore'))])

preprocessor = ColumnTransformer(transformers=[('num', numerical_transformer, num_columns),
                                               ('cat', categorical_transformer, cat_columns)])

model_xgb = XGBRegressor()
my_pipeline = Pipeline(steps=[('preprocessor', preprocessor),
                              ('xgb_model', model_xgb)])

gbm_param_grid = {
    'xgb_model__learning_rate': np.arange(.01, 1, .01),
    'xgb_model__max_depth': np.arange(1,21, 1),
    'xgb_model__n_estimators': np.arange(50, 1000, 10),
    'xgb_model__subsample': np.arange(.05, 1, .05),
    'xgb_model__colsample_bytree': np.arange(.1,1.05,.05)
}

randomized_neg_mse = RandomizedSearchCV(estimator=my_pipeline,
                                        param_distributions=gbm_param_grid,
                                        n_iter=10, scoring='neg_mean_squared_error', cv=5,
                                        n_jobs=-1,verbose=10)

randomized_neg_mse.fit(x_train, y_train)

predict_valid=randomized_neg_mse.predict(x_valid)
predict_train=randomized_neg_mse.predict(x_train)

print("Train r^2 score: {}".format(r2_score(y_train,predict_train)))
print("Valid r^2 score: {}".format(r2_score(y_valid,predict_valid)))

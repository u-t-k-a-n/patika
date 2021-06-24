def listeyi_çevir(x):
  x=x[::-1]
  for i in range(len(x)):
    if type(x[i])==list:
      x[i]=x[i][::-1]
  return x

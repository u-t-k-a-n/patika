https://app.patika.dev/egitimler/veri-bilimi-patikasi/sql/Odev8

1.test veritabanınızda employee isimli sütun bilgileri id(INTEGER), name VARCHAR(50), birthday DATE, email VARCHAR(100) olan bir tablo oluşturalım.

2.Oluşturduğumuz employee tablosuna 'Mockaroo' servisini kullanarak 50 adet veri ekleyelim.

3.Sütunların her birine göre diğer sütunları güncelleyecek 5 adet UPDATE işlemi yapalım.

4.Sütunların her birine göre ilgili satırı silecek 5 adet DELETE işlemi yapalım.

1.
CREATE TABLE  IF NOT EXISTS employee(
			id INTEGER,
			name VARCHAR(50),
			birthday DATE,
			email VARCHAR(100));
      
2.

insert into employee (id, name, birthday, email) values (1, 'Pauletta', '2005-04-21', null);

insert into employee (id, name, birthday, email) values (2, 'Kassie', '2002-03-10', 'kdutnall1@4shared.com');

insert into employee (id, name, birthday, email) values (3, 'Huntlee', '1943-11-07', null);

insert into employee (id, name, birthday, email) values (4, 'Bartholomeus', '1979-11-27', 'blenham3@sciencedaily.com');

insert into employee (id, name, birthday, email) values (5, 'Mareah', '1928-03-26', 'mskullet4@mediafire.com');

insert into employee (id, name, birthday, email) values (6, 'Hall', null, null);

insert into employee (id, name, birthday, email) values (7, 'Phineas', '1985-02-11', 'pmcghee6@reuters.com');

insert into employee (id, name, birthday, email) values (8, 'Renell', '1946-12-09', 'rhagergham7@stumbleupon.com');

insert into employee (id, name, birthday, email) values (9, 'Felicdad', '1917-07-26', null);

insert into employee (id, name, birthday, email) values (10, 'Jacquenette', '1914-12-15', null);

insert into employee (id, name, birthday, email) values (11, 'Kaleb', '2018-06-27', 'kgodsafea@scientificamerican.com');

insert into employee (id, name, birthday, email) values (12, 'Livvy', null, 'lcrooksb@unblog.fr');

insert into employee (id, name, birthday, email) values (13, 'Bianka', '1999-03-28', 'bassafc@oakley.com');

insert into employee (id, name, birthday, email) values (14, 'Zaria', null, 'zdockeryd@cam.ac.uk');

insert into employee (id, name, birthday, email) values (15, 'Verge', '1924-07-07', 'vmariote@jimdo.com');

insert into employee (id, name, birthday, email) values (16, 'Penny', '1904-02-25', 'pcowitzf@usatoday.com');

insert into employee (id, name, birthday, email) values (17, 'Edith', '1980-05-30', 'ebowlesg@alexa.com');

insert into employee (id, name, birthday, email) values (18, 'Cassie', '1927-06-04', 'cferaghh@altervista.org');

insert into employee (id, name, birthday, email) values (19, 'Artie', '1944-06-04', null);

insert into employee (id, name, birthday, email) values (20, 'Hailee', '1992-11-10', 'hburdusj@newyorker.com');

insert into employee (id, name, birthday, email) values (21, 'Susann', '1949-06-20', 'sstocksk@wisc.edu');

insert into employee (id, name, birthday, email) values (22, 'Rafa', '1942-10-14', null);

insert into employee (id, name, birthday, email) values (23, 'Theodoric', '1951-11-15', 'tstrowanm@delicious.com');

insert into employee (id, name, birthday, email) values (24, 'Freedman', '1940-05-21', null);

insert into employee (id, name, birthday, email) values (25, 'Steward', '1935-09-06', null);

insert into employee (id, name, birthday, email) values (26, 'Lynsey', null, 'loutridgep@amazonaws.com');

insert into employee (id, name, birthday, email) values (27, 'Kristan', null, 'koshesnanq@jugem.jp');

insert into employee (id, name, birthday, email) values (28, 'Weston', '1920-07-26', 'wcardor@dion.ne.jp');

insert into employee (id, name, birthday, email) values (29, 'Elita', '1927-05-18', null);

insert into employee (id, name, birthday, email) values (30, 'Vinnie', '1903-10-10', 'vsnowdent@who.int');

insert into employee (id, name, birthday, email) values (31, 'Eimile', '1970-10-03', null);

insert into employee (id, name, birthday, email) values (32, 'Leigha', '1976-01-27', 'lwakesv@gnu.org');

insert into employee (id, name, birthday, email) values (33, 'Clemmy', '1989-10-16', null);

insert into employee (id, name, birthday, email) values (34, 'Gabby', '1922-11-02', 'ghadawayx@exblog.jp');

insert into employee (id, name, birthday, email) values (35, 'Pip', '1962-01-16', 'pmichelly@webnode.com');

insert into employee (id, name, birthday, email) values (36, 'Pamella', '1937-11-18', 'pmoynhamz@geocities.jp');

insert into employee (id, name, birthday, email) values (37, 'Kristen', '2001-07-08', 'kmartignon10@nih.gov');

insert into employee (id, name, birthday, email) values (38, 'Culver', '1976-10-09', 'ccoburn11@nydailynews.com');

insert into employee (id, name, birthday, email) values (39, 'Rhonda', '1949-10-02', null);

insert into employee (id, name, birthday, email) values (40, 'Gwyneth', '1984-01-16', null);

insert into employee (id, name, birthday, email) values (41, 'Agace', '1970-09-12', 'aantoniottii14@deviantart.com');

insert into employee (id, name, birthday, email) values (42, 'Bat', '1993-06-16', 'bwillcox15@liveinternet.ru');

insert into employee (id, name, birthday, email) values (43, 'Veda', '1923-02-08', 'vplascott16@linkedin.com');

insert into employee (id, name, birthday, email) values (44, 'Pearce', '1963-11-29', 'pcamps17@nps.gov');

insert into employee (id, name, birthday, email) values (45, 'Richmound', '1994-03-01', 'rortes18@shinystat.com');

insert into employee (id, name, birthday, email) values (46, 'Chicky', '1929-06-09', 'cboyack19@sitemeter.com');

insert into employee (id, name, birthday, email) values (47, 'Vi', '1955-03-15', 'vdegregoli1a@opensource.org');

insert into employee (id, name, birthday, email) values (48, 'Delia', '1946-12-02', null);

insert into employee (id, name, birthday, email) values (49, 'Fidel', null, 'fgreggs1c@deviantart.com');

insert into employee (id, name, birthday, email) values (50, 'Goran', null, 'gtrenholm1d@weather.com');


3.
UPDATE employee
SET id=99, email='paul@etta.com'
WHERE id=1;

UPDATE employee
SET name='Will', birthday='1997-06-22'
WHERE name='Vi';

UPDATE employee
SET birthday='2000-06-22'
WHERE birthday is null;

UPDATE employee
SET name='Saul' , id=77
WHERE email='pcamps17@nps.gov';

UPDATE employee
SET birthday='1960-06-14' , email='pcamps77@nps.gov'
WHERE id=77;

4.
DELETE FROM employee
WHERE id=7;

DELETE FROM employee
WHERE name='Hall';

DELETE FROM employee
WHERE birthday='1943-11-07';

DELETE FROM employee
WHERE email is null;

DELETE FROM employee
WHERE email LIKE '%gov';

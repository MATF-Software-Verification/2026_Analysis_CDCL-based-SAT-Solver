# Analiza CDCL-based SAT Solver-a

Sprovodi se analiza projekta koji je napisan u Python-u za rešavanje SAT problema koristeći CDCL algoritam.

Napomena: fajlovi iz originalnog projekta `dpll_solver.py` i `cnf_data_structure.py` se nigde ne koriste - trebalo bi biti obrisani. `dpll_solver.py` ima smisla jer prikazuje jednostavniji ali manje efikasan DPLL algoritam. Fajl `cnf_data_structure.py` je skroz nepotreban (dupliran kod).

Primenjeni su sledeći alati za analizu projekta:
...

## Integraciono testiranje

Za proveru ispravnosti solver-a sprovedeno je integraciono testiranje.  
Testovi su smešteni u folderu `tests/integration` i sadrže formule u DIMACS CNF formatu.  
Svaki test proverava da li je data formula zadovoljiva (SAT) ili nezadovoljiva (UNSAT).  

Test primeri u folderu `/all_sat` preuzeti su sa sajta:  
https://www.cs.ubc.ca/~hoos/SATLIB/benchm.html

Integracionim testovima pokriveni su sledeći slučajevi:
TODO DODATI JOS TESTOVA
- Obične zadovoljive formule (SAT)
- Obične nezadovoljive formule (UNSAT)
- Specijalni slučajevi:
  - Prazna formula
  - Prazna klauza
  - Formule sa jednom promenljivom

Pokretanje integracionih testova vrši se pomoću skripte `test_integration.py`, koja prolazi kroz sve test fajlove i pokreće solver nad njima.

### Pokretanje testova

Testovi se pokreću naredbom:

```bash
pytest tests/integration
```
### Izlaz testova

Nakon pokretanja testova, `pytest` prikazuje rezultate izvršavanja, uključujući:

- broj uspešno izvršenih testova,
- eventualne greške,
- vreme izvršavanja.

Ovaj pristup omogućava jednostavnu reprodukciju testova i proveru funkcionalnosti kompletnog sistema.

## Jedinično testiranje

Jedinično testiranje ima za cilj proveru ispravnosti pojedinačnih komponenti rešavača izolovano od ostatka sistema.  
Ovaj tip testiranja omogućava rano otkrivanje grešaka i olakšava održavanje i dalji razvoj koda.

Testovi su smešteni u folderu `tests/unit` i organizovani po klasama koje testiraju.

### Pokrivene komponente

#### Klasa `Clause`

Klasa `Clause` predstavlja jednu logičku klauzu u CNF formuli i sadrži najkritičniju logiku za rad solvera. Testovima su pokriveni sledeći aspekti:

- Inicijalizacija klauze i otkrivanje tautologija u fazi preprocesiranja (`preprocess`)
- Provera stanja klauze - da li je jedinična (`is_unit`) ili prazna (`is_empty`)
- Boolean Constraint Propagation (`bcp`) - zadovoljavanje i falsifikovanje literala,
  kao i detekcija konflikta kada klauza ostane bez aktivnih literala
- Vraćanje klauze na prethodno stanje tokom backtrackinga (`restore`)
- Postavljanje nivoa odluke i sortiranje literala (`set_decision_levels`)
- Dohvatanje literala dodeljenih na zadatom nivou odluke (`literal_at_level`)
- Izračunavanje nivoa na koji treba da se vrati pretraga (`get_backtrack_level`)
- Operacija rezolucije dve klauze po zadatom literalu (`resolution_operate`)
- Potpuno restartovanje klauze na početno stanje (`restart`)

Tokom testiranja uočena je jedna nepravilnost - prilikom preprocesiranja, ukoliko je u pitanju tautologična klauza, vrednost se postavljana 1 (tačno) i veličina na 0. Međutim, u konstruktoru se veličina postavlja na dužinu niza klauze nakon poziva funkcije preprocess, i time se "obriše" to što je prilikom preprocesiranja postavljena na 0.

Nakon pokretanja testova komandom:
```bash
pytest tests/unit/test_clause.py -v
```
(opcija -v da bi ispis bio detaljniji)

dobija se sledeći izlaz:

![Izlaz iz terminala nakon pokretanja unit testova za klasu Clause](./images/test_clause_verbose.png)

Svih 28 testova je uspešno prošlo.

### Klasa `Implication_Graph`
Klasa `Implication_Graph` predstavlja graf implikacija koji se gradi tokom pretrage i koristi se za analizu konflikata i backtracking u CDCL algoritmu. Za svaki dodeljeni literal pamti se antecedent (klauza koja je uzrokovala dodelu) i nivo odluke na kom je literal dodeljen.

Testovima su pokriveni sledeći aspekti:

- Dodavanje jednog i više čvorova u graf (`add_node`) i provera ispravnosti upisanih podataka
- Uklanjanje čvorova pozitivnim i negativnim oblikom literala (`remove_node`), kao i pokušaj uklanjanja nepostojećeg čvora
- Provera da uklanjanje jednog čvora ne utiče na ostale čvorove u grafu
- Backtracking na zadati nivo odluke (`backtrack`) - uklanjanje svih literala dodeljenih na višem nivou, uz zadržavanje onih na nižem
- Backtracking nad praznim grafom i višestruki backtracking
- Dohvatanje antecedenta postojećeg i nepostojećeg literala (`get_antecedent`), uključujući slučaj kružnih referenci između čvorova (todo msm da nije potrebno to kruzno po specifikaciji?)

Nakon pokretanja testova komandom:
```bash
pytest tests/unit/test_implication_graph.py -v
```

dobija se sledeći izlaz:

![Izlaz iz terminala nakon pokretanja unit testova za klasu Implication_Graph](./images/test_implication_graph_verbose.png)

Svih 14 testova je uspešno prošlo.

## Pokrivenost koda - Coverage.py
Pokrivenost koda testovima merena je alatom **Coverage.py**, koji prati (po defaultu) koje linije koda su izvršene tokom testiranja.

### Pokrivenost klase `Clause`
Pokrivenost fajla `clause.py` jediničnim testovima merena je komandom:
```bash
pytest tests/unit/test_clause.py --cov=clause --cov-report=html
```
Detaljan izveštaj nalazi se u `coverage/clause_coverage/index.html`.

![Izveštaj pokrivenosti za klasu Clause](./images/clause_coverage.png)

Ukupna pokrivenost iznosi **97%**. Nepokrivene linije su:

- `elif x > m2` grana u metodi `get_backtrack_level` - analizom koda utvrđeno je da je ova grana nedostižna jer Python iterira nad `set` kolekcijom u rastućem redosledu za cele brojeve, pa svaki naredni element uvek zadovoljava uslov `x >= m1`, a nikad samo `x > m2`.
- `print` naredba u metodi `print_info` - ova metoda služi isključivo za debagovanje i nije pozivana u testovima jer njen izlaz nije deo funkcionalnosti koja se testira.

### Pokrivenost klase `Implication_Graph`

Pokrivenost fajla `implication_graph.py` jediničnim testovima merena je komandom:
```bash
pytest tests/unit/test_implication_graph.py --cov=implication_graph --cov-report=html
```
Detaljan izveštaj nalazi se u `coverage/implication_graph_coverage/index.html`.

![Izveštaj pokrivenosti za klasu Implication_Graph](./images/implication_graph_coverage.png)

Ukupna pokrivenost iznosi **100%** - sve linije koda klase `Implication_Graph` su pokrivene jediničnim testovima.


### Pokrivenost integracionih testova

Pokrivenost koda integracionim testovima merena je komandom:
```bash
pytest tests/integration/test_integration.py --cov=cdcl_solver --cov=clause --cov=cnf --cov=dimacs_parser --cov=implication_graph --cov=lazy_clause  --cov-report=html
```

Za razliku od jediničnih testova koji mere pokrivenost pojedinačnih klasa, integracioni testovi pokreću ceo solver, pa ima smisla meriti pokrivenost svih fajlova projekta zajedno.

Detaljan izveštaj nalazi se u `coverage/integration_coverage/index.html`.

![Izveštaj pokrivenosti za integracione testove](./images/integration_coverage.png)

Ukupna pokrivenost iznosi **84%**. Najniža pokrivenost je kod `clause.py` sa svega 48%. Pokrivenost ostalih komponenti je prilično visoka.

### Ukupna pokrivenost

Pokrivenost merena svim testovima zajedno (jediničnim i integracionim):
```bash
pytest tests/ --cov=cdcl_solver --cov=clause --cov=cnf --cov=dimacs_parser --cov=implication_graph --cov=lazy_clause --cov-report=html
```
Detaljan izveštaj nalazi se u `coverage/total_coverage/index.html`.

![Ukupna pokrivenost](./images/total_coverage.png)

Ukupna pokrivenost iznosi **92%**. Kombinovanjem jediničnih i integracionih testova pokrivenost `clause.py` je porasla sa 48% na 97%, što potvrđuje da se jedinični i integracioni testovi međusobno dopunjuju. Jedini fajl sa nešto nižom pokrivenošću je `cdcl_solver.py` (87%), što je i dalje dobar rezultat uzimajući u obzir da je ovo najkompleksniji fajl u projektu. 

Ukupna pokrivenost od 92% predstavlja odličan rezultat i ukazuje da testovi dobro pokrivaju funkcionalnost projekta.

## Statička analiza - Pylint
Pylint je alat za statičku analizu Python koda koji proverava stil, kvalitet i potencijalne greške bez pokretanja programa.  Može se instalirati komandom:
```bash
pip install pylint
```

Analiza je sprovedena nad glavnim fajlom solvera `cdcl_solver.py`, a ukupna ocena iznosi **6.23/10**.

### Kategorije pronađenih problema

Pylint klasifikuje probleme prema prefiksu u oznaci:
- **F** (Fatal) - fatalna greška koja je sprečila Pylint da nastavi analizu
- **E** (Error) - greške koje verovatno uzrokuju probleme pri izvršavanju
- **W** (Warning) - upozorenja na potencijalne greške
- **C** (Convention) - kršenje konvencija stila pisanja koda
- **R** (Refactor) - predlozi za poboljšanje strukture koda

Komanda za pokretanje:
```bash
pylint CDCL-based-SAT-Solver/cdcl_solver.py
```
izlaz:

![Izlaz](./images/pylint_izlaz.png)

Opisi problema su prilično informativni tako da se može lako razumeti gde je nastao koji problem.
### Pronađeni problemi

**Stilski problemi (C)** su najbrojniji. Dominiraju `trailing-whitespace` upozorenja - višak belina na kraju linija koda, kao i nekoliko `line-too-long` upozorenja gde linije prelaze dozvoljenih 100 karaktera. Pored toga, nedostaju docstringovi (tekstualni opisi) za modul, klasu i sve metode (`missing-module-docstring`, `missing-class-docstring`, `missing-function-docstring`). Takođe je uočen pogrešan redosled importa - standardne biblioteke (`random`, `time`) treba da budu importovane pre biblioteka trećih strana.

**Upozorenja (W)** ukazuju na tri nekorišćena importa: `numpy`, `random` i `Lazy_Clause` su importovani ali se nigde ne koriste u fajlu. Prisutna su i dva `fixme` upozorenja koja odgovaraju TODO komentarima u kodu - njihovo prisustvo u finalnoj verziji koda nije poželjno jer ukazuje na nedovršenu implementaciju i može zbuniti buduće čitaoce koda.

**Predlozi za refaktorisanje (R)** ukazuju na strukturne probleme: klasa `CDCL_Solver` ima previše atributa (16, dok je preporučeno maksimalno 7), glavna metoda solvera ima previše grana (19) i previše naredbi (68), što ukazuje na visoku složenost koja otežava čitanje i testiranje. Takođe je uočen `no-else-return` - nepotrebna `else` grana nakon `return` naredbe.

**Imenovanje** - ime klase `CDCL_Solver` ne prati Python konvenciju PascalCase (trebalo bi biti `CDCLSolver`).

### Zaključak

Većina pronađenih problema su stilske prirode i ne utiču na ispravnost programa. 
Međutim, upozorenja o nekorišćenim importima i previsokoj složenosti glavne metode solvera su vredni pažnje - nekorišćeni importi povećavaju nepotrebne zavisnosti, a visoka složenost glavne metode direktno otežava testiranje i održavanje.

TODO pokrenuti eventualno nad nekim drugim fajlom


## Profajliranje - cProfile
ugradjen u python
komanda za pokretanje:

python -m cProfile [-o output_file] [-s sort_order] myscript.py


python3 -m cProfile -o profileFile.prof -s cumulative ./CDCL-based-SAT-Solver/main.py -i ./tests/integration/unsat.cnf

sad fajl koji sam dobila profileFile.prof ubacim u snakeviz ili pyprof2calltree da bih bolje vizualizovala

http://pypi.org/project/pyprof2calltree/
instaliram pyprof2calltree i qcachegrind

pyprof2calltree -i profileFile.prof -k

TODO

izadje mi prozor koji mi nije jasan - vrv treba pokrenuti cProfile nad nekim drugim fajlom

## Analiza složenosti koda - Radon

Radon je Python alat koji izračunava različite metrike koda. Podržane metrike su:

- **Raw metrike** - broj linija izvornog koda, linija komentara i praznih linija
- **Ciklomatska složenost** - meri broj nezavisnih putanja kroz kod
- **Halstead metrike** - mere složenost na osnovu operatora i operanada u kodu
- **Maintainability Index** - metrika koja ocenjuje održivost koda vrednošću od 0 do 100

Može se instalirati komandom:
```bash
pip install radon
```

Radon ima više komandi, od kojih svaka meri drugačiju metriku:
- `raw` - raw metrike
- `cc` - ciklomatska složenost
- `hal` - Halstead metrike
- `mi` - Maintainability Index

Opšti oblik komande je:
```bash
radon [opcija] folder [-a] [-s]
```
gde `-a` prikazuje prosečnu složenost na kraju, a `-s` prikazuje ocenu (A, B, C...) uz svaki blok.

### Ciklomatska složenost

Ciklomatska složenost meri broj nezavisnih putanja kroz kod - što je veći broj, kod je teže testirati i održavati.

Analiza je sprovedena nad svim fajlovima projekta komandom:
```bash
radon cc ./CDCL-based-SAT-Solver -a -s > radon_output.txt
```
Detaljan izveštaj sa složenošću svake metode i klase sačuvan je u fajlu `radon_output.txt`.

Ukupno je analizirano 103 bloka (klase, funkcije i metode), a prosečna složenost iznosi **B (5.62)**, što je generalno prihvatljivo. Međutim, izdvajaju se dva kritična slučaja:

- `CDCL_Solver.solve` u `cdcl_solver.py` dobila je ocenu **E (35)** - ovo je glavna metoda solvera koja implementira celokupan CDCL algoritam i sadrži veliki broj grananja, što je u skladu sa Pylint nalazom o previše grana i naredbi u istoj metodi.

- `Lazy_Clause.bcp` u `cnf_data_structure.py` dobila je ocenu **E (31)**, a ista metoda u zasebnom fajlu `lazy_clause.py` ocenu **D (29)**. Ova metoda ima tri glavne grane u zavisnosti od veličine klauze, sa dodatnim grananjem unutar svake.

Ostatak koda je većinom ocenjen ocenama A i B, što ukazuje da su ostale komponente projekta dobro strukturirane. Visoka složenost je koncentrisana u metodama koje implementiraju centralnu logiku algoritma, što je delimično očekivano s obzirom na prirodu CDCL algoritma.
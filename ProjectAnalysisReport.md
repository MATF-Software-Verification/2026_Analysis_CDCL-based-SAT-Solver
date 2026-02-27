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
- Provera stanja klauze — da li je jedinična (`is_unit`) ili prazna (`is_empty`)
- Boolean Constraint Propagation (`bcp`) — zadovoljavanje i falsifikovanje literala,
  kao i detekcija konflikta kada klauza ostane bez aktivnih literala
- Vraćanje klauze na prethodno stanje tokom backtrackinga (`restore`)
- TODO dodati jos ?

Tokom testiranja uočena je jedna nepravilnost - prilikom preprocesiranja, ukoliko je u pitanju tautologična klauza, vrednost se postavljana 1 (tačno) i veličina na 0. Međutim, u konstruktoru se veličina postavlja na dužinu niza klauze nakon poziva funkcije preprocess, i time se "obriše" to što je prilikom preprocesiranja postavljena na 0.

### Klasa `Implication_Graph`
Klasa `Implication_Graph` predstavlja graf implikacija koji se gradi tokom pretrage i koristi se za analizu konflikata i backtracking u CDCL algoritmu. Za svaki dodeljeni literal pamti se antecedent (klauza koja je uzrokovala dodelu) i nivo odluke na kom je literal dodeljen.

Testovima su pokriveni sledeći aspekti:

- Dodavanje jednog i više čvorova u graf (`add_node`) i provera ispravnosti upisanih podataka
- Uklanjanje čvorova pozitivnim i negativnim oblikom literala (`remove_node`), kao i pokušaj uklanjanja nepostojećeg čvora
- Provera da uklanjanje jednog čvora ne utiče na ostale čvorove u grafu
- Backtracking na zadati nivo odluke (`backtrack`) — uklanjanje svih literala dodeljenih na višem nivou, uz zadržavanje onih na nižem
- Backtracking nad praznim grafom i višestruki backtracking
- Dohvatanje antecedenta postojećeg i nepostojećeg literala (`get_antecedent`), uključujući slučaj kružnih referenci između čvorova (todo msm da nije potrebno to kruzno po specifikaciji?)

#### Klasa `Lazy_Clause`
koristi postojecu implication graph klasu

### Klasa ... (dodati ostale klase)

### Pokretanje testova

Testovi se pokreću naredbom:

```bash
pytest tests/unit
```
### Izlaz testova

Nakon pokretanja testova, `pytest` prikazuje rezultate izvršavanja, uključujući:

- broj uspešno izvršenih testova,
- eventualne greške,
- vreme izvršavanja.

TODO dodati sliku nakon pokretanja

## Pokrivenost koda
TODO - videti da l da radim sa svim testovima ili odvojeno unit/integration
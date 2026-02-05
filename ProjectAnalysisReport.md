# Analiza CDCL-based SAT Solver-a

Sprovodi se analiza projekta koji je napisan u Python-u za rešavanje SAT problema koristeći CDCL algoritam.


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
pytest test_integration.py
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

Jedinični testovi obuhvatiće proveru ispravnosti ...
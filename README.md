# Analiza CDCL-based SAT Solver-a

## Opis projekta

Analiziran je CDCL-based SAT solver napisan u Python-u, koji rešava SAT problem koristeći CDCL (Conflict-Driven Clause Learning) algoritam.

- Originalni repozitorijum: https://github.com/thtran97/CDCL-based-SAT-Solver
- Grana: `main`
- Commit: `e61ba5d2d6c74760386c20d27f0c0f428aaafdc2`

Solver je dodat kao git submodul u folderu `CDCL-based-SAT-Solver`.

Detaljan opis analize i rezultati svakog korišćenog alata nalaze se u fajlu [ProjectAnalysisReport.md](ProjectAnalysisReport.md).

## Build
Primer pokretanja programa iz korena repozitorijuma:
```bash
python3 CDCL-based-SAT-Solver/main.py -i putanja_do_ulaznog_fajla.cnf
```

Program prima `.cnf` fajl u DIMACS formatu kao ulaz. Primeri ulaznih fajlova nalaze se u folderu `tests/integration`.

## Korišćeni alati i reprodukcija rezultata

### Integraciono testiranje - pytest
```bash
pip install pytest
chmod +x integration_testing/run_integration_tests.sh
./integration_testing/run_integration_tests.sh
```

### Jedinično testiranje - pytest
```bash
pip install pytest
chmod +x unit_testing/run_unit_tests.sh
./unit_testing/run_unit_tests.sh
```

### Pokrivenost koda - Coverage.py
```bash
pip install pytest-cov
chmod +x coverage/run_coverage.sh
./coverage/run_coverage.sh
```

### Statička analiza - Pylint
```bash
pip install pylint
chmod +x pylint/run_pylint.sh
./pylint/run_pylint.sh
```

### Analiza složenosti - Radon
```bash
pip install radon
chmod +x radon/run_radon.sh
./radon/run_radon.sh
```

### Profajliranje - cProfile i pyprof2calltree
```bash
pip install pyprof2calltree
brew install qcachegrind  # Mac
# sudo apt install kcachegrind  # Linux
chmod +x profiling/run_profiling.sh
./profiling/run_profiling.sh
```


## Zaključci

- Solver ispravno rešava SAT i UNSAT formule, što je potvrđeno integracionim i jediničnim testovima sa ukupnom pokrivenošću od 93%.
- Glavna metoda `CDCL_Solver.solve` ima izuzetno visoku ciklomatsku složenost (ocena E, vrednost 35), što otežava testiranje i održavanje.
- Profajliranje je pokazalo da `lazy_clause.bcp` dominira vremenom izvršavanja sa 39076 poziva na velikom UNSAT primeru - svako poboljšanje ove funkcije direktno bi ubrzalo ceo solver.
- Benchmark testiranje je potvrdilo da `large_unsat` (100 promenljivih, 160 klauza) traje značajno duže od `large_sat` (20 promenljivih, 91 klauza) - 107ms naspram 10ms. Ovo je posledica i razlike u veličini formule i same prirode UNSAT problema, gde solver mora da istraži ceo prostor pretrage pre nego što donese zaključak.
- Pylint je otkrio nekorišćene importe (`numpy`, `random`, `Lazy_Clause`) koji su uklonjeni u okviru formatiranja koda.
- Fajlovi `cnf_data_structure.py` i `dpll_solver.py` iz originalnog projekta nisu korišćeni i trebalo bi ih obrisati.

## Autor
Staša Đorđević 1007/2025

Projekt je urađen u okviru kursa **Verifikacija softvera** na Matematičkom fakultetu, Univerzitet u Beogradu.
# Analiza CDCL-based SAT Solver-a

## Opis projekta

Cilj projekta je analiza CDCL-based SAT solver-a i primena alata za verifikaciju softvera. 

Projekt je urađen u okviru kursa **Verifikacija softvera** na Matematičkom fakultetu, Univerzitet u Beogradu.

## SAT Solver
Solver je dodat kao submodule: CDCL-based-SAT-Solver  
Originalni repozitorijum: https://github.com/thtran97/CDCL-based-SAT-Solver

## Build
Primer pokretanja programa iz korena repozitorijuma:
```bash
python3 CDCL-based-SAT-Solver/main.py -i putanja_do_ulaznog_fajla.cnf
```

Program prima `.cnf` fajl u DIMACS formatu kao ulaz. Primeri ulaznih fajlova nalaze se u folderu `tests/integration`.

```
...
## Autor
Staša Đorđević 1007/2025

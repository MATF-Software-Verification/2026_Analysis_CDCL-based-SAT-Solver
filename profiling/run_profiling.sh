#!/bin/bash
python3 -m cProfile -s cumulative -o profiling/profileFile.prof ./CDCL-based-SAT-Solver/main.py -i ./tests/integration/large_unsat.cnf
pyprof2calltree -i profiling/profileFile.prof -k
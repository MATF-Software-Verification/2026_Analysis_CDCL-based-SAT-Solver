import pytest
import sys
import os
project_root = os.path.abspath(os.path.join(os.path.dirname(__file__), "../../CDCL-based-SAT-Solver"))
sys.path.insert(0, project_root)

from cdcl_solver import CDCL_Solver

all_sat_folder = os.path.join(os.path.dirname(__file__), "all_sat")
cnf_folder = os.path.join(os.path.dirname(__file__), ".")

def test_benchmark_large_sat(benchmark):
    file_path = os.path.join(all_sat_folder, "uf20-01.cnf")
    def run():
        solver = CDCL_Solver(file_path, verbose=False)
        return solver.solve()()
    result = benchmark(run)
    assert result == 1

def test_benchmark_unsat(benchmark):
    file_path = os.path.join(cnf_folder, "unsat.cnf")
    def run():
        solver = CDCL_Solver(file_path, verbose=False)
        return solver.solve()()
    result = benchmark(run)
    assert result == -1

def test_benchmark_one_var_sat(benchmark):
    file_path = os.path.join(cnf_folder, "one_var_sat.cnf")
    def run():
        solver = CDCL_Solver(file_path, verbose=False)
        return solver.solve()()
    result = benchmark(run)
    assert result == 1

def test_benchmark_one_var_unsat(benchmark):
    file_path = os.path.join(cnf_folder, "one_var_unsat.cnf")
    def run():
        solver = CDCL_Solver(file_path, verbose=False)
        return solver.solve()()
    result = benchmark(run)
    assert result == -1

def test_benchmark_large_unsat(benchmark):
    file_path = os.path.join(cnf_folder, "large_unsat.cnf")
    def run():
        solver = CDCL_Solver(file_path, verbose=False)
        return solver.solve()()
    result = benchmark(run)
    assert result == -1

def test_benchmark_chain_implications(benchmark):
    file_path = os.path.join(cnf_folder, "chain_implications.cnf")
    def run():
        solver = CDCL_Solver(file_path, verbose=False)
        return solver.solve()()
    result = benchmark(run)
    assert result == 1

def test_benchmark_unit_clause_sat(benchmark):
    file_path = os.path.join(cnf_folder, "unit_clause_sat.cnf")
    def run():
        solver = CDCL_Solver(file_path, verbose=False)
        return solver.solve()()
    result = benchmark(run)
    assert result == 1
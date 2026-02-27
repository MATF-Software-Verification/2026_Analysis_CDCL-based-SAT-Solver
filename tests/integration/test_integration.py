import pytest
import sys
import os
project_root = os.path.abspath(os.path.join(os.path.dirname(__file__), "../../CDCL-based-SAT-Solver"))
sys.path.insert(0, project_root)

from cdcl_solver import CDCL_Solver

all_sat_folder = os.path.join(os.path.dirname(__file__), "all_sat")
cnf_folder = os.path.join(os.path.dirname(__file__), ".")

def test_all_sat():
    for cnf_file in os.listdir(all_sat_folder):
        if cnf_file.endswith(".cnf"):
            file_path = os.path.join(all_sat_folder,cnf_file)
            solver = CDCL_Solver(file_path,verbose=True)
            result = solver.solve()() # pokrece solve koji vraca self.formula.get_value, pa uzimamo valuaciju formule 
            print(f"File {cnf_file} solved with result: {result}")
            assert result==1,f"File {cnf_file} expected SAT, got {result}"

def test_unsat():
    file_path = os.path.join(cnf_folder, "unsat.cnf")
    solver = CDCL_Solver(file_path,verbose=True)
    result = solver.solve()()
    print(f"File {file_path} solved with result: {result}")
    assert result==-1,f"File {file_path} expected SAT, got {result}"

# def test_empty_clause():
#     file_path = "empty_clause.cnf"
#     solver = CDCL_Solver(file_path,verbose=True)
#     result = solver.solve()()
#     print(f"File {file_path} solved with result: {result}")
#     assert result==-1,f"File {file_path} expected SAT, got {result}"

def test_empty_formula():
    file_path = os.path.join(cnf_folder, "empty_formula.cnf")
    solver = CDCL_Solver(file_path,verbose=True)
    result = solver.solve()()
    print(f"File {file_path} solved with result: {result}")
    assert result==1,f"File {file_path} expected SAT, got {result}"

def test_one_var_sat():
    file_path = os.path.join(cnf_folder, "one_var_sat.cnf")
    solver = CDCL_Solver(file_path,verbose=True)
    result = solver.solve()()
    print(f"File {file_path} solved with result: {result}")
    assert result==1,f"File {file_path} expected SAT, got {result}"

def test_one_var_unsat():
    file_path = os.path.join(cnf_folder, "one_var_unsat.cnf")
    solver = CDCL_Solver(file_path,verbose=True)
    result = solver.solve()()
    print(f"File {file_path} solved with result: {result}")
    assert result==-1,f"File {file_path} expected SAT, got {result}"

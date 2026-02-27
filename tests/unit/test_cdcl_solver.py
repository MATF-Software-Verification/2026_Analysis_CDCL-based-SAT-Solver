import pytest
import sys
import os
project_root = os.path.abspath(os.path.join(os.path.dirname(__file__), "../../CDCL-based-SAT-Solver"))
sys.path.insert(0, project_root)

from cdcl_solver import CDCL_Solver


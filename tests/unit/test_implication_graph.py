import pytest
import sys
import os
project_root = os.path.abspath(os.path.join(os.path.dirname(__file__), "../../CDCL-based-SAT-Solver"))
sys.path.insert(0, project_root)

from implication_graph import Implication_Graph

def test_add_one_node():
    g = Implication_Graph()
    g.add_node(-1, None, 0)
    assert g.graph[-1]==[None,0]
    assert -1 in g.assigned_vars

def test_add_two_nodes():
    g = Implication_Graph()
    g.add_node(1,None,0)
    g.add_node(2,None,0)
    assert g.graph[1]==[None,0]
    assert g.graph[2]==[None,0]
    assert 1 in g.assigned_vars
    assert 2 in g.assigned_vars

def test_remove_node_from_empty():
    g = Implication_Graph()
    g.remove_node(5)
def test_remove_node_positive_lit():
    g = Implication_Graph()
    g.add_node(4,None,0)
    g.remove_node(4)
    assert 4 not in g.graph
    assert 4 not in g.assigned_vars
def test_remove_node_negative_lit():
    g=Implication_Graph()
    g.add_node(1,None,0)
    g.remove_node(-1)
    assert 1 not in g.graph
    assert 1 not in g.assigned_vars
def test_remove_node_others():
    g=Implication_Graph()
    g.add_node(1,None,0)
    g.add_node(2,None,0)
    g.remove_node(-1)
    assert 1 not in g.assigned_vars
    assert 2 in g.assigned_vars
    assert 1 not in g.graph
    assert 2 in g.graph

def test_backtrack_basic():
    g=Implication_Graph()
    g.add_node(1,None,0)
    g.add_node(3,None,1)
    g.add_node(-2,None,2)
    g.backtrack(1)
    assert 1 in g.assigned_vars
    assert 3 in g.assigned_vars
    assert -2 not in g.assigned_vars
    g.backtrack(0)
    assert 3 not in g.assigned_vars
    assert 1 in g.assigned_vars

def test_backtrack_empty():
    g=Implication_Graph()
    g.backtrack(10)

def test_double_backtrack():
    g=Implication_Graph()
    g.add_node(-2,None,2)
    g.add_node(3,None,11)
    g.backtrack(2)
    assert 3 not in g.assigned_vars
    g.backtrack(2)
    assert 3 not in g.assigned_vars
    assert -2 in g.assigned_vars

def test_backtrack_removeAll():
    g=Implication_Graph()
    g.add_node(-2,None,2)
    g.add_node(3,None,11)
    g.add_node(1,[-2],1)
    g.backtrack(0)
    assert 3 not in g.assigned_vars
    assert 1 not in g.assigned_vars
    assert -2 not in g.assigned_vars

def test_get_antecedent_basic():
    g=Implication_Graph()
    g.add_node(1,None,0)
    g.add_node(2,1,1)
    assert g.get_antecedent(2)==1
    assert g.get_antecedent(1) is None

def test_get_antecedent_none():
    g=Implication_Graph()
    g.add_node(1,None,2)
    g.add_node(2,None,1)
    assert g.get_antecedent(2) is None
    assert g.get_antecedent(1) is None

def test_get_antecedent_notExists():
    g=Implication_Graph()
    g.add_node(1,2,2)
    g.add_node(2,1,1)
    assert g.get_antecedent(235) is None 

def test_get_antecedent_circle():
    g=Implication_Graph()
    g.add_node(1,2,2)
    g.add_node(2,1,1)
    assert g.get_antecedent(1)==2
    assert g.get_antecedent(2)==1
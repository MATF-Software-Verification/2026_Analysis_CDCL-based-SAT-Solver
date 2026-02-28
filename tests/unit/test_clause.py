import pytest
import sys
import os
project_root = os.path.abspath(os.path.join(os.path.dirname(__file__), "../../CDCL-based-SAT-Solver"))
sys.path.insert(0, project_root)

from clause import Clause

def test_init():
    c = Clause([3,1,2])
    assert c.size==3
    assert c.value==0
    assert c.clause==[3,1,2]
    assert c.decision_level==[-1,-1,-1]


#UOCENA JEDNA GRESKA!! postavlja se size nakon preprocess
def test_preprocess():
    c = Clause([3,1,2,-1])
    c.preprocess() # ako se ne pozove preprocess ovde bice size 4 iako u konstruktoru pozivamo preprocess
    assert c.size==0
    assert c.value==1
    assert c.clause==[3,1,2,-1]

def test_isUnit_false():
    c = Clause([1,2,3])
    assert c.is_unit()==False
def test_isUnit_true():
    c = Clause([1])
    assert c.is_unit()==True

def test_isEmpty_false():
    c = Clause([1,2,3])
    assert c.is_empty()==False
def test_isEmpty_true():
    c = Clause([])
    assert c.is_empty()==True


def test_bcp_positive_lit():
    c = Clause([3,1,-2])
    res = c.bcp(1,0)
    assert res==1
    assert c.size==0
    assert c.decision_level==[0,0,0]
def test_bcp_negative_lit():
    c = Clause([3,1,-2])
    assert c.size==3
    res = c.bcp(-1,0)
    assert res==0
    assert c.size==2
def test_bcp_negative_lit_unsat():
    c = Clause([1])
    res = c.bcp(-1,0)
    assert res==-1
    assert c.size==0
    assert c.value==-1
def test_bcp_unrelated_literal():
    c = Clause([3,1,-2])
    res = c.bcp(23,0)
    assert res==0
    assert c.size==3
    assert c.value==0

def test_restore_after_bcp_sat():
    c = Clause([3,1,-2])
    c.bcp(1,2)
    assert c.value==1
    assert c.size==0
    c.restore(1)
    assert c.size==3
    assert c.value==0
def test_restore_after_bcp_undef():
    c = Clause([3,1,-2])
    c.bcp(-3,5)
    assert c.size==2
    assert c.value==0
    c.restore(4)
    assert c.size==3
    assert c.value==0
def test_restore_to_higher_level():
    c = Clause([3,1,-2])
    c.bcp(-1,1)
    c.restore(10)
    assert c.size==2

def test_set_dec_levels():
    c = Clause([3,-1,2])
    c.set_decision_levels([1,2,0])
    assert c.decision_level == [2,1,0]
    assert c.clause == [-1,3,2]
def test_set_dec_levels_singe():
    c = Clause([-1])
    c.set_decision_levels([0])
    assert c.decision_level==[0]
    assert c.clause==[-1]
def test_set_dec_levels_sorting():
    c = Clause([3,-1,2])
    c.set_decision_levels([2,6,1])
    assert c.decision_level==[6,2,1]


def test_literal_at_level_basic():
    c = Clause([3,-1,2])
    c.decision_level=[1,2,3]
    assert c.literal_at_level(1)==[3]
    assert c.literal_at_level(2)==[-1]
    assert c.literal_at_level(3)==[2]
def test_literal_at_level_double():
    c = Clause([3,-1,2])
    c.decision_level=[1,1,3]
    assert c.literal_at_level(1)==[3,-1] or c.literal_at_level(1)==[-1,3]
    assert c.literal_at_level(3)==[2]
def test_literal_at_level_empty():
    c = Clause([3,-1,2])
    c.decision_level=[1,2,3]
    assert c.literal_at_level(11)==[]

def test_get_backtrack_level_basic():
    c = Clause([3,-1,2])
    c.decision_level=[1,1,3]
    assert c.get_backtrack_level()==1
def test_get_backtrack_level_nolevels():
    c = Clause([3,-1,2])
    assert c.get_backtrack_level()==-2
def test_get_backtrack_level_single():
    c = Clause([1])
    c.decision_level=[3]
    assert c.get_backtrack_level()==2

def test_resolution_operate_basic():
    c1 = Clause([3,-1,2])
    c2 = Clause([1,5])
    res = c1.resolution_operate(c2,-1)
    assert 3 in res.clause
    assert 2 in res.clause
    assert 5 in res.clause
    assert 1 not in res.clause
    assert -1 not in res.clause
def test_resolution_operate_empty_res():
    c1 = Clause([-1])
    c2 = Clause([1])
    assert c1.resolution_operate(c2,-1).clause==[]
def test_resolution_operate_dup():
    c1 = Clause([3,-1,2])
    c2 = Clause([1,2])
    res = c1.resolution_operate(c2,-1)
    assert res.clause.count(2)==1


def test_restart_size():
    c = Clause([3,-1,2])
    c.bcp(3,0)
    assert c.size==0
    c.restart()
    assert c.size==3
def test_restart_value():
    c = Clause([3,-1,2])
    c.bcp(3,0)
    assert c.value==1
    c.restart()
    assert c.value==0
def test_restart_dec_levels():
    c = Clause([3,-1,2])
    c.decision_level=[1,2,3]
    c.restart()
    assert c.decision_level==[-1,-1,-1]

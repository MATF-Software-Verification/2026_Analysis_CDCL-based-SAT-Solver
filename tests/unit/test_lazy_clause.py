import pytest
import sys
import os
project_root = os.path.abspath(os.path.join(os.path.dirname(__file__), "../../CDCL-based-SAT-Solver"))
sys.path.insert(0, project_root)

from lazy_clause import Lazy_Clause

# def test_init():
#     lazyC = Lazy_Clause([3,-1,2])
#     assert lazyC.value==0
#     assert lazyC.size==3
#     assert lazyC.decision_level==[-1,-1,-1]
#     assert (lazyC.refA==-1 and lazyC.refB==2) or \
#             (lazyC.refA==-1 and lazyC.refB==3) or \
#             (lazyC.refA==2 and lazyC.refB==-1) or \
#             (lazyC.refA==2 and lazyC.refB==3) or \
#             (lazyC.refA==3 and lazyC.refB==-1) or \
#             (lazyC.refA==3 and lazyC.refB==2)
    
# def test_init_single():
#     lazyC = Lazy_Clause([1])
#     assert lazyC.value==0
#     assert lazyC.size==1
#     assert lazyC.decision_level==[-1]
#     assert (lazyC.refA==1 and lazyC.refB==1)

# def test_init_refs_are_different():
#     lazyC = Lazy_Clause([3,1,-2])
#     assert lazyC.refA!=lazyC.refB
# def test_init_refs_in_clause():
#     lazyC = Lazy_Clause([3,1,-2])
#     assert lazyC.refA in lazyC.clause
#     assert lazyC.refB in lazyC.clause

# def test_isUnit_false():
#     lazyC = Lazy_Clause([3,-1,2])
#     assert lazyC.is_unit()==False
# def test_isUnit_true():
#     lazyC = Lazy_Clause([1])
#     assert lazyC.is_unit()==True

# #nije mi jasan deo kod update??

# def test_remove_refs_basic():
#     lazyC = Lazy_Clause([3,-1,2])
#     lazyC.remove_refs()
#     assert lazyC.refA is None
#     assert lazyC.refB is None

# #zipujemo clause i dec.l i sortiramo po dec.l opadajuce - tako nam ide redosled u klauzi
# def test_set_dec_levels():
#     lazyC = Lazy_Clause([3,-1,2])
#     lazyC.set_decision_levels([1,2,0])
#     assert lazyC.decision_level == [2,1,0]
#     assert lazyC.clause == [-1,3,2]

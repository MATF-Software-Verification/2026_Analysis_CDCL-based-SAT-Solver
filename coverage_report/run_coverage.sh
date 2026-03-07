#!/bin/bash
pytest tests/ --cov=cdcl_solver --cov=clause --cov=cnf --cov=dimacs_parser --cov=implication_graph --cov=lazy_clause --cov-report=html:coverage_report/htmlcov
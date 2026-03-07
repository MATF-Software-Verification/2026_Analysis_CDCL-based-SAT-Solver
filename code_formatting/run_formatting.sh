#!/bin/bash
cp -r ./CDCL-based-SAT-Solver /tmp/CDCL-based-SAT-Solver_formatted
black /tmp/CDCL-based-SAT-Solver_formatted

diff -ru ./CDCL-based-SAT-Solver /tmp/CDCL-based-SAT-Solver_formatted > code_formatting/formatting.patch
rm -rf /tmp/CDCL-based-SAT-Solver_formatted

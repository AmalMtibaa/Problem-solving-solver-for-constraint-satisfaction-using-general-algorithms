# Problem-solving-solver-for-constraint-satisfaction-using-general-algorithms

This project was part of Artifical intelligence assignement where we created a general algorithm that can solve N-Queens, Sudoku and ColoringMap problems using Python

#
We have created a csp class for the formalization of satisfaction problems of constraints. This class is represented by a set of variables. We associate to each variable a set of domains and constraints. 
The code of this class is in csp.py et cspUtil.py


Our application selects the problem from existing files containing the
formalization of the CSP. We have under the folder CSP in the project the files
N-Queens, Sudoku and ColoringMap which contain each one, a file for the constraints, a file for the variables and a file for the domains.

Variables are written on a single line separated by a space.
The domain of each variable is written on a single line separated by a space.
The constraints of each variable are written each in a line of the
form:
<Var1_Name> <operator> <Var2_Name>


the developed operators are: <,>, <=,> =, =,! =, if (for 8 queens) The constraints of the variables are separated by a line containing "##". We have developed 3 algorithms for solving these problems that are : Backtracking, Forward check and Forward check + Arc consistency
AC3

## Collaborators

Amal Mtibaa

Med Wassim Riahi

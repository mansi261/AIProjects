"""
We the undersigned promise that we have in good faith attempted to follow the principles of pair programming.
Although we were free to discuss ideas with others, the implementation is our own.
We have shared a common workspace (possibly virtually) and taken turns at the keyboard for the majority of the work that we are submitting.
Furthermore, any non programming portions of the assignment were done independently.
We recognize that should this not be the case, we will be subject to penalties as outlined in the course syllabus.
Paired Programmer_1: Rutuja Medhekar
Paired Programmer_2: Mansi Vyas
"""
'''
Constraint propagation

'''


def AC3(csp, queue=None, removals=None):
    """
    Initialize a queue for binary constraints between two variables.
    """
    if queue is None:
        queue = {(Xi, Xk) for Xi in csp.variables for Xk in csp.neighbors[Xi]}
    csp.support_pruning()
    

    """
    Continue till queue is not empty.
    dequeue the variables whose arcs' constraints are to be satisfied.
    """
    while queue:
        (Xi, Xj) = queue.pop()
    #Call revise function if domains of variables are updated
        if revise(csp, Xi, Xj, removals):
            if not csp.curr_domains[Xi]:
                return False,
            for Xk in csp.neighbors[Xi]:
                if Xk != Xj:
                    queue.add((Xk, Xi))
    return True 

def revise(csp, Xi, Xj,removals):
    """Return true if we remove a value.
    """
    revised = False
    for x in csp.curr_domains[Xi][:]:
       
        conflict = True
        for y in csp.curr_domains[Xj]:
            if csp.constraints(Xi, x, Xj, y):
                conflict = False

            if not conflict:
                break
        if conflict:
            csp.prune(Xi, x, removals)
            revised = True
    return revised

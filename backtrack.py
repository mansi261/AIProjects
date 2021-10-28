"""
We the undersigned promise that we have in good faith attempted to follow the principles of pair programming.
Although we were free to discuss ideas with others, the implementation is our own.
We have shared a common workspace (possibly virtually) and taken turns at the keyboard for the majority of the work that we are submitting.
Furthermore, any non programming portions of the assignment were done independently.
We recognize that should this not be the case, we will be subject to penalties as outlined in the course syllabus.
Paired Programmer_1: Rutuja Medhekar
Paired Programmer_2: Mansi Vyas

"""
from csp_lib.backtrack_util import first_unassigned_variable, no_inference, unordered_domain_values
def backtracking_search(csp, select_unassigned_variable=first_unassigned_variable,
                        order_domain_values=unordered_domain_values, inference=no_inference):
    def backtrack(assignment,csp):
        """
        If all variables are assigned ,return dictionary of assignments.
        """
        if len(assignment) == len(csp.variables):
            return assignment
        var = select_unassigned_variable(assignment,csp)
        for value in order_domain_values(var, assignment, csp):
            """
            if value consistent with assignment, add value to assignment.
            """
            if csp.nconflicts(var, value, assignment)==0:
                csp.assign(var, value, assignment)
                removals = csp.suppose(var, value)
                """
                propogate new constraints
                """
                if inference(csp, var, value, assignment, removals):
                    result = backtrack(assignment,csp)
                    if result is not None:
                        return (assignment)
                """
                either value inconsistent or further exploration failed
                restore assignment to its state at top of loop and try next value
                """
                csp.restore(removals)
                csp.unassign(var, assignment)
    #No value was consistent with the constraints
        return None
    #Return backtracking result
    result = backtrack({},csp)
    assert result is None or csp.goal_test(result)
    return (result,csp.nassigns)
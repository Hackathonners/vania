from pulp import *

tasks = ['t1', 't2', 't3']
users = ['j', 'm', 'a']

# Rows: users
# Columns: tasks
preferences = [
    [1, 2, 3],
    [3, 1, 2],
    [2, 3, 1]
]

# State problem
problem = LpProblem("Fair Distribution Problem", LpMinimize)

# Prepare variables
users_tasks_variables = {'x'+str(u)+str(t): LpVariable('x' + str(u) + str(t), lowBound=0, cat='Binary')
                         for (u, user) in enumerate(users) for (t, task) in enumerate(tasks)}

# Generate linear expression for preferences (Summation #1)
preferences_variables = [(users_tasks_variables['x' + str(u) + str(t)], preferences[u][t])
                         for (u, user) in enumerate(users) for (t, task) in enumerate(tasks)]
effort_expression = LpAffineExpression(preferences_variables)

# Generate linear expression for effort distribution (Summation #2 - E2)
total_users = len(users)
effort_diff_vars = []
for (u, user) in enumerate(users):
    effort_diff_aux_variable = LpVariable('effort_diff_'+str(u), lowBound=0)
    effort_diff_vars.append(effort_diff_aux_variable)

    negative_factor = -1 * total_users
    negative_effort_diff = LpAffineExpression([(users_tasks_variables[
                                              'x' + str(u) + str(t)], negative_factor * preferences[u][t]) for (t, task) in enumerate(tasks)]) + effort_expression
    positive_factor = 1 * total_users
    positive_effort_diff = LpAffineExpression([(users_tasks_variables[
                                              'x' + str(u) + str(t)], positive_factor * preferences[u][t]) for (t, task) in enumerate(tasks)]) - effort_expression

    problem += negative_effort_diff <= effort_diff_aux_variable, 'abs negative effort diff ' + \
        str(u)
    problem += positive_effort_diff <= effort_diff_aux_variable, 'abs positive effort diff ' + \
        str(u)

# Constraints
# Each task must be done
task_constraints = [lpSum([users_tasks_variables['x' + str(u) + str(t)] for (u, users)
                           in enumerate(users)]) for (t, task) in enumerate(tasks)]
for (tc, task_constraint) in enumerate(task_constraints):
    problem += task_constraint == 1, 'Task ' + str(tc) + ' must be done'


# Set objective function
problem += effort_expression + \
    lpSum(effort_diff_vars), "obj"

problem.writeLP('problem.lp')
problem.solve()

# Output
print("Status:", LpStatus[problem.status])
# Print the value of the variables at the optimum
for v in problem.variables():
    print(v.name, "=", v.varValue)
# Print the value of the objective
print("objective=", value(problem.objective))

import statistics
from pulp import pulp
from itertools import dropwhile
from time import time
import json
import sys

time_tags = [
    'VALIDATING',
    'PREPARING',
    'SUMMATION_1',
    'SUMMATION_2',
    'CONSTRAINTS',
    'SOLVING',
    'TOTAL',
]

solver_names = [
    'PULP_CBC',
    'CPLEX',
    'COIN'
]


def main():
    '''solver_list = [
        pulp.solvers.PULP_CBC_CMD,
        pulp.solvers.CPLEX,
        pulp.solvers.COIN
    ]'''
    # Generate models
    fixed_targets_models = list()
    for x in range(5, 51, 5):
        weights = list()
        for _ in range(5):
            weights.append([y for y in range(1, x + 1)])
        fixed_targets_models.append((x, weights))

    fixed_objects_models = list()
    for x in range(5, 51, 5):
        weights = list()
        for _ in range(x):
            weights.append([y for y in range(1, 6)])
        fixed_objects_models.append((x, weights))

    dynamic_models = list()
    for x in range(2, 23, 2):
        weights = list()
        for _ in range(x):
            weights.append([y for y in range(1, x + 1)])

        dynamic_models.append((x, weights))

    # Based on calling arguments, choose solver
    this_solver = solver_names[int(sys.argv[1])]

    # Build basic structure
    benchmark = {
        this_solver: {
            'fixed_targets': {
                '#targets': 5,
                'measures': []
            },
            'fixed_objects': {
                '#objects': 5,
                'measures': []
            },
            'dynamic': {
                'measures': []
            }
        }
    }

    # Initialize FairDistributor
    fd = FairDistributor()

    # Benchmark with fixed target number
    measures_list = benchmark[this_solver]['fixed_targets']['measures']
    targets = ['target_1', 'target_2', 'target_3', 'target_4', 'target_5']
    for model in fixed_targets_models:
        measure = dict()
        measure['#objects'] = model[0]
        times_list = measure['times'] = []
        objects = ['object_{0}'.format(str(s))
                   for s in range(model[0])]
        fd.set_data(targets, objects, model[1])
        # Setup for average and mean
        # TODO: This could be done abstractly for any number of tries.
        time_list_1 = list()
        fd.distribute(times_list=time_list_1)
        time_list_2 = list()
        fd.distribute(times_list=time_list_2)
        time_list_3 = list()
        fd.distribute(times_list=time_list_3)
        for i in range(len(time_tags)):
            current_times = [time_list_1[i][1], time_list_2[i][1], time_list_3[i][1]]
            times_list.append((time_list_1[i][0], statistics.mean(current_times), statistics.stdev(current_times)))
        measures_list.append(measure)

    print("Benchmark with Fixed Targets Done")
    print(benchmark)
    # Benchmark with fixed object number
    measures_list = benchmark[this_solver]['fixed_objects']['measures']
    objects = ['object_1', 'object_2', 'object_3', 'object_4', 'object_5']
    for model in fixed_objects_models:
        measure = dict()
        measure['#targets'] = model[0]
        times_list = measure['times'] = []
        targets = ['target_{0}'.format(str(s))
                   for s in range(model[0])]
        fd.set_data(targets, objects, model[1])
        # Setup for average and mean
        # TODO: This could be done abstractly for any number of tries.
        time_list_1 = list()
        fd.distribute(times_list=time_list_1)
        time_list_2 = list()
        fd.distribute(times_list=time_list_2)
        time_list_3 = list()
        fd.distribute(times_list=time_list_3)
        for i in range(len(time_tags)):
            current_times = [time_list_1[i][1], time_list_2[i][1], time_list_3[i][1]]
            times_list.append((time_list_1[i][0], statistics.mean(current_times), statistics.stdev(current_times)))
        measures_list.append(measure)

    print("Benchmark with Fixed Objects Done")
    print(benchmark)
    # Benchmark with dynamic values - both targets and objects increase
    measures_list = benchmark[this_solver]['dynamic']['measures']
    for model in dynamic_models:
        measure = dict()
        measure['#objects/#targets'] = model[0]
        times_list = measure['times'] = []
        objects = ['object_{0}'.format(str(s))
                   for s in range(model[0])]
        targets = ['target_{0}'.format(str(s))
                   for s in range(model[0])]
        fd.set_data(targets, objects, model[1])
        # Setup for average and mean
        # TODO: This could be done abstractly for any number of tries.
        time_list_1 = list()
        fd.distribute(times_list=time_list_1)
        time_list_2 = list()
        fd.distribute(times_list=time_list_2)
        time_list_3 = list()
        fd.distribute(times_list=time_list_3)
        for i in range(len(time_tags)):
            current_times = [time_list_1[i][1], time_list_2[i][1], time_list_3[i][1]]
            times_list.append((time_list_1[i][0], statistics.mean(current_times), statistics.stdev(current_times)))
        measures_list.append(measure)

    print("Benchmark with Dynamic Values Done")
    print(benchmark)
    # Write benchmark dict to disk as result
    filename = './benchmark_' + this_solver + '.json'
    with open(filename, 'w') as f:
        json.dump(benchmark, f)


class FairDistributor():
    def __init__(self, targets=[], objects=[], weights=[]):
        self.set_data(targets, objects, weights)

    def set_data(self, targets, objects, weights):
        self._targets = targets
        self._objects = objects
        self._weights = weights

    def validate(self):
        try:
            self._validate()
            return True
        except ValueError:
            return False

    def _validate(self):
        if len(self._weights) != len(self._targets):
            raise ValueError(
                "The amount of weight lines should match the amount of targets")

        # All values should be positive
        s = list(
            dropwhile(lambda x: len(x) == len(self._objects), self._weights))
        if len(s) != 0:
            raise ValueError(
                "The amount of weight columns should match the amount of objects")
        for lines in self._weights:
            for i in lines:
                if i < 0:
                    raise ValueError(
                        "All weights must be positive")

    def distribute(self, times_list, fairness=True, output=None):

        # Validate the problem variables

        first_time = initial_time = time()

        self._validate()

        times_list.append((time_tags[0], time() - initial_time))
        # State problem
        initial_time = time()

        problem = pulp.LpProblem(
            "Fair Distribution Problem", pulp.LpMinimize)

        # Prepare variables
        targets_objects = {}
        for (t, target) in enumerate(self._targets):
            for (o, object) in enumerate(self._objects):
                variable = pulp.LpVariable(
                    'x' + str(t) + str(o), lowBound=0, cat='Binary')
                position = {'target': t, 'object': o}
                targets_objects[
                    'x' + str(t) + str(o)] = (variable, position)

        times_list.append((time_tags[1], time() - initial_time))
        # Generate linear expression for self._weights (Summation #1)
        initial_time = time()

        weights = [(variable, self._weights[weight_position['target']][weight_position['object']])
                   for (variable, weight_position) in targets_objects.values()]
        weight_expression = pulp.LpAffineExpression(weights)

        times_list.append((time_tags[2], time() - initial_time))
        # Generate linear expression for effort distribution (Summation #2)
        initial_time = time()

        weight_diff_vars = []
        if fairness:
            total_targets = len(self._targets)
            for (t, target) in enumerate(self._targets):
                weight_diff_aux_variable = pulp.LpVariable(
                    'weight_diff_' + str(t), lowBound=0)
                weight_diff_vars.append(weight_diff_aux_variable)

                negative_effort_diff_weights = []
                positive_effort_diff_weights = []
                negative_factor = -1 * total_targets
                positive_factor = 1 * total_targets
                for (o, object) in enumerate(self._objects):
                    id = 'x' + str(t) + str(o)
                    negative_effort_diff_weights.append(
                        (targets_objects[id][0], negative_factor * self._weights[t][o]))
                    positive_effort_diff_weights.append(
                        (targets_objects[id][0], positive_factor * self._weights[t][o]))

                negative_effort_diff = pulp.LpAffineExpression(
                    negative_effort_diff_weights) + weight_expression
                positive_effort_diff = pulp.LpAffineExpression(
                    positive_effort_diff_weights) - weight_expression

                problem += negative_effort_diff <= weight_diff_aux_variable, 'abs negative effort diff ' + \
                           str(t)
                problem += positive_effort_diff <= weight_diff_aux_variable, 'abs positive effort diff ' + \
                           str(t)

        times_list.append((time_tags[3], time() - initial_time))
        # Constraints - Each task must be done
        initial_time = time()

        for (o, object) in enumerate(self._objects):
            constraints = []
            for (t, target) in enumerate(self._targets):
                constraints.append(
                    targets_objects['x' + str(t) + str(o)][0])
            problem += pulp.lpSum(constraints) == 1, 'Task ' + \
                       str(o) + ' must be done'

        times_list.append((time_tags[4], time() - initial_time))
        # Set objective function
        problem += weight_expression + \
                   pulp.lpSum(weight_diff_vars), "obj"

        if output:
            problem.writeLP(output)

        initial_time = time()
        problem.solve()
        times_list.append((time_tags[5], time() - initial_time))
        # Build output
        data = {}
        for v in filter(lambda x: x.varValue > 0, problem.variables()):
            if v.name not in targets_objects:
                continue
            position = targets_objects[v.name][1]
            target = self._targets[position['target']]
            object = self._objects[position['object']]

            if target not in data:
                data[target] = []

            data[target].append(object)

        times_list.append((time_tags[6], time() - first_time))
        return data


if __name__ == '__main__':
    main()

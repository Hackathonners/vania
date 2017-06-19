from vania import FairDistributor


def main():
    # User input for the number of targets and objects.
    users = ['user1', 'user2']
    tasks = ['task1', 'task2']
    preferences = [
        [1, 2],
        [2, 1],
    ]

    # Run solver
    distributor = FairDistributor(users, tasks, preferences)
    output = distributor.distribute(output='problem.lp')

    # Output
    print(output)

if __name__ == '__main__':
    main()

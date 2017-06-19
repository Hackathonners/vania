from vania import FairDistributor


def main():
    # User input for the number of targets and objects.
    number_of_targets = int(sys.argv[1])
    number_of_objects = int(sys.argv[2])

    # Generate dummy lists for objects, targets and dummy matrix for weights
    targets = ['target_{0}'.format(str(s))
               for s in range(number_of_targets)]
    objects = ['object_{0}'.format(str(s))
               for s in range(number_of_objects)]
    dummy_weights = list(range(1, number_of_objects+1))
    weights_matrix = list()
    for _ in range(number_of_targets):
        new_random_weight_list = list(dummy_weights)
        shuffle(new_random_weight_list)
        weights_matrix.append(new_random_weight_list)

    # Benchmark solver
    start_time = time.time()
    distributor = FairDistributor(targets, objects, weights_matrix)
    distributor.distribute()
    elapsed_time = time.time() - start_time

    # Output
    print('Number of Targets: {0}\nNumber of Objects: {1}\nTime elapsed: {2}'.format(
        number_of_targets, number_of_objects, elapsed_time))

if __name__ == '__main__':
    main()

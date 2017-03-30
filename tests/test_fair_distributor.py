import os
import filecmp
import shutil
from unittest import TestCase
from vania import FairDistributor
path = os.path.dirname(os.path.realpath(__file__))


class TestFairDistributor(TestCase):

    def setUp(self):
        self.distributor = FairDistributor()
        self._resetTmpTestDir()

    def tearDown(self):
        self.distributor = None
        self._cleanTmpTestDir()

    def test_constructor(self):
        objects = ['t1', 't2', 't3']
        targets = ['u1', 'u2', 'u3']
        weights = [
            [1, 2, 3],
            [3, 2, 1],
            [2, 3, 1]
        ]

        instance = FairDistributor(targets, objects, weights)

        self.assertEqual(objects, instance._objects)
        self.assertEqual(targets, instance._targets)
        self.assertEqual(weights, instance._weights)

    def test_set_data(self):
        objects = ['t1', 't2', 't3']
        targets = ['u1', 'u2', 'u3']
        weights = [
            [1, 2, 3],
            [3, 2, 1],
            [2, 3, 1]
        ]

        self.distributor.set_data(targets, objects, weights)

        self.assertEqual(objects, self.distributor._objects)
        self.assertEqual(targets, self.distributor._targets)
        self.assertEqual(weights, self.distributor._weights)

    def test_validate_correct_data(self):
        objects = ['t1', 't2', 't3']
        targets = ['u1', 'u2', 'u3']
        weights = [
            [1, 2, 3],
            [3, 2, 1],
            [2, 3, 1]
        ]

        self.distributor._objects = objects
        self.distributor._targets = targets
        self.distributor._weights = weights

        self.assertTrue(self.distributor.validate())

    def test_validate_objects_weights_mismatch(self):
        objects = ['t1', 't2', 't3']
        targets = ['u1']
        weights = [
            [1, 2, 3, 2]
        ]

        self.distributor._objects = objects
        self.distributor._targets = targets
        self.distributor._weights = weights

        self.assertFalse(self.distributor.validate())

    def test_validate_targets_weights_mismatch(self):
        objects = ['t1', 't2']
        targets = ['u1', 'u2']
        weights = [
            [1, 2]
        ]

        self.distributor._objects = objects
        self.distributor._targets = targets
        self.distributor._weights = weights

        self.assertFalse(self.distributor.validate())

    def test_validate_negative_weights(self):
        objects = ['t1', 't2']
        targets = ['u1', 'u2']
        weights = [
            [1, 2],
            [-1, -2]
        ]

        self.distributor._objects = objects
        self.distributor._targets = targets
        self.distributor._weights = weights

        self.assertFalse(self.distributor.validate())

    def test_validate_exception_raise(self):
        objects = ['t1', 't2']
        targets = ['u1', 'u2']
        weights = [
            [-1, 2],
            [3, -4],
        ]

        self.distributor._objects = objects
        self.distributor._targets = targets
        self.distributor._weights = weights

        with self.assertRaises(ValueError):
            self.distributor.distribute()

    def test_model_output(self):
        model_file = path+'/resources/model.lp'
        output_file = path+'/tmp/model.lp'
        objects = ['user1', 'user2']
        targets = ['task1', 'task2']
        weights = [
            [1, 2],
            [2, 1],
        ]

        self.distributor._objects = objects
        self.distributor._targets = targets
        self.distributor._weights = weights

        self.distributor.distribute(output=output_file)

        self.assertTrue(filecmp.cmp(model_file, output_file))

    def _resetTmpTestDir(self):
        self._cleanTmpTestDir(True)

    def _cleanTmpTestDir(self, reset=False):
        if os.path.exists(path + '/tmp'):
            shutil.rmtree(path + '/tmp')
        if reset:
            os.makedirs(path + '/tmp')

    def test_validate_output(self):
        targets = ['Team A', 'Team B', 'Team C']
        objects = ['Task 1', 'Task 2', 'Task 3', 'Task 4']
        weights = [
            [1, 2, 3, 2],
            [3, 1, 4, 2],
            [3, 4, 1, 1]
        ]

        self.distributor._objects = objects
        self.distributor._targets = targets
        self.distributor._weights = weights

        expected_output = {'Team A': ['Task 1'], 'Team C': ['Task 3', 'Task 4'], 'Team B': ['Task 2']}
        for key in expected_output:
            expected_output[key].sort()

        obtained_output = self.distributor.distribute()
        for key in obtained_output:
            obtained_output[key].sort()

        self.assertEqual(obtained_output, expected_output)

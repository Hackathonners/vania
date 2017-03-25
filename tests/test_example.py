from unittest import TestCase
from vania.fair_distributor import FairDistributor


class TestFairDistributor(TestCase):

    def setUp(self):
        self.distributor = FairDistributor()

    def tearDown(self):
        self.distributor = None

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

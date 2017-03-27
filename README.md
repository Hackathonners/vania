# Project Vania - A Fair Distributor
**Fair Distributor** is module that allows fair distribution of any number of **objects** through a group of **targets**.

Using linear programming, this module takes into consideration the **weights** of the **targets** relative to the **objects** and distributes them in the **fairest way possible**.

For instance, this module can be used to fairly distribute:
* A set of tasks (objects) among a group of people (targets) according to their preferences to do each task (weights).
* A set of projects (objects) among development teams (targets) according to their skill-level (weights) on the required skills for each project.


## Our Meaning of Fairness

We define **Fairness** as:
 * The total weight for the resulting attribution of objects to targets should be minimal.
This enforces that the least amount of shared effort is made.

_Optionally_, the following rule can be applied (enabled by default):
 * The difference between the total weight distributed between targets is minimal.
This enforces the least amount of individual effort.

## Documentation

You can find all the documentation in the following link:
https://hackathonners.github.io/vania

## Download and Install

Install the latest stable version of this module:

    $ pip install vania

To work with the source code, clone this repository:

    $ git clone git://github.com/hackathonners/vania.git

## Usage

A quick example for 3 abstract targets, 4 abstract objects and the following weight matrix.

```python
from vania.fair_distributor import FairDistributor

targets = ['user1', 'user2']
objects = ['task1', 'task2']
weights = [
    [1, 2],
    [2, 1]
]

distributor = FairDistributor(targets, objects, weights)
print(distributor.distribute())

# Output
{
    'user1': ['task1'], # User 1 does the task1
    'user2': ['task2']  # User 2 does the task2
}
```

## Contributions and Bugs

Found a bug and wish to report it? You can do so here: https://github.com/Hackathonners/vania/issues.
If you'd rather contribute to this project with the bugfix, awesome! Simply Fork the project on Github and make a Pull Request.
Please tell us if you are unfamiliar with Git or Github and we'll definitely help you make your contribution.

## Authors

Hackathonners is **_a group of people who build things_**.

You can check us out at http://hackathonners.org.

## License

The Fair Distributor is licensed under the [MIT License](https://opensource.org/licenses/MIT).

Copyright (C) 2017 Hackathonners

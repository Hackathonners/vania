# Project Vania - A Fair Distributor
**Fair Distributor** is a module which [fairly](#our-meaning-of-fairness) distributes a list of arbitrary **objects** through a set of **targets**.

To be more explicit, this module considers 3 key components:
* **object**: some kind of entity that can be assigned to something.
* **target**: the entity that will have one (or more) **objects** assigned to it.
* **weight**: represents the cost of assigning a given **object** to a **target**.

A collection of each of these components is given as input to the module.
Using linear programming, the **weights** of the **targets** relative to the **objects** are taken into consideration and used to build the constraints of an Integer Linear Programming (ILP) model. An ILP solver is then used, in order to distribute the **objects** through the **targets**, in the *fairest way possible*.

For instance, this module can be used to fairly distribute:
* A set of tasks (objects) among a group of people (targets) according to their preferences to do each task (weights).
* A set of projects (objects) among development teams (targets) according to their skill-level (weights) on the required skills for each project.


## Our Meaning of Fairness

We define **Fairness** as:
 * The total **weight** of distributing all **objects** through the **targets** should be minimal.
This enforces that the least amount of shared effort is made.

_Optionally_, the following rule can be applied (enabled by default):
 * The difference between the individual **weight** of each **target** is minimal.
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
To start using the **Fair Distributor**, you need first to import it, by doing this:
```python
from vania.fair_distributor import FairDistributor
```
Now, just feed it with your problem variables, and ask for the solution.
To better explain how you can do it, lets consider a specific example.

Suppose that you are managing a project, which contains **4** tasks: _Front-end Development_, _Back-end Development_, _Testing_, and _Documentation_.
There is a need to assign these **4** tasks through a set of **3** teams: _A_, _B_ and _C_.
You have the expected number of hours each team needs to finish each task:

|        |*Front-end Development*|*Back-end Development*|*Testing*|*Documentation*| 
|--------|-----------------------|----------------------|---------|---------------|
|_Team A_|          1h           |          2h          |    3h   |       2h      |
|_Team B_|          3h           |          1h          |    4h   |       2h      |
|_Team C_|          3h           |          4h          |    1h   |       1h      |

Here, we consider tasks as **objects**, teams as **targets** and the hours expressed in each cell are the **weights**.

It is necessary to create a data structure for each component. **Objects** and **targets** are lists, while **weights** is a collection, which contains for each target the cost of assigning every object to it, and is represented as a matrix.
The structures for this example would be as follow:

```python
targets = ['Team A', 'Team B', 'Team C']
objects = ['Front-end Development', 'Back-end Development', 'Testing', 'Documentation']
weights = [
    [1, 2, 3, 2],		# hours for Team A to complete each task
    [3, 1, 4, 2],		# hours for Team B to complete each task
    [3, 4, 1, 1]		# hours for Team C to complete each task
]
```

Now, just feed the **Fair Distributor** with all the components, and ask for the solution:
```python
distributor = FairDistributor(targets, objects, weights)
print(distributor.distribute())
```

And here is the solution!
```python
# Output
{
    'Team A': ['Front-end Development'],        # Team A does the Front-end Development
    'Team B': ['Back-end Development'],         # Team B does the Back-end Development
    'Team C': ['Testing', 'Documentation']      # Team C does the Testing and Documentation
}
```

Here is the final code of this example:
```python
from vania.fair_distributor import FairDistributor

targets = ['Team A', 'Team B', 'Team C']
objects = ['Front-end Development', 'Back-end Development', 'Testing', 'Documentation']
weights = [
    [1, 2, 3, 2],		# hours for Team A to complete each task
    [3, 1, 4, 2],		# hours for Team B to complete each task
    [3, 4, 1, 1]		# hours for Team C to complete each task
]

distributor = FairDistributor(targets, objects, weights)
print(distributor.distribute())
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

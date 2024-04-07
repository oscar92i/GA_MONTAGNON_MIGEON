# Genetic Algorithm Framework

This repository contains a generic genetic algorithm framework implemented in Python. Genetic algorithms are a type of optimization algorithm inspired by the process of natural selection. They are commonly used to find solutions to optimization and search problems.

## Overview

The framework consists of three main classes:

1. `Individual`: Represents an individual in the population. Each individual has a chromosome (a candidate solution) and a fitness value indicating how good the solution is.
2. `GAProblem`: Defines a specific optimization problem to be solved using a genetic algorithm. It provides methods for mutation, crossover, fitness evaluation, and chromosome creation.
3. `GASolver`: Implements the genetic algorithm itself. It initializes a population of individuals, applies selection, reproduction, and mutation operators, and evolves the population over multiple generations.

## Usage

To use the genetic algorithm framework, follow these steps:

1. Define a subclass of `GAProblem` to represent your specific optimization problem. Implement the required methods such as `mutation`, `create`, `calculate_fitness`, and `reproduction`.
   
2. Create an instance of your custom problem class and pass it to a `GASolver` object.

3. Initialize the population using the `reset_population` method of the `GASolver` object.

4. Evolve the population by calling the `evolve_for_one_generation` method of the `GASolver` object in a loop. Optionally, you can monitor the progress of the algorithm using the `show_generation_summary` method.

5. Retrieve the best solution found using the `get_best_individual` method of the `GASolver` object.

## Example

To use this script, all you need to do is create a .py file, which you'll need to adapt to your specific problem. 

Once this is done, you can code the functions `mutation`, `create`, `calculate_fitness`, and `reproduction` functions specific to your problem.

Finally, at the end of the script, add the following sequence to start the process


```python
if __name__ == '__main__':

    from ga_solver import GASolver  # Import the GASolver class

    # Create a Problem instance
    problem = Problem()
    # Create a GASolver object with the problem instance
    solver = GASolver(problem)

    # Reset the population of the solver
    solver.reset_population()
    # Evolve the population until the problem is solved
    solver.evolve_until()
    # Get the best individual from the solver
    best = solver.get_best_individual()
    # Print the best guess
    print(f"Best guess {best.chromosome}")
```
To illustrate how this algorithm works, two application cases are available in the folder `example`:

-Mastermind

-Cities


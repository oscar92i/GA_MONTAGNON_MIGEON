# -*- coding: utf-8 -*-
"""
Created on Thu Feb 18 2022

@author: tdrumond & agademer

Template file for your Exercise 3 submission 
(generic genetic algorithm module)
"""
import random


class Individual:
    """Represents an Individual for a genetic algorithm"""

    def __init__(self, chromosome: list, fitness: float):
        """Initializes an Individual for a genetic algorithm

        Args:
            chromosome (list[]): a list representing the individual's
            chromosome
            fitness (float): the individual's fitness (the higher the value,
            the better the fitness)
        """
        self.chromosome = chromosome
        self.fitness = fitness

    def __lt__(self, other):
        """Implementation of the less_than comparator operator"""
        return self.fitness < other.fitness

    def __repr__(self):
        """Representation of the object for print calls"""
        return f'Indiv({self.fitness:.1f},{self.chromosome})'


class GAProblem:
    """Defines a Genetic algorithm problem to be solved by ga_solver"""
    def __init__(self):
        """Initialize the GAProblem"""
        raise NotImplementedError("Subclasses must implement this method")

    def generate_individual(self):
        """Generate an individual for the problem"""
        raise NotImplementedError("Subclasses must implement this method")

    def calculate_fitness(self, individual):
        """Calculate the fitness of an individual"""
        raise NotImplementedError("Subclasses must implement this method")


class GASolver:
    def __init__(self, problem: GAProblem, selection_rate=0.5, mutation_rate=0.1):
        """Initializes an instance of a ga_solver for a given GAProblem

        Args:
            problem (GAProblem): GAProblem to be solved by this ga_solver
            selection_rate (float, optional): Selection rate between 0 and 1.0. Defaults to 0.5.
            mutation_rate (float, optional): mutation_rate between 0 and 1.0. Defaults to 0.1.
        """
        self._problem = problem
        self._selection_rate = selection_rate
        self._mutation_rate = mutation_rate
        self._population = []

    def reset_population(self, pop_size=50):
        """ Initialize the population with pop_size random Individuals """
        for i in range (pop_size):
            self._population.append(self._problem.generate_individual())

    def evolve_for_one_generation(self):
        """ Apply the process for one generation : 
            -	Sort the population (Descending order)
            -	Selection: Remove x% of population (less adapted)
            -   Reproduction: Recreate the same quantity by crossing the 
                surviving ones 
            -	Mutation: For each new Individual, mutate with probability 
                mutation_rate i.e., mutate it if a random value is below   
                mutation_rate
        """
        self._population.sort(reverse=True)
        limit = len(self._population)
        self._population = self._population[:int(len(self._population) * self._selection_rate)]
        good_parents = self._population
        while len(self._population) < limit:
            a, b = random.sample(good_parents, 2)
            x_point = random.randint(1, len(a.chromosome) - 1)
            new_chrom = a.chromosome[:x_point] + b.chromosome[x_point:]
            number = random.random()
            if number < self._mutation_rate:
                valid_colors = mm.get_possible_colors()
                new_gene = random.choice(valid_colors)
                new_chrom = a.chromosome[0:x_point] + [new_gene] + a.chromosome[x_point + 1:]
            new_individual = Individual(new_chrom, self._problem.calculate_fitness(new_chrom))
            self._population.append(new_individual)

        self._population.sort(reverse=True)

    def show_generation_summary(self):
        """ Print some debug information on the current state of the population """
        pass  # REPLACE WITH YOUR CODE

    def get_best_individual(self):
        """ Return the best Individual of the population """
        pass  # REPLACE WITH YOUR CODE

    def evolve_until(self, max_nb_of_generations=500, threshold_fitness=None):
        """ Launch the evolve_for_one_generation function until one of the two condition is achieved : 
            - Max nb of generation is achieved
            - The fitness of the best Individual is greater than or equal to
              threshold_fitness
        """
        pass  # REPLACE WITH YOUR CODE

solver=GASolver()
solver.reset_population()
solver.evolve_for_one_generation()
solver.evolve_until(max_nb_of_generations=500)
best = solver.get_best_individual()

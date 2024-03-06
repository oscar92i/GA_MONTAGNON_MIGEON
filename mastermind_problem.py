# -*- coding: utf-8 -*-
"""
Created on Thu Feb 18 2022

@author: tdrumond & agademer

Template file for your Exercise 3 submission 
(GA solving Mastermind example)
"""
from ga_solver import GAProblem
import mastermind as mm
import random


class MastermindProblem(GAProblem):
    """Implementation of GAProblem for the mastermind problem"""
    def __init__(self, match):
        """Initialize the MastermindProblem

        Args:
            match (MastermindMatch): Instance of MastermindMatch for the problem
        """
        super().__init__()
        self.match = match

    @property
    def generate_individual(self):
        """Generate an individual for the Mastermind problem"""
        x=0
        for i in range(self.match.secret_size()):
            x= mm.encode_guess([random.choice(mm.get_possible_colors())])
        return x

    def calculate_fitness(self, individual):
        """Calculate the fitness of an individual for the Mastermind problem"""
        fitness = self.match.rate_guess(mm.decode_guess(individual.chromosome))
        return fitness


if __name__ == '__main__':

    from ga_solver import GASolver

    match = mm.MastermindMatch(secret_size=6)
    problem = MastermindProblem(match)
    solver = GASolver(problem)

    solver.reset_population()
    solver.evolve_until()

    print(
        f"Best guess {mm.decode_guess(solver.getBestDNA())} {solver.get_best_individual()}")
    print(
        f"Problem solved? {match.is_correct(solver.get_best_individual().chromosome)}")

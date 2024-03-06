# -*- coding: utf-8 -*-
"""
Created on Thu Feb 18 2022

@author: tdrumond & agademer

Template file for your Exercise 3 submission 
(GA solving TSP example)
"""
from ga_solver import GAProblem
import cities
import random


class TSProblem(GAProblem):
    """Implementation of GAProblem for the traveling salesperson problem"""

    def __init__(self, city_dict):
        """Initialize the TSPProblem

        Args:
            city_dict (dict): Dictionary containing information about cities
        """
        super().__init__()
        self.city_dict = city_dict

    def generate_individual(self):
        """Generate an individual for the TSP problem"""
        cities_list = list(self.city_dict.keys())
        random.shuffle(cities_list)
        return cities


if __name__ == '__main__':
    from ga_solver import GASolver

    city_dict = cities.load_cities("cities.txt")
    problem = TSProblem()
    solver = GASolver(problem)
    solver.reset_population()
    solver.evolve_until()
    cities.draw_cities(city_dict, solver.getBestIndiv().chromosome)

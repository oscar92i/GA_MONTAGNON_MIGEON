# Importation des modules nécessaires
import mastermind as mm  # Module du jeu Mastermind
import random  # Module pour la génération de nombres aléatoires

# Initialisation d'une partie de Mastermind avec une taille de secret de 4
MATCH = mm.MastermindMatch(secret_size=4)

# Classe représentant un individu dans l'algorithme génétique
class Individual:
    def __init__(self, chromosome: list, fitness: float):
        """Initialise un individu pour un algorithme génétique 

        Args:
            chromosome (list[]): une liste représentant le chromosome de l'individu
            fitness (float): la fitness de l'individu (plus la fitness est élevée, meilleur est l'individu)
        """
        self.chromosome = chromosome  # Chromosome de l'individu
        self.fitness = fitness  # Fitness de l'individu

    def __lt__(self, other):
        """Implémentation de l'opérateur de comparaison moins que"""
        return self.fitness < other.fitness 

    def __repr__(self):
        """Représentation de l'objet pour les appels print"""
        return f'Indiv({self.fitness:.1f},{self.chromosome})' 

# Classe résolvant le problème génétique
class GASolver:
    def __init__(self, selection_rate=0.5, mutation_rate=0.1):
        """Initialise une instance d'un solveur pour un problème génétique

        Args:
            selection_rate (float, optionnel): Taux de sélection entre 0 et 1.0. Par défaut 0.5.
            mutation_rate (float, optionnel): Taux de mutation entre 0 et 1.0. Par défaut 0.1.
        """
        self._selection_rate = selection_rate  # Taux de sélection
        self._mutation_rate = mutation_rate  # Taux de mutation
        self._population = []  # Population d'individus

    def reset_population(self, pop_size=50):
        """Initialise la population avec pop_size Individus aléatoires"""
        for i in range(pop_size):
            chromosome = MATCH.generate_random_guess()  # Génération d'une supposition aléatoire
            fitness = MATCH.rate_guess(chromosome)  # Calcul de la fitness
            new_individual = Individual(chromosome, fitness)  # Création d'un nouvel individu
            self._population.append(new_individual)  # Ajout à la population

    def evolve_for_one_generation(self):
        """Applique le processus pour une génération"""
        self._population.sort(reverse=True)  # Tri de la population par ordre décroissant de fitness
        limit = len(self._population)  # Limite de la population
        self._population = self._population[:int(len(self._population) * self._selection_rate)]  # Sélection des meilleurs individus
        good_parents = self._population  # Sélection des bons parents

        while len(self._population) < limit:
            a, b = random.sample(good_parents, 2)  # Sélection de deux individus au hasard parmi les bons parents
            x_point = random.randint(1, len(a.chromosome) - 1)  # Point de croisement
            new_chrom = a.chromosome[:x_point] + b.chromosome[x_point:]  # Croisement des chromosomes
            number = random.random()  # Nombre aléatoire entre 0 et 1 permettant une mutation aléatoire
            if number < self._mutation_rate:
                valid_colors = mm.get_possible_colors()  # Couleurs possibles
                new_gene = random.choice(valid_colors)  # Sélection d'une nouvelle couleur au hasard
                new_chrom = a.chromosome[0:x_point] + [new_gene] + a.chromosome[x_point+1:]  # Mutation d'un gène
            new_individual = Individual(new_chrom, MATCH.rate_guess(new_chrom))  # Création d'un nouveau individu
            self._population.append(new_individual)  # Ajout du nouvel individu à la population

        self._population.sort(reverse=True)  # Tri de la population

    def show_generation_summary(self):
        """Affiche quelques informations de débogage sur l'état actuel de la population"""
        print(self._population)

    def get_best_individual(self):
        """Retourne le meilleur individu de la population"""
        return self._population[1]

    def evolve_until(self, max_nb_of_generations=500, threshold_fitness=12):
        """Lance evolve_for_one_generation jusqu'à atteindre max_nb_of_generations"""
        generation = 1
        while generation < max_nb_of_generations:
            solver.evolve_for_one_generation()
            generation += 1

solver = GASolver()  # Initialisation du solveur
solver.reset_population()  # Initialisation de la population

solver.evolve_until(threshold_fitness=MATCH.max_score())  # Évolution jusqu'à atteindre le score maximal

best = solver.get_best_individual()  # Récupération du meilleur individu
print(f"Best guess {best.chromosome}")  # Affichage de la meilleure supposition
print(f"Problem solved? {MATCH.is_correct(best.chromosome)}")  # Vérification si le problème est résolu





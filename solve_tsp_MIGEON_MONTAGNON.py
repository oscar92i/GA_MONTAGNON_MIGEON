# Importation des modules nécessaires
import cities  # Module contenant les fonctions relatives aux villes
import random  # Module pour la génération de nombres aléatoires

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
        path = "D:\cours\\4A\Professionnal_Programming\Tp3\genetic_part2\cities.txt"  # Chemin vers le fichier des villes
        self.city_dict = cities.load_cities(path)  # Chargement des données des villes

    def reset_population(self, pop_size=50):
        """Initialise la population avec pop_size Individus aléatoires"""
        for i in range(pop_size):
            chromosome = cities.default_road(self.city_dict)  # Génération d'un chromosome aléatoire
            random.shuffle(chromosome)  # Mélange des éléments du chromosome
            fitness = -cities.road_length(self.city_dict, chromosome)  # Calcul de la fitness
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
            added_cities = []  # Liste des villes ajoutées
            new_chrom = a.chromosome[:x_point]  # Nouveau chromosome initialisé avec la première moitié du premier parent
            for city in b.chromosome[x_point:]:
                if city not in new_chrom:
                    new_chrom.append(city)
                    added_cities.append(city)

            while len(new_chrom) != 12:
                possible_cities = cities.default_road(self.city_dict)  # Liste des villes possibles
                new_gen = random.choice(possible_cities)  # Sélection d'une nouvelle ville au hasard
                if new_gen not in new_chrom:
                    new_chrom.append(new_gen)  # Ajout de la nouvelle ville

            new_fitness = -cities.road_length(self.city_dict, new_chrom)  # Calcul de la fitness du nouvel individu
            new_individual = Individual(new_chrom, new_fitness)  # Création d'un nouvel individu
            self._population.append(new_individual)  # Ajout du nouvel individu à la population

        self._population.sort(reverse=True)  # Tri de la population

    def show_generation_summary(self):
        """Affiche quelques informations de débogage sur l'état actuel de la population"""
        print(self._population)

    def get_best_individual(self):
        """Retourne le meilleur individu de la population"""
        return self._population[1]

    def evolve_until(self, max_nb_of_generations=500):
        """Lance evolve_for_one_generation jusqu'à atteindre max_nb_of_generations"""
        generation = 1
        while generation < max_nb_of_generations:
            solver.evolve_for_one_generation()
            generation += 1

    def send_dict(self):
        """Renvoie les cille dans un dictionnaire"""
        return self.city_dict


solver = GASolver()  # Initialisation du solveur
solver.reset_population()  # Initialisation de la population

solver.evolve_until()  # Évolution jusqu'à max_nb_of_generations

best = solver.get_best_individual()  # Récupération du meilleur individu
city_dict = solver.send_dict()  # renvoie le dict des villes
print(best)  # Affichage du meilleur individu

cities.draw_cities(city_dict, best.chromosome)  # Dessin des villes et du chemin du meilleur individu





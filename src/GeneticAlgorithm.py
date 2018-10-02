import random

# TSP problem solver using genetic algorithms.
from src.TSPData import TSPData


class GeneticAlgorithm:

    # Constructs a new 'genetic algorithm' object.
    # @param generations the amount of generations.
    # @param popSize the population size.
    def __init__(self, generations, pop_size):
        self.generations = generations
        self.pop_size = pop_size

     # Knuth-Yates shuffle, reordering a array randomly
     # @param chromosome array to shuffle.
    def shuffle(self, chromosome):
        n = len(chromosome)
        for i in range(n):
            r = i + int(random.uniform(0, 1) * (n - i))
            swap = chromosome[r]
            chromosome[r] = chromosome[i]
            chromosome[i] = swap
        return chromosome

    # This method should solve the TSP.
    # @param pd the TSP data.
    # @return the optimized product sequence.
    def solve_tsp(self, tsp_data):
        list = []
        for i in range(18):
            list.append(i)
        return list

# Assignment 2.b
if __name__ == "__main__":
    #parameters
    population_size = 20
    generations = 20
    persistFile = "./tmp/productMatrixDist"
        
    #setup optimization
    tsp_data = TSPData.read_from_file(persistFile)
    ga = GeneticAlgorithm(generations, population_size)

    #run optimzation and write to file
    solution = ga.solve_tsp(tsp_data)
    tsp_data.writeActionFile(solution, "./data/TSP solution.txt")
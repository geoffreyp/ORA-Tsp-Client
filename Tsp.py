from Data import CitiesUSA
import random


class Tsp:
    def __init__(self):
        data = CitiesUSA()
        self.cities = data.cities
        self.numberOfCities = len(self.cities)
        self.distances = data.distances
        self.solution = self.generateSolution()

    def distance(self, city_a, city_b):
        """
        Return the distance between city_a and city_b
        :param city_a: int
        :param city_b: int
        :return: int
        """
        return self.distances[city_a][city_b]

    def generateSolution(self):
        """
        Generate a random solution
        :return: int array
        """
        solution = []
        for i in range(self.numberOfCities):
            solution.append(i)

        random.shuffle(solution)
        print(solution)
        return solution

    def fitness(self):
        """
        Compute the total distance if we are visiting all cities in the order of actual solution
        :return: int
        """
        fitness = 0
        for i in range(self.numberOfCities - 1):
            fitness += self.distance(self.solution[i], self.solution[i+1])

        return fitness

    def toString(self):
        """
        Return the solution with the OR-API format
        """
        res = ''
        for i in range(0, int(self.numberOfCities)):
            res += str(self.solution[i]) + '-'

        return res[:-1]

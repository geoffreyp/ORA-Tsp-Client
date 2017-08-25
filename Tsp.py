from Data import CitiesUSA


class Tsp:
    def __init__(self, ):
        data = CitiesUSA()
        self.cities = data.cities
        self.numberOfCities = len(self.cities)
        self.distances = data.distances

    def distance(self, city_a, city_b):
        """
        Return the distance between city_a and city_b
        :param city_a: int
        :param city_b: int
        :return: int
        """
        return self.distances[city_a, city_b]




tsp = Tsp()

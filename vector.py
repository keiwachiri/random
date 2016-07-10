import math
import operator


class Vector:
    def __init__(self, elements):
        self.elements = elements

    def _apply(self, func, other):
        if len(self.components) == len(other.components):
            return list(map(lambda t: func(t[0], t[1]), zip(self.components, other.components)))
        else:
            raise Exception("Canot add, subtract or dot two vectors with different lengths")

    def add(self, vector):
        return Vector(self._apply(operator.add, other))

    def subtract(self, vector):
        return Vector(self._apply(operator.sub, other))

    def dot(self, vector):
        return sum(self.apply(operator.mul, other))

    def norm(self):
        return math.sqrt(sum([element * element for element in self.elements]))

    def __str__(self):
        return str(tuple(self.elements)).replace(" ", "")

    def equals(self, other):
        return self.elements == other.elements

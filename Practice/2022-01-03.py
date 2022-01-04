# base class
class member:
    """인스턴스 메소드: self로 인스턴스 자기자신이 자동으로 전달"""
    def __init__(self, name, number):
        self.name = name
        self.number = number

    def __str__(self):
        return "Member: {0.name} (#{0.number})".format(self)

    def __repr__(self):
        return "Member: {0.name} (#{0.number})".format(self)

    def display(self):
        print(self)

joe = member('joe', 123)
jane = member('jane', 456)
print([joe, jane])

# sub-class
class officer(member):
    def __init__(self, name, number, rank ):
        member.__init__(self, name, number)
        self.rank = rank

    def __str__(self):
        return "{0.rank}: {0.name} (#{0.number})".format(self)

    def __repr__(self):
        return "officer('{0.name}', {0.number}, '{0.rank}')".format(self)

jack = officer('jack', 789, 'president')

members = [joe, jane, jack]
for m in members:
    m.display()

import numpy as np
import math
from abc import ABC, abstractmethod
from typing import Union

class Fauna(ABC):

    @abstractmethod
    def __init__(self, age:int = 0, weight:Union[float] = None):
        self._age = age
        self._weight = self.get_default_weight() if weight is None else weight

    @property
    def age(self):
        return self.age

    @classmethod
    def get_default_weight(cls):
        """cls로 자신의 클래스 전달
            클래스 생성자에 다른 형태의 파라미터를 전달하기 위해
            인스턴스가 공유"""
        return None

    def get_order(self):
        self._age += 1

    def fitness(self):
        """
        fitness = 0 if weight is zero, otherwise,
        q_plus(a, a_half, phi_age) * q_minut(weight, weight_half, phi_weight)
        q_plus or minus = 1 / (1 + e^ +- {phi * (x - x_half)}
        0 <= fitness <= 1
        """
        q_plus = 1 / (1 + math.exp(self._Herbivore_params["phi_age"] *
                                   (self.age - self._Herbivore_params["a_half"]) ))
        q_minus = 1 / (1 + math.exp(- self._Herbivore_params['phi_weight'] *
                                   (self._weight - self._Herbivore_params['w_half']) ))

    if self._weight <= 0:
        self.fitness = 0
    else:
        self.fitness = q_plus * q_minus

# TODO: Update or fix
    def birth_prob(self, cnt):
        """
        Birth probability:
        - If the number of animals is greater than 2, it follows:
            min(1, gamma * fitness * (the number of animal - 1)
        - if the number of animals is less than 1 or omega < zeta * (w_birth + sigma_birth):
            0

        Parameters
        - cnt: int ( number of animals)
        """
        # cnt = len(Herbivore)

        if cnt <= 1 or self.params['omega'] < self.params['zeta'] * (self.params['w_birth'] + self.params['sigma_birth']):
            return 0
        else:
            return min(1, self.params['gamma'] * self.calc_fitness() * (cnt - 1))

    def after_birth(self):
        """ At birth, the mother animal loses ξ times the
        actual birth weight of the baby.
        • If the mother would lose more than her own weight,
        then no baby is born and the weight of the mother remains unchanged"""
        mom.weight = [x for x if ]
        if self.birth_prob() > 0:
            mom.weight = mom.weight - self.params['xi']
            if mom.weight < self.weight

class Herbivore(Fauna):
    _Herbivore_params = {'w_birth' = 8.0, 'sigma_birth' = 1.5, 'beta' = 0.9,
                        'eta' = 0.05, 'a_half' = 40.0, 'phi_age' = 0.6,
                        'w_half' = 10.0, 'phi_weight' = 0.1, 'mu' = 0.25,
                        'gamma' = 0.2, 'zeta' = 3.5, 'xi' = 1.2,
                        'omega' = 0.4, 'F' = 10.0, 'DeltaPhiMax' = None}

    def __init__(self, property):
        super().__init__(age, weight)



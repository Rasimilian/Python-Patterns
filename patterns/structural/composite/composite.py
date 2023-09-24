from __future__ import annotations
from abc import ABC, abstractmethod
from typing import TypeVar, List


class Particle(ABC):
    def __init__(self, particle_id: int):
        self.particle_id = particle_id

    @abstractmethod
    def rotate(self):
        pass


Particle_ = TypeVar("Particle_", bound=Particle)


class Electron(Particle):
    def rotate(self):
        print(f"Electron {self.particle_id} is rotating...")


class Compound(Particle):
    def __init__(self, particle_id):
        super().__init__(particle_id)
        self._particles: List[Particle_] = []

    def rotate(self):
        print(f"Compound {self.particle_id} is rotating...")
        for particle in self._particles:
            particle.rotate()

    def add(self, particle: Particle_):
        self._particles.append(particle)

    def remove(self, particle: Particle_):
        self._particles.remove(particle)

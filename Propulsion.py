# below class contains specifications of the propulsion system that can be used in the SpaceCraft

class Propulsion:
    def __init__(self, name, spec_impuls, mass_throughput, mass):
        self.name = name
        self.I = spec_impuls
        self.delta_m = mass_throughput
        self.mass = mass

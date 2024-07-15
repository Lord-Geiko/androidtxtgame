import sprites
import TxtWorld
import os
import loot

weapons = ["Rusty Sword", "Excalibur"]

melee_weapons = {
    'Rusty Sword': {'damage': 2, 'cost': 5},
    'Excalibur': {'damage': 1_000_000, 'cost': 1_000_000},
    'Fist': {'damage': 1, 'cost': 0}
}

class weapon:

    def __init__(self, name, damage, cost):
        
        self.name = name
        self.damage = damage
        self.cost = cost

rusty_sword = weapon('Rusty Sword', 2, 5)

Excalibur = weapon('Excalibur', 1_000_000, 1_000_000)


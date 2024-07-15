import random

class Loot:
    def __init__(self, name, loot_type, value):
        self.name = name
        self.loot_type = loot_type
        self.value = value

# Example loot items
rusty_sword = Loot('Rusty Sword', 'weapon', 2)
excalibur = Loot('Excalibur', 'weapon', 1_000_000)
health_potion = Loot('Health Potion', 'potion', 10)

# Enemy drop table (adjust probabilities as needed)
goblin_drops = [rusty_sword, health_potion]
orc_drops = [excalibur]

# When an enemy is defeated, randomly select loot:
defeated_enemy = random.choice(goblin_drops)
print(f"You found a {defeated_enemy.name}!")

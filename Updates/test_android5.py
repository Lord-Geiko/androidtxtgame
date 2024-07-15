#Copyright 2024##########
#Dangerous Industries 808
#########################
#DO NOT GIVE AWAY CODES##
#########################
#All code is protected###
######### BY LAW ########

import time
import random
import webbrowser

def delay_print(s):
    for c in s:
        print(c, end='', flush=True) #print each character without new line
        time.sleep(0.10) # add a delay between characters

def __init__(self, name, health, attack_range, gold_range):

    self.name = name
    self.health = health
    self.attack = random.randit(*attack_range)
    self.gold_gain = random.randint(*gold_range)

current_room = "Dungeon"

def printInventory():
    for i in inventory:
        print(i)
    pass

class Loot:
    def __init__(self, name, loot_type, value):
        self.name = name
        self.loot_type = loot_type
        self.value = value

# Example loot items
rusty_sword = Loot('Rusty Sword', 'weapon', 2)
excalibur = Loot('Excalibur', 'weapon', 1_000_000)
health_potion = Loot('Health Potion', 'potion', 10)

class Player:
    def __init__(self, name):
        self.name = name
        self.maxhealth = 100
        self.health = self.maxhealth
        self.base_attack = 10
        self.gold = 1
        self.potions = 0
        self.weapons = ["Rusty Sword"]
        self.current_weapon = "Rusty Sword"
        self.weapon_bonus = {"Rusty Sword": 15} 
        self.current_room = "Dungeon"
        self.inventory = []

    def sell_item(self, item):
        if item in self.inventory:
            self.gold += item.value
            self.inventory.remove(item)
            print(f"You sold {item.name} for {item.value} gold coins.")
        else:
            print("You don't have that item in your inventory.")

    def __str__(self):
        return f"       {self.name}\n       GOLD: {self.gold}\n"
    
    def take_damage(self, damage):
        self.health -= damage
        
    def heal(self, amount):
        self.health = min(self.maxhealth, self.health + amount)  # corrected here
        
    def attack_npc(self, npc):
        bonus = self.weapon_bonus.get(self.current_weapon, 0)  # get the bonus attack value
        total_attack = self.base_attack + bonus  # add the bonus to the base attack
        npc.take_damage(total_attack)  # use the total attack value

    def display_gold(self):
        print(f"GOLD: {self.gold}")
    
    def addtoinventory(self, item):
        self.inventory.append(item)
    
    def set_health(self, new_health):
        self.health = min(self.maxhealth, new_health)

class NPC:
    def __init__(self, name, health, attack):
        self.name = name
        self.health = health
        self.attack = attack
        
    def take_damage(self, damage):
        self.health -= damage

def display_player_info(player, current_room, inventory, health, gold):
    print(f"{player.name} is in the {player.current_room}\nInventory: {player.inventory}\nPlayer Health: {player.health}HP\nGOLD: {player.gold}\n{'-' * 27}")

def Dungeon(player):
    
    player.current_room = "Dungeon"

    while True:
        
        display_player_info(player, current_room, player.inventory, player.health, player.gold)
        print("You woke up in a Dungeon, feeling dizzy, looking around you notice an Copper coin on the floor.....")
        print("Do you want to pick it up?")
        print("Yes/No")
        
        pickup = input()
        if pickup == "yes".lower():
            player.addtoinventory("copper coin")
            print(f"Inventory: {player.inventory}")
            print("You pick up the copper coin and walk into a dark Hallway")
            goblin_room(player)
            break
        elif pickup == "no".lower():
            print("so you leave the room and walk down the hallway")
            goblin_room(player)
            break
        else:
            print("Invalid Input.. Please try again")
        Dungeon(player)

def play_game(player):

    display_player_info(player, current_room, player.inventory, player.health, player.gold)
    game_over = False
    while player.health > 0 and not game_over:
        current_room = get_current_room(player)
        print("You are in " + current_room)
        
        if current_room == "fight room":
            print("You find yourself in a dark room. You see a door in front of you.")
            action = input("What would you like to do? (enter 'door' to proceed): ")
            if action.lower() == "door":
                player.current_room = "beach"
        
        elif current_room == "beach":
            print("You teleport on a sunny beach.")
            npc = NPC("Goblin", 50, 10)
            print("A wild " + npc.name + " appears!")
            while npc.health > 0 and player.health > 0:
                print("\nPlayer Health:", player.health)
                print(npc.name + " Health:", npc.health)
                action = input("What would you like to do? (enter 'attack' to attack, 'run' to run away): ")
                
                if action.lower() == "attack":
                    player.attack_npc(npc)
                    if npc.health > 0:
                        npc_attack = random.randint(1, 10)
                        player.take_damage(npc_attack)
                elif action.lower() == "run":
                    print("You ran away from the " + npc.name + ".")
                    print("GAME_OVER")
                    game_over = True
                    break
                else:
                    print("Invalid action. Try again.")
                
            if player.health <= 0:
                print("You were defeated by the " + npc.name + ". Game Over.")
                game_over = True
                
            elif not game_over:
                print("You defeated the " + npc.name + ". You find a potion and some gold.")

                player.potions += 1
                player.gold += random.randint(1, 10)
                player.current_room = "sewer room"
                sewer_room(player)
                break

def kitchen_room(player):

    player.current_room = "Kitchen looking area"
    
    while True:

        display_player_info(player, current_room, player.inventory, player.health, player.gold)
        print("You walk into a area that looks like a kitchen.\nLooking around you see BIG Roaches flying around a dim light bulb thats slowly moving back and forth\nTiny mice eating old mouldy bread.\n Do you want to retrieve the old mouldy bread")
        print("yes or no?")
        pickup = input().lower()

        if pickup == "yes".lower():

            addtoinventory("mouldy bread")
            print(f"{player.name} picked up the Mouldy Bread and put it in his pocket")
            print("You exit the Kitchen looking area")
            print("Looking left is a long path of darkness")
            print("Looking right is a dim light shining from a short distance")
            print("*"*10)
            print("Do you choose to go Left or Right")

        elif pickup == "no".lower():

            print(f"{player.name} ignores getting the mouldy bread from the dirty looking mice")
            print("You exit the Kitchen looking area")
            print("Looking left is a long path of darkness")
            print("Looking right is a dim light shining from a short distance")
            print("*"*10)
            print("Do you choose to go Left or Right")

        direction = input().lower()
        if direction =="right":
            random_room(player)
            break
        elif direction == "left":
            sewer_room(player)
            break         
        else:
            print("Invalid Input! Please choose again")

def hallway_room(player):

    player.current_room = "Darkness of a Hallway"

    while True:

        display_player_info(player, current_room, player.inventory, player.health, player.gold)
        print("You start walking down a dimly lit hallway,\nwith only the flickering light from a single torch casting eerie shadows on the moss covered cobblestone walls\nThe air is damp and carries a faint, musty rotten onion odor.")
        print("As you take a cautious step foward\nthe floorboards creak under your weight\nechoing through the darkness silence\nThe hallway stretches ahead\ndisappearing into darkness\nYou can barely make out the outline shadow of something very Colossal running up towards you")
        print("Will you choose to run or stay to fight")
        print("*"*10)
        display_player_info(player, current_room, player.inventory, player.health, player.gold)
        print("fight or run: ")
        
        direction = input().lower()
        if direction =="run":
            construction_room(player)
            break
        elif direction == "fight":
            fight_room(player)
            break
        else:
            print("Invalid Input! Please choose again")

def sewer_room(player):

    player.current_room = "sewer room"

    while True:

        display_player_info(player, current_room, player.inventory, player.health, player.gold)
        print("You are in a Stink Sewer area, you can go left or right")
        direction = input().lower()
        if direction == "right":
            na_moo_riddle(player)
            break
        elif direction == "left":
            print("You fall into a Trap! GAME OVER!")
            break
            game_over(player)
        else:
            print("Invalid Input! Please choose again!")

def goblin_room(player):
    player.current_room = "Dark Hallway"

    while True:
        
        print("You walk down the hallway and see a Goblin. He asks you for a copper coin to continue. Give it to him? (yes/no)")
        look = input()

        if look == "yes":
            if "copper coin" in player.inventory:
                player.inventory.remove("copper coin")
                print(f"You gave Jeriko your copper coin.\nNow you have {player.inventory} in your bag")
                print("Jeriko being so happy that you gave him copper coins, he snapped his fingers & teleported away")
                hallway_room(player)
                break  # Exit the loop after moving to the next room
            else:
                print("*"*5)
                print("***You don't have a copper coin to give.***")
                print("*"*5)
                continue  # Go back to the start of the loop
        elif look == "no":
            textdisplay3 = "The Goblin named Jeriko lets you pass with a stern warning about the dangers ahead."
            delay_print(textdisplay3)
            print("Under construction")
            game_over(player)
            break  # Exit the loop after displaying the message
        else:
            print("Invalid input. Please enter 'yes' or 'no'.")

def menu_room(player):

    player.current_room = "menu room"

    while True: 

        display_player_info(player, current_room, player.inventory, player.health, player.gold)
        print("**Entering District 1**")
        print("*****@@ Zone 1 @@******")
        print("**Imagination Realm***")
        print("*"*15)
        print("*"*15)
        print("Choose by entering the menu number")
        print("................................ ")
        print("(1)  Start Game: ")
        print(" ...............................")
        print("(2)  Quit: ")
        print("..........................")
        print("Enter Number: ")
        direction = input().lower()  # Fixed: use '=' for assignment
        if direction == "1":
            Dungeon(player)
            break
        elif direction == "2":  # Fixed: use 'elif' to avoid executing the 'else' block after 'if'
            game_over(player)
            break
        else:
            print("Invalid Input! Please choose again!")

def game_over(player):

    print("*"*25)
    print("***GAME OVER!!!***")
    print("*"*25)

    url = "https://t4.ftcdn.net/jpg/02/11/54/33/360_F_211543376_kv7x0SwdITkWbqajGzglhcvZV25AsPsS.jpg"
    webbrowser.open(url)

    while True:
        print("Do you want to start over on your adventure?")
        direction = input().lower()  
        if direction == "yes":
            menu_room(player)  
        elif direction == "no": 
            game_over(player)
            break

def fight_room(player):
    player.current_room = "fight room"
    is_game_over = False
    npc_defeated = False

    while not is_game_over and not npc_defeated:
        display_player_info(player, player.current_room, player.inventory, player.health, player.gold)
        
        if player.current_room == "fight room":
            print("You find yourself face-to-face with a Giant Crab. You see a door in front of you.")
            action = input("What would you like to do? (enter 'yes' to proceed): ")
            if action.lower() == "yes":
                player.current_room = "beach"
                continue
        
        elif player.current_room == "beach":
            print("You are now on a dense beach-like area.")
            npc = NPC("Giant Crab", 50, 10)
            print("A savage " + npc.name + " appears!")
            
            while npc.health > 0 and player.health > 0:
                print("\nPlayer Health:", player.health)
                print(npc.name + " Health:", npc.health)
                action = input("What would you like to do? (enter '1' to attack, 'run' to run away): ")
                
                if action.lower() == "1":
                    player.attack_npc(npc)
                    if npc.health > 0:
                        npc_attack = random.randint(1, 10)
                        player.take_damage(npc_attack)
                elif action.lower() == "run":
                    print("You ran away from the " + npc.name + " and fell into a giant hole.")
                    print("*" * 10)
                    player.current_room = "Construction Room"  # Transition to the menu room
                    npc_defeated = True
                else:
                    print("Invalid action. Try again.")
            
            if player.health <= 0:
                print("You were defeated by the " + npc.name + ". Game Over.")
                is_game_over = True
            else:
                print("You defeated the " + npc.name + ". You find a potion and some gold.")
                player.potions += 1
                player.gold += random.randint(1, 10)
                player.addtoinventory("potion")
                print("*"*10)  # Corrected method name
                npc_defeated = True
                construction_room(player)# Transition to the next room (e.g., call next_room(player))
                # For now, let's assume the next room is "menu room"
                player.current_room = "Construction Room"

def construction_room(player):

    player.current_room = "Construction Room"

    display_player_info(player, player.current_room, player.inventory, player.health, player.gold)

    while True:

        print("THIS ROOM IS UNDER CONSTRUCTION")

        next_action = input("What do you want to do next? (explore/exit): ").lower()
        if next_action == "explore":
        # Call the next room or function
            next_room(player)
            break
        elif next_action == "exit":
            print("Exiting the construction room...")
        # Transition to another part of the game or end the game
            end_game(player)
            break
        else:
            print("Invalid choice. Please try again.")
            construction_room(player)

def next_room(player):
    player.current_room = "next room"

    print("You move to the next room... thats under construction")
    quit()

def mystery_forest(player):

    player.current_room = "mystery forest"

    print("In forest")
    game_over(player)

def void_room(player):

    player.current_room = "void room"

    print("in void room")
    game_over(player)

def na_moo_riddle(player):

    player.current_room = "moo room"

    secret_number = random.randint(1, 10)

    attempts = 0

    loser = 2

    print("You descended into the murky depths of the sewer, the air thick with decay. Walls dripped slime,\nand flickering torches barely illuminated winding tunnels.\nYou see doo-doo and vomit looking material floating in a slow pace current into the abyss.")
    print("As you go to step away from the foul-smelling water,\na giant rat the size of a house cat runs past you!\nYou accidentally fall into the septic sewer water")
    print("You quickly jump out of the water disgusted and start puking, but suddenly stop\nOut of the murky depths of the fetid swamp of sewer water,\nan ancient toad the size of a boulder squats,\nits warty skin oozing with a putrid slime. Its bulging eyes, yellowed and grimy,\nfixate on you as it croaks in a guttural voice,")
    print("Aloha e ka hoa!\n'O ko'u inoa 'o NA MO'O.\nHe aha kāu hana ma kēia kai i lalo nei i nā wai kūkulu kūkulu?")
    print("Pono 'oe e koho i nā helu ma waena o ho'okahi a me 'umi:")
    print("Do you understand this Creature: Ae/Aole\n")
    
    understand = input().lower()

    if understand == "ae":
        pass
    elif understand == "aole":
        print("Heluhelu hou")
        na_moo_riddle(player)

    else:
        print("NA MO'O doesn't understand you, say it again")
        na_moo_riddle(player)

    while True:

        guess = input("E komo i kāu pane: ")

        try:
            guess = int(guess)

        except ValueError:
            print("NA MO'O doesn't understand you, say it again.")
            continue

        attempts += 1

        if guess < secret_number:
            print("E hele i luna.")

        elif guess > secret_number:
            print("E hele i lalo.")

        else:
            
            #replace 'hero' with {player.name}
            print("Aloha! Ua mahalo au i kou hoomaopopo ana i ka kakou olelo kahiko.")
            print("E 'ae mai ko mākou hui malu iā 'oe a e hele i laila i kēlā me kēia manawa āu e makemake\nai iā mākou e ho'ohana wale i kēia pūpū e puhi ai e kāhea iā mākou.\n{OB TITLE}{OB ARTIFACT}")
            print("Na Mo'o teleports you into the abyssal void")
            void_room(player)
            break

        if attempts >= loser:
            
            print("'A'ole maopopo iā 'oe ke 'ano a me ka 'ōlelo o ko kākou mo'omeheu kahiko!")
            print("MAI OLA!")
            print("Na Moo teleports you into mystery forest")
            mystery_forest(player)
            break

def end_game(player):
    player.current_room = "end game"
    print("Thank you for playing!")

def main():

    print("Welcome to Imagination Land")
    name = input("Enter your character's name: ")
    player = Player(name)
    print(f"Aloha, {player.name}!")
    menu_room(player)

if __name__ == "__main__":
    main()
 
menu_room()
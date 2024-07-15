import time
import random

def delay_print(s):
    for c in s:
        print(c, end='', flush=True) #print each character without new line
        time.sleep(0.10) # add a delay between characters

#Copyright 2024
#quit() #to end game


# Checks if the file to save has been created
#file_exists = os.path.isfile("loadfile.txt")

#skeleton key for rooms
#def room():

   # s = ""
    #save(s)

    #while True:

        #print()
        #direction == input().lower()
       # if direction == '':
           # 
            #room name go to next
        #if direction == '':
            #room name
        #else:
            #print("Invalid Input! Please choose again!")
#skeleton for enumerate inventory
#def printInventory():

    #input == "see inventory".lower()
    #print("This is your inventory: ")
    #for slot in range(len(inventory)):
       # item = inventory[slot]
       # print(f"{slot}: {item}")
    #pass
#health
#def room(health):
     #print("You are attacked")
    # health = health - 5
    # return health
#def attack(player_health):
        #player_health - 5
        #return player_health
#def monster(monster_health):
        #print("You face a might dragon... he attacks you!!")
        #health = attack(player_health)
        #print("you suffer burns", player_health, "health left")

#load the text file
#def load():
    if file_exists:
        file=open("loadfile.txt", "r")
        room = file.read()
        file.close()
    else:
        room = "startroom"

    roomchooser(room)

#def save(s):
    file = open("loadfile.txt", "w")
    file.write(s)
    file.close()

#def roomchooser(room):
    if room == "startroom":
        startroom()
    if room == "kitchen_room":
        kitchen_room()
    if room == "hallway_room":
        hallway_room()
    if room == "sewer_room":
        sewer_room()
    if room == "goblin_room":
        goblin_room()
    if room == "random_room":
        random_room()

def __init__(self, name, health, attack_range, gold_range):

    self.name = name
    self.health = health
    self.attack = random.randit(*attack_range)
    self.gold_gain = random.randint(*gold_range)

current_room = "startroom"
player_health = 100

inventory = ["rusted sword", "rubber slipper"]

#sub-routine to add items to the inventory
def addtoinventory(item):
    inventory.append(item)

def printInventory():
    for i in inventory:
        print(i)
    pass

class Player:
    def __init__(self, name):
        self.name = name
        self.maxhealth = 100
        self.health = self.maxhealth
        self.base_attack = random.randint(1, 10)
        self.gold = 1
        self.potions = 0
        self.weapons = ["Rusty Sword"]
        self.current_weapon = "Rusty Sword"

    def __str__(self):
        return f"       {self.name}\n       GOLD: {self.gold}\n"



class enemy:

    def __init__(self, name):

        self.name = name
        self.health = health
        self.attack = attack.random.randint()
        self.gold_gain = gold.random.randint()


def display_player_info(player, current_room, inventory, player_health):
    print(f"You are in the {current_room}\nInventory: {inventory}\nPlayer Health: {player_health}HP\n{'-' * 27}")


def startroom(player):
    
    s = "startroom"
    


    while True:
        

        
        display_player_info(player, current_room, inventory, player_health)
        print("You woke up in a Dungeon, feeling dizzy, looking around you notice an Copper coin on the floor.....")
        print("Do you want to pick it up?")
        print("Yes/No")
        print("*"*27)
        print("*"*27)
        print("*"*27)

        pickup = input()
        if pickup == "yes".lower():
            addtoinventory("copper coin")
            print("You pick up the copper coin and walk into a dark Hallway")
            print("*"*27)
            print("*"*27)
            print("*"*27)
            goblin_room(player)
        if pickup == "no".lower():
            print("so you leave the room and walk down the hallway")
            print("*"*27)
            print("*"*27)
            print("*"*27)
            goblin_room(player)
        else:
            print("Invalid Input.. Please try again")
        startroom()
    
def kitchen_room(player):

    s = "kitchen_room"
    
    
    while True:

        
        display_player_info(player, current_room, inventory, player_health)
        print("You are in a Kitchen, You can go left or right")
        print("*"*27)
        print("*"*27)
        print("*"*27)
        direction = input().lower()
        if direction =="right":
            random_room(player)
            
        if direction == "left":
            sewer_room(player)           
        else:
            print("Invalid Input! Please choose again")

def hallway_room(player):

    s = "hallway_room"
    

    while True:

        
        display_player_info(player, current_room, inventory, player_health)
        print("Your are in a hallway, you can go left or right")
        print("*"*27)
        print("*"*27)
        print("*"*27)
        direction = input().lower()
        if direction =="right":
            
            random_room(player)
        if direction == "left":
            
            kitchen_room(player)
        else:
            print("Invalid Input! Please choose again")

def sewer_room(player):

    s = "sewer_room"
    

    while True:
        
        
        display_player_info(player, current_room, inventory, player_health)
        print("You are in a Stink Sewer area, you can go left or right")
        print("*"*27)
        print("*"*27)
        print("*"*27)
        direction = input().lower()
        if direction == "right":
            
            kitchen_room(player)
        if direction == "left":
            print("You fall into a Trap! GAME OVER!")
            print("*"*27)
            print("*"*27)
            print("*"*27)
            quit()
        else:
            print("Invalid Input! Please choose again!")

def goblin_room(player):
    s = "goblin_room"
    

    while True:
        
        display_player_info(player, current_room, inventory, player_health)
        print("You walk down the hallway and see a Goblin. He asks you for a copper coin to continue. Give it to him? (yes/no)")
        look = input()

        if look == "yes":
            if "copper coin" in inventory:
                inventory.remove("copper coin")
                hallway_room(player)
                break  # Exit the loop after moving to the next room
            else:
                print("You don't have a copper coin to give.")
        if look == "no":
            textdisplay3 = "The Goblin named Jeriko lets you pass with a stern warning about the dangers ahead."
            delay_print(textdisplay3)
            print("*"*27)
            print("*"*27)
            print("*"*27)
            print("Game is STILL Under construction")
            quit()
            break  # Exit the loop after displaying the message
        else:
            print("Invalid input. Please enter 'yes' or 'no'.")

def random_room(player):

    
    
    print("In random room 1, game over")
    quit()

def main():

    print("*******COPYRIGHT 2024*******")
    print("****************************")
    print("Welcome to Imagination Land")
    print("****************************")
    print("****************************")
    
    name = input("Enter your character's name: ")
    player = Player(name)
    print("***********************")
    print(f"Aloha,{player}! Let your adventure into Imagination Realm BEGIN!!!!")
    startroom(player)
if __name__ =="__main__":
    main()

   
startroom()
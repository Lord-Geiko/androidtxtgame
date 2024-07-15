import random

def play_number_guessing_game():
    # Generate a random number between 1 and 10 for example
    secret_number = random.randint(1, 10)
    attempts = 0
    loser = 2  # Set the number of allowed attempts before losing

    print("You descended into the murky depths of the sewer, the air thick with decay. Walls dripped slime, and flickering torches barely illuminated winding tunnels.\nYou see doo-doo and vomit looking material floating in a slow pace current into the abyss.")
    print("As you go to step away from the foul-smelling water, a giant rat the size of a house cat runs past you and you accidentally fall into the septic sewer water")
    print("You quickly jump out of the water disgusted and start puking, but suddenly stop\nOut of the murky depths of the fetid swamp of sewer water, an ancient toad the size of a boulder squats, its warty skin oozing with a putrid slime. Its bulging eyes, yellowed and grimy, fixate on you as it croaks in a guttural voice,")
    print("Aloha e ka hoa! ʻO koʻu inoa ʻo NA MO'O. He aha kāu hana ma kēia kai i lalo nei i nā wai kūkulu kūkulu?”")
    print("Do you understand this Creature: Yes/No\n")
    understand = input().lower()
    if understand == "yes":
        pass
    elif understand == "no":
        pass
    else:
        print("NA MO'O doesn't understand you, say it again")

    while True:
        guess = input("Enter your guess: ")
        try:
            guess = int(guess)
        except ValueError:
            print("Please enter a valid integer.")
            continue

        attempts += 1

        if guess < secret_number:
            print("Try a higher number.")
        elif guess > secret_number:
            print("Try a lower number.")
        elif attempts > loser:
            print("You get eaten\nGAME_OVER!")
            break
        else:
            print(f"Congratulations! You guessed it in {attempts} attempts.")
            break

if __name__ == "__main__":
    play_number_guessing_game()
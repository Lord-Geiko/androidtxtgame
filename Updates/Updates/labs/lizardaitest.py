import random
import os

def mystery_forest():
    print("In forest")
    os.sleep(100)
    quit()

def void_room():
    print("in void room")
    os.sleep(100)
    quit()

def na_moo_riddle():

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
        na_moo_riddle()

    else:
        print("NA MO'O doesn't understand you, say it again")

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
            print(f"Aloha {player.name} ! Ua mahalo au i kou hoomaopopo ana i ka kakou olelo kahiko.")
            print("E 'ae mai ko mākou hui malu iā 'oe a e hele i laila i kēlā me kēia manawa āu e makemake ai iā mākou e ho'ohana wale i kēia pūpū e puhi ai e kāhea iā mākou.{OB TITLE}{OB ARTIFACT}")
            print("Na Mo'o teleports you into the abyssal void")
            void_room()
            break

        if attempts >= loser:
            print("'A'ole maopopo iā 'oe ke 'ano a me ka 'ōlelo o ko kākou mo'omeheu kahiko!")
            print("MAI OLA!")
            print("Na Moo teleports you into mystery forest")
            mystery_forest()
            break

if __name__ == "__main__":
    na_moo_riddle()

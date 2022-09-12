import random

import requests

# define random pokemon


def random_pokemon():
    pokemon_number = random.randint(1, 151)
    url = 'https://pokeapi.co/api/v2/pokemon/{}/'.format(pokemon_number)
    response = requests.get(url)
    pokemon = response.json()

    return{
        'name': pokemon['name'],
        'id': pokemon['id'],
        'height': pokemon['height'],
        'weight': pokemon['weight']

    }


def run():

    # round 1
    # assign and output pokemon for player
    print("Round 1")
    my_pokemon = random_pokemon()

    pokemon_id = my_pokemon["id"],
    height = my_pokemon["height"],
    weight = my_pokemon["weight"]

    print("Your pokemon is: {}".format(my_pokemon["name"]))
    print("Your pokemon stats are: id=", pokemon_id, "height =", height, "weight =", weight)

    stat_choice = input("Which stat do you want to use? (id, height or weight?)")

    opponent_pokemon = random_pokemon()
    print("The opponent chose: {}".format(opponent_pokemon["name"]))

    my_stat = my_pokemon[stat_choice]
    opponent_stat = opponent_pokemon[stat_choice]

    # running the game
    if my_stat > opponent_stat:
        print("You win this round!")
        my_score_1 = 1
        opponent_score1 = 0
    elif my_stat < opponent_stat:
        print("You lose this round!")
        my_score_1 = 0
        opponent_score1 = 1
    else:
        print("Its' a draw for round 1")
        my_score_1 = 1
        opponent_score1 = 1

    # outputting game results
    print("Your score in for round 1 is: ", my_score_1)
    print("The opponent's score for round 1 is: ", opponent_score1)

    # round 2
    print("\nRound 2")
    my_pokemon = random_pokemon()
    pokemon_id = my_pokemon["id"],
    height = my_pokemon["height"],
    weight = my_pokemon["weight"]

    print("Your pokemon is: {}".format(my_pokemon["name"]))
    print("Your pokemon stats are: id=", pokemon_id, "height =", height, "weight =", weight)

    stat_choice = input("Which stat do you want to use? (id, height, weight) ")

    opponent_pokemon = random_pokemon()
    print("The opponent chose: {}".format(opponent_pokemon["name"]))

    my_stat = my_pokemon[stat_choice]
    opponent_stat = opponent_pokemon[stat_choice]

    if my_stat > opponent_stat:
        print("You win this round!")
        my_score_2 = 1
        opponent_score2 = 0
    elif my_stat < opponent_stat:
        print("You lose this round!")
        my_score_2 = 0
        opponent_score2 = 1
    else:
        print("Its' a draw")
        my_score_2 = 1
        opponent_score2 = 1

    print("Your score for round 2 is: ", my_score_2)
    print("The opponent's score for round 2 is: ", opponent_score2)

    # round 3
    print("\nRound 3")
    my_pokemon = random_pokemon()
    pokemon_id = my_pokemon["id"],
    height = my_pokemon["height"],
    weight = my_pokemon["weight"]

    print("Your pokemon is: {}".format(my_pokemon["name"]))
    print("Your pokemon stats are: id=", pokemon_id, "height =", height, "weight =", weight)

    stat_choice = input("Which stat do you want to use? (id, height, weight) ")

    opponent_pokemon = random_pokemon()
    print("The opponent chose: {}".format(opponent_pokemon["name"]))

    my_stat = my_pokemon[stat_choice]
    opponent_stat = opponent_pokemon[stat_choice]

    if my_stat > opponent_stat:
        print("You win this round!")
        my_score_3 = 1
        opponent_score3 = 0
    elif my_stat < opponent_stat:
        print("You lose this round!")
        my_score_3 = 0
        opponent_score3 = 1
    else:
        print("Its' a draw")
        my_score_3 = 1
        opponent_score3 = 1

    print("Your score for round 3 is: ", my_score_3)
    print("The opponent's score for round 3 is: ", opponent_score3)

    my_total_score = [my_score_1, my_score_2, my_score_3]
    opponent_total_score = [opponent_score1, opponent_score2, opponent_score3]
    print("\nYour total score for the game is: ", sum(my_total_score))
    print("The opponent's total score for the game is: ", sum(opponent_total_score))

    if my_total_score > opponent_total_score:
        print("\nYou win the game!")
    elif my_total_score < opponent_total_score:
        print("\nThe opponent wins the game!")
    else:
        print("\nIt's a draw!")


run()





from os import system, name
from pokemon import Pokemon
import sys
from time import sleep
from moves import Moves, Outputs
import string

"""
This file contains all the functions that are responsible
for displaying the outputs of round, and receiving
data (what move to use, what pokemon to use) from players
"""


def clear():
    """Function that clear the screen"""
    if name == "nt":
        _ = system('cls')
    else:
        _ = system("clear")


def delayed_print(text):
    """Function that print letters wih slight delay"""
    for letters in text:
        sys.stdout.write(letters)
        sys.stdout.flush()
        sleep(0.030)


def chose_game_mode():
    """Function that allows player to choose gamemode"""
    delayed_print("PLESE CHOOSE GAME MODE\n")
    delayed_print("1: PLAVER VS PLAYER \n2: PLAYER VS SI\n")
    try:
        game_mode = int(input())
        if game_mode in range(1, 3):
            if game_mode == 1:
                delayed_print("PLAYER VS PLAYER\n")
                return game_mode
            elif game_mode == 2:
                delayed_print("PLAYER VS COMPUTER\n")
                return game_mode
    except ValueError:
        delayed_print("INVALID VALUE SELECTED\n")
        return chose_game_mode()


def show_team(player):
    """Function that print player's team"""
    starting_index = 1
    for pokemon in player.team():
        print(str(starting_index), pokemon.name(), pokemon.hp(), "HP")
        starting_index += 1


def show_options(player):
    """Function that show player's options"""
    pokemon = player.current_pokemon()
    print("PLAYER : ", player.name())
    print("ACTIVE POKEMON : ", pokemon.name(), pokemon.hp(), "HP")
    print("1: ATTACK\n2: SPECIAL ATTACK\n3: DEFEND\n4: SWITCH")


def choose_move(player):
    """Function that allow player to choose move of their pokemon"""
    try:
        opcja = int(input())
        if opcja not in range(5):
            delayed_print("INVALID VALUE SELECTED\n")
            return choose_move(player)
        if opcja == 2:
            if player.current_pokemon().second_type() == "":
                return Moves.TYPE_1
            else:
                delayed_print("WHICH TYPE WOULD YOU LIKE TO USE\n")
                return chose_special_attack(player)
        elif opcja == 4:
            if len(player.alive_pokemons_in_team()) == 1:
                delayed_print("THIS IS YOUR LAST POKEMON, PICK ANOTHER MOVE\n")
                return choose_move(player)
            else:
                return Moves.SWITCH
        else:
            return Moves(opcja)
    except ValueError:
        delayed_print("INVALID VALUE SELECTED\n")
        return choose_move(player)


def chose_special_attack(player):
    """Function that allow player player type of special attack"""
    print(player.current_pokemon().show_types())
    try:
        type = int(input())
        if type == 1:
            return Moves.TYPE_1
        elif type == 2:
            return Moves.TYPE_2
        else:
            delayed_print("INVALID VALUE SELECTED\n")
            return chose_special_attack(player)
    except ValueError:
        delayed_print("INVALID VALUE SELECTED\n")
        return chose_special_attack(player)


def chose_pokemon(player):
    """Function that allows player to select pokemon from their team"""
    delayed_print("SELECT POKEMON\n")
    show_team(player)
    try:
        index = int(input())
        if index not in range(len(player.team()) + 1):
            delayed_print("INVALID VALUE SELECTED\n")
            return chose_pokemon(player)
        else:
            if player.team()[index - 1].is_alive():
                if player.team()[index - 1] == player.current_pokemon():
                    delayed_print("IT'S YOUR ACTIVE POKEMON, PICK ANOTHER")
                    return chose_pokemon(player)
                else:
                    return index
            else:
                delayed_print("THIS POKEMON IS DEAD, CHOSE ANOTHER\n")
                return chose_pokemon(player)
    except ValueError:
        delayed_print("INVALID VALUE SELECTED\n")
        return chose_pokemon(player)


def output_of_battle(
    faster_player: object, slower_player: object, faster_pokemon: object,
    slower_pokemon: object, faster_move: object, slower_move: object,
    battle_result: object
):
    """
    Returns text with info about the course of the round
    """
    f_move = faster_move
    s_move = slower_move
    slow_pok = slower_pokemon
    fast_pok = faster_pokemon
    if battle_result == Outputs.OUTPUT_1:
        return f"{output_of_move(faster_player, fast_pok, slow_pok, f_move)}"\
            f"\n{output_of_move(slower_player, slow_pok, fast_pok, s_move)}"
    elif battle_result == Outputs.OUTPUT_2:
        return f"{output_of_move(faster_player, fast_pok, slow_pok, f_move)}"\
            f"\n{slower_pokemon.name()}"\
            " TOOK TOO MUCH DAMAGE AND IS UNABLE TO FIGHT"
    elif battle_result == Outputs.OUTPUT_3:
        return f"{output_of_move(faster_player, fast_pok, slow_pok, f_move)}"\
            f"\n{output_of_move(slower_player, slow_pok, fast_pok, s_move)}"\
            f"\n{faster_pokemon.name()}"\
            f" TOOK TOO MUCH DAMAGE AND IS UNABLE TO FIGHT"
    elif battle_result == Outputs.OUTPUT_4:
        return f"{output_of_move(faster_player, fast_pok, slow_pok, f_move)}"\
            f"\n{output_of_move(slower_player, slow_pok, fast_pok, s_move)}"\
            f"\n{faster_pokemon.name()}"\
            " TOOK TOO MUCH DAMAGE AND IS UNABLE TO FIGHT"
    elif battle_result == Outputs.OUTPUT_5:
        return f"{output_of_move(faster_player, fast_pok, slow_pok, f_move)}."\
            f"{slower_pokemon.name()}"\
            f" TOOK TOO MUCH DAMAGE AND IS UNABLE TO FIGHT"\
            f"\n{output_of_move(slower_player, slow_pok, fast_pok, s_move)}"
    elif battle_result == Outputs.OUTPUT_6:
        target = faster_player.current_pokemon()
        return f"{output_of_move(faster_player, fast_pok, slow_pok, f_move)}"\
            f"\n{output_of_move(slower_player, slow_pok, target, s_move)}"
    elif battle_result == Outputs.OUTPUT_7:
        return f"{output_of_move(faster_player, fast_pok, slow_pok, f_move)}"\
            f"\n{output_of_move(slower_player, slow_pok, fast_pok, s_move)}"
    elif battle_result == Outputs.OUTPUT_8:
        return f"{output_of_move(faster_player, fast_pok, slow_pok, f_move)}"\
            f"\n{output_of_move(slower_player, slow_pok, fast_pok, s_move)}"


def output_of_move(
    player: object,
    pok_1: object,
    pok_2: object,
    move: str
):
    """
    Returns the info about move used by player
    """
    normal_type_attack = pok_2.calculate_weakness(pok_1, "normal")
    first_type_atack = pok_2.calculate_weakness(pok_1, pok_1.first_type())
    type_1 = pok_1.first_type().upper()
    type_2 = pok_1.second_type().upper()
    if pok_1.second_type() != "":
        second_type_attack = pok_2.calculate_weakness(
            pok_1, pok_1.second_type()
        )
    if move == Moves.ATTACK:
        if normal_type_attack == 1:
            text = f"{pok_1.name()} USED NORMAL ATTACK ON {pok_2.name()}..."\
                f"{pok_2.name()} HAS {pok_2.hp()} LEFT "
        if normal_type_attack > 1:
            text = f"{pok_1.name()} USED NORMAL ATTACK ON " \
                f"{pok_2.name()}. IT WAS SUPER EFFECTIVE..."\
                f"{pok_2.name()} HAS {pok_2.hp()} LEFT "
        if normal_type_attack < 1:
            text = f"{pok_1.name()} USED NORMAL ATTACK ON {pok_2.name()}." \
                " IT WAS NOT VERY EFFECTIVE..."\
                f"{pok_2.name()} HAS {pok_2.hp()} LEFT "
    elif move == Moves.TYPE_1:
        if first_type_atack == 1:
            text = f"{pok_1.name()} USED {type_1}"\
                f" TYPE ATTACK ON {pok_2.name()}..."\
                f"{pok_2.name()} HAS {pok_2.hp()} LEFT "
        if first_type_atack > 1:
            text = f"{pok_1.name()} USED {type_1} TYPE ATTACK" \
                f" ON {pok_2.name()}. IT WAS SUPER EFFECTIVE..."\
                f"{pok_2.name()} HAS {pok_2.hp()} LEFT "
        if first_type_atack < 1:
            text = f"{pok_1.name()} USED {type_1} TYPE ATTACK" \
                f" ON {pok_2.name()}. IT WAS NOT VERY EFFECTIVE..."\
                f"{pok_2.name()} HAS {pok_2.hp()} LEFT "
    elif move == Moves.TYPE_2:
        if second_type_attack == 1:
            text = f"{pok_1.name()} USED {type_2}" \
                f" TYPE ATTACK ON {pok_2.name()}..."\
                f"{pok_2.name()} HAS {pok_2.hp()} LEFT "
        if second_type_attack > 1:
            text = f"{pok_1.name()} USED {type_2} TYPE ATTACK" \
                f" ON {pok_2.name()}. IT WAS SUPER EFFECTIVE..."\
                f"{pok_2.name()} HAS {pok_2.hp()} LEFT "
        if second_type_attack < 1:
            text = f"{pok_1.name()} USED {type_2} TYPE ATTACK" \
                f" ON {pok_2.name()}. IT WAS NOT VERY EFFECTIVE..."\
                f"{pok_2.name()} HAS {pok_2.hp()} LEFT "
    elif move == Moves.DEFEND:
        text = f"DEFENSE OF {pok_1.name()} ROSE BY 10%..."
        pass
    else:
        text = f"{player.name()} IS SWITCHING POKEMON...." \
            f"{player.current_pokemon().name()} IS ENTERING THE BATTLEFIELD..."
    return text


def indication_of_winner(player_1: object, player_2: object):
    """Functon that return tuple in form (winner, loser)"""
    if len(player_1.alive_pokemons_in_team()) != 0:
        return player_1, player_2
    else:
        return player_2, player_1


def output_of_winner(player_1: object, player_2: object):
    """Function that return text with information who won the game"""
    winner = indication_of_winner(player_1, player_2)[0]
    loser = indication_of_winner(player_1, player_2)[1]
    return f"\nALL POKEMONS OF {loser.name()} ARE UNABLE TO FIGHT." \
        f"\nTHE WINNER IS {winner.name()} "


def amount_of_pokemons_in_team():
    """Returns a number between 1-6. It's an amount of pokemons in team"""
    delayed_print("SELECT AMOUNT OF POKEMON IN TEAM\n")
    try:
        amount = int(input())
        if amount in range(1, 7):
            clear()
            return amount
        else:
            delayed_print("PLEASE SELECT A NUMBER BETWEEN 1-6\n")
            return amount_of_pokemons_in_team()
    except ValueError:
        delayed_print("PLEASE SELECT A NUMBER BETWEEN 1-6\n")
        return amount_of_pokemons_in_team()


def choose_letter_of_pokemon(list_of_pokemons: list):
    """Function that allow player to enter letter from the alphabet
    and then it show all pokemon whose name starts with this letter"""
    delayed_print("CHOOSE THE FIRST LETTER OF POKEMON : ")
    letter = input().upper()
    alphabet = list(string.ascii_uppercase)
    if len(letter) == 1:
        if letter in alphabet:
            return letter
        else:
            delayed_print("IT'S NOT A LETTER\n")
            return choose_letter_of_pokemon(list_of_pokemons)
    else:
        delayed_print("YOU HAVE TO ENTER ONLY 1 LETTER\n")
        return choose_letter_of_pokemon(list_of_pokemons)


def show_pokemons(letter: str, list_of_pokemons: list):
    """Function that show all pokemons whose name starts
    with certain letter"""
    print(
        "| %-20s | %-10s | %-10s | %-10s | %-12s | %-15s" %
        ("NAME", "ATTACK", "DEFENSE", "HP", "SPEED", "TYPES")
    )
    print("-" * 92)
    text = ""
    for pokemon in list_of_pokemons:
        if pokemon[0][0] == letter:
            text += (
                "| %-20s | %-10s | %-10s | %-10s | %-12s | %-15s" %
                (pokemon[0].upper(), pokemon[1],  pokemon[2], pokemon[3],
                 pokemon[4], pokemon[5].upper() + " " + pokemon[6].upper())
            )
            text += "\n"
    return text


def enter_pokemon_name(list_of_names: list):
    """Function that return name of pokemon
    only if the name is entered correctly"""
    delayed_print("ENTER POKEMON NAME : ")
    pokemon_name = input().title()
    if pokemon_name in list_of_names:
        return pokemon_name
    else:
        delayed_print("YOU ENTER WRONG NAME\n")
        return enter_pokemon_name(list_of_names)


def create_team(
    amount_of_pokemons,
    list_of_pokemons,
    list_of_names):
    """Function that allow to create team of pokemons by
    entering their names"""
    team = []
    for i in range(0, amount_of_pokemons):
        letter = choose_letter_of_pokemon(list_of_pokemons)
        print(show_pokemons(letter, list_of_pokemons))
        pokemon_name = enter_pokemon_name(list_of_names)
        for stats in list_of_pokemons:
            name, atack, defense, hp, speed, type1, type2, weakness = stats
            if pokemon_name == name:
                pokemon = Pokemon(
                    name,
                    atack,
                    defense,
                    hp,
                    speed,
                    type1,
                    type2,
                    weakness
                    )
                team.append(pokemon)
                clear()
    return team


def enter_name():
    """Function that returns players name"""
    delayed_print("ENTER YOUR NAME: ")
    name = input().upper()
    if name != "":
        return name
    else:
        delayed_print("YOU HAVE TO ENTER THE NAME!\n")
        return enter_name()

from moves import Moves, Outputs
from interface import output_of_battle, output_of_winner
from random import randint
from interface import (
    delayed_print, clear, create_team, chose_pokemon, show_options,
    choose_move, enter_name
    )
from pokemon_file import read_from_file
from time import sleep


list_of_pokemons = read_from_file("pokemon.csv")[0]
list_of_names = read_from_file("pokemon.csv")[1]


class Game:
    """
    Class game. Contains all the methods needed to determine
    the course of the round and whole battle.
    """
    def __init__(self):
        pass

    def create_player(self, amount_of_pokemons: int):
        """Function that returns name and team of a player"""
        name = enter_name()
        delayed_print(f'\n{name} PLEASE CHOOSE YOUR TEAM\n')
        team = create_team(amount_of_pokemons, list_of_pokemons, list_of_names)
        clear()
        return (name, team)

    def selection_of_starting_poekmon(self, player: object):
        """Function that returns text about player's starting pokemon"""
        delayed_print(f"{player.name()} PLEASE CHOSE YOUR STARTING POKEMON\n")
        pokemon_1_index = chose_pokemon(player)
        player.set_pokemon(pokemon_1_index)
        name = player.current_pokemon().name()
        text = f"\n{player.name()} CHOSE {name} AS FIRST POKEMON"
        clear()
        return text

    def check_is_there_a_winner(self, player_1: object, player_2: object):
        """
        Function that checks if both player's have alive pokemons in their
        teams
        """
        team_1 = player_1.alive_pokemons_in_team()
        team_2 = player_2.alive_pokemons_in_team()
        if len(team_1) != 0 and len(team_2) != 0:
            return False
        else:
            return True

    def evaluate_move(self, player_1, player_2, move):
        """Method that evaluate move of pokemon"""
        pokemon = player_1.current_pokemon()
        enemy_pokemon = player_2.current_pokemon()
        if move == Moves.ATTACK:
            pokemon.attack_pokemon(enemy_pokemon, "normal")
        elif move == Moves.TYPE_1:
            pokemon.attack_pokemon(enemy_pokemon, pokemon.first_type())
        elif move == Moves.TYPE_2:
            pokemon.attack_pokemon(enemy_pokemon, pokemon.second_type())
        elif move == Moves.DEFEND:
            pokemon.reinforcment()
        elif move == Moves.SWITCH:
            pass

    def who_is_faster(
        self, player_1: object, player_2: object, player_1_move: object,
        player_2_move: object, switch_1: int, switch_2: int
    ):
        """
        Functions receive both players, theirs moves and
        values of switch in the case they would like
        change pokemos
        Chceks which of players current pokemon is faster
        and it returns tuple of data
        ((faster_player, faster_move, faster_swtch),
        (slower_player, slower_move, slower_switch))
        """
        pokemon_1 = player_1.current_pokemon()
        pokemon_2 = player_2.current_pokemon()
        if pokemon_1.speed() > pokemon_2.speed():
            return (
                (player_1, player_1_move, switch_1),
                (player_2, player_2_move, switch_2)
                )
        elif pokemon_1.speed() < pokemon_2.speed():
            return (
                (player_2, player_2_move, switch_2),
                (player_1, player_1_move, switch_1)
                )
        else:
            starting_number = randint(1, 2)
            if starting_number == 1:
                return (
                    (player_1, player_1_move, switch_1),
                    (player_2, player_2_move, switch_2)
                    )
            else:
                return (
                    (player_2, player_2_move, switch_2),
                    (player_1, player_1_move, switch_1)
                    )

    def round(
        self, faster_player: object,
        slower_player: object, faster_pokemon_move: object,
        slower_pokemon_move: object, faster_switch: int,
        slower_switch: int
    ):
        """
        Based on informations about both player's move, returns one
        out of 8 possible outcomes of battle. More info about possible
        outcomes is in file moves.py
        """
        if (
            faster_pokemon_move == Moves.SWITCH and
            slower_pokemon_move != Moves.SWITCH
        ):
            faster_player.set_pokemon(faster_switch)
            self.evaluate_move(
                slower_player,
                faster_player,
                slower_pokemon_move
                )
            battle_result = Outputs.OUTPUT_6
            if not faster_player.current_pokemon().is_alive():
                battle_result = Outputs.OUTPUT_4
        elif (
            slower_pokemon_move == Moves.SWITCH and
            faster_pokemon_move != Moves.SWITCH
        ):
            self.evaluate_move(
                faster_player,
                slower_player,
                faster_pokemon_move
                )
            if slower_player.current_pokemon().is_alive():
                battle_result = Outputs.OUTPUT_7
                slower_player.set_pokemon(slower_switch)
            else:
                battle_result = Outputs.OUTPUT_5
                slower_player.set_pokemon(slower_switch)
        elif (
            faster_pokemon_move == Moves.SWITCH and
            slower_pokemon_move == Moves.SWITCH
        ):
            faster_player.set_pokemon(faster_switch)
            slower_player.set_pokemon(slower_switch)
            battle_result = Outputs.OUTPUT_8
        else:
            self.evaluate_move(
                faster_player, slower_player, faster_pokemon_move
                )
            if slower_player.current_pokemon().is_alive():
                self.evaluate_move(
                    slower_player, faster_player,
                    slower_pokemon_move
                    )
                battle_result = Outputs.OUTPUT_1
                if not faster_player.current_pokemon().is_alive():
                    battle_result = Outputs.OUTPUT_3
            else:
                battle_result = Outputs.OUTPUT_2
        return battle_result

    def battle(
        self, faster_player: object, slower_player: object,
        faster_move: object, slower_move: object, faster_switch: int,
        slower_switch: int
    ):
        """
        Returns tuple with text about what happend in round and result of
        this round. Result of rund allows to point the winner or give a signal
        to  one of the players that he has to change a dead pokemon
        """
        faster_pokemon = faster_player.current_pokemon()
        slower_pokemon = slower_player.current_pokemon()
        battle_result = self.round(
            faster_player, slower_player,
            faster_move,
            slower_move, faster_switch, slower_switch
            )
        if self.check_is_there_a_winner(faster_player, slower_player) is True:
            return (
                output_of_battle(
                    faster_player, slower_player, faster_pokemon,
                    slower_pokemon, faster_move, slower_move, battle_result),
                (output_of_winner(faster_player, slower_player))
                )
        else:
            return (output_of_battle(
                faster_player, slower_player, faster_pokemon, slower_pokemon,
                faster_move, slower_move, battle_result), battle_result)

    def play(self, player_1: object, player_2: object):
        """Function that allows to play in mode PLAYER VS PLAYER"""
        while self.check_is_there_a_winner(player_1, player_2) is False:
            sleep(2)
            clear()
            show_options(player_1)
            player_1_move = choose_move(player_1)
            if player_1_move == Moves.SWITCH:
                switch_1 = chose_pokemon(player_1)
            else:
                switch_1 = None
            clear()
            show_options(player_2)
            player_2_move = choose_move(player_2)
            if player_2_move == Moves.SWITCH:
                switch_2 = chose_pokemon(player_2)
            else:
                switch_2 = None
            clear()
            player_and_move = self.who_is_faster(
                player_1, player_2, player_1_move,
                player_2_move, switch_1, switch_2
                )
            faster_player = player_and_move[0][0]
            faster_move = player_and_move[0][1]
            slower_player = player_and_move[1][0]
            slower_move = player_and_move[1][1]
            faster_switch = player_and_move[0][2]
            slower_switch = player_and_move[1][2]
            result = self.battle(
                faster_player, slower_player, faster_move,
                slower_move, faster_switch, slower_switch
            )
            delayed_print(result[0])
            if result[1] == Outputs.OUTPUT_2:
                Id = slower_player.name()
                delayed_print(f"\n{Id} PLEASE CHOOSE YOUR NEXT POKEMON\n")
                switch_2 = chose_pokemon(slower_player)
                slower_player.set_pokemon(switch_2)
            elif result[1] == Outputs.OUTPUT_3:
                Id = faster_player.name()
                delayed_print(f"\n{Id} PLEASE CHOOSE YOUR NEXT POKEMON\n")
                switch_1 = chose_pokemon(faster_player)
                faster_player.set_pokemon(switch_1)
            elif result[1] == Outputs.OUTPUT_4:
                Id = faster_player.name()
                delayed_print(f"\n{Id} PLEASE CHOOSE YOUR NEXT POKEMON\n")
                switch_1 = chose_pokemon(faster_player)
                faster_player.set_pokemon(switch_1)
            elif result[1] == output_of_winner(player_1, player_2):
                delayed_print(result[1])

    def play_against_computer(self, player_1: object, computer: object):
        """Function that allows to play in mode PLAYER VS COMPUTER"""
        while self.check_is_there_a_winner(player_1, computer) is False:
            sleep(2)
            clear()
            show_options(player_1)
            player_1_move = choose_move(player_1)
            if player_1_move == Moves.SWITCH:
                switch_1 = chose_pokemon(player_1)
            else:
                switch_1 = None
            clear()
            computer_move = computer.SI_pick_move(player_1)
            if computer_move == Moves.SWITCH:
                computer_switch = computer.pokemon_to_switch()
            else:
                computer_switch = None
            player_and_move = self.who_is_faster(
                player_1, computer, player_1_move,
                computer_move, switch_1, computer_switch
                )
            faster_player = player_and_move[0][0]
            faster_move = player_and_move[0][1]
            slower_player = player_and_move[1][0]
            slower_move = player_and_move[1][1]
            faster_switch = player_and_move[0][2]
            slower_switch = player_and_move[1][2]
            result = self.battle(
                faster_player, slower_player, faster_move,
                slower_move, faster_switch, slower_switch
            )
            delayed_print(result[0])
            if result[1] == Outputs.OUTPUT_2:
                if computer == slower_player:
                    delayed_print("\nCOMPUTER IS SWITCHING POKEMON\n")
                    index = computer.pokemon_to_switch()
                    computer.SI_SWITCH(index)
                else:
                    Id = slower_player.name()
                    delayed_print(f"\n{Id} PLEASE CHOOSE YOUR NEXT POKEMON\n")
                    switch_2 = chose_pokemon(slower_player)
                    slower_player.set_pokemon(switch_2)
            elif result[1] == Outputs.OUTPUT_3:
                if computer == faster_player:
                    delayed_print("\nCOMPUTER IS SWITCHING POKEMON\n")
                    index = computer.pokemon_to_switch()
                    computer.SI_SWITCH(index)
                else:
                    Id = faster_player.name()
                    delayed_print(f"\n{Id} PLEASE CHOOSE YOUR NEXT POKEMON\n")
                    switch_1 = chose_pokemon(faster_player)
                    faster_player.set_pokemon(switch_1)
            elif result[1] == Outputs.OUTPUT_4:
                if computer == faster_player:
                    delayed_print("\nCOMPUTER IS SWITCHING POKEMON\n")
                    index = computer.pokemon_to_switch()
                    computer.SI_SWITCH(index)
                else:
                    Id = faster_player.name()
                    delayed_print(f"\n{Id} PLEASE CHOOSE YOUR NEXT POKEMON\n")
                    switch_1 = chose_pokemon(faster_player)
                    faster_player.set_pokemon(switch_1)
            elif result[1] == output_of_winner(player_1, computer):
                delayed_print(result[1])

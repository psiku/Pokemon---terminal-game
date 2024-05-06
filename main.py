from game import Game
from player import Player
from time import sleep
from pokemon import Pokemon
from interface import (
    clear, delayed_print, chose_game_mode,
    amount_of_pokemons_in_team

    )
from computer import Computer
from pokemon_file import read_from_file


list_of_pokemons = read_from_file("pokemon.csv")[0]
list_of_names = read_from_file("pokemon.csv")[1]


if __name__ == "__main__":

    game = Game()
    computer = Computer(team=[])
    
    delayed_print("WELCOME TO THE POKEMON BATTLE SIMULATOR\n")
    game_mode = chose_game_mode()
    amount_of_pokemons = amount_of_pokemons_in_team()
    player_1_info = game.create_player(amount_of_pokemons)
    player_1 = Player(player_1_info[0], player_1_info[1])
    if game_mode == 1:
        player_2_info = game.create_player(amount_of_pokemons)
        player_2 = Player(player_2_info[0], player_2_info[1])
        game.selection_of_starting_poekmon(player_1)
        game.selection_of_starting_poekmon(player_2)
        game.play(player_1, player_2)
    if game_mode == 2:
        delayed_print("COMPUTER IS CHOSING TEAM\n")
        computer.SI_pick_team(amount_of_pokemons, list_of_pokemons)
        sleep(2)
        clear()
        game.selection_of_starting_poekmon(player_1)
        computer.set_starting_pokemon(0)
        computer_name = computer._current_pokemon.name().upper()
        delayed_print(f"COMPUTER CHOSE {computer_name} AS FIRST POKEMON")
        sleep(2)
        game.play_against_computer(player_1, computer)

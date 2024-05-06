from player import Player
from pokemon import Pokemon
import pytest


def test_create_player_NameError():
    team = []
    p1 = Pokemon(
        'Bulbasaur', 49, 49, 45, 45, 'grass', 'poison',
        ('1', '1', '1', '0.5', '0.5', '0.5', '2', '2', '1', '0.25', '1', '2',
         '1', '1', '2', '1', '1', '0.5'))
    team.append(p1)
    with pytest.raises(NameError):
        Player("", team)


def test_create_player():
    team = []
    p1 = Pokemon(
        'Bulbasaur', 49, 49, 45, 45, 'grass', 'poison',
        ('1', '1', '1', '0.5', '0.5', '0.5', '2', '2', '1', '0.25', '1', '2',
         '1', '1', '2', '1', '1', '0.5'))
    team.append(p1)
    player = Player("ASH", team)
    assert player.name() == "ASH"
    assert player.team() == team


def test_all_pokemons_in_team_are_alive():
    team = []
    p1 = Pokemon(
        'Bulbasaur', 49, 49, 45, 45, 'grass', 'poison',
        ('1', '1', '1', '0.5', '0.5', '0.5', '2', '2', '1', '0.25', '1', '2',
         '1', '1', '2', '1', '1', '0.5'))
    p2 = Pokemon(
        'Bulbasaur', 49, 49, 45, 45, 'grass', 'poison',
        ('1', '1', '1', '0.5', '0.5', '0.5', '2', '2', '1', '0.25', '1', '2',
         '1', '1', '2', '1', '1', '0.5'))
    team.append(p1)
    team.append(p2)
    player = Player("ASH", team)
    alive_pokemons = player.alive_pokemons_in_team()
    assert len(alive_pokemons) == 2


def test_number_of_alive_pokemons_in_team():
    team = []
    p1 = Pokemon(
        'Bulbasaur', 49, 49, 45, 45, 'grass', 'poison',
        ('1', '1', '1', '0.5', '0.5', '0.5', '2', '2', '1', '0.25', '1', '2',
         '1', '1', '2', '1', '1', '0.5'))
    p2 = Pokemon(
        'Bulbasaur', 49, 49, 45, 45, 'grass', 'poison',
        ('1', '1', '1', '0.5', '0.5', '0.5', '2', '2', '1', '0.25', '1', '2',
         '1', '1', '2', '1', '1', '0.5'))
    team.append(p1)
    team.append(p2)
    player = Player("ASH", team)
    alive_pokemons = player.alive_pokemons_in_team()
    assert len(alive_pokemons) == 2
    p2.take_damage(70)
    alive_pokemons = player.alive_pokemons_in_team()
    assert len(alive_pokemons) == 1


def test_not_active_pokemon():
    team = []
    p1 = Pokemon(
        'Bulbasaur', 49, 49, 45, 45, 'grass', 'poison',
        ('1', '1', '1', '0.5', '0.5', '0.5', '2', '2', '1', '0.25', '1', '2',
         '1', '1', '2', '1', '1', '0.5'))
    p2 = Pokemon(
        'Bulbasaur', 49, 49, 45, 45, 'grass', 'poison',
        ('1', '1', '1', '0.5', '0.5', '0.5', '2', '2', '1', '0.25', '1', '2',
         '1', '1', '2', '1', '1', '0.5'))
    team.append(p1)
    team.append(p2)
    player = Player("ASH", team)
    assert player.current_pokemon() is None


def test_active_pokemon():
    team = []
    p1 = Pokemon(
        'Bulbasaur', 49, 49, 45, 45, 'grass', 'poison',
        ('1', '1', '1', '0.5', '0.5', '0.5', '2', '2', '1', '0.25', '1', '2',
         '1', '1', '2', '1', '1', '0.5'))
    p2 = Pokemon(
        'Komala', '115', '65', '65', '65', 'normal', '',
        ('1', '1', '1', '1', '1', '2', '1', '1', '0', '1', '1', '1', '1',
         '1', '1', '1', '1', '1'))
    team.append(p1)
    team.append(p2)
    player = Player("ASH", team)
    player.set_pokemon(1)  # index - 1, więc 1 to tak naprawdę team[0]
    assert player.current_pokemon().name() == "BULBASAUR"
    player.set_pokemon(2)
    assert player.current_pokemon().name() == "KOMALA"

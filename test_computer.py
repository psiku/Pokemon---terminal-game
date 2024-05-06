from player import Player
from pokemon import Pokemon
from computer import Computer
from moves import Moves


def test_computer_pokemon_in_team_all_alive():
    p1 = Pokemon(
        'Bulbasaur', 49, 49, 45, 45, 'grass', 'poison',
        ('1', '1', '1', '0.5', '0.5', '0.5', '2', '2', '1', '0.25', '1', '2',
         '1', '1', '2', '1', '1', '0.5'))
    p2 = Pokemon(
        'Bulbasaur', 49, 49, 45, 45, 'grass', 'poison',
        ('1', '1', '1', '0.5', '0.5', '0.5', '2', '2', '1', '0.25', '1', '2',
         '1', '1', '2', '1', '1', '0.5'))
    team = []
    team.append(p1)
    team.append(p2)
    computer = Computer(team)

    assert len(computer.team()) == 2


def test_computer_pokemon_in_team_one_is_dead():
    p1 = Pokemon(
        'Bulbasaur', 49, 49, 45, 45, 'grass', 'poison',
        ('1', '1', '1', '0.5', '0.5', '0.5', '2', '2', '1', '0.25', '1', '2',
         '1', '1', '2', '1', '1', '0.5'))
    p2 = Pokemon(
        'Bulbasaur', 49, 49, 45, 45, 'grass', 'poison',
        ('1', '1', '1', '0.5', '0.5', '0.5', '2', '2', '1', '0.25', '1', '2',
         '1', '1', '2', '1', '1', '0.5'))
    team = []
    team.append(p1)
    team.append(p2)
    p2.take_damage(80)
    computer = Computer(team)

    assert len(computer.alive_pokemons_in_team()) == 1


def test_set_starting_pokemon():
    p1 = Pokemon(
        'Bulbasaur', 49, 49, 45, 45, 'grass', 'poison',
        ('1', '1', '1', '0.5', '0.5', '0.5', '2', '2', '1', '0.25', '1', '2',
         '1', '1', '2', '1', '1', '0.5'))
    p2 = Pokemon(
        'Komala', '115', '65', '65', '65', 'normal', '',
        ('1', '1', '1', '1', '1', '2', '1', '1', '0', '1', '1', '1', '1',
         '1', '1', '1', '1', '1'))

    team = []
    team.append(p1)
    team.append(p2)
    computer = Computer(team)
    computer.set_starting_pokemon(0)
    assert computer.current_pokemon() == computer.team()[0]
    computer.set_starting_pokemon(1)
    assert computer.current_pokemon() == computer.team()[1]


def test_pokemon_to_switch_active_pokemon_has_indeks_0():
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
    computer = Computer(team)
    computer.set_starting_pokemon(0)
    assert computer.pokemon_to_switch() == 1


def test_pokemon_to_switch_active_pokemon_has_indeks_0_and_index_2_is_dead():
    team = []
    p1 = Pokemon(
        'Bulbasaur', 49, 49, 45, 45, 'grass', 'poison',
        ('1', '1', '1', '0.5', '0.5', '0.5', '2', '2', '1', '0.25', '1', '2',
         '1', '1', '2', '1', '1', '0.5'))
    p2 = Pokemon(
        'Komala', '115', '65', '65', '65', 'normal', '',
        ('1', '1', '1', '1', '1', '2', '1', '1', '0', '1', '1', '1', '1',
         '1', '1', '1', '1', '1'))
    p3 = Pokemon(
            'Stich', '115', '65', '65', '65', 'normal', '',
            ('1', '1', '1', '1', '1', '2', '1', '1', '0', '1', '1', '1', '1',
             '1', '1', '1', '1', '1'))
    p4 = Pokemon(
        'Archen', '112', '45', '55', '70', 'rock', 'flying',
        ('0.5', '1', '1', '2', '1', '1', '0.5', '0.5', '1', '1', '0', '2',
         '0.5', '0.5', '1', '2', '2', '2'))
    team.append(p1)
    team.append(p2)
    team.append(p3)
    team.append(p4)
    p3.take_damage(100)
    p4.take_damage(1000)
    computer = Computer(team)
    computer.set_starting_pokemon(0)
    assert computer.pokemon_to_switch() == 1


def test_SI_SWITCH_when_one_out_of_3_pokemons_is_dead():
    p1 = Pokemon(
        'Bulbasaur', 49, 49, 45, 45, 'grass', 'poison',
        ('1', '1', '1', '0.5', '0.5', '0.5', '2', '2', '1', '0.25', '1', '2',
         '1', '1', '2', '1', '1', '0.5'))
    p2 = Pokemon(
        'Komala', '115', '65', '65', '65', 'normal', '',
        ('1', '1', '1', '1', '1', '2', '1', '1', '0', '1', '1', '1', '1',
         '1', '1', '1', '1', '1'))
    p3 = Pokemon(
        'Stich', '115', '65', '65', '65', 'normal', '',
        ('1', '1', '1', '1', '1', '2', '1', '1', '0', '1', '1', '1', '1',
         '1', '1', '1', '1', '1'))
    team = []
    team.append(p1)
    team.append(p2)
    team.append(p3)
    computer = Computer(team)
    p3.take_damage(120)
    computer.set_starting_pokemon(1)
    assert computer.current_pokemon().name() == "KOMALA"
    indeks = computer.pokemon_to_switch()
    computer.SI_SWITCH(indeks)
    assert computer.current_pokemon().name() == "BULBASAUR"


def test_SI_calculate_attack_weaknes():
    p1 = Pokemon(
        'Bulbasaur', 49, 49, 45, 45, 'grass', 'poison',
        ('1', '1', '1', '0.5', '0.5', '0.5', '2', '2', '1', '0.25', '1', '2',
         '1', '1', '2', '1', '1', '0.5'))
    p2 = Pokemon(
        'Komala', '115', '65', '65', '65', 'normal', '',
        ('1', '1', '1', '1', '1', '2', '1', '1', '0', '1', '1', '1', '1',
         '1', '1', '1', '1', '1'))

    p3 = Pokemon(
        'Archen', '112', '45', '55', '70', 'rock', 'flying',
        ('0.5', '1', '1', '2', '1', '1', '0.5', '0.5', '1', '1', '0', '2',
         '0.5', '0.5', '1', '2', '2', '2'))

    p4 = Pokemon(
        'Emboar', '123', '65', '110', '65', 'fire', 'fighting',
        ('0.25', '0.5', '1', '1', '1', '1', '0.5', '2', '1', '0.5', '2',
         '0.5', '1', '1', '2', '1', '0.5', '2'))

    player_team = [p1, p2]
    computer_team = [p3, p4]
    player = Player("KUBA", player_team)
    computer = Computer(computer_team)
    player.set_pokemon(1)
    computer.set_starting_pokemon(1)
    weakness = computer.SI_calculate_attack_weakness(player)
    assert weakness == [1, 1, 0.5]


def test_SI_calculate_attack_effectivnes():
    p1 = Pokemon(
        'Bulbasaur', 49, 49, 45, 45, 'grass', 'poison',
        ('1', '1', '1', '0.5', '0.5', '0.5', '2', '2', '1', '0.25', '1', '2',
         '1', '1', '2', '1', '1', '0.5'))
    p2 = Pokemon(
        'Komala', '115', '65', '65', '65', 'normal', '',
        ('1', '1', '1', '1', '1', '2', '1', '1', '0', '1', '1', '1', '1',
         '1', '1', '1', '1', '1'))

    p3 = Pokemon(
        'Archen', '112', '45', '55', '70', 'rock', 'flying',
        ('0.5', '1', '1', '2', '1', '1', '0.5', '0.5', '1', '1', '0', '2',
         '0.5', '0.5', '1', '2', '2', '2'))

    p4 = Pokemon(
        'Emboar', '123', '65', '110', '65', 'fire', 'fighting',
        ('0.25', '0.5', '1', '1', '1', '1', '0.5', '2', '1', '0.5', '2',
         '0.5', '1', '1', '2', '1', '0.5', '2'))

    player_team = [p1, p2]
    computer_team = [p3, p4]
    player = Player("KUBA", player_team)
    computer = Computer(computer_team)
    player.set_pokemon(1)
    computer.set_starting_pokemon(1)
    effectivness = computer.SI_calculate_attack_effectivness(player)
    assert effectivness == {'fire': 2.0, "fighting": 0.5, 'normal': 1.0}


def test_SI_calculate_attack_effectivnes_another_example():
    p1 = Pokemon(
        'Bulbasaur', 49, 49, 45, 45, 'grass', 'poison',
        ('1', '1', '1', '0.5', '0.5', '0.5', '2', '2', '1', '0.25', '1', '2',
         '1', '1', '2', '1', '1', '0.5'))
    p2 = Pokemon(
        'Komala', '115', '65', '65', '65', 'normal', '',
        ('1', '1', '1', '1', '1', '2', '1', '1', '0', '1', '1', '1', '1',
         '1', '1', '1', '1', '1'))

    p3 = Pokemon(
        'Archen', '112', '45', '55', '70', 'rock', 'flying',
        ('0.5', '1', '1', '2', '1', '1', '0.5', '0.5', '1', '1', '0', '2',
         '0.5', '0.5', '1', '2', '2', '2'))

    p4 = Pokemon(
        'Emboar', '123', '65', '110', '65', 'fire', 'fighting',
        ('0.25', '0.5', '1', '1', '1', '1', '0.5', '2', '1', '0.5', '2',
         '0.5', '1', '1', '2', '1', '0.5', '2'))

    player_team = [p1, p2]
    computer_team = [p3, p4]
    player = Player("KUBA", player_team)
    computer = Computer(computer_team)
    player.set_pokemon(1)
    # IT"S DIFFERENT METHOD (number 1 measns it is the  first pokemon  in list)
    computer.set_starting_pokemon(0)
    assert computer.current_pokemon().name() == "ARCHEN"
    assert player.current_pokemon().name() == "BULBASAUR"
    effectivness = computer.SI_calculate_attack_effectivness(player)
    assert effectivness == {'rock': 1.0, "flying": 2.0, 'normal': 1.0}


def test_SI_pick_move():
    p1 = Pokemon(
        'Bulbasaur', 49, 49, 45, 45, 'grass', 'poison',
        ('1', '1', '1', '0.5', '0.5', '0.5', '2', '2', '1', '0.25', '1', '2',
         '1', '1', '2', '1', '1', '0.5'))
    p2 = Pokemon(
        'Komala', '115', '65', '65', '65', 'normal', '',
        ('1', '1', '1', '1', '1', '2', '1', '1', '0', '1', '1', '1', '1',
         '1', '1', '1', '1', '1'))

    p3 = Pokemon(
        'Archen', '112', '45', '55', '70', 'rock', 'flying',
        ('0.5', '1', '1', '2', '1', '1', '0.5', '0.5', '1', '1', '0', '2',
         '0.5', '0.5', '1', '2', '2', '2'))

    p4 = Pokemon(
        'Emboar', '123', '65', '110', '65', 'fire', 'fighting',
        ('0.25', '0.5', '1', '1', '1', '1', '0.5', '2', '1', '0.5', '2',
         '0.5', '1', '1', '2', '1', '0.5', '2'))

    player_team = [p1, p2]
    computer_team = [p3, p4]
    player = Player("KUBA", player_team)
    computer = Computer(computer_team)
    player.set_pokemon(1)
    computer.set_starting_pokemon(1)
    # Fire is 2x effective against grass types, so computer should use
    # fire attack - fire is Emboar's first type
    assert computer.SI_pick_move(player) == Moves.TYPE_1


def test_SI_pick_move_switch():
    p1 = Pokemon(
        'Bulbasaur', 49, 49, 45, 45, 'grass', 'poison',
        ('1', '1', '1', '0.5', '0.5', '0.5', '2', '2', '1', '0.25', '1', '2',
         '1', '1', '2', '1', '1', '0.5'))
    p2 = Pokemon(
        'Komala', '115', '65', '65', '65', 'normal', '',
        ('1', '1', '1', '1', '1', '2', '1', '1', '0', '1', '1', '1', '1',
         '1', '1', '1', '1', '1'))

    p3 = Pokemon(
        'Archen', '112', '45', '55', '70', 'rock', 'flying',
        ('0.5', '1', '1', '2', '1', '1', '0.5', '0.5', '1', '1', '0', '2',
         '0.5', '0.5', '1', '2', '2', '2'))

    p4 = Pokemon(
        'Emboar', '123', '65', '110', '65', 'fire', 'fighting',
        ('0.25', '0.5', '1', '1', '1', '1', '0.5', '2', '1', '0.5', '2',
         '0.5', '1', '1', '2', '1', '0.5', '2'))

    player_team = [p3, p4]
    computer_team = [p1, p2]
    player = Player("KUBA", player_team)
    computer = Computer(computer_team)
    player.set_pokemon(2)
    computer.set_starting_pokemon(0)
    # Bulbasaur is weak against fire types so computer should use move switch
    assert computer.SI_pick_move(player) == Moves.SWITCH


def test_SI_pick_move_computer_cannot_switch():
    # Bulbasaur is weak against fire types so computer should use move
    # switch but has only one pokemon left so computer have to attack or defend
    # Bulbasaur will not use special attack, because it would be as
    # effective as normal atack so computer picks the first option
    p1 = Pokemon(
        'Bulbasaur', 49, 49, 45, 45, 'grass', 'poison',
        ('1', '1', '1', '0.5', '0.5', '0.5', '2', '2', '1', '0.25', '1', '2',
         '1', '1', '2', '1', '1', '0.5'))
    p2 = Pokemon(
        'Komala', '115', '65', '65', '65', 'normal', '',
        ('1', '1', '1', '1', '1', '2', '1', '1', '0', '1', '1', '1', '1',
         '1', '1', '1', '1', '1'))

    p3 = Pokemon(
        'Archen', '112', '45', '55', '70', 'rock', 'flying',
        ('0.5', '1', '1', '2', '1', '1', '0.5', '0.5', '1', '1', '0', '2',
         '0.5', '0.5', '1', '2', '2', '2'))

    p4 = Pokemon(
        'Emboar', '123', '65', '110', '65', 'fire', 'fighting',
        ('0.25', '0.5', '1', '1', '1', '1', '0.5', '2', '1', '0.5', '2',
         '0.5', '1', '1', '2', '1', '0.5', '2'))

    player_team = [p3, p4]
    computer_team = [p1, p2]
    player = Player("KUBA", player_team)
    computer = Computer(computer_team)
    player.set_pokemon(2)
    computer.set_starting_pokemon(0)
    p2.take_damage(300)
    assert computer.SI_pick_move(player) in [Moves.ATTACK, Moves.DEFEND]

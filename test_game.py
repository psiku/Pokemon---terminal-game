from game import Game
from pokemon import Pokemon
from player import Player
from moves import Moves
from moves import Outputs


def test_check_is_there_a_winner_false():
    game = Game()
    team1 = []
    team2 = []
    p1 = Pokemon(
        'Bulbasaur', 49, 49, 45, 45, 'grass', 'poison',
        ('1', '1', '1', '0.5', '0.5', '0.5', '2', '2', '1', '0.25', '1', '2',
         '1', '1', '2', '1', '1', '0.5'))
    team1.append(p1)
    player1 = Player("ASH", team1)

    p2 = Pokemon(
        'Komala', '115', '65', '65', '65', 'normal', '',
        ('1', '1', '1', '1', '1', '2', '1', '1', '0', '1', '1', '1', '1',
         '1', '1', '1', '1', '1'))
    team2.append(p2)
    player2 = Player("JOHN", team2)
    assert game.check_is_there_a_winner(player1, player2) is False


def test_check_is_there_a_winner_True():
    game = Game()
    team1 = []
    team2 = []
    p1 = Pokemon(
        'Bulbasaur', 49, 49, 45, 45, 'grass', 'poison',
        ('1', '1', '1', '0.5', '0.5', '0.5', '2', '2', '1', '0.25', '1', '2',
         '1', '1', '2', '1', '1', '0.5'))
    team1.append(p1)
    player1 = Player("ASH", team1)

    p2 = Pokemon(
        'Komala', '115', '65', '65', '65', 'normal', '',
        ('1', '1', '1', '1', '1', '2', '1', '1', '0', '1', '1', '1', '1',
         '1', '1', '1', '1', '1'))
    team2.append(p2)
    player2 = Player("JOHN", team2)
    player2.set_pokemon(1)
    player2.current_pokemon().take_damage(123)
    assert len(player2.alive_pokemons_in_team()) == 0
    assert game.check_is_there_a_winner(player1, player2) is True


def test_who_is_faster_player_2_is_faster():
    game = Game()
    team1 = []
    team2 = []
    p1 = Pokemon(
        'Bulbasaur', 49, 49, 45, 45, 'grass', 'poison',
        ('1', '1', '1', '0.5', '0.5', '0.5', '2', '2', '1', '0.25', '1', '2',
         '1', '1', '2', '1', '1', '0.5'))
    team1.append(p1)
    player1 = Player("ASH", team1)
    player1.set_pokemon(1)

    p2 = Pokemon(
        'Komala', '115', '65', '65', '65', 'normal', '',
        ('1', '1', '1', '1', '1', '2', '1', '1', '0', '1', '1', '1', '1',
         '1', '1', '1', '1', '1'))
    team2.append(p2)
    player2 = Player("JOHN", team2)
    player2.set_pokemon(1)
    player1_move = Moves.ATTACK
    player2_move = Moves.DEFEND
    switch1 = None
    switch2 = None
    result = game.who_is_faster(
        player1, player2, player1_move,
        player2_move, switch1, switch2
        )
    assert result == (
        (player2, player2_move, switch2),
        (player1, player1_move, switch1)
        )


def test_who_is_faster_player_1_is_faster():
    game = Game()
    team1 = []
    team2 = []
    p2 = Pokemon(
        'Bulbasaur', 49, 49, 45, 45, 'grass', 'poison',
        ('1', '1', '1', '0.5', '0.5', '0.5', '2', '2', '1', '0.25', '1', '2',
         '1', '1', '2', '1', '1', '0.5'))
    team2.append(p2)
    player2 = Player("ASH", team2)
    player2.set_pokemon(1)

    p1 = Pokemon(
        'Komala', '115', '65', '65', '65', 'normal', '',
        ('1', '1', '1', '1', '1', '2', '1', '1', '0', '1', '1', '1', '1',
         '1', '1', '1', '1', '1'))
    team1.append(p1)
    player1 = Player("JOHN", team1)
    player1.set_pokemon(1)
    player1_move = Moves.ATTACK
    player2_move = Moves.DEFEND
    switch1 = None
    switch2 = None
    result = game.who_is_faster(
        player1, player2, player1_move,
        player2_move, switch1, switch2
        )
    assert result == (
        (player1, player1_move, switch1),
        (player2, player2_move, switch2)
        )


def test_round_OUTPUT_1():
    game = Game()
    team1 = []
    team2 = []
    p1 = Pokemon(
        'Bulbasaur', 49, 49, 45, 45, 'grass', 'poison',
        ('1', '1', '1', '0.5', '0.5', '0.5', '2', '2', '1', '0.25', '1', '2',
         '1', '1', '2', '1', '1', '0.5'))
    team1.append(p1)
    player1 = Player("ASH", team1)
    player1.set_pokemon(1)

    p2 = Pokemon(
        'Komala', '115', '65', '65', '65', 'normal', '',
        ('1', '1', '1', '1', '1', '2', '1', '1', '0', '1', '1', '1', '1',
         '1', '1', '1', '1', '1'))
    team2.append(p2)
    player2 = Player("JOHN", team2)
    player2.set_pokemon(1)
    player1_move = Moves.ATTACK
    player2_move = Moves.ATTACK
    switch1 = None
    switch2 = None
    result = game.round(
        player2, player1, player2_move, player1_move, switch2, switch1
        )
    assert result == Outputs.OUTPUT_1


def test_round_OUTPUT_8():
    game = Game()
    team1 = []
    team2 = []
    p1 = Pokemon(
        'Bulbasaur', 49, 49, 45, 45, 'grass', 'poison',
        ('1', '1', '1', '0.5', '0.5', '0.5', '2', '2', '1', '0.25', '1', '2',
         '1', '1', '2', '1', '1', '0.5'))
    p12 = Pokemon(
        'Bulbasaur', 49, 49, 45, 45, 'grass', 'poison',
        ('1', '1', '1', '0.5', '0.5', '0.5', '2', '2', '1', '0.25', '1', '2',
         '1', '1', '2', '1', '1', '0.5'))
    team1.append(p1)
    team1.append(p12)
    player1 = Player("ASH", team1)
    player1.set_pokemon(1)

    p2 = Pokemon(
        'Komala', '115', '65', '65', '65', 'normal', '',
        ('1', '1', '1', '1', '1', '2', '1', '1', '0', '1', '1', '1', '1',
         '1', '1', '1', '1', '1'))
    p22 = Pokemon(
        'Komala', '115', '65', '65', '65', 'normal', '',
        ('1', '1', '1', '1', '1', '2', '1', '1', '0', '1', '1', '1', '1',
         '1', '1', '1', '1', '1'))
    team2.append(p2)
    team2.append(p22)
    player2 = Player("JOHN", team2)
    player2.set_pokemon(1)
    player1_move = Moves.SWITCH
    player2_move = Moves.SWITCH
    switch1 = 2
    switch2 = 2
    result = game.round(
        player2, player1, player2_move, player1_move, switch2, switch1
        )
    assert result == Outputs.OUTPUT_8


def test_round_OUTPUT_4():
    game = Game()
    team1 = []
    team2 = []
    p1 = Pokemon(
        'Bulbasaur', 49, 49, 45, 45, 'grass', 'poison',
        ('1', '1', '1', '0.5', '0.5', '0.5', '2', '2', '1', '0.25', '1', '2',
         '1', '1', '2', '1', '1', '0.5'))
    p12 = Pokemon(
        'Bulbasaur', 49, 49, 45, 45, 'grass', 'poison',
        ('1', '1', '1', '0.5', '0.5', '0.5', '2', '2', '1', '0.25', '1', '2',
         '1', '1', '2', '1', '1', '0.5'))
    team1.append(p1)
    team1.append(p12)
    player1 = Player("ASH", team1)
    player1.set_pokemon(1)

    p2 = Pokemon(
        'Komala', '115', '65', '65', '65', 'normal', '',
        ('1', '1', '1', '1', '1', '2', '1', '1', '0', '1', '1', '1', '1',
         '1', '1', '1', '1', '1'))
    p22 = Pokemon(
        'Komala', '115', '65', '65', '65', 'normal', '',
        ('1', '1', '1', '1', '1', '2', '1', '1', '0', '1', '1', '1', '1',
         '1', '1', '1', '1', '1'))
    team2.append(p2)
    team2.append(p22)
    p22.set_hp(1)
    player2 = Player("JOHN", team2)
    player2.set_pokemon(2)
    player1_move = Moves.ATTACK
    player2_move = Moves.SWITCH
    switch1 = None
    switch2 = 2
    result = game.round(
        player2, player1, player2_move, player1_move, switch2, switch1
        )
    assert result == Outputs.OUTPUT_4


def test_round_OUTPUT_6():
    game = Game()
    team1 = []
    team2 = []
    p1 = Pokemon(
        'Bulbasaur', 49, 49, 45, 45, 'grass', 'poison',
        ('1', '1', '1', '0.5', '0.5', '0.5', '2', '2', '1', '0.25', '1', '2',
         '1', '1', '2', '1', '1', '0.5'))
    p12 = Pokemon(
        'Bulbasaur', 49, 49, 45, 45, 'grass', 'poison',
        ('1', '1', '1', '0.5', '0.5', '0.5', '2', '2', '1', '0.25', '1', '2',
         '1', '1', '2', '1', '1', '0.5'))
    team1.append(p1)
    team1.append(p12)
    player1 = Player("ASH", team1)
    player1.set_pokemon(1)

    p2 = Pokemon(
        'Komala', '115', '65', '65', '65', 'normal', '',
        ('1', '1', '1', '1', '1', '2', '1', '1', '0', '1', '1', '1', '1',
         '1', '1', '1', '1', '1'))
    p22 = Pokemon(
        'Komala', '115', '65', '65', '65', 'normal', '',
        ('1', '1', '1', '1', '1', '2', '1', '1', '0', '1', '1', '1', '1',
         '1', '1', '1', '1', '1'))
    team2.append(p2)
    team2.append(p22)
    player2 = Player("JOHN", team2)
    player2.set_pokemon(2)
    player1_move = Moves.ATTACK
    player2_move = Moves.SWITCH
    switch1 = None
    switch2 = 1
    result = game.round(
        player2, player1, player2_move, player1_move, switch2, switch1
        )
    assert result == Outputs.OUTPUT_6


def test_round_OUTPUT_3():
    game = Game()
    team1 = []
    team2 = []
    p1 = Pokemon(
        'Bulbasaur', 49, 49, 45, 45, 'grass', 'poison',
        ('1', '1', '1', '0.5', '0.5', '0.5', '2', '2', '1', '0.25', '1', '2',
         '1', '1', '2', '1', '1', '0.5'))
    p12 = Pokemon(
        'Bulbasaur', 49, 49, 45, 45, 'grass', 'poison',
        ('1', '1', '1', '0.5', '0.5', '0.5', '2', '2', '1', '0.25', '1', '2',
         '1', '1', '2', '1', '1', '0.5'))
    team1.append(p1)
    team1.append(p12)
    player1 = Player("ASH", team1)
    player1.set_pokemon(1)

    p2 = Pokemon(
        'Komala', '115', '65', '65', '65', 'normal', '',
        ('1', '1', '1', '1', '1', '2', '1', '1', '0', '1', '1', '1', '1',
         '1', '1', '1', '1', '1'))
    p22 = Pokemon(
        'Komala', '115', '65', '65', '65', 'normal', '',
        ('1', '1', '1', '1', '1', '2', '1', '1', '0', '1', '1', '1', '1',
         '1', '1', '1', '1', '1'))
    team2.append(p2)
    team2.append(p22)
    player2 = Player("JOHN", team2)
    player2.set_pokemon(2)
    p22.set_hp(1)
    player1_move = Moves.ATTACK
    player2_move = Moves.ATTACK
    switch1 = None
    switch2 = None
    result = game.round(
        player2, player1, player2_move, player1_move, switch2, switch1
        )
    assert result == Outputs.OUTPUT_3


def test_round_OUTPUT_2():
    game = Game()
    team1 = []
    team2 = []
    p1 = Pokemon(
        'Bulbasaur', 49, 49, 45, 45, 'grass', 'poison',
        ('1', '1', '1', '0.5', '0.5', '0.5', '2', '2', '1', '0.25', '1', '2',
         '1', '1', '2', '1', '1', '0.5'))
    p12 = Pokemon(
        'Bulbasaur', 49, 49, 45, 45, 'grass', 'poison',
        ('1', '1', '1', '0.5', '0.5', '0.5', '2', '2', '1', '0.25', '1', '2',
         '1', '1', '2', '1', '1', '0.5'))
    team1.append(p1)
    team1.append(p12)
    player1 = Player("ASH", team1)
    player1.set_pokemon(1)

    p2 = Pokemon(
        'Komala', '115', '65', '65', '65', 'normal', '',
        ('1', '1', '1', '1', '1', '2', '1', '1', '0', '1', '1', '1', '1',
         '1', '1', '1', '1', '1'))
    p22 = Pokemon(
        'Komala', '115', '65', '65', '65', 'normal', '',
        ('1', '1', '1', '1', '1', '2', '1', '1', '0', '1', '1', '1', '1',
         '1', '1', '1', '1', '1'))
    team2.append(p2)
    team2.append(p22)
    player2 = Player("JOHN", team2)
    player2.set_pokemon(2)
    p1.set_hp(1)
    player1_move = Moves.ATTACK
    player2_move = Moves.ATTACK
    switch1 = None
    switch2 = None
    result = game.round(
        player2, player1, player2_move, player1_move, switch2, switch1
        )
    assert result == Outputs.OUTPUT_2


def test_round_OUTPUT_5():
    game = Game()
    team1 = []
    team2 = []
    p1 = Pokemon(
        'Bulbasaur', 49, 49, 45, 45, 'grass', 'poison',
        ('1', '1', '1', '0.5', '0.5', '0.5', '2', '2', '1', '0.25', '1', '2',
         '1', '1', '2', '1', '1', '0.5'))
    p12 = Pokemon(
        'Bulbasaur', 49, 49, 45, 45, 'grass', 'poison',
        ('1', '1', '1', '0.5', '0.5', '0.5', '2', '2', '1', '0.25', '1', '2',
         '1', '1', '2', '1', '1', '0.5'))
    team1.append(p1)
    team1.append(p12)
    player1 = Player("ASH", team1)
    player1.set_pokemon(1)

    p2 = Pokemon(
        'Komala', '115', '65', '65', '65', 'normal', '',
        ('1', '1', '1', '1', '1', '2', '1', '1', '0', '1', '1', '1', '1',
         '1', '1', '1', '1', '1'))
    p22 = Pokemon(
        'Komala', '115', '65', '65', '65', 'normal', '',
        ('1', '1', '1', '1', '1', '2', '1', '1', '0', '1', '1', '1', '1',
         '1', '1', '1', '1', '1'))
    team2.append(p2)
    team2.append(p22)
    player2 = Player("JOHN", team2)
    player2.set_pokemon(1)
    p1.set_hp(1)
    player1_move = Moves.SWITCH
    player2_move = Moves.ATTACK
    switch1 = 2
    switch2 = None
    result = game.round(
        player2, player1, player2_move, player1_move, switch2, switch1
        )
    assert result == Outputs.OUTPUT_5


def test_round_OUTPUT_7():
    game = Game()
    team1 = []
    team2 = []
    p1 = Pokemon(
        'Bulbasaur', 49, 49, 45, 45, 'grass', 'poison',
        ('1', '1', '1', '0.5', '0.5', '0.5', '2', '2', '1', '0.25', '1', '2',
         '1', '1', '2', '1', '1', '0.5'))
    p12 = Pokemon(
        'Bulbasaur', 49, 49, 45, 45, 'grass', 'poison',
        ('1', '1', '1', '0.5', '0.5', '0.5', '2', '2', '1', '0.25', '1', '2',
         '1', '1', '2', '1', '1', '0.5'))
    team1.append(p1)
    team1.append(p12)
    player1 = Player("ASH", team1)
    player1.set_pokemon(1)

    p2 = Pokemon(
        'Komala', '115', '65', '65', '65', 'normal', '',
        ('1', '1', '1', '1', '1', '2', '1', '1', '0', '1', '1', '1', '1',
         '1', '1', '1', '1', '1'))
    p22 = Pokemon(
        'Komala', '115', '65', '65', '65', 'normal', '',
        ('1', '1', '1', '1', '1', '2', '1', '1', '0', '1', '1', '1', '1',
         '1', '1', '1', '1', '1'))
    team2.append(p2)
    team2.append(p22)
    player2 = Player("JOHN", team2)
    player2.set_pokemon(1)
    player1_move = Moves.SWITCH
    player2_move = Moves.ATTACK
    switch1 = 2
    switch2 = None
    result = game.round(
        player2, player1, player2_move, player1_move, switch2, switch1
        )
    assert result == Outputs.OUTPUT_7


def test_battle_result_boh_players_attack_using_normal_move():
    game = Game()
    team1 = []
    team2 = []
    p1 = Pokemon(
        'Bulbasaur', 49, 49, 45, 45, 'grass', 'poison',
        ('1', '1', '1', '0.5', '0.5', '0.5', '2', '2', '1', '0.25', '1', '2',
            '1', '1', '2', '1', '1', '0.5'))
    team1.append(p1)
    player1 = Player("ASH", team1)
    player1.set_pokemon(1)

    p2 = Pokemon(
        'Komala', '115', '65', '65', '65', 'normal', '',
        ('1', '1', '1', '1', '1', '2', '1', '1', '0', '1', '1', '1', '1',
            '1', '1', '1', '1', '1'))
    team2.append(p2)
    player2 = Player("JOHN", team2)
    player2.set_pokemon(1)
    player1_move = Moves.ATTACK
    player2_move = Moves.ATTACK
    switch1 = None
    switch2 = None
    round = game.battle(
        player2, player1, player2_move, player1_move, switch2, switch1
    )[0]
    hp_1 = player1.current_pokemon().hp()
    hp_2 = player2.current_pokemon().hp()
    text = f"KOMALA USED NORMAL ATTACK ON BULBASAUR...BULBASAUR HAS {hp_1}"\
        " LEFT \nBULBASAUR USED NORMAL ATTACK ON KOMALA...KOMALA HAS"\
        f" {hp_2} LEFT "
    assert round == text


def test_battle_result_boh_players_defend():
    game = Game()
    team1 = []
    team2 = []
    p1 = Pokemon(
        'Bulbasaur', 49, 49, 45, 45, 'grass', 'poison',
        ('1', '1', '1', '0.5', '0.5', '0.5', '2', '2', '1', '0.25', '1', '2',
            '1', '1', '2', '1', '1', '0.5'))
    team1.append(p1)
    player1 = Player("ASH", team1)
    player1.set_pokemon(1)

    p2 = Pokemon(
        'Komala', '115', '65', '65', '65', 'normal', '',
        ('1', '1', '1', '1', '1', '2', '1', '1', '0', '1', '1', '1', '1',
            '1', '1', '1', '1', '1'))
    team2.append(p2)
    player2 = Player("JOHN", team2)
    player2.set_pokemon(1)
    player1_move = Moves.DEFEND
    player2_move = Moves.DEFEND
    switch1 = None
    switch2 = None
    round = game.battle(
        player2, player1, player2_move, player1_move, switch2, switch1
    )[0]
    text = "DEFENSE OF KOMALA ROSE BY 10%..."\
        "\nDEFENSE OF BULBASAUR ROSE BY 10%..."
    assert round == text


def test_battle_result_boh_players_attack_using_normal_or_special_move():
    game = Game()
    team1 = []
    team2 = []
    p1 = Pokemon(
        'Bulbasaur', 49, 49, 45, 45, 'grass', 'poison',
        ('1', '1', '1', '0.5', '0.5', '0.5', '2', '2', '1', '0.25', '1', '2',
            '1', '1', '2', '1', '1', '0.5'))
    team1.append(p1)
    player1 = Player("ASH", team1)
    player1.set_pokemon(1)

    p2 = Pokemon(
        'Komala', '115', '65', '65', '65', 'normal', '',
        ('1', '1', '1', '1', '1', '2', '1', '1', '0', '1', '1', '1', '1',
            '1', '1', '1', '1', '1'))
    team2.append(p2)
    player2 = Player("JOHN", team2)
    player2.set_pokemon(1)
    player1_move = Moves.TYPE_1
    player2_move = Moves.ATTACK
    switch1 = None
    switch2 = None
    round = game.battle(
        player2, player1, player2_move, player1_move, switch2, switch1
    )[0]
    hp_1 = player1.current_pokemon().hp()
    hp_2 = player2.current_pokemon().hp()
    text = f"KOMALA USED NORMAL ATTACK ON BULBASAUR...BULBASAUR HAS {hp_1}"\
        f" LEFT \nBULBASAUR USED GRASS TYPE ATTACK ON KOMALA..."\
        f"KOMALA HAS {hp_2} LEFT "
    assert round == text


def test_battle_result_faster_switched_pokemon_and_slower_attacked():
    game = Game()
    team1 = []
    team2 = []
    p1 = Pokemon(
        'Bulbasaur', 49, 49, 45, 45, 'grass', 'poison',
        ('1', '1', '1', '0.5', '0.5', '0.5', '2', '2', '1', '0.25', '1', '2',
            '1', '1', '2', '1', '1', '0.5'))
    p12 = Pokemon(
        'Archen', '112', '45', '55', '70', 'rock', 'flying',
        ('0.5', '1', '1', '2', '1', '1', '0.5', '0.5', '1', '1', '0', '2',
         '0.5', '0.5', '1', '2', '2', '2'))

    team1.append(p1)
    team1.append(p12)
    player1 = Player("ASH", team1)
    player1.set_pokemon(1)

    p2 = Pokemon(
        'Komala', '115', '65', '65', '65', 'normal', '',
        ('1', '1', '1', '1', '1', '2', '1', '1', '0', '1', '1', '1', '1',
            '1', '1', '1', '1', '1'))
    p22 = Pokemon(
        'Emboar', '123', '65', '110', '65', 'fire', 'fighting',
        ('0.25', '0.5', '1', '1', '1', '1', '0.5', '2', '1', '0.5', '2',
         '0.5', '1', '1', '2', '1', '0.5', '2'))
    team2.append(p2)
    team2.append(p22)
    player2 = Player("JOHN", team2)
    player2.set_pokemon(1)
    player1_move = Moves.ATTACK
    player2_move = Moves.SWITCH
    switch1 = None
    switch2 = 2
    round = game.battle(
        player2, player1, player2_move, player1_move, switch2, switch1
    )[0]
    hp_2 = player2.current_pokemon().hp()
    text = f"JOHN IS SWITCHING POKEMON....EMBOAR IS ENTERING THE BATTLEFIELD"\
        "...\nBULBASAUR USED NORMAL ATTACK ON EMBOAR..."\
        f"EMBOAR HAS {hp_2} LEFT "
    assert round == text


def test_battle_result_faster_pokemon_killed_the_slower_one():
    game = Game()
    team1 = []
    team2 = []
    p1 = Pokemon(
        'Bulbasaur', 49, 49, 1, 45, 'grass', 'poison',
        ('1', '1', '1', '0.5', '0.5', '0.5', '2', '2', '1', '0.25', '1', '2',
            '1', '1', '2', '1', '1', '0.5'))
    p12 = Pokemon(
        'Archen', '112', '45', '55', '70', 'rock', 'flying',
        ('0.5', '1', '1', '2', '1', '1', '0.5', '0.5', '1', '1', '0', '2',
         '0.5', '0.5', '1', '2', '2', '2'))

    team1.append(p1)
    team1.append(p12)
    player1 = Player("ASH", team1)
    player1.set_pokemon(1)

    p2 = Pokemon(
        'Komala', '115', '65', '65', '65', 'normal', '',
        ('1', '1', '1', '1', '1', '2', '1', '1', '0', '1', '1', '1', '1',
            '1', '1', '1', '1', '1'))
    p22 = Pokemon(
        'Emboar', '123', '65', '110', '65', 'fire', 'fighting',
        ('0.25', '0.5', '1', '1', '1', '1', '0.5', '2', '1', '0.5', '2',
         '0.5', '1', '1', '2', '1', '0.5', '2'))
    team2.append(p2)
    team2.append(p22)
    player2 = Player("JOHN", team2)
    player2.set_pokemon(1)
    player1_move = Moves.ATTACK
    player2_move = Moves.ATTACK
    switch1 = None
    switch2 = None
    round = game.battle(
        player2, player1, player2_move, player1_move, switch2, switch1
    )[0]
    hp_1 = player1.current_pokemon().hp()
    text = f"KOMALA USED NORMAL ATTACK ON BULBASAUR...BULBASAUR HAS {hp_1}"\
        " LEFT \nBULBASAUR TOOK TOO MUCH DAMAGE AND IS UNABLE TO FIGHT"
    assert round == text


def test_battle_result_slower_pokemon_killed_the_faster_one():
    game = Game()
    team1 = []
    team2 = []
    p1 = Pokemon(
        'Bulbasaur', 49, 49, 45, 45, 'grass', 'poison',
        ('1', '1', '1', '0.5', '0.5', '0.5', '2', '2', '1', '0.25', '1', '2',
            '1', '1', '2', '1', '1', '0.5'))
    p12 = Pokemon(
        'Archen', '112', '45', '55', '70', 'rock', 'flying',
        ('0.5', '1', '1', '2', '1', '1', '0.5', '0.5', '1', '1', '0', '2',
         '0.5', '0.5', '1', '2', '2', '2'))

    team1.append(p1)
    team1.append(p12)
    player1 = Player("ASH", team1)
    player1.set_pokemon(1)

    p2 = Pokemon(
        'Komala', '115', '65', '1', '65', 'normal', '',
        ('1', '1', '1', '1', '1', '2', '1', '1', '0', '1', '1', '1', '1',
            '1', '1', '1', '1', '1'))
    p22 = Pokemon(
        'Emboar', '123', '65', '110', '65', 'fire', 'fighting',
        ('0.25', '0.5', '1', '1', '1', '1', '0.5', '2', '1', '0.5', '2',
         '0.5', '1', '1', '2', '1', '0.5', '2'))
    team2.append(p2)
    team2.append(p22)
    player2 = Player("JOHN", team2)
    player2.set_pokemon(1)
    player1_move = Moves.ATTACK
    player2_move = Moves.ATTACK
    switch1 = None
    switch2 = None
    round = game.battle(
        player2, player1, player2_move, player1_move, switch2, switch1
    )[0]
    hp_1 = player1.current_pokemon().hp()
    hp_2 = player2.current_pokemon().hp()
    text = f"KOMALA USED NORMAL ATTACK ON BULBASAUR...BULBASAUR HAS {hp_1}"\
        f" LEFT \nBULBASAUR USED NORMAL ATTACK ON KOMALA...KOMALA HAS {hp_2}"\
        " LEFT \nKOMALA TOOK TOO MUCH DAMAGE AND IS UNABLE TO FIGHT"
    assert round == text


def test_battle_result_super_effective_move_and_not_very_effective_move():
    game = Game()
    team1 = []
    team2 = []
    p1 = Pokemon(
        'Tapu Fini', '75', '115', '70', '85', 'water', 'fairy',
        ('0.5', '0.5', '0', '2', '1', '0.5', '0.5', '1', '1', '2', '1',
         '0.5', '1', '2', '1', '1', '1', '0.5'))
    p12 = Pokemon(
        'Archen', '112', '45', '55', '70', 'rock', 'flying',
        ('0.5', '1', '1', '2', '1', '1', '0.5', '0.5', '1', '1', '0', '2',
         '0.5', '0.5', '1', '2', '2', '2'))

    team1.append(p1)
    team1.append(p12)
    player1 = Player("ASH", team1)
    player1.set_pokemon(1)

    p2 = Pokemon(
        'Komala', '115', '65', '1', '65', 'normal', '',
        ('1', '1', '1', '1', '1', '2', '1', '1', '0', '1', '1', '1', '1',
            '1', '1', '1', '1', '1'))
    p22 = Pokemon(
        'Emboar', '123', '65', '110', '65', 'fire', 'fighting',
        ('0.25', '0.5', '1', '1', '1', '1', '0.5', '2', '1', '0.5', '2',
         '0.5', '1', '1', '2', '1', '0.5', '2'))
    team2.append(p2)
    team2.append(p22)
    player2 = Player("JOHN", team2)
    player2.set_pokemon(2)
    player1_move = Moves.TYPE_1
    player2_move = Moves.TYPE_1
    switch1 = None
    switch2 = None
    round = game.battle(
        player2, player1, player2_move, player1_move, switch2, switch1
    )[0]
    hp_1 = player1.current_pokemon().hp()
    hp_2 = player2.current_pokemon().hp()
    text = f"EMBOAR USED FIRE TYPE ATTACK ON TAPU FINI. IT WAS NOT VERY"\
        f" EFFECTIVE...TAPU FINI HAS {hp_1} LEFT \nTAPU FINI USED WATER"\
        f" TYPE ATTACK ON EMBOAR. IT WAS SUPER EFFECTIVE"\
        f"...EMBOAR HAS {hp_2} LEFT "
    assert round == text


def test_battle_result_info_player_has_to_switch_pokemon():
    game = Game()
    team1 = []
    team2 = []
    p1 = Pokemon(
        'Bulbasaur', 49, 49, 1, 45, 'grass', 'poison',
        ('1', '1', '1', '0.5', '0.5', '0.5', '2', '2', '1', '0.25', '1', '2',
            '1', '1', '2', '1', '1', '0.5'))
    p12 = Pokemon(
        'Archen', '112', '45', '55', '70', 'rock', 'flying',
        ('0.5', '1', '1', '2', '1', '1', '0.5', '0.5', '1', '1', '0', '2',
         '0.5', '0.5', '1', '2', '2', '2'))

    team1.append(p1)
    team1.append(p12)
    player1 = Player("ASH", team1)
    player1.set_pokemon(1)

    p2 = Pokemon(
        'Komala', '115', '65', '65', '65', 'normal', '',
        ('1', '1', '1', '1', '1', '2', '1', '1', '0', '1', '1', '1', '1',
            '1', '1', '1', '1', '1'))
    p22 = Pokemon(
        'Emboar', '123', '65', '110', '65', 'fire', 'fighting',
        ('0.25', '0.5', '1', '1', '1', '1', '0.5', '2', '1', '0.5', '2',
         '0.5', '1', '1', '2', '1', '0.5', '2'))
    team2.append(p2)
    team2.append(p22)
    player2 = Player("JOHN", team2)
    player2.set_pokemon(1)
    player1_move = Moves.ATTACK
    player2_move = Moves.ATTACK
    switch1 = None
    switch2 = None
    round = game.battle(
        player2, player1, player2_move, player1_move, switch2, switch1
    )
    assert round[1] == Outputs.OUTPUT_2

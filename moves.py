from enum import Enum


class Moves(Enum):
    ATTACK = 1
    SPECIAL_ATTACK = 2
    DEFEND = 3
    SWITCH = 4
    TYPE_1 = 5
    TYPE_2 = 6


class Outputs(Enum):
    """
    Description of every output:
    1: Both pokemons made normal move
    2: Faster pokemon attacked and slower pokemon didn't survive the attack
    3: Both pokemons attack, and faster pokemon didn't survive the attack
    4: Faster player changed pokemon and slower pokemon attacked the new
       pokemon of faster player. Faster player's new pokemon didn't survive
       the attack
    5: Slower player wanted to change pokemons. But his current pokemon died
       after faster pokemon's attack. Now slower player is switching pokemon
    6: Faster plauer changed pokemons. Slower pokemon attacked the new one
    7: Slower player wanted to change pokemons. His current pokemon surive the
       faster pokemon's attack. Now slower player is switching pokemon
    8: Both players have switched pokemons
    """
    OUTPUT_1 = 1
    OUTPUT_2 = 2
    OUTPUT_3 = 3
    OUTPUT_4 = 4
    OUTPUT_5 = 5
    OUTPUT_6 = 6
    OUTPUT_7 = 7
    OUTPUT_8 = 8

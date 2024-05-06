from random import randint
from pokemon import Pokemon
from moves import Moves
from player import Player


class Computer(Player):
    """
    Class Computer. Contain's computer team. Inherits from the player's class.
    """
    def __init__(self, team: list):
        super().__init__("COMPUTER", team)

    def set_starting_pokemon(self, index: int):
        """Function that set computer's starting pokemon"""
        self._current_pokemon = self.team()[index]
        return self._current_pokemon

    def SI_pick_pokemon(self, list_of_pokemons: list):
        """Function that pick random pokemon from pokemon's list"""
        pokemon_number = randint(0, 801)
        stats = list_of_pokemons[pokemon_number]
        name, attack, defense, hp, speed, type1, type2, weakness = stats
        pokemon = Pokemon(
            name,
            attack,
            defense,
            hp,
            speed,
            type1,
            type2,
            weakness
        )
        return pokemon

    def SI_pick_team(self, amount_of_pokemons: int, list_of_pokemons: list):
        """Function that create computer's team of pokemons"""
        for pokemon in range(1, amount_of_pokemons + 1):
            pokemon = self.SI_pick_pokemon(list_of_pokemons)
            self._team.append(pokemon)
        return self._team

    def SI_calculate_attack_weakness(self, player: object):
        """Function that return a sorted list of enemies attack effectiveness
        against computer current pokemon"""
        dict_of_weakness = {}
        pokemon_SI = self._current_pokemon
        player_pok = player.current_pokemon()
        first_type = player_pok.first_type()
        second_type = player_pok.second_type()
        normal_SI = pokemon_SI.calculate_weakness(player_pok, "normal")
        first_type_SI = pokemon_SI.calculate_weakness(player_pok, first_type)
        if player_pok.second_type() != "":
            second_type_SI = pokemon_SI.calculate_weakness(
                                        player_pok, second_type
            )
        else:
            second_type_SI = 0
        dict_of_weakness["normal"] = normal_SI
        dict_of_weakness[player_pok.first_type()] = first_type_SI
        dict_of_weakness[player_pok.second_type()] = second_type_SI
        return sorted(dict_of_weakness.values(), reverse=True)

    def SI_calculate_attack_effectivness(self, player: object):
        """Function that return dictionary of computer's pokemon type as
        keys and multipliers as values against player current pokemon"""
        dict_of_effectivness = {}
        pokemon_SI = self._current_pokemon
        player_pokemon = player.current_pokemon()
        normal_SI = player_pokemon.calculate_weakness(player_pokemon, "normal")
        first_type_SI = player_pokemon.calculate_weakness(
            player_pokemon, pokemon_SI.first_type()
        )
        if pokemon_SI.second_type() != "":
            second_type_SI = player_pokemon.calculate_weakness(
                player_pokemon, pokemon_SI.second_type()
            )
        else:
            second_type_SI = 0
        if pokemon_SI.first_type() != "normal":
            dict_of_effectivness["normal"] = normal_SI
        dict_of_effectivness[pokemon_SI.first_type()] = first_type_SI
        dict_of_effectivness[pokemon_SI.second_type()] = second_type_SI
        return dict_of_effectivness

    def SI_pick_atacking_move(self, player: object):
        """Function that returns computer's best possible attacking move"""
        pokemon_SI = self._current_pokemon
        first_type = pokemon_SI.first_type()
        second_type = pokemon_SI.second_type()
        if self.SI_calculate_attack_effectivness(player)["normal"] > 1:
            return Moves.ATTACK
        elif self.SI_calculate_attack_effectivness(player)[first_type] > 1:
            return Moves.TYPE_1
        elif self.SI_calculate_attack_effectivness(player)[second_type] > 1:
            return Moves.TYPE_2
        else:
            random_move = randint(1, 4)
            if random_move == 1:
                return Moves.DEFEND
            else:
                return Moves.ATTACK

    def SI_pick_switch(self, player: object):
        """Function that check whether computer can switch pokemon"""
        if len(self.alive_pokemons_in_team()) > 1:
            return Moves.SWITCH
        else:
            return self.SI_pick_atacking_move(player)

    def SI_pick_move(self, player: object):
        """Function that return  the best move for computer
        based on computer's pokemon and player's pokemon"""
        pokemon_SI = self._current_pokemon
        player_pokemon = player.current_pokemon()
        if pokemon_SI.speed() >= player_pokemon.speed():
            if max(self.SI_calculate_attack_weakness(player)) > 1.0:
                return self.SI_pick_switch(player)
            else:
                return self.SI_pick_atacking_move(player)
        elif pokemon_SI.speed() < player_pokemon.speed():
            if pokemon_SI.hp() > 25.0:
                if max(self.SI_calculate_attack_weakness(player)) > 1.0:
                    return self.SI_pick_switch(player)
                else:
                    return self.SI_pick_atacking_move(player)
            else:
                return self.SI_pick_atacking_move(player)

    def pokemon_to_switch(self):
        """Function that returns index of pokemon"""
        team = self.team()
        index_of_pokemon_to_switch = randint(0, len(team) - 1)
        if (
            team[index_of_pokemon_to_switch].is_alive() and
            team[index_of_pokemon_to_switch] != self.current_pokemon()
        ):
            return index_of_pokemon_to_switch
        else:
            return self.pokemon_to_switch()

    def SI_SWITCH(self, index_of_pokemon_to_switch: int):
        """Function that switches computer's current pokemon with
        another one"""
        return self.set_starting_pokemon(index_of_pokemon_to_switch)

class Player:
    """
    Class Player. Contains player's name and his team
    :name: name of a player
    :type_name: string
    :team: list of player's pokemon
    :type_team: list of objects

    return NameError when:
    - given name is ""
    """
    def __init__(self, name: str, team: list):
        if name == "":
            raise NameError("Name cannot be empty")
        self._name = name
        self._team = team
        self._current_pokemon = None

    """
    Defined getters of the Pokemon
    """

    def name(self):
        return self._name

    def team(self):
        return self._team

    def current_pokemon(self):
        return self._current_pokemon

    def alive_pokemons_in_team(self):
        """Returns list of alive pokemon in player's team"""
        alive_pokemons = []
        for pokemon in self.team():
            if pokemon.is_alive():
                alive_pokemons.append(pokemon)
        return alive_pokemons

    def set_pokemon(self, index_of_pokemon: int):
        """Function that changes player's current pokemon"""
        self._current_pokemon = self.team()[index_of_pokemon - 1]
        return self.current_pokemon()

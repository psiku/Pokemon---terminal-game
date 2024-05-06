from random import randint


class Pokemon:
    """
    Class Pokemon. Contains stats of a pokemon.
    :name: name of pokemon
    :type_name: string
    :attack: attack points of a pokemon
    :type_atack: float
    :defense: defense points of a pokemon
    :type_defense: float
    :hp: pokemon health
    :type_hp: float
    :speed: speed of a pokemon
    :type_speed: float
    :first_type: pokemon's first type
    :type_first_type: string
    :second_type: pokemon second type if exists, else is None
    :type_second_type: string
    :weakness: tuple of multipliers against different types
    :type_weakness: tuple of floats
    """
    dict_of_weaknes = {
        "bug": 0,
        "dark": 1,
        "dragon": 2,
        "electric": 3,
        "fairy": 4,
        "fighting": 5,
        "fire": 6,
        "flying": 7,
        "ghost": 8,
        "grass": 9,
        "ground": 10,
        "ice": 11,
        "normal": 12,
        "poison": 13,
        "psychic": 14,
        "rock": 15,
        "steel": 16,
        "water": 17
    }

    def __init__(
                 self,
                 name: str,
                 atack: float,
                 defense: float,
                 hp: float,
                 speed: float,
                 first_type: str,
                 second_type,
                 weakness: tuple
    ):
        self._name = name
        self._atack = float(atack)
        self._defense = float(defense)
        self._hp = float(hp)
        self._speed = float(speed)
        self._first_type = first_type
        self._second_type = second_type
        self._weakness = weakness

    def __str__(self):
        return f"{self._name}"

    """
    Defined getters of the Pokemon
    """

    def name(self):
        return self._name.upper()

    def atack(self):
        return self._atack

    def defense(self):
        return self._defense

    def hp(self):
        return self._hp

    def speed(self):
        return self._speed

    def first_type(self):
        return self._first_type

    def second_type(self):
        return self._second_type

    def is_alive(self):
        """" Chceking if pokemon is alive"""
        return self._hp > 0

    def take_damage(self, damage: float):
        """Function that set pokemon's new health"""
        damage = float(damage)
        new_hp = round(self._hp - damage, 2)
        return self.set_hp(max(new_hp, 0))

    def set_hp(self, new_hp: float):
        new_hp = float(new_hp)
        self._hp = new_hp

    def set_defense(self, new_defense):
        new_defense = float(new_defense)
        self._defense = new_defense

    def crit_chance(self) -> int:
        """Function that calculate chance for critical hit
        based on pokemo's speed"""
        treshold = self.speed() / 2
        value = randint(0, 255)
        if treshold > value:
            crit_dmg = 2
        else:
            crit_dmg = 1
        return crit_dmg

    def reinforcment(self) -> float:
        """Function that increase pokemon's defense by 10%"""
        new_defence = round(self._defense * 1.1, 2)
        return self.set_defense(new_defence)

    def calculate_weakness(self, other: object, atack_type: str) -> float:
        """Function that calculate weakness against other pokemon's attack"""
        if atack_type not in Pokemon.dict_of_weaknes.keys():
            raise ValueError
        defending_type = other.dict_of_weaknes[atack_type]
        weakness = float(self._weakness[defending_type])
        return weakness

    def calculate_stab(self, attack_type: str) -> float:
        """Function which checks wheter pokemon has stab"""
        if attack_type in [self.first_type(), self.second_type()]:
            stab = 1.5
        else:
            stab = 1
        return stab

    def show_types(self):
        if self.second_type() == "":
            return f"1: {self.first_type().upper()}"
        else:
            return f"1: {self.first_type().upper()}\n"\
                f"2: {self.second_type().upper()}"

    def calculate_dealt_damage(self, other: object, atack_type: str) -> float:
        """Function that calculate damage given to the opponent's pokemon"""
        if atack_type not in Pokemon.dict_of_weaknes.keys():
            raise ValueError
        crit = self.crit_chance()
        a_d = float(self.atack() / other.defense())
        weakness = other.calculate_weakness(self, atack_type)
        ran = float(randint(217, 255) / 50)
        stab = self.calculate_stab(atack_type)
        dmg = (((((2 * crit / 5) + 2) * a_d) / 50) + 2) * weakness * ran * stab
        return dmg

    def attack_pokemon(self, other: object, atack_type: str):
        """Function that allows pokemon attack another pokemon"""
        damage = self.calculate_dealt_damage(other, atack_type)
        other.take_damage(damage)

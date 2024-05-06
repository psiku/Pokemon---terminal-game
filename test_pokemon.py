from pokemon import Pokemon
import pytest


def test_pokemon_create():
    p = Pokemon(
        'Bulbasaur', 49, 49, 45, 45, 'grass', 'poison',
        ('1', '1', '1', '0.5', '0.5', '0.5', '2', '2', '1', '0.25', '1', '2',
         '1', '1', '2', '1', '1', '0.5')
        )
    assert p.name() == 'BULBASAUR'
    assert p.atack() == 49
    assert p.defense() == 49
    assert p.hp() == 45
    assert p.speed() == 45
    assert p.first_type() == "grass"
    assert p.second_type() == 'poison'
    w = ('1', '1', '1', '0.5', '0.5', '0.5', '2', '2', '1', '0.25', '1', '2',
         '1', '1', '2', '1', '1', '0.5')
    assert p._weakness == w


def test_pokemon_is_alive():
    pokemon = Pokemon(
        'Bulbasaur', 49, 49, 45, 45, 'grass', 'poison',
        ('1', '1', '1', '0.5', '0.5', '0.5', '2', '2', '1', '0.25', '1', '2',
         '1', '1', '2', '1', '1', '0.5')
        )
    assert pokemon.is_alive()


def test_pokemon_is_not_alive():
    pokemon = Pokemon(
        'Bulbasaur', 49, 49, 45, 45, 'grass', 'poison',
        ('1', '1', '1', '0.5', '0.5', '0.5', '2', '2', '1', '0.25', '1', '2',
         '1', '1', '2', '1', '1', '0.5')
        )
    pokemon.take_damage(45)
    assert not pokemon.is_alive()


def test_calculate_weakness():
    p1 = Pokemon(
        'Bulbasaur', 49, 49, 45, 45, 'grass', 'poison',
        ('1', '1', '1', '0.5', '0.5', '0.5', '2', '2', '1', '0.25', '1', '2',
         '1', '1', '2', '1', '1', '0.5'))
    p2 = Pokemon(
        'Bulbasaur', 49, 49, 45, 45, 'grass', 'poison',
        ('1', '1', '1', '0.5', '0.5', '0.5', '2', '2', '1', '0.25', '1', '2',
         '1', '1', '2', '1', '1', '0.5'))
    assert p1.calculate_weakness(p2, p1.first_type()) == 0.25


def test_calculate_weakness_normal_type():
    p1 = Pokemon(
        'Komala', '115', '65', '65', '65', 'normal', '',
        ('1', '1', '1', '1', '1', '2', '1', '1', '0', '1', '1', '1', '1',
         '1', '1', '1', '1', '1'))
    p2 = Pokemon(
        'Bulbasaur', 49, 49, 45, 45, 'grass', 'poison',
        ('1', '1', '1', '0.5', '0.5', '0.5', '2', '2', '1', '0.25', '1', '2',
         '1', '1', '2', '1', '1', '0.5'))
    assert p2.calculate_weakness(p1, p1.first_type()) == 1


def test_calculate_weakness_wrong_attack_type():
    p1 = Pokemon(
        'Bulbasaur', 49, 49, 45, 45, 'grass', 'poison',
        ('1', '1', '1', '0.5', '0.5', '0.5', '2', '2', '1', '0.25', '1', '2',
         '1', '1', '2', '1', '1', '0.5'))
    p2 = Pokemon(
        'Bulbasaur', 49, 49, 45, 45, 'grass', 'poison',
        ('1', '1', '1', '0.5', '0.5', '0.5', '2', '2', '1', '0.25', '1', '2',
         '1', '1', '2', '1', '1', '0.5'))
    with pytest.raises(ValueError):
        p1.calculate_weakness(p2, "lunar")


def test_stab_is_on():
    p1 = Pokemon(
        'Komala', '115', '65', '65', '65', 'normal', '',
        ('1', '1', '1', '1', '1', '2', '1', '1', '0', '1', '1', '1', '1',
         '1', '1', '1', '1', '1'))
    assert p1.calculate_stab("normal") == 1.5


def test_stab_is_off():
    p1 = Pokemon(
        'Bulbasaur', 49, 49, 45, 45, 'grass', 'poison',
        ('1', '1', '1', '0.5', '0.5', '0.5', '2', '2', '1', '0.25', '1', '2',
         '1', '1', '2', '1', '1', '0.5'))
    assert p1.calculate_stab("normal") == 1


def test_set_hp():
    p1 = Pokemon(
        'Bulbasaur', 49, 49, 45, 45, 'grass', 'poison',
        ('1', '1', '1', '0.5', '0.5', '0.5', '2', '2', '1', '0.25', '1', '2',
         '1', '1', '2', '1', '1', '0.5'))
    assert p1.hp() == 45.0
    p1.set_hp(23.4)
    assert p1.hp() == 23.4


def test_take_damage(monkeypatch):
    p1 = Pokemon(
        'Bulbasaur', 49, 49, 45, 45, 'grass', 'poison',
        ('1', '1', '1', '0.5', '0.5', '0.5', '2', '2', '1', '0.25', '1', '2',
         '1', '1', '2', '1', '1', '0.5'))

    def fake_damage(a):
        return 15.64

    monkeypatch.setattr("pokemon.Pokemon.calculate_dealt_damage", fake_damage)
    dmg = p1.calculate_dealt_damage()
    p1.take_damage(dmg)
    assert p1.hp() == 29.36


def test_take_damage_bigger_than_hp(monkeypatch):
    p1 = Pokemon(
        'Bulbasaur', 49, 49, 45, 45, 'grass', 'poison',
        ('1', '1', '1', '0.5', '0.5', '0.5', '2', '2', '1', '0.25', '1', '2',
         '1', '1', '2', '1', '1', '0.5'))

    def fake_damage(a):
        return 87.93

    monkeypatch.setattr("pokemon.Pokemon.calculate_dealt_damage", fake_damage)
    dmg = p1.calculate_dealt_damage()
    p1.take_damage(dmg)
    assert p1.hp() == 0


def test_reinforcment():
    p1 = Pokemon(
        'Komala', '115', '65', '65', '65', 'normal', '',
        ('1', '1', '1', '1', '1', '2', '1', '1', '0', '1', '1', '1', '1',
         '1', '1', '1', '1', '1'))
    assert p1.defense() == 65.0
    p1.reinforcment()
    assert p1.defense() == 71.5


def test_crit_active(monkeypatch):
    p1 = Pokemon(
        'Komala', '115', '65', '65', '65', 'normal', '',
        ('1', '1', '1', '1', '1', '2', '1', '1', '0', '1', '1', '1', '1',
         '1', '1', '1', '1', '1'))

    def fake_chance(a):
        return 2

    monkeypatch.setattr("pokemon.Pokemon.crit_chance", fake_chance)
    assert p1.crit_chance() == 2


def test_crit_not_active(monkeypatch):
    p1 = Pokemon(
        'Komala', '115', '65', '65', '65', 'normal', '',
        ('1', '1', '1', '1', '1', '2', '1', '1', '0', '1', '1', '1', '1',
         '1', '1', '1', '1', '1'))

    def fake_chance(a):
        return 1

    monkeypatch.setattr("pokemon.Pokemon.crit_chance", fake_chance)
    assert p1.crit_chance() == 1


def test_attack_pokemon():
    p1 = Pokemon(
        'Komala', '115', '65', '65', '65', 'normal', '',
        ('1', '1', '1', '1', '1', '2', '1', '1', '0', '1', '1', '1', '1',
         '1', '1', '1', '1', '1'))
    p2 = Pokemon(
        'Bulbasaur', 49, 49, 45, 45, 'grass', 'poison',
        ('1', '1', '1', '0.5', '0.5', '0.5', '2', '2', '1', '0.25', '1', '2',
         '1', '1', '2', '1', '1', '0.5'))

    assert p2.hp() == 45.
    p1.attack_pokemon(p2, "normal")
    assert p2.hp() < 45.0
    assert p1.hp() == 65.0
    p2.attack_pokemon(p1, "normal")
    assert p1.hp() < 65.0

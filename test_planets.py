from planet_classes import *
import pytest

# Earth and Luna
earth = planet(name = "Earth", radius = 6371.0084, color = "blue")
luna = moon(name="Moon", radius=33, color="white",  tidally_locked=True,planet_companion=earth)
luna.update_planet()

# Jupiter and its moons
jupiter = planet(name='Jupiter',radius=69911, color='Orange')
europa = moon(name='Europa',radius=1560.8,color='Blue',planet_companion=jupiter,tidally_locked=True)
io = moon(name='Io',radius=1821.5,color='Yellow',planet_companion=jupiter,tidally_locked=True)
ganymede = moon(name='Ganymede',radius=2631.2,color='Grey',planet_companion=jupiter,tidally_locked=True)

# Saturn and its moons
saturn = planet(name='Saturn',radius=58232,color='Tan')
titan = moon(planet_companion=saturn,name='Titan',radius=2575,color='Green',tidally_locked=True)
hyperion = moon(planet_companion=saturn,name='Hyperion',radius=266,color='Grey')


def test_planet_update():
    # Earth
    luna.update_planet()
    assert earth.moon_list[0].name == "Moon"
    # Jupiter
    europa.update_planet()
    assert jupiter.moon_list[0].name == "Europa"
    # Saturn
    hyperion.update_planet()
    assert saturn.moon_list[0].name == "Hyperion"
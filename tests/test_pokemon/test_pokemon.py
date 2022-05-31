import json
import pytest
import jsonpath
from common.api.PokemonEndpoints import PokemonEndpoints

pkm_endpoints = PokemonEndpoints()

@pytest.fixture(scope="module",autouse=True)
def before_all_after_all():
    print(" ")
    print("before all")
    print("---------------------------")
    yield
    print(" ")
    print("after all")
    print("---------------------------")


@pytest.fixture(autouse=True)
def before_each_after_each():
    print(" ")
    print("beforeEach")
    print("---------------------------")
    yield
    print(" ")
    print("afterEach")
    print("---------------------------")


def test_validate_pokemon_data():

    file = open('fixtures/pokemonApi/pokemon_list.json', 'r')
    json_input = file.read()
    request_body = json.loads(json_input)

    file = open('env_vars.json', 'r')
    json_input = file.read()
    env_vars = json.loads(json_input)
    pokemon_base_endpoint = jsonpath.jsonpath(env_vars, 'pokeApiUrl')

    for pokemon in request_body:
        pokemon_resource = pkm_endpoints.pokemon_name_resourse(pokemon)
        print(pokemon_resource)

from project.pokemon import Pokemon

class Trainer:
    def __init__(self, name: str):
        self.name = name
        self.pokemons = []

    def add_pokemon(self, pokemon: Pokemon):
        if pokemon not in self.pokemons:
            self.pokemons.append(pokemon)
            return f"Caught {Pokemon.pokemon_details(pokemon)}"
        return "This pokemon is already caught"

    def release_pokemon(self, pokemon_name: str):
        for poke in self.pokemons:
            if poke.name == pokemon_name:
                self.pokemons.remove(poke)
                return f"You have released {pokemon_name}"
        return "Pokemon is not caught"

    def trainer_data(self):
        return (f"Pokemon Trainer {self.name}\nPokemon count {len(self.pokemons)}\n" +
                '\n'.join(f"- {Pokemon.pokemon_details(pok)}" for pok in self.pokemons))
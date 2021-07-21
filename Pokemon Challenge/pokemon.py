class Pokemon:
  def __init__(self, name, level, type_of, maximum_health = 50, current_health= 50, is_knocked_out = False, experience_points = 0):
    self.name = name
    self.level = level
    self.type_of = type_of
    self.maximum_health = maximum_health
    self.health = current_health
    self.is_knocked_out = is_knocked_out
    self.experience_points = experience_points
  def lose_health(self, points_lost):
    if self.health > points_lost:
      self.health -= points_lost
      print("{} was hit! -{} health points! Current health: {}".format(self.name, points_lost, self.health))
    else:
      self.health = 0
      print("{} was hit! -{} health points! Current Health: 0. Game over!".format(self.name, points_lost))
      self.knock_out()
  def heal(self, points_gained):
    if self.health > 0: 
      if self.maximum_health - self.health > points_gained:
        self.health += points_gained
        print("+ {} health points! {} now has {} health points.".format(points_gained, self.name, self.health))
      else:
        self.health = self.maximum_health
        print("Maximum health was reached! {} now has {} health points.".format(self.name, self.health))
    else: 
      print("\n ----------- \n{} has 0 health points! You cannot heal him. Game over! ". format(self.name))
  def knock_out(self):
    if self.health == 0:
      self.is_knocked_out = True
      print("\n ----------- \n{} was knocked out! \n ----------- \n".format(self.name))
    else:
      print("\n ----------- \nKeep fighting, you still have a chance to win!\n ----------- \n")
  def revive(self):
    if self.is_knocked_out:
      self.health = self.maximum_health
      self.is_knocked_out = False
      print("""\n ----------- \n {}'s health was restored!\n {}... {}...""".format(self.name, self.name, self.name))
    else:
      print("You cannot revive {} yet.".format(self.name))
      
  def attack(self, pokemon_attacked):
    if self.type_of == "Fire":
      if pokemon_attacked.type_of == "Grass":
        damage = 2 * self.level
        print("{} attacks {}...".format(self.name, pokemon_attacked.name))
        print("Super-effective!")
        pokemon_attacked.lose_health(damage)
      elif pokemon_attacked.type_of == "Water":
        damage = (self.level)/2
        print("{} attacks {}...".format(self.name, pokemon_attacked.name))
        print("Not very effective...")
        pokemon_attacked.lose_health(damage)
      else:
        damage = (self.level)/2
        print("{} attacks {}...".format(self.name, pokemon_attacked.name))
        print("Not very effective...")
        pokemon_attacked.lose_health(damage)
    elif self.type_of == "Water":
      if pokemon_attacked.type_of == "Grass":
        damage = (self.level)/2
        print("{} attacks {}...".format(self.name, pokemon_attacked.name))
        print("Not very effective...")
        pokemon_attacked.lose_health(damage)
      elif pokemon_attacked.type_of == "Fire":
        damage = 2*self.level
        print("{} attacks {}...".format(self.name, pokemon_attacked.name))
        print("Super-effective!")
        pokemon_attacked.lose_health(damage)
      else:
        damage = (self.level)/2
        print("{} attacks {}...".format(self.name, pokemon_attacked.name))
        print("Not very effective...")
        pokemon_attacked.lose_health(damage)
    elif self.type_of == "Grass":
      if pokemon_attacked.type_of == "Fire":
        damage = (self.level)/2
        print("{} attacks {}...".format(self.name, pokemon_attacked.name))
        print("Not very effective...")
        pokemon_attacked.lose_health(damage)
      elif pokemon_attacked.type_of == "Water":
        damage = 2*self.level
        print("{} attacks {}...".format(self.name, pokemon_attacked.name))
        print("Super-effective!")
        pokemon_attacked.lose_health(damage)
      else:
        damage = (self.level)/2
        print("{} attacks {}...".format(self.name, pokemon_attacked.name))
        print("Not very effective...")
        pokemon_attacked.lose_health(damage)
  def gain_experience(self):
    if self.health <= 0:
      self.experience_points += 1
      print("\n{} lost the battle! Don't be sad... For your effort, you gained + 1 experience point. Total experience: {}\n".format(self.name, self.experience_points))
      if self.experience_points >= self.level:
        print("\n{} is ready to evolve!\n".format(self.name))
    else:
      self.experience_points += 2
      print("\n{} won the battle! Congrats, you are one step closer to becoming a e Master! You gained + 2 experience points. Total experience: {}\n".format(self.name, self.experience_points))
      if self.experience_points >= self.level:
        print("\n{} is ready to evolve!\n".format(self.name))

  def evolve(self, evolution_name):
    if self.experience_points >= self.level:
      print("What? {} is evolving!".format(self.name))
      old_name= self.name
      self.name = evolution_name
      self.level = self.level * 2
      print("{} evolved to {}".format(old_name, self.name))
    else:
      missing = self.level - self.experience_points
      print("{} doesn't have enough experience to evolve yet. You need more {} experience points to evolve!".format(self.name, missing))
      
class Trainer:
  def __init__(self, name, number_of_potions, pokemon_list, active_pokemon ):
    self.name = name
    self.potions = number_of_potions
    self.pokemons = pokemon_list
    self.active_pokemon = active_pokemon
  def choose_pokemon(self, chosen_pokemon):
    if self.pokemons[self.active_pokemon] != self.pokemons[chosen_pokemon] :
      if self.pokemons[chosen_pokemon]. is_knocked_out == False:
        print("\n ----------- \n{}:\n{}, I choose you!".format(self.name, self.pokemons[chosen_pokemon].name))
        self.active_pokemon = chosen_pokemon
        print("{} is your currently active pokémon.\n ----------- \n".format(self.pokemons[self.active_pokemon].name))
      else:
        print("{} is knocked out... let it rest! Choose another pokémon or revive {}.".format(self.pokemons[chosen_pokemon].name, self.pokemons[chosen_pokemon].name))
    else:
      print("{} is already your currently active pokémon. Choose another!\n ----------- \n".format(self.pokemons[self.active_pokemon].name))
  def use_potion(self):
    if self.potions>0:
      print("\n ----------- \n{}:".format(self.name))
      self.pokemons[self.active_pokemon]. heal(self.pokemons[self.active_pokemon].level)
      self.potions -= 1
      print("{}, you used 1 potion to heal {}. Potions left: {} \n ----------- \n".format (self.name, self.pokemons[self.active_pokemon].name, self.potions))
    else:      
      print("\n ----------- \nSorry, you are out of potions! You can't heal your pokémon.\n ----------- \n")
  def call_to_battle(self, other_trainer):
    print("{}: {}, let's battle!\n ----------- \n".format(self.name, other_trainer.name))
    my_pokemon = self.pokemons[self.active_pokemon]
    other_pokemon = other_trainer.pokemons[other_trainer.active_pokemon]
    print("Ready to fight: {} with trainer {} x {} with trainer {}\n ----------- \n".format(my_pokemon.name, self.name, other_pokemon.name, other_trainer.name) )
  def attack_trainer(self, other_trainer):
    my_pokemon = self.pokemons[self.active_pokemon]
    other_pokemon = other_trainer.pokemons[other_trainer.active_pokemon]
    if my_pokemon.is_knocked_out == True:
      
      print("\n ----------- \n{}:\nA Pokémon that is knocked out cannot attack another Pokémon. {}, choose another pokémon to battle.\n ----------- \n".format(self.name, self.name))
    else:
      if other_pokemon.is_knocked_out == False:
        print("\n ----------- \n {}: {}, attack {}!" .format(self.name, my_pokemon.name, other_pokemon.name))
        my_pokemon.attack(other_pokemon)
        self.battle_result(other_trainer)    
      else:
        print("\n ----------- \n{}, you won the battle!\n ----------- \n".format(self.name))
  def battle_result(self, other_trainer):
    my_pokemon = self.pokemons[self.active_pokemon]
    other_pokemon = other_trainer.pokemons[other_trainer.active_pokemon]
    if other_pokemon.health == 0 and my_pokemon.health > 0:
      print("\n ----------- \n{}, you won the battle!\n".format(self.name))
      my_pokemon.gain_experience()
      print("{},\n".format(other_trainer.name))
      other_pokemon.gain_experience()
    elif other_pokemon.health > 0 and my_pokemon.health == 0:
      print("\n ----------- \n{}, you won the battle!".format(other_trainer.name))
      other_pokemon.gain_experience()
      print("{},\n".format(self.name))
      my_pokemon.gain_experience()
  def revive_pokemon(self, pokemon_to_revive):
    self.pokemons[pokemon_to_revive].revive()
      
    
# Pokémons:
charmander = Pokemon("Charmander", 6, "Fire")
charizard = Pokemon("Charizard", 24, "Fire")
rapidash = Pokemon("Rapidash", 12, "Fire")
vulpix = Pokemon("Vulpix", 6, "Fire")

squirtle = Pokemon("Squirtle", 6, "Water")
blastoise = Pokemon("Blastoise", 24, "Water")
psyduck = Pokemon("Psyduck", 6, "Water")
gyarados = Pokemon("Gyarados", 12, "Water")
    
bulbasaur = Pokemon("Bulbasaur", 6, "Grass")
ivysaur = Pokemon("Ivysaur", 12, "Grass")
venusaur = Pokemon("Venusaur", 24, "Grass")
oddish = Pokemon("Oddish", 6, "Grass")   

#Trainers
laisa = Trainer("Laisa", 5, [charizard, bulbasaur, gyarados, psyduck, charmander, oddish], 1)

taina = Trainer("Taina", 5, [squirtle, vulpix, oddish, charmander, rapidash, venusaur], 1)

alex = Trainer( "Alexandre", 5, [charizard, bulbasaur, gyarados, psyduck, charmander, oddish], 1)

alex.call_to_battle(taina)

alex.attack_trainer(taina)
alex.attack_trainer(taina)
alex.attack_trainer(taina)

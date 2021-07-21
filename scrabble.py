letters = ["A", "B", "C", "D", "E", "F", "G", "H", "I", "J", "K", "L", "M", "N", "O", "P", "Q", "R", "S", "T", "U", "V", "W", "X", "Y", "Z"]
points = [1, 3, 3, 2, 1, 4, 2, 4, 1, 8, 5, 1, 3, 4, 1, 3, 10, 1, 1, 1, 1, 4, 4, 8, 4, 10]

letters += [letter.lower() for letter in letters]
points += points


letter_to_points = {key: value for key, value in zip(letters, points)}
letter_to_points[" "] = 0
def score_word(word):
  point_total = 0
  for letter in word:
    point_total += letter_to_points.get(letter, 0)
  return point_total
brownie_points = score_word("BROWNIE")


player_to_words = {"player 1": ["BLUE", 'TENNIS', "EXIT"], "wordNerd": ['EARTH', 'EYES', 'MACHINE'], "Lexi Con": ['ERASER', 'BELLY', 'HUSKY'], "Prof Reader": ['ZAP', 'COMA', 'PERIOD'] }
player_to_points = {}
for player, words in player_to_words.items():
  player_points = 0
  for word in words:
    player_points += score_word(word)
  player_to_points[player] = player_points
  

def player_word(player, word):
  player_to_words[player] = player_to_words[player] + [word]
  return player_to_words.get(player)

player_word("player 1", "battle")
print(player_to_words)

def update_point_totals():
  for player, words in player_to_words.items():
    player_points = 0
    for word in words:
      player_points += score_word(word)
    player_to_points[player] = player_points
  return player_to_points
print(update_point_totals())
print(player_to_points)
  
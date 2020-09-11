# Write a class to hold player information, e.g. what room they are in
# currently.
class Player:
    def _init_(self, name, currently):
        self.name = name
        self.currently = currently

first_player = Player("Eddie", ["outside"])

print(first_player.name)
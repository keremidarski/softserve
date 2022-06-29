class Gallows:
    def __init__(self):
        self.words = []
        self.game_over = False

    def play(self, word):
        if self.words == [] or word[0] == self.words[-1][-1] and word not in self.words:
            self.words.append(word)
            return self.words
        else:
            self.game_over = True
            return "game over"

    def restart(self):
        self.words = []
        self.game_over = False
        return "game restarted"


my_gallows = Gallows()
print(my_gallows.restart())
print(my_gallows.words)
print(my_gallows.game_over)
print(my_gallows.play("hostess"))
print(my_gallows.game_over, False)
print(my_gallows.play("stash"))
print(my_gallows.play("hostess"))
print(my_gallows.words)

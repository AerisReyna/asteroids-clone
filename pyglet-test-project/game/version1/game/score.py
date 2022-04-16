import pyglet

class ScoreLabel(pyglet.text.Label):

    def __init__(self, text, x, y, batch=None):
        super().__init__(text, x=x, y=y, batch=batch)

    def increment(self):
        current_score = int(self.text[7:])
        self.text = "Score: " + str(current_score + 1)
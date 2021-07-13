import arcade

class Score():

    def __init__(self):

        self.score = 0

    def update(self):
        
        self.score += 1
    
    def draw(self):

        score = "Score: " + str(self.score)

        arcade.draw_text(score, 600, 600, arcade.color.WHITE, 15, font_name="GARA")

    def draw_end(self):

        game_over = "GAME OVER"

        arcade.draw_text(game_over, 500, 500, arcade.color.WHITE, 20, font_name="GARA" )

        




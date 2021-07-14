import arcade

class Score():

    def __init__(self):

        self.score = 0

    def update(self):
        
        self.score += 1

    def t(self):
        
        t = "T"
        arcade.draw_text(t, 60 , 660 , arcade.color.WHITE, 30, font_name = "GARA")
    def e(self):
        e = "E"
        arcade.draw_text(e, 80 , 660 , arcade.color.RED, 30, font_name = "GARA")
    def tt(self):
        tt = "T"
        arcade.draw_text(tt, 100 , 660 , arcade.color.GREEN, 30, font_name = "GARA")
    def r(self):
        r = "R"
        arcade.draw_text(r, 120 , 660 , arcade.color.BLUE, 30, font_name = "GARA")
    def i(self):
        i = "I"
        arcade.draw_text(i, 140 , 660 , arcade.color.ORANGE, 30, font_name = "GARA")
    def s(self):
        s = "S"
        arcade.draw_text(s, 150 , 660 , arcade.color.WHITE, 30, font_name = "GARA")
    
    def draw(self):

        score = "Score: " + str(self.score)

        arcade.draw_text(score, 600, 600, arcade.color.WHITE, 15, font_name="GARA")

    def draw_end(self):

        game_over = "GAME OVER"

        arcade.draw_text(game_over, 500, 500, arcade.color.RED, 20, font_name="GARA" )

        




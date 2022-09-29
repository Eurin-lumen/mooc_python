import turtle                # importation du module turtle
turtle.up()                  # tant que la tortue est en mode “up”,
turtle.shape('turtle')       # son déplacement ne trace rien
                             # change la forme de la tortue (en tortue)
turtle.goto(-80,0)           # la tortue se place en coordonnées (-80, 0)
                             # (-80 pour l’axe des "x" et 0 l’axe des "y")
turtle.color('blue')        # la tortue est bleu
turtle.down()               # tant que la tortue est “down”,
                            # elle tracera la ligne de ses déplacements
turtle.begin_fill()         # va remplir l’intérieur de ce qui est tracé entre
                            # maintenant et le turtle.end_fill() ultérieur
turtle.forward(300)         # la tortue avance de 300 (à droite)
turtle.right(144)
turtle.forward(300)
turtle.right(144)
turtle.forward(300)
turtle.right(144)
turtle.forward(300)
turtle.right(144)
turtle.forward(300)
turtle.right(144)
turtle.end_fill()
turtle.hideturtle()
turtle.done()
from random import randint

WIDTH = 800 # Set game window width to 800 pixel
HEIGHT = 600 # Set game window height to 600 pixel

balloon = Actor("balloon") # Create a balloon sprite
balloon.pos = 400, 300 # Set balloon sprite starting position at (400, 300)

bird = Actor("bird-up") # write your explaination  after the #
bird.pos = randint(800, 1600), randint(10, 200)

house = Actor("house")
house.pos = randint(800, 1600), 460

tree = Actor("tree")
tree.pos = randint(800, 1600), 450

bird_up = True # True:Enable bird-up image, False: enable bird-down image
up = False # True: balloon rising, False: balloon falling
game_over = False # True: game is over. False: game is still going
score = 0 # variable storing the current score of the player
number_of_updates = 0 # related bird flap()

scores = [] # List, is for keeping track of highest scores that's ever played

def update_high_scores():
     global score, scores
     filename = r"high_scores.txt"
     with open(filename, "r") as file:
         line = file.readline()
         high_scores = line.split()
         for high_score in high_scores:
            if(score > int(high_score)):
                scores.append(str(score) + " ")
                score = int(high_score)
            else:
                scores.append(str(high_score) + " ")
            print(scores)
     with open(filename, "w") as file:
         for high_score in scores:
             file.write(high_score)

def display_high_scores():
     screen.draw.text("HIGH SCORES", (350, 150), color="black")
     y = 175
     position = 1
     for high_score in scores:
         screen.draw.text(str(position) + ". " + (high_score), (350, y), color="black")
         y += 25
         position += 1

def draw():
    """Fill background.
        If game is not over, we draw sprites.
        If game is over, display highest scores"""
    screen.blit("background", (0, 0)) # Fills background using a image named "background"
    if not game_over:
        balloon.draw()
        bird.draw()
        house.draw()
        tree.draw()
        screen.draw.text("Score: "+ str(score), (700, 5), color="black")
    else:
        display_high_scores()

def on_mouse_down():
    """Raising the balloon on mouse down. """
    global up
    up = True
    balloon.y -= 50 # Reduce the y coordinate of balloon = balloon goes higher.
                    # -= means balloon.y = balloon.y - 50

def on_mouse_up():
    """Stop raising the balloon"""
    global up
    up = False

def flap():
    global bird_up
    if bird_up:
        bird.image = "bird-down"
        bird_up = False
    else:
        bird.image = "bird-up"
        bird_up = True

def update():
    global game_over, score, number_of_updates # tells update that these variables are global variables.
    if not game_over: # game_over is False ==> not game_over is True ==> condition is satisfied.

        # drop balloon
        # when mouse is down, up is True
        # When up is True, we do not drop balloon
        if not up: # check if we can drop balloon now.
            balloon.y += 1 # drop balloon by 1

        # Move bird, flap the bird,
        if bird.x > 0: # check is the bird on window
            bird.x -= 4 # move the bird left
            # this animate bird flapping wing.
            if number_of_updates ==9:
                flap()
                number_of_updates = 0
            else:
                number_of_updates += 1
        # respawn the bird.
        else: # bird has moved out of the screen.
            bird.x = randint(800, 1600) # reset a random position for the bird on the right side of the screen.
            bird.y = randint(10, 200)
            score += 1 # bird gets to the edge of the screen without touching balloon. Increase score.
            number_of_updates = 0 # reset variable for bird flap animation.

        # moving house to the left of the screen
        if house.right>0:
            house.x -= 2 # house.x = house.x -2
        else:
            house.x = randint(800, 1600)
            score += 1

        if tree.right > 0:
            tree.x -= 2
        else:
            tree.x = randint(800, 1600)
            tree.x -= 2

        if balloon.top < 0 or balloon.bottom > 560:
            game_over = True
            update_high_scores()

        if balloon.collidepoint(bird.x, bird.y) or \
            balloon.collidepoint(house.x, house.y) or \
            balloon.collidepoint(tree.x, tree.y):

            game_over = True
            update_high_scores()

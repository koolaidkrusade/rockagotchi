#################################################
################## ROCKAGOTCHI ##################
############# Name: Bahaar Esfahani #############
############## Andrew ID: besfahan ##############
#################################################

import random, os

# Graphics framework made by https://www.cs.cmu.edu/~112/
from cmu_112_graphics import *

##############################################
############## GLOBAL FUNCTIONS ##############
##############################################

# rgbString() made by https://www.cs.cmu.edu/~112/
def rgbString(r, g, b):
    return f'#{r:02x}{g:02x}{b:02x}'

rockagotchiPink = rgbString(191, 148, 186)
rockagotchiPurple = rgbString(107, 58, 97)
rockagotchiBlue = rgbString(66, 124, 145)

###############################################
############## START SCREEN MODE ##############
###############################################

def startScreenMode_redrawAll(app, canvas):
    drawBackground(app, canvas)
    startScreenMode_drawButtons(app,canvas)
    
def startScreenMode_coordinates(app):
    # Coordinates used multiple times in functions across mode
    cx = app.width // 2
    x0 = app.width // 2 - app.offset * 2
    x1 = app.width // 2 + app.offset * 2
    y = app.height // 3

    return cx, x0, x1, y

def startScreenMode_drawButtons(app, canvas):
    cx, x0, x1, y = startScreenMode_coordinates(app)
    
    # "Play" button
    canvas.create_rectangle(x0, y + app.offset // 2,
                            x1,  app.height // 3 + app.offset * 2, 
                            fill = rockagotchiPurple, outline = "")
    canvas.create_image(cx, y + app.offset + (app.offset // 5), 
                        image = ImageTk.PhotoImage(app.playButton))

    # "Instructions" button
    canvas.create_rectangle(x0, (y + app.offset * 3) - app.offset // 2,
                            x1, (y + app.offset * 2) + app.offset * 2, 
                            fill = rockagotchiPurple, outline = "")
    canvas.create_image(cx, y + app.offset * 3 + (app.offset // 5), 
                        image = ImageTk.PhotoImage(app.instructionsButton))

    # "About" button
    canvas.create_rectangle(x0, (y + app.offset * 5) - app.offset // 2,
                            x1, (y + app.offset * 4) + app.offset * 2, 
                            fill = rockagotchiPurple, outline = "")
    canvas.create_image(cx, y + app.offset * 5 + (app.offset // 5), 
                        image = ImageTk.PhotoImage(app.aboutButton))

def startScreenMode_mousePressed(app, event):
    cx, x0, x1, y = startScreenMode_coordinates(app)

    if x0 <= event.x <= x1:
        
        # If you press "Play"
        if y + app.offset // 2 <= event.y <= y + app.offset * 2:
            app.mode = "adoptMode"

        # If you press "Instructions"
        elif ((y + app.offset * 3) - app.offset // 2 <= event.y 
              <= (y + app.offset * 2) + app.offset * 2):
            app.mode = "instructionsMode"

        # If you press "About"
        elif ((y + app.offset * 5) - app.offset // 2 <= event.y 
              <= (y + app.offset * 4) + app.offset * 2):
            app.mode = "aboutMode"

###############################################
############## INSTRUCTIONS MODE ##############
###############################################

def instructionsMode_redrawAll(app, canvas):
    drawBackground(app, canvas)
    instructionsMode_drawInstructions(app, canvas)
    instructionsMode_drawButtons(app, canvas)

def instructionsMode_coordinates(app):
    # Coordinates used multiple times in functions across mode
    cx = app.width // 2
    x0 = app.width // 2 - app.offset
    x1 = app.width // 2 + app.offset
    y = app.height // 4

    return cx, x0, x1, y

def instructionsMode_drawButtons(app, canvas):
    cx, x0, x1, y = instructionsMode_coordinates(app)
    
    # "Back" button
    canvas.create_rectangle(x0, 3 * y - app.offset // 2,
                            x1, 3 * y + app.offset // 2,
                            fill = rockagotchiPurple, outline = "")
    canvas.create_image(cx, 3 * y, image = ImageTk.PhotoImage(app.backButton))

    
def instructionsMode_drawInstructions(app, canvas):
    instructions1 = ("Customize your own pet rock with\naccessories, clothes, "
                    "and a name!\nThere are over 500 combinations!")

    instructions2 = ("Make sure to take good care\nof your rock by feeding it, "
                    "\nwalking it, and putting it\nto bed on time! Monitor\nits "
                    "needs using the mood\nbars and make sure they\ndon't get "
                    "too low...\nyour pet may run away!")

    cx, x0, x1, y = instructionsMode_coordinates(app)
   
    canvas.create_text(x1 + app.offset, 9 * y // 5, text = instructions1, 
                       anchor = "s", font = "TkFixedFont",
                       fill = rockagotchiPink)

    canvas.create_text(app.width // 5, 5 * y // 2, text = instructions2, 
                       anchor = "w", font = "TkFixedFont",
                       fill = rockagotchiPink)

def instructionsMode_mousePressed(app, event):
    cx, x0, x1, y = instructionsMode_coordinates(app)

    # If you click on "Back"
    if x0 <= event.x <= x1:
        if 3 * y - app.offset // 2 <= event.y <= 3 * y + app.offset // 2:
            app.mode = "startScreenMode"

########################################
############## ABOUT MODE ##############
########################################

def aboutMode_redrawAll(app, canvas):
    drawBackground(app, canvas)
    aboutMode_drawAbout(app, canvas)
    aboutMode_drawButtons(app, canvas)
    
def aboutMode_coordinates(app):
    # Coordinates used multiple times in functions across mode
    cx = app.width // 2
    cy = 3 * app.height // 4
    x0 = app.width // 2 - app.offset
    x1 = app.width // 2 + app.offset
    y0 = 3 * app.height // 4 - app.offset // 2
    y1 = 3 * app.height // 4 + app.offset // 2

    return cx, cy, x0, x1, y0, y1

def aboutMode_drawAbout(app, canvas):
    about = ("For budding geologists and lovers of bad 1970s fads\nalike comes "
             "'Rockagotchi', a game where you can\nlive out your dream of being "
             "a rock parent! Raise\nyour rock from infancy to young adulthood "
             "and watch your\nlittle one go off to college right before your "
             "eyes!\n\n'Rockagotchi' is made by me, Bahaar Esfahani, for 15-112"
             "\nat CMU where I'm a Drama major. Confession time: I'm not\neven, "
             "like, some weird fan of rocks or anything. I just\nthought 'What "
             "am I actually capable of drawing?' and\nlanded on a round blob "
             "and ran with it. If there's\nanything I CAN do, though, it's "
             "commit to a bit.\n\nHint: Press 'v' in game mode.")

    canvas.create_text(app.width // 2, app.height // 3 + app.offset // 3, 
                       text = about, anchor = "n", font = "TkFixedFont",
                       fill = rockagotchiPink)

def aboutMode_drawButtons(app, canvas):
    cx, cy, x0, x1, y0, y1 = aboutMode_coordinates(app)

    # "Back" button
    canvas.create_rectangle(x0, y0, x1, y1, fill = rockagotchiPurple, 
                            outline = "")
    canvas.create_image(cx, cy, image = ImageTk.PhotoImage(app.backButton))

def aboutMode_mousePressed(app, event):
    cx, cy, x0, x1, y0, y1 = aboutMode_coordinates(app)

    # If you press "Back"
    if x0 <= event.x <= x1 and y0 <= event.y <= y1:
            app.mode = "startScreenMode"

########################################
############## ADOPT MODE ##############
########################################

def adoptMode_redrawAll(app, canvas):
    drawBackground(app, canvas)
    adoptMode_drawText(app, canvas)
    adoptMode_drawButtons(app, canvas)

def adoptMode_coordinates(app):
    # Coordinates used multiple times in functions across mode
    cx = app.width // 2
    cy = app.height // 2
    x0 = app.width // 2 - app.offset * 1.5
    x1 = app.width // 2 + app.offset * 1.5
    y0 = app.height // 2 - app.offset
    y1 = app.height // 2 + app.offset - app.offset // 2

    return cx, cy, x0, x1, y0, y1

def adoptMode_drawText(app, canvas):
    cx, cy, x0, x1, y0, y1 = adoptMode_coordinates(app)
    text = "Be careful... rocks are a lot of work!"

    canvas.create_text(cx, cy + app.offset, text = text, font = "TkFixedFont",
                       fill = rockagotchiPurple)

def adoptMode_drawButtons(app, canvas):
    cx, cy, x0, x1, y0, y1 = adoptMode_coordinates(app)

    # "Adopt" button
    canvas.create_rectangle(x0, y0, x1, y1, fill = rockagotchiPurple,
                            outline = "")
    canvas.create_image(cx, cy - app.offset // 4,
                        image = ImageTk.PhotoImage(app.adoptButton))

def adoptMode_mousePressed(app, event):
    cx, cy, x0, x1, y0, y1 = adoptMode_coordinates(app)
    
    # If you press "Adopt"
    if x0 <= event.x <= x1 and y0 <= event.y <= y1:
            app.mode = "customizeMode"

############################################
############## CUSTOMIZE MODE ##############
############################################

def customizeMode_redrawAll(app, canvas):
    drawBackground(app, canvas)
    app.rock.drawRock(app, canvas, app.width // 5, app.height // 2 - app.offset)
    customizeMode_drawDoneButton(app, canvas)
    customizeMode_drawSelectionButtons(app, canvas)
    customizeMode_drawText(app, canvas)

def customizeMode_doneButtonCoordinates(app):
    # Coordinates used multiple times in functions across mode
    cx = app.width // 2
    cy = 4 * app.height // 5
    x0 = app.width // 2 - app.offset
    x1 = app.width // 2 + app.offset
    y0 = 4 * app.height // 5 - app.offset // 2
    y1 = 4 * app.height // 5 + app.offset // 2

    return cx, cy, x0, x1, y0, y1

def customizeMode_selectionCoordinates(app):
    # Coordinates used multiple times in functions across mode
    cx = app.width // 5
    cy = app.height // 10
    x0 = app.width // 5 - app.offset
    x1 = app.width // 5 + app.offset
    y = app.height // 10

    return cx, cy, x0, x1, y

def customizeMode_drawSelectionButtons(app, canvas):
    cx, cy, x0, x1, y = customizeMode_selectionCoordinates(app)
    # Random and Reset
    canvas.create_rectangle(x0, 6 * y - app.offset // 2, x1, 
                            6 * y + app.offset // 3, fill = rockagotchiPurple, 
                            outline = "")
    canvas.create_image(cx, 6 * cy, image = ImageTk.PhotoImage(app.resetButton))
    canvas.create_rectangle(x0, 7 * y - app.offset // 2, x1, 
                            7 * y + app.offset // 3, fill = rockagotchiPurple,
                            outline = "")
    canvas.create_image(cx, 7 * cy, image = ImageTk.PhotoImage(app.randomButton))

def customizeMode_drawDoneButton(app, canvas):
    cx, cy, x0, x1, y0, y1 = customizeMode_doneButtonCoordinates(app)

    canvas.create_rectangle(x0, y0, x1, y1, fill = rockagotchiPurple,
                            outline = "")
    canvas.create_image(cx, cy, image = ImageTk.PhotoImage(app.doneButton))

def customizeMode_drawText(app, canvas):
    # Colors
    canvas.create_text(app.width // 2, app.height // 2, 
                       text = "press n for normal\npress m for camo\n"
                       "press c for cheetah\npress r for rainbow\n"
                       "press u for purple\npress i for pink\n"
                       "press v for hearts\npress h for candy corn",
                       font = "TkFixedFont", fill = rockagotchiBlue, 
                       anchor = "s")
    
    # Glasses
    canvas.create_text(app.width // 2, app.height // 2 + app.offset, 
                       text = "press g for nerd\npress p for harry potter\n"
                       "press f for fancy lady\npress b for cool guy",
                       font = "TkFixedFont", fill = rockagotchiBlue, 
                       anchor = "n")
    
    # Costume
    canvas.create_text(2 * app.width // 3 + app.offset,
                       app.height // 3 + app.offset // 2, 
                       text = "press d for tutu\npress s for bowtie\n"
                       "press t for top hat\npress w for blush",
                       font = "TkFixedFont", fill = rockagotchiBlue, 
                       anchor = "w")

    # Pet
    canvas.create_text(2 * app.width // 3 + app.offset,
                       app.height // 2 + app.offset, 
                       text = "press k for chicken\npress o for fish\n"
                       "press y for teddy bear\npress e for rock",
                       font = "TkFixedFont", fill = rockagotchiBlue, 
                       anchor = "nw")

def customizeMode_mousePressed(app, event):
    cx, cy, x0, x1, y0, y1 = customizeMode_doneButtonCoordinates(app)
    cxS, cyS, x0S, x1S, yS = customizeMode_selectionCoordinates(app)
    
    if x0S <= event.x <= x1S:
        # If you press "Reset"
        if 6 * yS - app.offset // 2 <= event.y <= 6 * yS + app.offset // 3:
            app.rock.reset()
        # If you press "Random"
        elif 7 * yS - app.offset // 2 <= event.y <= 7 * yS + app.offset // 3: 
            app.rock.random(app)
    
    # If the rock is still in question marks, user cannot move on
    if app.rock.color == None:
        return
    
    # If you press "Done"
    if x0 <= event.x <= x1 and y0 <= event.y <= y1:
            app.mode = "namingMode"

def customizeMode_keyPressed(app, event):
    # Colors
    if event.key == "n" or event.key == "N":
        app.rock.colorChanger(app.normalColor)
    
    elif event.key == "m" or event.key == "M":
        app.rock.colorChanger(app.camoColor)

    elif event.key == "c" or event.key == "C":
        app.rock.colorChanger(app.cheetahColor)

    elif event.key == "r" or event.key == "R":
        app.rock.colorChanger(app.rainbowColor)

    elif event.key == "u" or event.key == "U":
        app.rock.colorChanger(app.purpleColor)

    elif event.key == "i" or event.key == "I":
        app.rock.colorChanger(app.pinkColor)
    
    elif event.key == "v" or event.key == "V":
        app.rock.colorChanger(app.heartsColor)

    elif event.key == "h" or event.key == "H":
        app.rock.colorChanger(app.candyColor)

    # Glasses
    elif event.key == "g" or event.key == "G":
        app.rock.glassesChanger(app.nerdGlasses)

    elif event.key == "p":
        app.rock.glassesChanger(app.harryPotterGlasses)

    elif event.key == "b" or event.key == "B":
        app.rock.glassesChanger(app.coolGuyGlasses)

    elif event.key == "f" or event.key == "F":
        app.rock.glassesChanger(app.heartGlasses)

    # Costumes
    elif event.key == "d" or event.key == "D":
        app.rock.addTutu()

    elif event.key == "s" or event.key == "S":
        app.rock.addBowtie()

    elif event.key == "t" or event.key == "T":
        app.rock.addHat()

    elif event.key == "w" or event.key == "W":
        app.rock.addBlush()

    # Pets
    elif event.key == "k" or event.key == "K":
        app.rock.petChanger(app.chickenPet)

    elif event.key == "o" or event.key == "O":
        app.rock.petChanger(app.fishPet)

    elif event.key == "y" or event.key == "Y":
        app.rock.petChanger(app.bearPet)

    elif event.key == "e" or event.key == "E":
        app.rock.petChanger(app.rockPet)

#########################################
############## NAMING MODE ##############
#########################################

def namingMode_redrawAll(app, canvas):
    drawBackground(app, canvas)
    namingMode_drawText(app, canvas)
    namingMode_drawInputBox(app, canvas)
    app.rock.drawRock(app, canvas, app.width // 2,
                      app.height // 2 - app.offset // 2)

def namingMode_coordinates(app):
    # Coordinates used multiple times in functions across mode
    cx = app.width // 2
    cy = 2 * app.height // 3
    x0 = app.width // 2 - app.offset * 2
    x1 = app.width // 2 + app.offset * 2
    y0 = 2 * app.height // 3 - app.offset // 3
    y1 = 2 * app.height // 3 + app.offset // 3

    return cx, cy, x0, x1, y0, y1

def namingMode_drawText(app, canvas):
    cx, cy, x0, x1, y0, y1 = namingMode_coordinates(app)
    text = "Congratulations, you're a rock owner! What's their name?"

    canvas.create_text(cx, app.height // 2 + app.offset * 1.25, 
                       text = text, font = "TkFixedFont", 
                       fill = rockagotchiPurple)

def namingMode_drawInputBox(app, canvas):
    # Draws name input box with name and cursor
    cx, cy, x0, x1, y0, y1 = namingMode_coordinates(app)

    canvas.create_rectangle(x0, y0, x1, y1, fill = "white", outline = "")
    canvas.create_text(cx, cy, text = f"{app.name}{app.cursor}",
                       fill = rockagotchiPurple, font = "TkFixedFont")

def namingMode_timerFired(app):
    # For cursor blink
    app.cursorTime += app.timerDelay
   
    # Cursor blinks every 2 timerFired's
    if app.cursorTime % 600 == 0:
        app.cursorState = not app.cursorState

    # Changes cursor state (monospaced font allows this to not shift text)
    if app.cursorState == True:
        app.cursor = "_"
    
    elif app.cursorState == False:
        app.cursor = " "

def namingMode_keyPressed(app, event):
    # For text entry
    # Pressing enter finalizes name and moves user to game
    if event.key == "Return" or event.key == "Enter":
        app.mode = "gameMode"
    
    if (event.key == "BackSpace"):
        # If the first thing the user does is backspace, it entirely deletes the 
        # default name rather than make the user delete each character
        if app.keysPressed == "":
            app.name = app.name[0:0]
        
        else:
            app.name = app.name[0:-1]
            # To track whether the backspace is the first thing a user presses,
            # we initialize an empty list that gets added to with each press
            app.keysPressed = app.keysPressed + event.key
    
    # Doesn't allow for more than 23 characters in name, under "BackSpace" so
    # user can still backspace
    if len(app.name) >= 23:
        return

    elif event.key == "Space":
        app.name = app.name + " "
        app.keysPressed = app.keysPressed + event.key

    # Doesn't allow for keys like "Tab" or "Up" or "Down" etc. to appear
    # but allows all digits and special characters.
    elif len(event.key) == 1:
        app.name = app.name + event.key
        app.keysPressed = app.keysPressed + event.key

#######################################
############## GAME MODE ##############
#######################################

def gameMode_colorTracker(app, mood):
    # Tracks each given mood and changes the bar color appropriately
    if 81 <= mood <= 100:
        barFill = "green"
        textFill = rockagotchiPink
    
    elif 61 <= mood <= 80:
        barFill = "light green"
        textFill = rockagotchiBlue
    
    elif 41 <= mood <= 60:
        barFill = "gold"
        textFill = rockagotchiBlue

    elif 21 <= mood <= 40:
        barFill = "orange"
        textFill = rockagotchiBlue
    
    elif 0 <= mood <= 20:
        barFill = "red"
        textFill = rockagotchiBlue

    return barFill, textFill

def gameMode_redrawAll(app, canvas):
    drawBackground(app, canvas)
    gameMode_drawHungerBar(app, canvas)
    gameMode_drawEnergyBar(app, canvas)
    gameMode_drawFunBar(app, canvas)
    gameMode_drawNameAge(app, canvas)
    gameMode_drawButtons(app, canvas)
    gameMode_drawSpeechBubble(app, canvas)
    app.rock.drawRock(app, canvas, app.width // 2,
                      app.height // 2 - app.offset // 2)

def gameMode_barCoordinates(app):
    # Coordinates used multiple times in functions across mode
    cx = app.width - 3 * app.offset
    x0 = app.width - 5 * app.offset
    x1 = app.width - app.offset

    return cx, x0, x1

def gameMode_drawHungerBar(app, canvas):
    # Draws the hunger bar
    cx, x0, x1 = gameMode_barCoordinates(app)
    barFill, textFill = gameMode_colorTracker(app, app.hunger)
    
    # White bar underneath that stays fixed
    canvas.create_rectangle(x0, app.offset, x1, app.offset * 1.5,
                            fill = "white", outline = "")
    # Mood bar that changes both size and color based on mood
    canvas.create_rectangle(x0, app.offset, app.hungerBar, app.offset * 1.5,
                            fill = barFill, outline = "")
    canvas.create_text(cx, app.offset * 1.25, 
                       text = f"Hunger: {app.hunger}%", font = "TkFixedFont",
                       fill = textFill)
    
def gameMode_drawEnergyBar(app, canvas):
    # Draws the energy bar
    cx, x0, x1 = gameMode_barCoordinates(app)
    barFill, textFill = gameMode_colorTracker(app, app.energy)

    # White bar underneath that stays fixed
    canvas.create_rectangle(x0, app.offset * 2, x1, app.offset * 2.5,
                            fill = "white", outline = "")
    # Mood bar that changes both size and color based on mood
    canvas.create_rectangle(x0, app.offset * 2, app.energyBar, app.offset * 2.5,
                            fill = barFill, outline = "")
    canvas.create_text(cx, app.offset * 2.25, 
                       text = f"Energy: {app.energy}%", font = "TkFixedFont",
                       fill = textFill)
    
def gameMode_drawFunBar(app, canvas):
    # Draws the fun bar
    cx, x0, x1 = gameMode_barCoordinates(app)
    barFill, textFill = gameMode_colorTracker(app, app.fun)

    # White bar underneath that stays fixed
    canvas.create_rectangle(x0, app.offset * 3, x1, app.offset * 3.5,
                            fill = "white", outline = "")
    # Mood bar that changes both size and color based on mood
    canvas.create_rectangle(x0, app.offset * 3, app.funBar, app.offset * 3.5,
                            fill = barFill, outline = "")
    canvas.create_text(cx, app.offset * 3.25, text = f"Fun: {app.fun}%",
                       font = "TkFixedFont", fill = textFill)
    
def gameMode_drawNameAge(app, canvas):
    cx = app.width // 2
    cy = app.height // 2
    # Name
    canvas.create_text(cx, cy + app.offset * 1.5, text = f"{app.name}",
                       fill = rockagotchiPurple, font = "TkFixedFont")
    # Age
    canvas.create_text(cx, cy + app.offset * 2, text = f"Age: {app.age}",
                       fill = rockagotchiPurple, font = "TkFixedFont")
    
def gameMode_drawButtons(app, canvas):
    # "Walk" button
    canvas.create_rectangle(app.width // 4,
                             4 * app.height // 5 - app.offset // 2,
                             (app.width // 2 - 2 * app.offset),
                             4 * app.height // 5 + app.offset // 2,
                             fill = rockagotchiPurple, outline = "")
    canvas.create_image(app.width // 4 + app.offset, 4 * app.height // 5,
                        image = ImageTk.PhotoImage(app.walkButton))
    # "Feed" button
    canvas.create_rectangle(app.width // 2 - app.offset,
                             4 * app.height // 5 - app.offset // 2,
                             app.width // 2 + app.offset, 
                             4 * app.height // 5 + app.offset // 2,
                             fill = rockagotchiPurple, outline = "")
    canvas.create_image(app.width // 2, 4 * app.height // 5,
                        image = ImageTk.PhotoImage(app.feedButton))
    # "Sleep" button
    canvas.create_rectangle((3 * app.width // 4 - 2 * app.offset),
                             4 * app.height // 5 - app.offset // 2,
                             3 * app.width // 4, 
                             4 * app.height // 5 + app.offset // 2,
                             fill = rockagotchiPurple, outline = "")
    canvas.create_image(3 * app.width // 4 - app.offset, 4 * app.height // 5, 
                        image = ImageTk.PhotoImage(app.sleepButton))

def gameMode_food(app):
    # Random list of food. One is chosen each time "Feed" is legally pressed
    # Based on the favorite foods of my friends on Instagram!
    foodList = ["figs", "mac 'n' cheese", "rice", "corn and beans",
                "shrimp", "seafood boil", "Puerto Rican\npasteles",
                "curried vegetables\nfrom the UGA dining\nhall",
                "flat iron steak", "chicken adobo", "pasta", "pesto",
                "sweet potatoes", "pozole", "burger", "chili",
                "lasagna from\nKatie Mae's mom", "french fries", "wings",
                "waffles", "spaghetti and\nmeatballs", "Mediterranean\nfood", 
                "toasted bagel\nwith cream cheese", "wedding soup",
                "masala dosa", "bean and cheese\nburrito", "ramen"]
    
    food = random.choice(foodList)
    return food

def gameMode_drawSpeechBubble(app, canvas):
    # Stores all the possible phrases the rock can say
    speechBubble = ["Thanks for adopting\na rock in need like me!",
                    "I may just be a rock,\nbut I love spending\ntime with you!", 
                    ("Yay! I love walks!\nI know you feel like\nI kind of just, "
                    "sit\nthere… but it sure\nmakes me happy!"),
                    "Every rock needs\nits beauty sleep!",
                    f"Yummmmm! Thanks for\nthe {app.food}!",
                    "I’m too tired to walk\nright now!",
                    "I’ll fall asleep in my food\nif I try and eat right now!",
                    "I’m too hungry to\ngo on a walk!",
                    ("My stomach is growling\ntoo much for me to fall\n"
                    "asleep right now!"),
                    ("I would eat… but could\nyou put me in front\nof the TV "
                    "first or\nsomething? I’m bored!"), 
                    ("I would sleep… but could\nyou read me a bed time\nstory "
                    "first or something?\nI’m bored!"), 
                    "I want to go on vacation!",
                    "Hey, I'm tired!", "Hey, I'm hungry!", "Hey, I'm bored!"]

    canvas.create_text(app.width // 5, app.height // 4, 
                       text = f"{speechBubble[app.speechBubbleIndex]}",
                       font = "TkFixedFont", fill = rockagotchiPurple)

def gameMode_needsBounds(app):
    # Bar does not go less than zero
    if app.hunger <= 0:
        app.hunger = 0
        app.hungerBar = app.width - 5 * app.offset
    
    if app.energy <= 0:
        app.energy = 0
        app.energyBar = app.width - 5 * app.offset

    if app.fun <= 0:
        app.fun = 0
        app.funBar = app.width - 5 * app.offset
    
    # Bar does not go more than 100
    if app.hunger >= 100:
        app.hunger = 100
        app.hungerBar = app.width - app.offset
    
    if app.energy >= 100:
        app.energy = 100
        app.energyBar = app.width - app.offset

    if app.fun >= 100:
        app.fun = 100
        app.funBar = app.width - app.offset

def gameMode_defaultSpeech(app):     
    # If nothing has been selected...
    if app.walk != True and app.sleep != True and app.feed != True:
        # ...and energy is less than 40, rock says it's tired
        if app.energy <= 40:
            app.speechBubbleIndex = 12
        # ...if energy not less than 40 but hunger is, rock says it's hungry
        elif app.hunger <= 40:
            app.speechBubbleIndex = 13

        # ...if energy and hunger not less than 40, 
        # but fun is, rock says it's bored
        elif app.fun <= 40:
            app.speechBubbleIndex = 14

        # ...if nothing is less than 40, default happy text
        else:
            if app.chances == None:
                app.speechBubbleIndex = 0

            elif app.chances <= 8:
                app.speechBubbleIndex = 1
                
        # 20% chance for secret "vacation" hint as default happy text
            else:
                app.speechBubbleIndex = 11

    # If something has been selected...
    elif app.walk == True or app.sleep == True or app.feed == True:
        # ...start a timer
        app.needsSelectionTime += app.timerDelay
        # Once the timer hits its limit, selection is changed back to false
        # to allow default text to reappear
        if app.needsSelectionTime >= 3600:
            app.needsSelectionTime = 0
            app.walk = False
            app.sleep = False
            app.feed = False

def gameMode_timerFired(app):
    app.rock.moodChanger(app)
    allMoods = app.hunger + app.energy + app.fun
    app.time += app.timerDelay
    
    # Every 10 seconds needs go down
    if app.time % 9900 == 0:
        gameMode_toggleNeeds(app, "down", "all")
    
    # Every 60 seconds... birthday!
    if app.time % 59400 == 0:
        app.age += 1

    # Gameover
    if allMoods == 0:
        app.mode = "gameOverMode"

    if app.age > 18:
        app.mode = "happyGameOverMode"

    # Checks default speech and bounds each timer fired
    gameMode_defaultSpeech(app)
    gameMode_needsBounds(app)

def gameMode_mousePressed(app, event):
    if 4 * app.height // 5 - app.offset <= event.y <= 4 * app.height // 5 + app.offset:
        # If you press "Sleep"
        if (3 * app.width // 4 - 2 * app.offset) <= event.x <= 3 * app.width // 4:
            app.sleep = True
            app.feed = False
            app.walk = False
            app.chances = random.randint(1, 10)
        
        # If you press "Feed"
        elif app.width // 2 - app.offset <= event.x <= app.width // 2 + app.offset:
            app.feed = True
            app.sleep = False
            app.walk = False
            app.food = gameMode_food(app)
            app.chances = random.randint(1, 10)
        
        #If you press "Walk"
        elif app.width // 4 <= event.x <= (app.width // 2 - 2 * app.offset):
            app.walk = True
            app.sleep = False
            app.feed = False
            app.chances = random.randint(1, 10)

    # Checks hierarchy of needs to see if press is legal
    gameMode_checkNeedsHierarchy(app)

def gameMode_checkNeedsHierarchy(app):
    # If you pressed "Sleep"...
    if app.sleep == True:
        # ...if energy is not critical and hunger is, appropriate refusal text
        if app.energy > 40 and app.hunger <= 40:
            app.speechBubbleIndex = 8
        # ...if energy and hunger are not critical but fun is, 
        # appropriate refusal text
        elif app.energy > 40 and app.fun <= 40:
            app.speechBubbleIndex = 10
        # ...if neither of the above checks, move is legal and energy toggles
        # appropriately
        else:
            gameMode_toggleNeeds(app, "up", "energy")

    # If you pressed "Feed"...
    elif app.feed == True:
        # ...if energy is critical, appropriate refusal text
        if app.energy <= 40:
            app.speechBubbleIndex = 6
        # ...if energy and hunger are not critical but fun is, 
        # appropriate refusal text
        elif app.hunger > 40 and app.fun <= 40:
            app.speechBubbleIndex = 9
        # ...if neither of the above checks, move is legal and hunger toggles
        # appropriately
        else:
            gameMode_toggleNeeds(app, "up", "hunger")

    # If you pressed "Walk"...
    elif app.walk == True:
        # ...if energy is critical, appropriate refusal text
        if app.energy <= 40:
            app.speechBubbleIndex = 5
        # ...if hunger is critical, appropriate refusal text
        elif app.hunger <= 40:
            app.speechBubbleIndex = 7
        # ...if neither of the above checks, move is legal and fun toggles
        # appropriately
        else:
            gameMode_toggleNeeds(app, "up", "fun")
    
def gameMode_toggleNeeds(app, direction, need):
    # Used to toggle needs the appropriate amount based on selection. Though user
    # can't toggle needs "down" in game, used for debugging in keyPressed
    if direction == "down" and need == "all":
            app.hunger -= 5
            app.hungerBar -= 10
            app.energy -= 5
            app.energyBar -= 10
            app.fun -= 10
            app.funBar -= 20

    if direction == "up":
        if need == "all":
            app.hunger += 5
            app.hungerBar += 10
            app.energy += 5
            app.energyBar += 10
            app.fun += 10
            app.funBar += 20

        elif need == "energy":
            app.energy += 80
            app.energyBar += 160
            app.speechBubbleIndex = 3

        elif need == "hunger":
            app.hunger += 60
            app.hungerBar += 120
            app.speechBubbleIndex = 4

        elif need == "fun":
            app.fun += 30
            app.funBar += 60
            app.energy -= 5
            app.energyBar -= 10
            app.speechBubbleIndex = 2
        
        gameMode_needsBounds(app)

def gameMode_keyPressed(app, event):
    # Secret vacation mode! Makes fun automatically 100!
    if event.key == "v" or event.key == "V":
        app.mode = "vacationMode"
        app.fun += 100
    
    # *** For debugging purposes ***
    # Toggle age up and down
    if event.key == "Up":
        app.age += 1

    if event.key == "Down" and app.age != 0:
        app.age -= 1

    # Toggle needs right and left
    if event.key == "Right":
        gameMode_toggleNeeds(app, "up", "all")

    if event.key == "Left":
        gameMode_toggleNeeds(app, "down", "all")

    gameMode_needsBounds(app)

###########################################
############## VACATION MODE ##############
###########################################

def vacationMode_redrawAll(app, canvas):
    drawBackground(app, canvas)
    vacationMode_drawButtons(app, canvas)
    vacationMode_drawText(app, canvas)
    vacationMode_drawSelectionBoxes(app, canvas)

def vacationMode_drawText(app, canvas):
    x = app.width // 2
    y = app.height // 3 - app.offset // 1.5
    canvas.create_text(x, y, text = ("Choose a vacation "
                       "destination and check your desktop for a souvenir!"), 
                       fill = rockagotchiBlue, font = "TkFixedFont")

def vacationMode_drawButtons(app, canvas):
    # "Back" button
    canvas.create_rectangle(app.width // 2 - app.offset,
                             4 * app.height // 5 - app.offset // 2,
                             app.width // 2 + app.offset, 
                             4 * app.height // 5 + app.offset // 2,
                             fill = rockagotchiPurple, outline = "")
    canvas.create_image(app.width // 2, 4 * app.height // 5,
                        image = ImageTk.PhotoImage(app.backButton))

def vacationMode_selectionBoxCoordinates(app):
    # Coordinates used multiple times in functions across mode
    x = app.width // 5
    y0 = app.height // 2 - app.offset * 2
    y1 = app.height // 2 + app.offset * 2

    return x, y0, y1

def vacationMode_drawSelectionBoxes(app, canvas):
    x, y0, y1 = vacationMode_selectionBoxCoordinates(app)
    
    # "Grand Canyon" button
    canvas.create_image(x, app.height // 2,
                        image = ImageTk.PhotoImage(app.grandCanyonPreview))
    canvas.create_rectangle(x - app.offset * 2, y0, x + app.offset * 2, y1, 
                            fill = "", outline = rockagotchiPurple, width = 10)
    # "Mount Everest" button
    canvas.create_image(2.5 * x, app.height // 2,
                        image = ImageTk.PhotoImage(app.everestPreview))
    canvas.create_rectangle(2.5 * x - app.offset * 2, y0, 2.5 * x + app.offset * 2, y1, 
                            fill = "", outline = rockagotchiPurple, width = 10)
    
    # "Rock and Roll Hall of Fame" button
    canvas.create_image(4 * x, app.height // 2,
                        image = ImageTk.PhotoImage(app.rockAndRollPreview))
    canvas.create_rectangle(4 * x - app.offset * 2, y0, 4 * x + app.offset * 2, y1,
                            fill = "", outline = rockagotchiPurple, width = 10)

def vacationMode_mousePressed(app, event):
    x, y0, y1 = vacationMode_selectionBoxCoordinates(app)
    
    # If you press "Back" button
    if (4 * app.height // 5 - app.offset <= event.y <= 
        4 * app.height // 5 + app.offset and app.width // 2 - app.offset <= 
        event.x <= app.width // 2 + app.offset):
            app.mode = "gameMode"

    if y0 <= event.y <= y1:
    # If you press "Grand Canyon"
        if x - app.offset * 2 <= event.x <= x + app.offset * 2:
            # Sets the right destination for the photo and prints
            app.vacationDestination = app.grandCanyon
            app.vacationDestinationName = "the Grand Canyon"
            app.rock.saveRock(app)
            app.mode = "gameMode"
    # Mount Everest
        if 2.5 * x - app.offset * 2 <= event.x <= 2.5 * x + app.offset * 2:
            app.vacationDestination = app.everest
            app.vacationDestinationName = "Mount Everest"
            app.rock.saveRock(app)
            app.mode = "gameMode"

    # Rock and Roll Hall of Fame
        if 4 * x - app.offset * 2 <= event.x <= 4 * x + app.offset * 2:
            app.vacationDestination = app.rockAndRoll
            app.vacationDestinationName = "the Rock and Roll Hall of Fame"
            app.rock.saveRock(app)
            app.mode = "gameMode"

############################################
############## GAME OVER MODE ##############
############################################

def gameOverMode_redrawAll(app, canvas):
    drawBackground(app, canvas)
    gameOverMode_drawText(app, canvas)
    gameOverMode_drawButtons(app, canvas)

def gameOverMode_coordinates(app):
    # Coordinates used multiple times in functions across mode
    cx = app.width // 2
    cy = 4 * app.height // 5
    x0 = app.width // 2 - app.offset * 1.5
    x1 = app.width // 2 + app.offset * 1.5
    y0 = 4 * app.height // 5 - app.offset // 2
    y1 = 4 * app.height // 5 + app.offset // 2

    return cx, cy, x0, x1, y0, y1

def gameOverMode_drawText(app, canvas):
    cx, cy, x0, x1, y0, y1 = gameOverMode_coordinates(app)
    text = (f"Oh no... {app.name} seems to have... grown legs? and ran\naway!!!? "
            "Maybe take better care of it next time...")

    canvas.create_text(cx, app.height // 2 + app.offset * 1.25, 
                       text = text, font = "TkFixedFont",
                       fill = rockagotchiPurple)

def gameOverMode_drawButtons(app, canvas):
    cx, cy, x0, x1, y0, y1 = gameOverMode_coordinates(app)

    # "Play again" button
    canvas.create_rectangle(x0, y0, x1, y1, fill = rockagotchiPurple,
                            outline = "")
    canvas.create_image(cx, cy, image = ImageTk.PhotoImage(app.playAgainButton))

def gameOverMode_mousePressed(app, event):
    cx, cy, x0, x1, y0, y1 = gameOverMode_coordinates(app)
    
    # If you press "Play again"
    if x0 <= event.x <= x1:
        if y0 <= event.y <= y1:
            restart(app)

##################################################
############## HAPPY GAME OVER MODE ##############
##################################################

def happyGameOverMode_redrawAll(app, canvas):
    drawBackground(app, canvas)
    happyGameOverMode_drawText(app, canvas)
    happyGameOverMode_drawButtons(app, canvas)

def happyGameOverMode_coordinates(app):
    # Coordinates used multiple times in functions across mode
    cx = app.width // 2
    cy = 4 * app.height // 5
    x0 = app.width // 2 - app.offset * 1.5
    x1 = app.width // 2 + app.offset * 1.5
    y0 = 4 * app.height // 5 - app.offset // 2
    y1 = 4 * app.height // 5 + app.offset // 2

    return cx, cy, x0, x1, y0, y1

def happyGameOverMode_drawText(app, canvas):
    cx, cy, x0, x1, y0, y1 = happyGameOverMode_coordinates(app)
    text = f"{app.name} is off to college. *sniff* They grow up so fast!"

    canvas.create_text(cx, app.height // 2 + app.offset * 1.25, 
                       text = text, font = "TkFixedFont",
                       fill = rockagotchiPurple)

def happyGameOverMode_drawButtons(app, canvas):
    cx, cy, x0, x1, y0, y1 = happyGameOverMode_coordinates(app)

    # "Play again" button
    canvas.create_rectangle(x0, y0, x1, y1, fill = rockagotchiPurple, 
                            outline = "")
    canvas.create_image(cx, cy, image = ImageTk.PhotoImage(app.playAgainButton))

def happyGameOverMode_mousePressed(app, event):
    cx, cy, x0, x1, y0, y1 = happyGameOverMode_coordinates(app)
    
    # If you press "Play again"
    if x0 <= event.x <= x1:
        if y0 <= event.y <= y1:
            restart(app)

######################################
############## MAIN APP ##############
######################################

# Rock object tracks chosen name and clothing across modes
class Rock(object):
    def __init__(self, name, age, outline, resetColor, mood, color = None, 
                 glasses = None, tutu = False, hat = False, blush = False,
                 bowtie = False, pet = None):

        self.name = name
        self.age = age
        self.outline = outline
        self.resetColor = resetColor
        self.color = color
        self.mood = mood
        self.glasses = glasses
        self.tutu = tutu
        self.hat = hat
        self.blush = blush
        self.bowtie = bowtie
        self.pet = pet

    # Changers/adders used in customizer
    def colorChanger(self, newColor):
        # If you click on an already selected option, it unselects
        if self.color == newColor:
            self.color = None
        else:
            self.color = newColor

    def glassesChanger(self, newGlasses):
        if self.glasses == newGlasses:
            self.glasses = None
        else:
            self.glasses = newGlasses

    def petChanger(self, newPet):
        if self.pet == newPet:
            self.pet = None
        else:
            self.pet = newPet

    def addTutu(self):
        self.tutu = not self.tutu

    def addHat(self):
        self.hat = not self.hat

    def addBlush(self):
        self.blush = not self.blush

    def addBowtie(self):
        self.bowtie = not self.bowtie

    # Reset used in customizer
    def reset(self):
        self.color = None
        self.glasses = None
        self.tutu = False
        self.hat = False
        self.blush = False
        self.bowtie = False
        self.pet = None

    # Random used in customizer
    def random(self, app):
        self.color = random.choice(app.colorsList)
        self.glasses = random.choice(app.glassesList)
        self.tutu = random.choice([True, False])
        self.hat = random.choice([True, False])
        self.blush = random.choice([True, False])
        self.bowtie = random.choice([True, False])
        self.pet = random.choice(app.petsList)

    # Changes facial expression based on mood
    def moodChanger(self, app):
        allMoods = app.hunger + app.energy + app.fun
        
        if 240 <= allMoods <= 300:
            self.mood = app.ecstatic
        
        if 180 <= allMoods <= 239:
            self.mood = app.happy

        if 120 <= allMoods <= 179:
            self.mood = app.neutral

        if 60 <= allMoods <= 119:
            self.mood = app.annoyed

        if 0 <= allMoods <= 59:
            self.mood = app.angry
    
    # saveRock derived with help from armaanaki (https://github.com/armaanaki)
    def saveRock(self, app):
        rock = Image.new("RGBA", (800, 600))
        
        app.vacationDestination.paste(self.color, (0, 0), self.color)
        app.vacationDestination.paste(self.outline, (0, 0), self.outline)
        app.vacationDestination.paste(app.eyes, (0, 0), app.eyes)
        app.vacationDestination.paste(app.ecstatic, (0, 0), app.ecstatic)
            
        if self.glasses != None:
            app.vacationDestination.paste(self.glasses, (0, 0), self.glasses)
            
        if self.tutu == True:
            app.vacationDestination.paste(app.tutu, (0, 0), app.tutu)
            
        if self.hat == True:
            app.vacationDestination.paste(app.hat, (0, 0), app.hat)
            
        if self.blush == True:
            app.vacationDestination.paste(app.blush, (0, 0), app.blush)
            
        if self.bowtie == True:
            app.vacationDestination.paste(app.bowtie, (0, 0), app.bowtie)
            
        if self.pet != None:
            app.vacationDestination.paste(self.pet, (0, 0), self.pet)

        app.vacationDestination.save(os.path.expanduser(f"~/Desktop/{app.name} "
            f"at {app.vacationDestinationName}.png"))
    
    # Draws rock in proper layering order. Only draws if actually selected!
    def drawRock(self, app, canvas, x, y):
        canvas.create_image(x, y, image = ImageTk.PhotoImage
                           (app.scaleImage(self.resetColor, 2/5)))
        
        if self.color != None:
            canvas.create_image(x, y, image = ImageTk.PhotoImage
                               (app.scaleImage(self.color, 2/5)))
            canvas.create_image(x, y, image = ImageTk.PhotoImage
                               (app.scaleImage(app.eyes, 2/5)))
            canvas.create_image(x, y, image = ImageTk.PhotoImage
                               (app.scaleImage(self.mood, 2/5)))
            canvas.create_image(x, y, image = ImageTk.PhotoImage
                               (app.scaleImage(self.outline, 2/5)))
        
        if self.glasses != None:
            canvas.create_image(x, y, image = ImageTk.PhotoImage
                               (app.scaleImage(self.glasses, 2/5)))

        if self.tutu == True:
            canvas.create_image(x, y, image = ImageTk.PhotoImage
                               (app.scaleImage(app.tutu, 2/5)))

        if self.hat == True:
            canvas.create_image(x, y, image = ImageTk.PhotoImage
                               (app.scaleImage(app.hat, 2/5)))

        if self.blush == True:
            canvas.create_image(x, y, image = ImageTk.PhotoImage
                               (app.scaleImage(app.blush, 2/5)))
        
        if self.bowtie == True:
            canvas.create_image(x, y, image = ImageTk.PhotoImage
                               (app.scaleImage(app.bowtie, 2/5)))
        
        if self.pet != None:
            canvas.create_image(x, y, image = ImageTk.PhotoImage
                               (app.scaleImage(self.pet, 2/5)))

def restart(app):
    backgroundImages(app)
    buttonImages(app)
    rockImages(app)

    # Initializing modes and important numbers
    app.mode = "startScreenMode"
    app.offset = 50
    
    # Rock attributes
    app.defaultNames = ["Rock 'The Rock' Rockson", "Erocka", "Brock",
                        "Rocky Gervais", "Roc Flair, pro wrestler", 
                        "Rock and Morty", "Rocky Martin", "Eroc", "Patrock",
                        "Rocky Balboa"]
    app.name = random.choice(app.defaultNames)
    app.age = 0
    app.rock = Rock(app.name, app.age, app.rockOutline, app.resetColor, app.ecstatic)
    
    # Used in customizeMode
    app.colorsList = [app.normalColor, app.camoColor, app.cheetahColor, 
                      app.rainbowColor, app.purpleColor, app.pinkColor, 
                      app.heartsColor, app.candyColor]
    app.glassesList = [app.coolGuyGlasses, app.harryPotterGlasses,
                       app.heartGlasses, app.nerdGlasses, None]
    app.petsList = [app.bearPet, app.chickenPet, app.fishPet, app.rockPet, None]
    
    # Used in namingMode
    app.cursor = "_"
    app.keysPressed = ""
    app.cursorState = True
    app.cursorTime = 0

    # Used in gameMode
    app.hunger = 100
    app.energy = 100
    app.fun = 100

    app.hungerBar = app.width - app.offset
    app.energyBar = app.width - app.offset
    app.funBar = app.width - app.offset
    
    app.walk = False
    app.sleep = False
    app.feed = False
    
    app.speechBubbleIndex = 0
    app.time = 0
    app.needsSelectionTime = 0
    app.food = ""
    app.chances = None

    # Used in vacationMode
    app.vacationDestination = None
    app.vacationDestinationName = None

def drawBackground(app, canvas):
    # Draws appropriate background based on current mode
    if app.mode == "startScreenMode":
        canvas.create_image(app.width // 2, app.height // 2,
                            image = ImageTk.PhotoImage(app.titleBackground))
    
    elif app.mode == "aboutMode":
        canvas.create_image(app.width // 2, app.height // 2,
                            image = ImageTk.PhotoImage(app.aboutBackground))
 
    elif app.mode == "instructionsMode":
        canvas.create_image(app.width // 2, app.height // 2,
                            image = ImageTk.PhotoImage(app.instructionsBackground))

    elif app.mode == "customizeMode":
        canvas.create_image(app.width // 2, app.height // 2,
                            image = ImageTk.PhotoImage(app.customizeBackground))
    
    elif app.mode == "gameMode":
        canvas.create_image(app.width // 2, app.height // 2,
                            image = ImageTk.PhotoImage(app.gameBackground))

    elif app.mode == "gameOverMode":
        canvas.create_image(app.width // 2, app.height // 2,
                            image = ImageTk.PhotoImage(app.gameOverBackground))

    elif app.mode == "happyGameOverMode":
        canvas.create_image(app.width // 2, app.height // 2,
                            image = ImageTk.PhotoImage(app.happyGameOverBackground))

    elif app.mode == "vacationMode":
        canvas.create_image(app.width // 2, app.height // 2,
                            image = ImageTk.PhotoImage(app.vacationBackground))
    
    else:
        canvas.create_image(app.width // 2, app.height // 2,
                            image = ImageTk.PhotoImage(app.defaultBackground))

# All loaded images, (at the bottom because ahhhhhh)
def backgroundImages(app):
    app.titleBackground = app.loadImage('images/background_title.png')
    app.instructionsBackground = app.loadImage('images/background_instructions.png')
    app.aboutBackground = app.loadImage('images/background_about.png')
    app.customizeBackground = app.loadImage('images/background_customize.png')
    app.defaultBackground = app.loadImage('images/background_main.png')
    app.gameBackground = app.loadImage('images/background_game.png')
    app.gameOverBackground = app.loadImage('images/background_game over.png')
    app.happyGameOverBackground1 = app.loadImage('images/background_happy game over 1.png')
    app.happyGameOverBackground2 = app.loadImage('images/background_happy game over 2.png')
    app.happyGameOverBackground = random.choice([app.happyGameOverBackground1, 
                                                 app.happyGameOverBackground2])
    app.vacationBackground = app.loadImage('images/background_vacation.png')

    app.grandCanyon = app.loadImage('images/vacation_grand canyon.png')
    app.grandCanyonPreview = app.scaleImage(app.loadImage('images/preview_grand canyon.png'), 1/3)
    app.everest = app.loadImage('images/vacation_mount everest.png')
    app.everestPreview = app.scaleImage(app.loadImage('images/preview_mount everest.png'), 1/3)
    app.rockAndRoll = app.loadImage('images/vacation_rock and roll.png')
    app.rockAndRollPreview = app.scaleImage(app.loadImage('images/preview_rock and roll.png'), 1/3)

def buttonImages(app):
    app.playButton = app.scaleImage(app.loadImage('images/button_play.png'), 1/4)
    app.instructionsButton = app.scaleImage(app.loadImage('images/button_instructions.png'), 1/4)
    app.aboutButton = app.scaleImage(app.loadImage('images/button_about.png'), 1/4)
    app.backButton = app.scaleImage(app.loadImage('images/button_back.png'), 1/7)
    app.adoptButton = app.scaleImage(app.loadImage('images/button_adopt.png'), 1/6)
    
    app.randomButton = app.scaleImage(app.loadImage('images/button_random.png'), 1/8)
    app.resetButton = app.scaleImage(app.loadImage('images/button_reset.png'), 1/8)
    app.doneButton = app.scaleImage(app.loadImage('images/button_done.png'), 1/9)
    
    app.walkButton = app.scaleImage(app.loadImage('images/button_walk.png'), 1/9)
    app.feedButton = app.scaleImage(app.loadImage('images/button_feed.png'), 1/9)
    app.sleepButton = app.scaleImage(app.loadImage('images/button_sleep.png'), 1/9)

    app.playAgainButton = app.scaleImage(app.loadImage('images/button_play again.png'), 1/6)
    
def rockImages(app):
    # Rock customizer
    app.rockOutline = app.loadImage('images/rock_outline.png')
    
    # Colors
    app.resetColor = app.loadImage('images/reset_default.png')
    app.normalColor = app.loadImage('images/color_normal.png')
    app.camoColor = app.loadImage('images/color_camo.png')
    app.cheetahColor = app.loadImage('images/color_cheetah.png')
    app.rainbowColor = app.loadImage('images/color_rainbow.png')
    app.purpleColor = app.loadImage('images/color_purple.png')
    app.pinkColor = app.loadImage('images/color_pink.png')
    app.heartsColor = app.loadImage('images/color_hearts.png')
    app.candyColor = app.loadImage('images/color_candy.png')

    # Glasses
    app.coolGuyGlasses = app.loadImage('images/glasses_cool guy.png')
    app.harryPotterGlasses = app.loadImage('images/glasses_harry potter.png')
    app.heartGlasses = app.loadImage('images/glasses_heart.png')
    app.nerdGlasses = app.loadImage('images/glasses_nerd.png')

    # Costumes
    app.hat = app.loadImage('images/accessory_hat.png')
    app.tutu = app.loadImage('images/accessory_tutu.png')
    app.bowtie = app.loadImage('images/accessory_bowtie.png')
    app.blush = app.loadImage('images/accessory_blush.png')
    
    # Pet
    app.bearPet = app.loadImage('images/pet_bear.png')
    app.chickenPet = app.loadImage('images/pet_chicken.png')
    app.fishPet = app.loadImage('images/pet_fish.png')
    app.rockPet = app.loadImage('images/pet_rock.png')

    # Rock moods
    app.eyes = app.loadImage('images/mood_eyes.png')
    app.ecstatic = app.loadImage('images/mood_ecstatic.png')
    app.happy = app.loadImage('images/mood_happy.png')
    app.neutral = app.loadImage('images/mood_neutral.png')
    app.annoyed = app.loadImage('images/mood_annoyed.png')
    app.angry = app.loadImage('images/mood_angry.png')

def playRockagotchi():
    runApp(width = 800, height = 600)

def appStarted(app):
    restart(app)

playRockagotchi()
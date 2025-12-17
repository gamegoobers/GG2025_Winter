# The script of the game goes in this file.


# Declare characters used by this game. The color argument colorizes the
# name of the character.
define kid = Character("Kid", color="#00b3ff")
define dad = Character("Dad", color="#0037ff")

# Declare Backgrounds
image bg frontdoor = im.Scale("bg tempfrontdoor.png", 1920, 1080)
image bg doorway = im.Scale("bg doorway.png", 1920, 1080)
image bg kitchen = im.Scale("bg kitchen.png", 1920, 1080)

# The game starts here.
label start:

    # Show a background. This uses a placeholder by default, but you can
    # add a file (named either "bg room.png" or "bg room.jpg") to the
    # images directory to show it.
    scene bg frontdoor

    # This shows a character sprite. A placeholder is used, but you can
    # replace it by adding a file named "eileen happy.png" to the images
    # directory.
    # show eileen happy

    # These display lines of dialogue.
    "{i}This is the beginning of Divorced Dad Sim (Title Pending)"

## ====  Example Choice menu code ===== ##
    # window hide dissolve
    # menu:
    #     "Choice 1":
    #         pass

    #     "Choice 2":
    #         pass

    #     "Choice 3":
    #         pass
## =================================== ##

    show kid temp at center with dissolve

    kid "coding with RenPy is definitely gonna need some getting used to"

label junction:

    show bg doorway with dissolve

    show kid temp at center with move

    menu:
        "Dog":
            jump dog

        "Prototype Microwave Game":
            jump kitchen

        "End Game":
            jump ending

label dog:

    show kid temp at left with move

    kid "ayo is that a f*ckin' DOG?"

    dad ".{cps=1}.."

    show screen example 
    play sound "audio/vine-boom.mp3"

    ""

    hide screen example

    jump junction

label kitchen:    

    show bg kitchen with dissolve

    call screen microwavegame

    show kid at center with move

    if (abs(5.0 - microwave_time) < 0.3):

        $ culinary_expert = True

        kid "yo we got a culinary expert over here"

    else:

        $ culinary_expert = False

        kid "booo you stink"
    
    jump junction

screen example():
    add "its-cold-out-imma-wear-my-jamas-question-mark-dog-restored-v0-009m4oh1o0b91.webp": 
        align (0.5, 0.2)

default microwave_time = 0.0
default start_timer = False
default game_started = False
default culinary_expert = False
screen microwavegame():
    on "show" action [SetVariable("microwave_time", 0.0), SetVariable("start_timer", False), SetVariable("game_started", False), SetVariable("culinary_expert", False)]
    frame:
        background "#000a" 
        text "Stop the Timer as close to 5.0 Seconds as possible" 
        xalign 0.5 yalign 0.1
    frame:
        background "#000a" 
        hbox:
            textbutton "Start/ Stop" action [ToggleVariable("start_timer"), SetVariable ("game_started", True), If(game_started is True, Return(), None)]
            textbutton "Reset" action SetVariable("microwave_time", 0.0)
            spacing 20
        xalign 0.5 
        yalign 0.3
    frame:
        background "#000a" 
        text "Time elapsed: [microwave_time:.1f]"
        xalign 0.5 yalign 0.2

    if start_timer:
        timer 0.1 action [SetVariable("microwave_time", microwave_time + 0.1)] repeat start_timer

label ending:

    show kid at center with move

    if culinary_expert:

        kid "yo this pizza pocket kinda hit ngl, ya did good Chef"

    else:

        kid "bro how'd you f*ck up the microwave game, the timer ain't even hidden LOL"

    kid "anyway game's over byeeeeeeeee"

    # This ends the game.
    return
# The script of the game goes in this file.


# Declare characters used by this game. The color argument colorizes the
# name of the character.
define kid = Character("Kid", color="#00b3ff")
define dad = Character("Dad", color="#0037ff")

# Declare Backgrounds
image bg frontdoor = im.Scale("bg tempfrontdoor.png", 1920, 1080)

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

    show kid temp at center

    kid "coding with RenPy is definitely gonna need some getting used to"

    show kid temp at left with move

    kid "ayo is that a f*ckin' DOG?"

    dad ".{cps=1}.."

    show screen example 
    play sound "audio/vine-boom.mp3"

    call screen microwavegame

    ""

    # This ends the game.
    return

screen example():
    add "its-cold-out-imma-wear-my-jamas-question-mark-dog-restored-v0-009m4oh1o0b91.webp": 
        align (0.5, 0.2)

init:
    $ current_time = 0
    $ start_timer = False
    
screen microwavegame():
    hbox:
        xalign 0.5 
        yalign 0.2
        textbutton "Start" action SetVariable("start_timer", True)
        textbutton "Stop" action SetVariable("start_timer", False)
        textbutton "Reset" action SetVariable("current_time", 0.0)

    text "Time elapsed: [current_time:.1f]" xalign 0.5 yalign 0.1

    if start_timer:
        timer 0.1 action SetScreenVariable("current_time", current_time + 0.1) repeat start_timer

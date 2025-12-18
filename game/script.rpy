# The script of the game goes in this file.


# Declare characters used by this game. The color argument colorizes the
# name of the character.
define kid = Character("Kid", color="#00b3ff")
define dad = Character("Dad", color="#0037ff")

# Declare Backgrounds
image bg frontdoor = im.Scale("bg tempfrontdoor.png", 1920, 1080)
image bg doorway = im.Scale("bg doorway.png", 1920, 1080)
image bg kitchen = im.Scale("bg kitchen.png", 1920, 1080)
image bg diningtable = im.Scale("bg diningtable.png", 1920, 1080)
image table = im.Scale("table.png", 1920, 1080)

init:
    $ performance = 0

transform halfsize:
    zoom 0.5

transform diningposition:
    xalign 0.5
    yalign 0.4

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

    "{i}You are suddenly woken up by a text on your phone"

    "{i}you check your phone screen and read a text from your ex-wife"

    "\"By the way, just dropped off K. {w}First time in a while he's spending his birthday with you, huh?\""

    dad "{alpha=0.5}It's his birthday?" with hpunch

    # play sound "door knocking sound effect"

    dad "{alpha=0.5}What time is it?"

    "{i}[[12:04 PM, July 16th]"

    dad "{alpha=0.5}He's here? {w}But I have nothing prepared!"

    "{i}You run to the door and let your son in..."

    show kid neutral temp at halfsize, center with dissolve

    dad "Hey Kiddo... {w}another year, {w}another..."

    window hide dissolve
    menu:
        "June 16th":
            $ performance += 0
        "July 16th":
            $ performance += 1
        "July 15th":
            $ performance += 0
            
    if performance == 1:

        kid "Yeah, {w}another year..."

    else:

        kid "Uh... {w}not quite..."

        dad "oh... {w}sorry Kiddo..."

    dad "How does some homemade lunch sound? {w}And of course, {w}I've got your present ready to go too!"
    
    dad "{alpha=0.5}Wait, I don't... {w}what am I going to do?"

    kid "Yeah, sounds cool. {w}I have homework due soon so I asked Mom to pick me up at 3."

    dad "Alright, no problem. Let's make your favourite meal together."

    dad "{alpha=0.5}What did he like to eat again?"

    kid "Ok"

label junction:

    scene bg doorway with dissolve

    show kid neutral temp at halfsize, center with move

    menu:
        "Dog":
            jump dog

        "Prototype Microwave Game":
            jump kitchen

        "End Game":
            jump ending

label dog:

    show kid neutral temp at halfsize, left with move

    kid "ayo is that a f*ckin' DOG?"

    dad ".{cps=1}.."

    show screen example 
    play sound "audio/vine-boom.mp3"

    ""

    hide screen example

    jump junction

label kitchen:    

    scene bg kitchen with dissolve

    call screen foodselection

    call screen microwavegame

    scene bg diningtable
    show table at center 
    with dissolve
    
    # Like Food
    if foodchoice == 3:

        $ performance += 2
        
        show kid hopeful temp behind table at halfsize, diningposition with moveinleft

        kid "Well... {w}I'm happy that you remembered my favorite food."

        dad "Of course I'd remember!"

    # Tolerate Food
    elif foodchoice == 2 or foodchoice == 4:

        $ performance += 1

        show kid neutral temp at halfsize, diningposition with moveinleft

        kid "I wouldn't say food is my favourite..."

        dad "I thought you liked it the last time I made it..."

    # Dislike Food
    else:

        $ performance += 0

        show kid disappointed temp at halfsize, diningposition with moveinleft

        kid "Um... {w}maybe I didn't say it before but I don't really like food"

        dad "Really? {w}Why didn't you tell me?"

    kid "{alpha=0.5}*munch munch"

    dad "So... {w}How was it?"
    # Perfect Performance
    if abs(5.0 - microwave_time) <= 1.0:

        $ performance += 2

        $ culinary_expert = True

        show kid hopeful temp

        kid "It's good... {w}not over or undercooked like the last couple of times"

        dad "RESPONSE"
    # Good Performance
    elif abs(5.0 - microwave_time) <= 3.0:

        $ performance += 1

        show kid neutral temp

        kid "It's palatable, I'll get used to it"

        dad "RESPONSE"
    # Bad Performance
    else:

        $ performance += 0

        show kid disappointed temp

        kid "I'm not too hungry right now, can I get it in a container to bring home?"

        dad "RESPONSE"

    jump junction

screen example():
    add "its-cold-out-imma-wear-my-jamas-question-mark-dog-restored-v0-009m4oh1o0b91.webp": 
        align (0.5, 0.2)

default foodchoice = 0
screen foodselection():
    on "show" action [SetVariable("foodchoice", 0)]
    grid 2 2:
        xalign 0.5
        yalign 0.5
        spacing 10
        frame:
            background "#000a" 
            textbutton "Food Item 1" action [SetVariable("foodchoice", 1), Return()]
        frame:
            background "#000a" 
            textbutton "Food Item 2" action [SetVariable("foodchoice", 2), Return()]
        frame:
            background "#000a" 
            textbutton "Food Item 3" action [SetVariable("foodchoice", 3), Return()]
        frame:
            background "#000a" 
            textbutton "Food Item 4" action [SetVariable("foodchoice", 4), Return()]


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

    show kid at halfsize, center with move

    if culinary_expert:

        kid "yo this pizza pocket kinda hit ngl, ya did good Chef"

    else:

        kid "bro how'd you f*ck up the microwave game, the timer ain't even hidden LOL"

    kid "anyway game's over byeeeeeeeee"

    # This ends the game.
    return
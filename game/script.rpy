# The script of the game goes in this file.

# Declare characters used by this game. The color argument colorizes the
# name of the character.
define kid = Character("Kid", color="#00b3ff")
define dad = Character("Dad", color="#0037ff")

# Declare Backgrounds
image bg doorway = im.Scale("bg sprites/bg doorway.png", 1920, 1080)
image bg bedroom = im.Scale("bg sprites/bg bedroom.png", 1920, 1080)
image bg kitchen = im.Scale("bg sprites/bg kitchen.png", 1920, 1080)
image bg diningtable = im.Scale("bg sprites/bg diningtable.png", 1920, 1080)
image table = im.Scale("bg sprites/table.png", 1920, 1080)

init:
    $ performance = 0

transform halfsize:
    zoom 0.5

transform diningposition:
    xalign 0.5
    yalign 0.2

# The game starts here.
label start:

    # Show a background. This uses a placeholder by default, but you can
    # add a file (named either "bg room.png" or "bg room.jpg") to the
    # images directory to show it.
    scene bg bedroom

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

    "\"By the way, just dropped off K. {w=0.5}First time in a while he's spending his birthday with you, huh?\""

    dad "{alpha=0.5}It's his birthday?" with hpunch

    # play sound "door knocking sound effect"

    dad "{alpha=0.5}What time is it?"

    "{i}[[12:04 PM, {w=0.4}July 16th]"

    dad "{alpha=0.5}He's here? {w=0.5}But I have nothing prepared!"

    "{i}You run to the door and let your son in..."

    scene bg doorway with dissolve

    show kid neutral temp at halfsize, truecenter with dissolve

    dad "Hey Kiddo... {w=0.8}another year, {w=0.5}another..."

    window hide dissolve
    menu:
        "June 16th":
            $ performance += 0
        "July 16th":
            $ performance += 1
        "July 15th":
            $ performance += 0
            
    if performance == 1:

        kid "Yeah, {w=0.5}another year..."

    else:

        kid "Uh... {w=0.5}not quite..."

        dad "oh... {w=0.5}sorry Kiddo..."

    dad "How does some homemade lunch sound? {w=0.3}And of course, {w=0.1}I've got your present ready to go too!"
    
    dad "{alpha=0.5}Wait, I don't... {w=0.5}what am I going to do?"

    kid "Yeah, sounds cool. {w=0.5}I have homework due soon so I asked Mom to pick me up at 3."

    dad "Alright, no problem. Let's make your favourite meal together."

    dad "{alpha=0.5}What did he like to eat again?"

    kid "Ok"

label junction:

    scene bg doorway 
    show kid neutral temp at halfsize, truecenter 
    with dissolve

    menu:
        "Dog":
            jump dog

        "Prototype Microwave Game":
            jump kitchen

        "Gift Selection":
            jump bedroom

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

    call screen foodselection with dissolve

    call screen microwavegame with dissolve

    scene bg diningtable
    show table at center 
    with dissolve

    show kid neutral temp behind table at halfsize, diningposition with moveinleft
    
    # Like Food
    if foodchoice == "poptart":

        $ performance += 2
        
        show kid hopeful temp behind table at halfsize

        kid "Well... {w=0.5}I'm happy that you remembered my favorite food."

        dad "Of course I'd remember!"

    # Tolerate Food
    elif foodchoice == "cup" or foodchoice == "lasagna" or foodchoice == "mac":

        $ performance += 1

        show kid neutral temp at halfsize

        kid "I wouldn't say food is my favourite..."
        
        dad "I thought you liked it the last time I made it..."

    # Dislike Food
    else:

        $ performance += 0

        show kid disappointed temp at halfsize

        kid "Um... {w=0.5}maybe I didn't say it before but I don't really like food."

        dad "Really? {w=0.5}Why didn't you tell me?"

    kid "{alpha=0.5}*munch munch"

    dad "So... {w=0.5}How was it?"
    # Perfect Performance
    if abs(5.0 - microwave_time) <= 1.0:

        $ performance += 2

        $ culinary_expert = True

        show kid hopeful temp

        kid "It's good... {w=0.5}not over or undercooked like the last couple of times."

        dad "I think I’ve gotten the hang of it, {w=0.5}just took a lot of tries..."

    # Good Performance
    elif abs(5.0 - microwave_time) <= 3.0:

        $ performance += 1

        show kid neutral temp

        kid "It's palatable, {w=0.3}I'll get used to it."

        dad "At least it's not worse?"

    # Bad Performance
    else:

        $ performance += 0

        show kid disappointed temp

        kid "I'm not too hungry right now, {w=0.3}can I get it in a container to bring home?"

        dad "Oh {w=0.2}uh... {w=0.8}I don't think I have any. {w=0.5}I'll just leave it here for you the next time you visit."

    jump junction

label bedroom:

    scene bg bedroom with dissolve

    call screen giftselection

    dad "gift number [selectedgift] selected"

    jump junction

screen example():
    add "its-cold-out-imma-wear-my-jamas-question-mark-dog-restored-v0-009m4oh1o0b91.webp": 
        align (0.5, 0.2)

default selectedgift = 0
screen giftselection():
    on "show" action SetVariable("selectedgift", 0)
    grid 2 2:
        xalign 0.5
        yalign 0.5
        spacing 10
        frame:
            background "#000a" 
            textbutton "Gift Item 1" action [SetVariable("selectedgift", 1), Return()]
        frame:
            background "#000a" 
            textbutton "Gift Item 2" action [SetVariable("selectedgift", 2), Return()]
        frame:
            background "#000a" 
            textbutton "Gift Item 3" action [SetVariable("selectedgift", 3), Return()]
        frame:
            background "#000a" 
            textbutton "Gift Item 4" action [SetVariable("selectedgift", 4), Return()]

default foodchoice = "cup"
screen foodselection():
    on "show" action [SetVariable("foodchoice", "cup")]
    imagebutton:
        focus_mask True
        idle "food sprites/cup before.png" 
        align (0.2, 0.1)
        at Transform(zoom = 0.3)
        action [SetVariable("foodchoice", "cup"), Return()]
    imagebutton:
        focus_mask True
        idle "food sprites/lasagna before.png" 
        align (0.5, 0.1)
        at Transform(zoom = 0.3)
        action [SetVariable("foodchoice", "lasagna"), Return()]
    imagebutton:
        focus_mask True
        idle "food sprites/mac before.png"
        align (0.8, 0.1)
        at Transform(zoom = 0.3)
        action [SetVariable("foodchoice", "mac"), Return()]
    imagebutton:
        focus_mask True
        idle "food sprites/meat before.png"
        align (0.2, 0.8)
        at Transform(zoom = 0.3)
        action [SetVariable("foodchoice", "meat"), Return()]
    imagebutton:
        focus_mask True
        idle "food sprites/poptart before.png"
        align (0.5, 0.8)
        at Transform(zoom = 0.3)
        action [SetVariable("foodchoice", "poptart"), Return()]
    imagebutton:
        focus_mask True
        idle "food sprites/spicy before.png"
        align (0.8, 0.8)
        at Transform(zoom = 0.3)
        action [SetVariable("foodchoice", "spicy"), Return()]

default microwave_time = 0.0
default start_timer = False
default game_started = False
default game_ended = False
default culinary_expert = False
screen microwavegame():
    modal True
    on "show" action [SetVariable("microwave_time", 0.0), SetVariable("start_timer", False), SetVariable("game_started", False), SetVariable("culinary_expert", False), SetVariable("game_started", False)]
    add "michaelwave sprites/microwave main.png" align (0.5, 0.5)

    imagebutton:
        focus_mask True
        idle "michaelwave sprites/microwave button.png" 
        align (0.5, 0.5)
        action [ToggleVariable("start_timer"), SetVariable ("game_started", True), If(game_started is True, SetVariable("game_ended", True), None)]
    frame:
        background "#000a" 
        text "Stop the Timer as close to 5.0 Seconds as possible" 
        xalign 0.5 yalign 0.05
    frame:
        background "#000a" 
        text "[microwave_time:.1f]"
        xalign 0.75 yalign 0.3

    # Draw Food
    if not game_ended:
        add "food sprites/[foodchoice] before.png" align (0.375, 0.65) zoom 0.3
        # Microwave Door
        if not start_timer:
            add "michaelwave sprites/microwave opendoor.png" align (0.5, 0.5)
        else:
            add "michaelwave sprites/microwave closed lightson.png" align (0.5, 0.5)
    else:
        add "food sprites/[foodchoice] after.png" align (0.375, 0.65) zoom 0.3
        add "michaelwave sprites/microwave opendoor.png" align (0.5, 0.5)
        timer 2.0 action Return()

    if start_timer:
        timer 0.1 action [SetVariable("microwave_time", microwave_time + 0.1), SetVariable("game_started", True)] repeat start_timer


label ending:

    show kid neutral temp at halfsize, truecenter with move

    # Good Ending
    if performance >= 4:

        kid "Hey dad... {w=0.5}Can I talk to you about something?"

        dad "Yeah, {w=0.5}what's up?"

        kid "So... {w=0.8}I've been seeing someone... {w=0.8}and they're really important to me..."

        kid "It's been getting kinda serious {w=0.5}and we've been talking about meeting each other's parents."

        kid "but I've been hesitating on it..."

        kid "But also, {w=0.5}it does feel like I can open up to you more now."

        dad "Oh K... {w=1.0}you know I'm always here for you."

        dad "I messed up when you were growing up."

        dad "it took {w=0.3}a lot for me to learn to pivot my priorities away from myself when you were born."

    # Neutral Ending
    elif performance >= 2:
        
        "{i}your phone receives a notification"

        kid "Hey Dad, {w=0.8}Mom said she's here. {w=0.5}I better get going, {w=0.5} I wouldn't want to make her wait."

        dad "Already?"

        "{i}[[3:00PM]"

        dad "I guess so."

        kid "It was nice spending my birthday with you, {w=0.8}it reminded me of when I was little. {w=0.5}Thank for the [[GIFT] too."

    # Bad Ending
    else:
        pass

    # if culinary_expert:

    #     kid "yo this pizza pocket kinda hit ngl, ya did good Chef"

    # else:

    #     kid "bro how'd you f*ck up the microwave game, the timer ain't even hidden LOL"

    # kid "anyway game's over byeeeeeeeee"

    # This ends the game.
    return
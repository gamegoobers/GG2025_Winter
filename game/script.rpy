# The script of the game goes in this file.

# Declare characters used by this game. The color argument colorizes the
# name of the character.
define kid = Character("Kid", color="#00b3ff")
define dad = Character("Dad", color="#0037ff")

# Declare Backgrounds
image bg titlescreen = im.Scale("bg sprites/bg titlescreen.png", 1920, 1080)
image bg doorway = im.Scale("bg sprites/bg doorway open.png", 1920, 1080)
image bg doorway closed = im.Scale("bg sprites/bg doorway closed.png", 1920, 1080)
image bg bedroom = im.Scale("bg sprites/bg bedroom.png", 1920, 1080)
image bg kitchen = im.Scale("bg sprites/bg kitchen.png", 1920, 1080)
image bg diningtable = im.Scale("bg sprites/bg diningtable.png", 1920, 1080)
image table = im.Scale("bg sprites/table.png", 1920, 1080)
image bg goodending = im.Scale("goodending sprites/bg hug.png", 1920, 1080)

init:
    $ performance = 0

transform halfsize:
    zoom 0.5
transform diningposition:
    xalign 0.5
    yalign 0.2
transform zoomed_and_centered:
    zoom 0.3
    align (0.5, 0.5)
transform foodposition:
    zoom 0.3
    align (0.5, 0.5)

# The game starts here.
label start:

    scene bg bedroom with fade
    play sound "audio/PhoneNotifBuzz.ogg"
    pause(3)
    play sound "audio/PhoneNotifBuzz.ogg"
    pause(3)
    show phone at right, halfsize with easeinright 
    "\"By the way, just dropped off K. {w=0.5}First time in a while he's spending his birthday with you, huh?\""
    dad "{alpha=0.5}It's their birthday?" with hpunch
    dad "{alpha=0.5}What time is it?"
    "{i}[[12:04 PM, {w=0.4}July 16th]"
    play sound "audio/DoorKnock.ogg"
    hide phone with easeoutright 
    dad "{alpha=0.5}He's here? {w=0.5}But I have nothing prepared!"
    "{i}You run to the door and let your son in..."
    scene bg doorway with dissolve
    pause 1.0
    play music "music/dialogue-draft1.ogg"
    show kid neutral temp at halfsize, truecenter with dissolve
    dad "Hey Kiddo... {w=0.8}another year, {w=0.5}another..."

    window hide dissolve
    menu:
        "June 16th":
            $ performance += 0
            kid "Uh... {w=0.5}not quite..."
            dad "oh... {w=0.5}sorry Kiddo..."
        "July 16th":
            $ performance += 1
            kid "Yeah, {w=0.5}another year..."
        "July 15th":
            $ performance += 0
            kid "Uh... {w=0.5}not quite..."
            dad "oh... {w=0.5}sorry Kiddo..."

    dad "How does some homemade lunch sound? {w=0.3}And of course, {w=0.1}I've got your present ready to go too!" 
    dad "{alpha=0.5}Wait, I don't... {w=0.5}what am I going to do?"
    kid "Yeah, sounds cool. {w=0.5}I have homework due soon so I asked Mom to pick me up at 3."
    dad "Alright, no problem. Let's make your favourite meal together."
    dad "{alpha=0.5}What did he like to eat again?"
    kid "Okay"
    stop music fadeout 0.5
    pause (0.5)

    play music "music/COOKINGTIME.ogg"

label kitchen:    
    scene bg kitchen
    call screen foodselection with dissolve

    if selectedfood == "cup":
        show cup before at zoomed_and_centered with dissolve
        dad "A little salty {w=0.15}but who doesn't like cup noodles?"
    elif selectedfood == "spicy":
        show spicy before at zoomed_and_centered with dissolve
        dad "K should be able to handle spice."
    elif selectedfood == "mac":
        show mac before at zoomed_and_centered with dissolve
        dad "I remember making this for K all the time!"
    elif selectedfood == "meat":
        show meat before at zoomed_and_centered with dissolve
        dad "My mom brought this over when she came by."
    elif selectedfood == "lasagna":
        show lasagna before at zoomed_and_centered with dissolve
        dad "I'm pretty sure I made this using my ex-wife's recipe."
    elif selectedfood == "poptart":
        show poptart before at zoomed_and_centered with dissolve
        dad "K's got a sweet tooth but... {w=0.3}this isn't really a meal {w=0.2}is it?"

    dad "Should be ready after [microwave_time_target:.0f] seconds in the Microwave."
    menu:
        "Select Food":
            pass
        "Pick Another":
            jump kitchen

    scene bg kitchen with dissolve
    call screen microwavegame with moveinleft
    
    stop music fadeout 0.5
    scene bg diningtable
    show table at center 
    show expression "%s after" % selectedfood at truecenter, foodposition
    with dissolve

    show kid neutral temp behind table at halfsize, diningposition with moveinleft
    play music "music/dialogue-draft1.ogg"
    
    # Like Food
    if selectedfood == "poptart":
        $ performance += 2
        show kid hopeful temp behind table at halfsize
        kid "Well... {w=0.5}I'm happy that you remembered my favorite food."
        dad "Of course I'd remember!"
    # Tolerate Food
    elif selectedfood == "cup" or selectedfood == "mac" or selectedfood == "lasagna" :
        $ performance += 1
        show kid neutral temp behind table at halfsize
        kid "I wouldn't say this is my favourite..."
        dad "I thought you liked it the last time I made it..."
    # Dislike Food
    else:
        $ performance += 0
        show kid disappointed temp behind table at halfsize
        kid "Um... {w=0.5}maybe I didn't say it before but I don't really like this."
        dad "Really? {w=0.5}Why didn't you tell me?"

    kid "{alpha=0.5}*munch munch"
    dad "So... {w=0.5}How is it?"

    # Perfect Performance
    if abs(microwave_time_target - microwave_time) <= 0.75:
        $ performance += 2
        show kid hopeful temp behind table at halfsize
        kid "Wow... {w=0.5}it's good this time."
        dad "I think I've gotten the hang of it, {w=0.5}just took a lot of tries..."
    # Good Performance
    elif abs(microwave_time_target - microwave_time) <= 1.5:
        $ performance += 1
        show kid neutral temp behind table at halfsize
        kid "It's palatable, {w=0.3}I'll get used to it."
        dad "At least it's not worse?"
    # Bad Performance
    else:
        $ performance += 0
        show kid disappointed temp behind table at halfsize
        kid "I'm not too hungry right now, {w=0.3}can I get it in a container to bring home?"
        dad "Oh {w=0.2}uh... {w=0.8}I don't think I have any. {w=0.5}I'll just leave it here for you the next time you visit."

label conversation_start:
    dad ".{cps=2}....."
    menu:
        "So, how's school going?":
            jump conversation_school
        "What have you been up to recently?":
            jump conversation_recent

label conversation_school:
    kid "It's fine I guess"
    menu:
        "How are your grades?":
            jump conversation_grades
        "Have you thought about what direction you're going?":
            jump conversation_direction

label conversation_grades:
    kid "I don't know yet, {w=0.3}they're not out..."
    menu:
        "Well, how do you think you're doing?":
            $ performance += 1
            kid "Fine? {w=0.4}It's not like I'm failing..."
            dad "Well {w=0.2}what do your teachers think?"
            kid "They haven't given much feedback yet."
            dad "...Okay."
            dad "{alpha=0.5}Maybe I should just drop it..."

        "You can tell me if you're doing bad at school":
            $ performance += 0
            kid "I'm not, {w=0.3}I'm doing fine. {w=0.3}Why do you have to assume the worst?"
            dad "I'm trying to help here."
            kid "It feels like you're putting me on trial."
            dad ".{cps=1}.."
            dad "{alpha=0.5}Is it?"

    jump conversation_end

label conversation_direction:
    kid "I don't know... {w=0.3}I haven't decided."
    menu:
        "Have you considered going into law like me?":
            $ performance += 0
            kid "No... {w=0.3}I don't think I want to."
            dad "Why not?"
            kid "Seems stressful."
            kid "You're always working until late and complaining about still not being a partner after so many years."
            dad "But... {w=0.3}at least it pays well?"
            dad "{alpha=0.5}Did I really vent about work that much?"

        "Well, you've got time.":
            $ performance += 1
            kid "Yeah {w=0.2}I know."
            dad "But I don't want you going through life without knowing what you want to do."
            kid "That's true."
            dad "It's tough out there, success comes to people with motivation."
            dad "{alpha=0.5}Are they even listening?"
            kid ".{cps=1}.."

    jump conversation_end

label conversation_recent:
    kid "Nothing much..."
    kid "Actually, {w=0.5}I did compete recently."
    dad "Oh cool, {w=0.4}was it in..."
    menu:
        "Basketball?":
            $ performance += 0
            kid "No... {w=0.3}that's more your thing."
            dad "What? {w=0.4}I remember you loved it!"
            kid "You're remembering wrong. {w=0.3}You're the one who asked my teacher to put me on the team. {w=0.3}I never wanted to."
            dad "I only made a suggestion based on your gym class marks. {w=0.4}You can't just sit at home all day drawing scribbles."
            kid ".{cps=2}.. {/cps}{w=0.5}Scribbles?"
            dad "{alpha=0.5}Ah, {w=0.3}that probably was too harsh..."

        "Art?":
            $ performance += 2
            kid "Yeah, {w=0.3}it was."
            kid "There was a contest at school that my teacher recommended I enter."
            dad "So how did it go? {w=0.3}First place?"
            kid "Well I haven't won yet {w=0.3}but I did get to the finalists round. {w=0.3}Feeling pretty good about it."
            dad "Can I see what you made?"
            kid "Uh {w=0.2}yeah, {w=0.3}I'll send it to you when I get home."
            
        "Piano?":
            $ performance += 1
            kid "No... {w=0.3}I haven't played piano in a while..."
            dad "Really? {w=0.3}I remember you loved it!"
            kid "When I was younger... {w=0.2}maybe..."
            kid "I mainly went along with it since you and mom kept taking me to lessons."
            dad "Your piano teacher said you were really good, {w=0.3}like {w=0.3}competition level!"
            kid "That's not quite something I wanted to do..."
            dad "Oh.{cps=2}.."

    jump conversation_end

label conversation_end:
    pause 1.5
    dad ".{cps=1}.."
    kid ".{cps=1}.."
    dad "{alpha=0.5}I've run out of things to talk about, {w=0.3}maybe it's time to give them their gift."
    dad "{alpha=0.5}But I don't have anything! {w=0.3}I'll have to see what I can pass off as one."
    dad "Before you go, {w=0.3}I'll give you your birthday gift! {w=0.3}Just give me a second to grab it!"
    kid "Oh, {w=0.4}okay"

label giftpicking:

    scene bg bedroom
    call screen giftselection with dissolve

    if selectedgift == "book":
        show book after at zoomed_and_centered with dissolve
        dad "A casebook, {w=0.3}must have taken this one from work, but they won't notice it being missing."
    elif selectedgift == "cologne":
        show cologne after at zoomed_and_centered with dissolve
        dad "Mmm, {w=0.5}top notes of whiskey and charcoal..."
    elif selectedgift == "money":
        show money after at zoomed_and_centered with dissolve
        dad "A $20 bill. {w=0.5}Hey, {w=0.3}money is money."
    elif selectedgift == "notebook":
        show notebook after at zoomed_and_centered with dissolve
        dad "Just gotta rip out the pages I already wrote in and it's ready for K to use."
    elif selectedgift == "shirt":
        show shirt after at zoomed_and_centered with dissolve
        dad "A limited edition tour-only t-shirt of the hit musician, Rocker Bander!"
    elif selectedgift == "socks":
        show socks after at zoomed_and_centered with dissolve
        dad "No holes {w=0.3}and fresh from the laundry."
    elif selectedgift == "watch":
        show watch after at zoomed_and_centered with dissolve
        dad "Got this when I passed 15 years at the firm... {w=0.5}still not a partner though."

    menu:
        "Select Gift":
            pass
        "Choose Another":
            jump giftpicking

    scene bg doorway closed
    show kid neutral temp at halfsize, truecenter with dissolve

    dad "Sorry for the wait! {w=0.3}Here, {w=0.3}I got you this!"
    
    # Likes Gift
    if selectedgift == "notebook":
        $ performance += 2
        kid "Oh, {w=0.3}did mom tell you to get this? {w=0.3}I've been wanting a new notebook."
    # Tolerates Gift
    elif selectedgift == "shirt" or selectedgift == "money" or selectedgift == "watch":
        $ performance += 1
        kid "Oh uh... {w=0.5}thanks {w=0.2}I guess..."
    # Dislikes Gift
    else:
        $ performance += 0
        kid "Oh... {w=0.2}uh... {w=0.3}it's okay, I don't need a gift."
 
label ending:

    show kid neutral temp at halfsize, truecenter with move

    # Good Ending
    if performance >= 6:
        kid "Hey dad... {w=0.5}Can I talk to you about something?"
        dad "Yeah, {w=0.5}what's up?"
        kid "So... {w=0.8}I've been seeing someone... {w=0.8}and they're really important to me..."
        kid "It's been getting kinda serious {w=0.5}and we've been talking about meeting each other's parents."
        kid "but I've been hesitating on it..."
        kid "But also, {w=0.5}it does feel like I can open up to you more now."
        dad "Oh K... {w=1.0}you know I'm always here for you."
        dad "I messed up when you were growing up."
        dad "I was focusing too much on work to notice my family crumbling."
        dad "Leaving all the housework to your mom... {w=0.3}dismissing your hobbies..."
        dad "I'm sorry... {w=0.3}I haven't been present when I should have. {w=0.3}It took a long time to realize that."
        kid "I'm sorry too, {w=0.3}I could have been less guarded around you."
        kid "It was nice spending my birthday with you, {w=0.8}it reminded me of when I was little. {w=0.5}Thank for the gift too."
        kid "Oh {w=0.2}and I'll text you later about when and where we can have dinner with my partner."
        dad "Sounds great. {w=0.4}How about a hug for the road?"
        kid "Sure."
        scene bg hug with fade
        show hug at halfsize, truecenter with dissolve
        pause 2.0
        dad "{cps=*0.65}I love you, K."
        kid "{cps=*0.65}I love you too, {w=0.3}Dad."

    # Neutral Ending
    elif performance >= 3:
        play sound "audio/PhoneNotifBuzz.ogg"
        pause(3.0)
        kid "Hey Dad, {w=0.8}Mom said she's here. {w=0.5}I better get going, {w=0.5} I wouldn't want to make her wait."
        dad "Already?"
        show phone at right, halfsize with easeinright 
        "{i}[[3:00PM]"
        dad "I guess so."
        hide phone with easeoutright
        dad "How about a hug?"
        kid "I really have to go, {w=0.3}maybe next time."
        show bg doorway with dissolve
        hide kid with dissolve
        pause 3.0
        dad "{alpha=0.5}{i}sigh {/i}{w=0.5}I messed up their birthday again huh? {w=0.3}I don't know how to make that kid happy."
        dad "{alpha=0.5}I guess I could have made more of an effort to remember their birthday, {w=0.3}but it's so hard to read that kid."
        dad "I wonder what I could have done differently..."

    # Bad Ending
    else:
        pause 3.0
        kid "You know what... {w=0.3}I think I'm going to go now."
        dad "So soon? {w=0.3}You just got here"
        kid "Yeah... {w=0.3}I don't know what I expected coming here."
        kid "I thought maybe for my birthday you would have made more of an effort."
        dad "That's not true K. {w=0.3}I always put in effort for you."
        kid "And this was the best you could do? {w=0.3}It doesn't even feel like you remembered it's my birthday today."
        kid "It's clear you don't really care."
        dad "No, {w=0.15}I do! {w=0.3}I'll try better next time!"
        kid "{w=0.3}Forget next time! {w=0.3}I've already given you 20 chances at my birthday!" with hpunch
        dad "How am I supposed to know when you don't talk to me about anything?"
        kid "That's your job! {w=0.3}You're supposed to be comfortable to be around so that I can be myself when I'm with you." with hpunch
        kid "I see you regularly just cause you're my dad, {w=0.3}but it feels like we both don't want to be here."
        dad "{alpha=0.5}No... {w=0.3}this isn't how it's supposed to go..."
        dad "Hey, {w=0.3}I-{nw}"
        kid "I'll rip off the bandaid here and say that we don't have to force ourselves to see each other regularly."
        kid "Goodbye"
        hide kid with dissolve
        pause 4.0
        dad "{alpha=0.5}How did it go so wrong? {w=0.3}Is there any coming back from this?"
        dad "I wonder what I could have done differently..."

    return

screen example():
    add "its-cold-out-imma-wear-my-jamas-question-mark-dog-restored-v0-009m4oh1o0b91.webp": 
        align (0.5, 0.2)

label dog:
    show kid neutral temp at halfsize, left with move
    kid "ayo is that a f*ckin' DOG?"
    dad ".{cps=1}.."
    show screen example 
    play sound "audio/vine-boom.mp3"
    ""
    hide screen example
    jump start
init python:
    renpy.music.register_channel("music2", "music", True)
    renpy.music.register_channel("sound2", "sfx", False)
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
        idle "michaelwave sprites/microwave button idle.png" 
        hover "michaelwave sprites/microwave button hover.png"
        activate_sound "audio/MicrowaveBeep.ogg"
        sensitive not game_ended
        align (0.5, 0.5)
        action [ToggleVariable("start_timer"), SetVariable ("game_started", True), If(game_started is True, \
        [Play("sound", "audio/MicrowaveOpen.ogg"), Play("sound2", "audio/MicrowaveStopNoBeep.ogg"), SetVariable("game_ended", True)], \
        [Play("sound", "audio/MicrowaveClose.ogg"), Play("sound2", "audio/MicrowaveStartAndLoop.ogg")])]
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
        add "food sprites/[selectedfood] before.png" align (0.375, 0.65) zoom 0.3
        # Microwave Door
        if not start_timer:
            add "michaelwave sprites/microwave opendoor.png" align (0.5, 0.5)
        else:
            add "michaelwave sprites/microwave closed lightson.png" align (0.5, 0.5)
    else:
        add "food sprites/[selectedfood] after.png" align (0.375, 0.65) zoom 0.3
        add "michaelwave sprites/microwave opendoor.png" align (0.5, 0.5)
        timer 2.0 action Return()

    if start_timer:
        timer 0.1 action [SetVariable("microwave_time", microwave_time + 0.1), SetVariable("game_started", True)] repeat start_timer
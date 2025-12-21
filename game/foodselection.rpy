default selectedfood = "cup"
default microwave_time_target = 5.0
default fridgeopen = False
screen foodselection():
    on "show" action [SetVariable("selectedfood", "cup")]
    add im.Scale("foodselection sprites/bg kitchen minigame.png", 1920, 1080)
    # Cup Noodle Foods
    imagebutton:
        focus_mask True
        idle "food sprites/cup before.png"
        hover "food sprites/cup hover.png"
        align (0.0, 0.62)
        at Transform(zoom = 0.3)
        action [SetVariable("selectedfood", "cup"), SetVariable("microwave_time_target", 3.0), Return()]
    imagebutton:
        focus_mask True
        idle "food sprites/spicy before.png"
        hover "food sprites/spicy hover.png"
        align (0.2, 0.62)
        at Transform(zoom = 0.3)
        action [SetVariable("selectedfood", "spicy"), SetVariable("microwave_time_target", 3.0), Return()]
    # Fridge Door Sprites
    if not fridgeopen:
        imagebutton:
            focus_mask True
            idle im.Scale("foodselection sprites/fridgedoor closed idle.png", 1920, 1080)
            hover im.Scale("foodselection sprites/fridgedoor closed hover.png", 1920, 1080)
            align (0.5, 0.5)
            action [SetVariable("fridgeopen", True)]
    else:
        imagebutton:
            focus_mask True
            idle im.Scale("foodselection sprites/fridgedoor opened idle.png", 1920, 1080)
            hover im.Scale("foodselection sprites/fridgedoor opened hover.png", 1920, 1080)
            align (0.5, 0.5)
            action [SetVariable("fridgeopen", False)]
        # Refrigerated Food Sprites
        imagebutton:
            focus_mask True
            idle "food sprites/lasagna before.png"
            hover "food sprites/lasagna hover.png"
            align (0.68, 0.35)
            at Transform(zoom = 0.3)
            action [SetVariable("selectedfood", "lasagna"), SetVariable("microwave_time_target", 7.0), Return()]
        imagebutton:
            focus_mask True
            idle "food sprites/mac before.png"
            hover "food sprites/mac hover.png"
            align (0.95, 0.35)
            at Transform(zoom = 0.3)
            action [SetVariable("selectedfood", "mac"), SetVariable("microwave_time_target", 5.0), Return()]
        imagebutton:
            focus_mask True
            idle "food sprites/meat before.png"
            hover "food sprites/meat hover.png"
            align (0.65, 1.2)
            at Transform(zoom = 0.3)
            action [SetVariable("selectedfood", "meat"), SetVariable("microwave_time_target", 7.0), Return()]
        imagebutton:
            focus_mask True
            idle "food sprites/poptart before.png"
            hover "food sprites/poptart hover.png"
            align (0.95, 1.0)
            at Transform(zoom = 0.3)
            action [SetVariable("selectedfood", "poptart"), SetVariable("microwave_time_target", 4.0), Return()]
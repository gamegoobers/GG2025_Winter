transform move_to_center:
    linear 1.0 xalign 0.5 yalign 0.5
default selectedgift = "book"
screen giftselection():
    on "show" action SetVariable("selectedgift", "book")
    add im.Scale("bg sprites/bg bedroom.png", 1920, 1080)

    imagebutton:
        focus_mask True
        idle "gift sprites/book before.png"
        hover "gift sprites/book hover.png"
        align (0.65, 0.73)
        at Transform(zoom = 0.5)
        action [SetVariable("selectedgift", "book"), Return()]
    
    imagebutton:
        focus_mask True
        idle "gift sprites/cologne before.png"
        hover "gift sprites/cologne hover.png"
        align (0.39, 0.18)
        at Transform(zoom = 0.5)
        action [SetVariable("selectedgift", "cologne"), Return()]
    imagebutton:
        focus_mask True
        idle "gift sprites/money before.png"
        hover "gift sprites/money hover.png"
        align (0.05, 1.2)
        at Transform(zoom = 0.5)
        action [SetVariable("selectedgift", "money"), Return()]
    imagebutton:
        focus_mask True
        idle "gift sprites/notebook before.png"
        hover "gift sprites/notebook hover.png"
        align (1.0, 0.36)
        at Transform(zoom = 0.5)
        action [SetVariable("selectedgift", "notebook"), Return()]
    imagebutton:
        focus_mask True
        idle "gift sprites/shirt before.png"
        hover "gift sprites/shirt hover.png"
        align (0.45, 1.1)
        at Transform(zoom = 0.5)
        action [SetVariable("selectedgift", "shirt"), Return()]
    imagebutton:
        focus_mask True
        idle "gift sprites/socks before.png"
        hover "gift sprites/socks hover.png"
        align (0.88, 1.2)
        at Transform(zoom = 0.5)
        action [SetVariable("selectedgift", "socks"), Return()]
    imagebutton:
        focus_mask True
        idle "gift sprites/watch before.png"
        hover "gift sprites/watch hover.png"
        align (0.08, 0.35)
        at Transform(zoom = 0.5)
        action [SetVariable("selectedgift", "watch"), Return()]
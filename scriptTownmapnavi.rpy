#Contains Text and Code needed to transition to/from and use Town Map Navigation Screen

label townmapnavi:
    window hide

    show screen townmap
    hide screen townmap

    stop music fadeout 1.0

    show black
    with fade

    pause 1
    
    play music "audio/A Way of Life.mp3"

    $ renpy.transition(dissolve) 
    call screen townmap

label returntownmapnavi:
    window hide

    show screen townmap
    hide screen townmap

    $ renpy.transition(dissolve) 
    call screen townmap

label interactGekkoukanHS:
    scene bg townmap
    with dissolve

    window show

    p "Seeing as your school is in the middle of a little spacetime incident right now, you quickly reconsider this choice."

    jump returntownmapnavi

label visitIwatodaiStripMall:
    scene bg iwatodai strip mall
    with fade

    window show

    p "> You wander around Iwatodai Strip Mall for a bit."
    p "> It's a slow day today."
    p "> Probably because the students who like to hang out here are still trapped in the school... Awkward."

    if metFuukaAtShrine == False:
        p "> There's no sign of Fuuka here. Also the lack of people is kinda unsettling... You decide to get going."

    else:
        p "> The lack of people is pretty unsettling... You decide to get going."

    window hide

    show black
    with fade

    jump returntownmapnavi

label visitPortIslandStation:
    scene bg port island station
    with fade

    window show

    p "> You take a surprisingly empty train to Port Island Station."

    if metFuukaAtShrine == False:
        p "> It's a ghost town here. And worse yet, no sign of Fuuka."

    else:
        p "> The place is deserted except for a few weird adults..."

    p "> You decide to catch a train and go somewhere with better vibes."

    window hide

    show black
    with fade

    jump returntownmapnavi

label returntodormearly:
    scene bg townmap
    with dissolve

    window show

    p "> Return to dorm early?"

    menu:
        "Yes":
            jump transevening

        "No":
            jump returntownmapnavi
#Contains labels/scenes associated with ending the game

label endday:
    p "> It's getting late..."
    p "> You decide to head back to your dorm."

    jump EndingController

label EndingController:
    stop music fadeout 1.0
    window hide

    show black
    with fade

    pause 1

#Hang out With No One Ending

    if endingVar == "Fuuka":
        play music "audio/Burn My Dread.mp3"
        scene bg ending_fuuka
        with dissolve

        window show

        p "{b}{u}{i}Fuuka Ending{/i}{/u}{/b}"
        p "Fuuka's {color=#14b326}Bond{/color} with you: [fuukaRel.bond]"

        if fuukaRel.getBond() < 16:
            p "Fuuka enjoyed spending time with you!"
            p "Still, maybe you could've shown her an even better time if you word things a bit differently."

        else:
            p "Fuuka felt really comforted by your presence. She wasn't feeling well, but you helped her feel better. Great job!"


    elif endingVar == "Yukari":
        play music "audio/Burn My Dread.mp3"
        scene bg ending_yukari
        with dissolve

        window show

        p "{b}{u}{i}Yukari Ending{/i}{/u}{/b}"
        p "Yukari's {color=#14b326}Bond{/color} with you: [yukariRel.bond]"

        if yukariRel.getBond() < 20:
            p "Yukari definitely appreciated the time you spent together."
            p "Though perhaps if you worded things differently she would've had an even better time."

        else:
            p "Yukari absolutely savored your moments together! You're a great friend."


    elif endingVar == "Junpei":
        play music "audio/Burn My Dread.mp3"
        scene bg ending_junpei
        with dissolve

        window show

        p "{b}{u}{i}Junpei Ending{/i}{/u}{/b}"
        p "Junpei's {color=#14b326}Bond{/color} with you: [junpeiRel.bond]"

        if junpeiRel.getBond() < 17:
            p "Junpei enjoyed hanging out with you overall, but maybe if you chose your words differently he'd like you a bit more..."
            p "...Unless you don't care whether he likes you, which is also fair. He is a bit of a jerk sometimes."

        else:
            p "Besides, the food poisoning, Junpei really had a great and thought-provoking time with you today! Good job!"

    #elif endingVar == "Theodore":
        #play music "audio/P3 FES.mp3"
        #scene bg ending_theodore
        #with dissolve

        #window show

    else:
        play music "audio/A Way of Life -Deep inside my mind Remix-.mp3"

        scene bg ending_loner
        with dissolve

        window show

        p "{b}{u}{i}Loner Ending{/i}{/u}{/b}"
        p "We appreciate self love here, but maybe try spending time with someone else next time. Ya hear?"

    p "{b}- Final Stats -{/b}"
    p "{color=#2d7bb3}Charm{/color}: [meiko.charm]"
    p "{color=#2d7bb3}Confidence{/color}: [meiko.confidence]"
    p "{color=#2d7bb3}Intelligence{/color}: [meiko.intelligence]"
    p "{color=#2d7bb3}Money{/color}: [meiko.money] Yen"

    p "{u}{i}Thanks for playing!{/i}{/u}"

    $ persistent.finishedGame = True

    window hide

    stop music fadeout 1.0

    show black
    with fade

    pause 2
    
    $ renpy.quit()
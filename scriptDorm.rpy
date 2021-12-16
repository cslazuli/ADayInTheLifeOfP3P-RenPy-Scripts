#Contains scenes and transitions used when the player is in the dorm or transitioning to the dorm

label fuukaDormScene:
    scene bg dorm
    with fade

    window show

    p "> Back home..."
    p "> It looks like Yukari and Junpei went back to their rooms to rest."
    p "> The lobby is pretty empty with everyone else gone..."

    if metFuukaAtShrine == False:
        p "> You hear the front door open quietly."

        show fuuka neutral
        with dissolve

        fuuka "Oh... Hi, Meiko-chan."
        fuuka "How's your day been? Where is everyone else?"

        menu:

            "\"It's... Hard to explain.\"":
                fuuka "Oh... really?"

            "\"They're out of town.\"":
                fuuka "That's rather abrupt of them. Where did they go?"

        show black
        with fade

        p "> You fill Fuuka in on all of today's weird events."

        hide black
        with fade

        fuuka "Oh wow... I can't believe I missed everything."
        fuuka "Well... I suppose I can believe it, but it sure is strange timing."
        fuuka "I wasn't feeling well after lunch. My home room teacher let me leave school early to clear my head."

        fuuka "Speaking of, I'll be going to my room to rest now."
        fuuka "I'm sorry that we weren't able to meet today... Hopefully when things are fixed we can cook together again soon."
        
        menu:
            "\"Thank you.\"":
                pass

            "\"It's okay. You couldn't help it.\"":
                p "> You assure Fuuka that the entire school slipping into a space between reality and dreams was totally out of her control."

            "\"Feel better soon.\"":
                pass

        fuuka "I'll see you later, Meiko-chan."

        hide fuuka
        with dissolve

    jump dormQuery

label dormQuery:

    p "> You still have a bit more free time before your self-imposed midnight curfew."
    p "> What should you do now?"

    window hide 

    menu:

        "Go to bed early":
            window show
            p "> You've been through a lot today, and would rather not be through more."

            show black
            with fade

            p "> You head straight to bed, and your eyes feel heavy..."
            jump EndingController

        "Study until midnight":
            window show
            p "> Despite all of the supernatural drama, you're still a student and part of that role involves studying."

            show black
            with fade

            p "> You head to your desk and get to work..."
            p "> ..."
            p "> ... ..."
            p "> ... ... ..."

            $ meiko.greatlyIncrIntelligence()
            p "> ...And you finished your problem sets!"
            p "> Your {color=#2d7bb3}Intelligence{/color} has greatly increased!"
            jump EndingController

        "Head into town":
            jump townmapnavi

##Avoid transitioning directly to a scene to avoid glitches. Make/Use a transition label so you can set everything up/update the screen THEN go to the scene
label returntodormevening:
    stop music fadeout 1.0

    show black
    with fade

    scene bg dorm

    hide black
    with fade

    play music "audio/Iwatodai Dorm.mp3"

    window show
    jump dormQuery

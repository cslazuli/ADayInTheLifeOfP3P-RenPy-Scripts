label fuukaShrineScene:

    window hide

    stop music fadeout 1.0

    show black
    with fade

    pause 1

    play music "audio/Time.mp3"

    scene bg shrine
    with dissolve

    window show

    p "> Naganaki Shrine..."
    p "> As always, the shrine is at peace."

    if metFuukaAtShrine == False:

        $ metFuukaAtShrine = True

        show fuuka neutral
        with dissolve

        fuuka "Oh hello, Meiko-chan. I wasn't expecting to see you here."

        menu:
            "\"I'm so glad you're okay!\"":
                fuuka "Oh my, I appreciate your concern..."

            "\"Where have you been?\"":
                pass

        fuuka "I'm sorry that I wasn't at our cooking club like I said I would be. Were you really worried about me?"

        show black
        with fade

        p "> You fill Fuuka in on all of today's weird events."

        hide black
        with fade

        fuuka "Oh wow... I can't believe I missed everything."
        fuuka "Well... I suppose I can believe it, but it sure is strange timing."
        fuuka "I wasn't feeling well after lunch. My home room teacher let me leave school early to clear my head."

        fuuka "Well, I suppose we could still do something together."

    else:
        show fuuka neutral
        with dissolve

        fuuka "Hi, Meiko-chan."
        fuuka "I'm just enjoying the breeze right now."

        jump fuukaSpendTimeQuery

label fuukaSpendTimeQuery:

    p "> It seems like Fuuka is free today. Should you spend time with Fuuka?"

    menu:

        "Spend time with her":
            p "> Fuuka seems really excited to spend time with you!"
            jump fuukaSpendTime

        "\"No, thank you.\"":
            fuuka "That's alright. I'll probably rest here awhile longer then."
            fuuka "See you later, Meiko-chan."

            hide fuuka
            with dissolve
            
            jump townmapnavi

        "Give Gift":
            jump fuukaGiftMenu




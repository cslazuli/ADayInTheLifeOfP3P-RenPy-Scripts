#Contains text and control for Fuuka's after school events (that aren't specific to a room/navigation screen)

label fuukaSpendTime:
    window hide

    stop music fadeout 1.0

    show black
    with fade

    pause 1

    play music "audio/Joy.mp3"

    scene bg bebluev
    with fade

    window show

    p "> You and Fuuka decide to browse around the healing shop..."

    p "> Fuuka files through many lotions before swiftly grabing two of them."

    show fuuka neutral
    with dissolve

    fuuka "Hey, Meiko-chan, what kind of lotion do you think is best?"

    p "> Fuuka shows you the two bottles."
    p "> One has a rose and aloe vera scent, the other is passionfruit with notes of kiwi."

    menu: 

        "\"The flowery lotion for sure.\"":
            p "> Fuuka puts the flower lotion in her basket."

        "\"The fruity one, of course.\"":
            p "> Fuuka puts the fruit lotion in her basket."

    window hide
    
    hide fuuka
    with dissolve

    pause 1.5
    window show

    show fuuka neutral
    with dissolve

    fuuka "Hey, Meiko... I was curious what are your thoughts on being part of SEES?"

    hide fuuka
    with dissolve

    p "> (For the uninitiated, SEES stands for the \"{color=#2d7bb3}Specialized Extracurricular Execution Squad{/color}\")"
    p "> (Y'know, your typical school club.)"
    p "> (SEES is a secret club for Persona-users at Gekkoukan High School that fronts as a normal student-organization.)"


    show fuuka neutral
    with dissolve

    fuuka "Navigating you all through Tartarus using my Persona has been its own challenge..."
    fuuka "I can only imagine having to fight through the shadows of Tartarus myself..."

    menu:

        "\"You have it so easy.\"":
            fuuka "Yeah... You guys are put in direct danger and I just stay outside the door listening in..."
            fuuka "I wish I was a little more capable..."
            p "> Fuuka looks a little put down."

        "\"Could be worse.\"":
            fuuka "Yeah... that's fair. It's great that no one's been badly hurt, despite everything."

            $ fuukaRel.incrBond()
            p "> Fuuka looks a little relieved."

        "\"It's easier with your support.\"":
            fuuka "You really think so, Meiko-chan?"

            $ fuukaRel.incrBondBy(5)
            fuuka "> Fuuka holds her shoulders up high."
            
    fuuka "For me, I'm just glad to get this chance to help to everyone. Even a little."

    window hide
    
    hide fuuka
    with dissolve

    pause 1.5

    show fuuka neutral
    with dissolve

    window show

    p "> You follow Fuuka throughout the store for awhile longer."
    p "> Eventually, Fuuka approaches the self-checkout."

    menu:

        "Let her pay":
            fuuka "Did you want anything else? I can help pay."

            menu:
                "\"No thank you.\"":
                    pass

                "\"Nah.\"":
                    pass

        "\"Let me pay.\"":
            fuuka "Oh gosh... I could never make you do that..."
            fuuka "Thanks so much, though."

            $ fuukaRel.incrBondBy(5)
            p "> Fuuka smiles sweetly."

    window hide
    
    hide fuuka
    with dissolve

    pause 1.5

    window show

    p "> Fuuka pays for all the lotions and relaxation items you both accumulated on your trip." 

    window hide

    show black
    with fade

    window show

    p "> Fuuka and you leave the store together. The both of you split off. Then, you head home."

    $ endingVar = "Fuuka"

    jump transevening

label fuukaGiftMenu:

    $ totalGiftItems = jackfrostdoll.getAmount() + antiquekatana.getAmount()

    if totalGiftItems > 0:

        window hide

        menu:

            #Normal Responses
            "Antique Katana" if antiquekatana.getAmount() >= 1:
                $ antiquekatana.decrAmount(1)
                $ giftType = antiquekatana.getAttribute()
                jump fuukaGiftResponse    

            "Jack Frost Doll" if jackfrostdoll.getAmount() >= 1:
                $ jackfrostdoll.decrAmount(1)
                $ giftType = jackfrostdoll.getAttribute()
                jump fuukaGiftResponse

    else:
        p "> You don't have any gifts to give..."
        jump fuukaSpendTimeQuery


label fuukaGiftResponse:
    window show
    p "> You present your gift to Fuuka."

#Interesting Gift Response
    window show

    if giftType == "Interesting":

        fuuka "This looks really unique. Thank you, Meiko-chan."

        $ fuukaRel.incrBondBy(5)
        p "> Fuuka appreciated your gift!"

        jump fuukaSpendTimeQuery

#Anything but Interesting Response
    else:

        fuuka "Oh... I'm not really interested in this kind of thing."
        fuuka "Still, I appreciate the thought."

        p "> Fuuka didn't really like your gift..."

        jump fuukaSpendTimeQuery
#Contains scenes/transitions associated with the Velvet Room (Navigation) Screen

label velvetroomnavi:
    stop music fadeout 1.0

    window hide

    show black
    with fade

    pause 1

    play music "audio/Blues in Velvet Room.mp3"

    $ naviName = "The Velvet Room"

    $ renpy.transition(dissolve)
    call screen velvetroom

#Labels referenced only in screen velvetroom
    label talkJunpei:
        scene bg velvetroomblurred

        show junpei neutral 
        with dissolve

        window show
        junpei "This year just keeps getting weirder, huh..."
        junpei "Still... If we were saved just to hang out together, who am I to question fate?"

    label junpeiSpendTimeQuery:
        p "> It seems like Junpei is free today. Should you spend time with Junpei?"

        menu:

            "Spend time with him":
                p "> Junpei seems glad to have a chance to hang out with you!"
                jump junpeiSpendTime

            "\"No way.\"":
                junpei "Aw man... At this rate those two should've just let me fall into that \"luminous\" space... or whatever it's called."
                
                jump returnvelvetroomnavi

            "Give Gift":
                jump junpeiGiftMenu

    label talkYukari:
        scene bg velvetroomblurred

        show yukari neutral 
        with dissolve

        window show
        yukari "These Tartarus anomalies are becoming so overwhelming..."
        yukari "...But perhaps a day out is exactly what we need to take our minds off it. At least until that Theodore guy fixes the problem."

        jump yukariSpendTimeQuery

    label yukariSpendTimeQuery:
        p "> It seems like Yukari is free today. Should you spend time with Yukari?"

        menu:

            "Spend time with her":
                p "> Yukari seems pumped for the girl-talk vibes!"
                jump yukariSpendTime

            "\"No thanks.\"":
                yukari "Well, I suppose if you're busy I can try and find something to do by myself."

                show junpei neutral at right 
                with moveinright
                junpei "Hey wait! We could do something together!"

                yukari "As I was saying: I'll try and find something to do by myself."
                
                jump returnvelvetroomnavi

            "Give Gift":
                jump yukariGiftMenu

    label talkIgor:
        scene bg velvetroomblurred

        show igor neutral 
        with dissolve

        window show
        igor "What is it that you require, Meiko? Something which Theodore cannot attend to, I presume?"

        menu:

            "Fuse Personas":
                igor "Unfortunately, Theodore is hard at work fixing your school's shattered reality."
                igor "He'll be finished within the coming hours, no doubt. But as it stands he is unable to fuse your Persona."

                p "> You aren't able to fuse Personas right now..."

                igor "You should consider"

                jump returnvelvetroomnavi

            "\"How do I get cuter?\"":
                igor "..."
                igor "I have yet to hear a human ask me such a question."
                igor "..."
                igor "Consider taking advantage of the various services available to you around town."
                igor "It's possible that being at the right place at the right time may just increase your {color=#2d7bb3}Charm{/color}... And perhaps other attributes."
                igor "A {color=#2d7bb3}charming{/color} smile can take one to incredible places, as can a {color=#2d7bb3}couragous{/color} heart, and an unshakable {color=#2d7bb3}intellect{/color}."
                
                p "> (You can check your {color=#2d7bb3}attributes{/color}, {color=#14b326}bonds{/color}, and items within the Status Menu by pressing the \'M\' key.)"

                p "> Despite the sound advice, Igor still appears shaken through his usual perma-smile."
                jump returnvelvetroomnavi

            "\"Nothing.\"":
                jump returnvelvetroomnavi

    label talkTheodore:
        scene bg velvetroomblurred

        show theodore neutral
        with dissolve

        window show
        
        if dayNight == 0:
            theodore "Hello, Meiko! You can trust that I will have Gekkoukan High School in its proper state before morning tomorrow."
            theodore "Afterward, Tartatus should become accessable and I will be able to perform Persona fusion for you once more."

        if dayNight == 1:
            theodore "Good evening, Meiko! I'm sure you're curious how I came to discover it is now dusk."

            menu:
                "\"You looked outside?\"":
                    pass

                "\"You learned how to use a clock?\"":
                    pass

                "\"I'm completely and utterly lost as to how you managed this most profound of tasks.\"":
                    theodore "Oh... My apologies, Meiko..."
                    theodore "I did not consider the concept of human time-keeping methods would pose as difficult a quandary for you as it did for I..."

            theodore "I managed to learn how to use, what you humans call, a \"digital clock\" the other day all by myself."
            theodore "With this knowledge, I can also acertain that I am a few hours from emerging Gekkoukan High School from its liminal space."

        menu:

            "\"Good luck~!\"":
                theodore "Unfortunately, as I do not possess a Persona myself, I am unable to reap the benefits of such a statistic being \"good\"."
                p "> Theodore appears to sadly ponder the thought of him lacking a Persona..."

                if meiko.getCharm() > 0:
                    theodore "However, I too hope that all goes well so I may assist you at my full capabilities once more, Meiko."
                    p "> All at once you see his moon-pale face beam at the thought of supporting you."

                    $ theodoreRel.incrRel()
                    p "> You feel your {color=#14b326}Bond{/color} with Theodore has deepened in {color=#cc0066}many ways{/color}."
                    #p "> Still, you wonder if Theodore would let you spend time with him if you were a bit more {color=#2d7bb3}intelligent{/color} and {color=#2d7bb3}confident{/color} enough to ask."

                    jump returnvelvetroomnavi

                else:
                    p "> You feel as though if you had a bit more {color=#2d7bb3}Charm{/color}, your attempt at being sweet would've been better recieved..."
                    jump returnvelvetroomnavi

            "\"Alright.\"":
                jump returnvelvetroomnavi

            "Give Jack Frost Doll" if jackfrostdoll.getAmount() >= 1:
                $ jackfrostdoll.decrAmount(1)
                p "> You produce the {color=#8c7a07}Jack Frost Doll{/color} from its hiding place behind your back and present it to Theodore."
                theodore "What an interesting specimen. I have heard that some humans actually collect these."
                theodore "Why collect something of this sort though? What is its true value? Does it strengthen your statistical values?"
                
                menu:
                    "\"It's cute!\"":
                        theodore "Meiko, that is genius. Such a reason simply hadn't crossed my mind."
                        theodore "Do humans truly value \"cute\" things such that they can keep them close for their entire lives?"

                        p "> Theodore gives you a lingering glance with a warm smile, until he catches his expression and shyly looks away."

                    "\"It might fetch a high price as an antique some day.\"":
                        theodore "That's true. Humans do love to exchange currency for goods."
                        theodore "However, I'm unsure as to how an object inherently accumulates value as it ages... Could you perhaps elaborate?"
                        
                        p "> You feel bad giving Theodore a poorly worded explainer on appreciating and depreciating assets..."
                        p "> But then you remember economics is about as internally consistent as \nastrology anyway."
                        p "> However, considering you just discovered you're living in a world with real monsters and real magic this year... "
                        p "> ...Maybe you'll start to keep an eye out for the invisible hand of the free market when you're exploring Tartatus."

                    "\"It strengthens your \'statistical values\'.\"":
                        theodore "That settles the matter. Please tell me, what is the mechanism of this exchange?"
                        theodore "Do you confide in the doll so it may impart its wisdom upon you?"
                        theodore "...Or perhaps there is a ritual you must do to honor the doll so it may reward your piety?"
                        
                        p "> You tell Theodore that humans actually swallow the doll whole."

                        theodore "..."
                        theodore "Humans have such magnificent practices."

                $ theodoreRel.incrBondBy(5)
                p "> You feel your {color=#14b326}bond{/color} with Theodore has deepened."

                jump returnvelvetroomnavi

    label exitQueryVelvetRoom:
        scene bg velvetroomblurred
        show igor neutral 
        with dissolve

        window show
        igor "Leaving now, are we?"

        menu:

            "Yes":
                igor "Very well. See you soon no doubt."
                hide igor 
                with dissolve

                window hide

                pause 0.4

            #When showing an all white screen, use dissolve so it doesn't fade to black then turn white, it just goes straight to white
                show white
                with dissolve

                pause 0.5
                
                jump paulowinamallnavi

            "No":
                igor "Carefully consider who, if anyone, you will increase your bond with today, Meiko."
                
                jump returnvelvetroomnavi

    label returnvelvetroomnavi:
    #The "call screen" statement doesn't accept typical "with" statement for transitions
    #This is because screens are called inherently with a transition of "none"
    #So you need to use one of Renpy's python language commands to force a transition to happen with it

        window hide

        hide screen velvetroom
        show screen velvetroom
        hide screen velvetroom

        $ renpy.transition(dissolve)
        call screen velvetroom


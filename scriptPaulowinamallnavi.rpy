#Contains scenes/transitions associated with the Paulowina Mall (Navigation) Screen

label paulowinamallnavi:
    window hide

    stop music fadeout 1.0

    show black
    with fade

    pause 1

    play music "audio/A Way of Life.mp3"

    $ naviName = "Paulowina Mall"

    show screen paulowinamall
    hide screen paulowinamall

    $ renpy.transition(dissolve)
    call screen paulowinamall

##Labels Called only within screen paulowinamall
    #Day NPCs:
    label talkGirls:
        scene bg chagall cafe exterior
        show npc_bluehair at left
        show npc_greengirl at right
        with dissolve

        window show
        npc_bluehair "I'm starving..."
        npc_bluehair "Should we grab a bite to eat?"

        npc_greengirl "Sure! Let's get takoyaki at that Octopia restaurant."

        npc_bluehair "But that's all the way at Iwatodai Strip Mall... I guess we'll have to take the monorail."

        jump returnpaulowinamallnavi

    label talkOldDude:
        scene bg antiqueshop exterior
        show npc_olddude
        with dissolve

        window show
        npc_olddude "Times change, but things, like school ghost stories, never die."
        npc_olddude "...Unlike the students who became said ghosts, of course."
        npc_olddude "I used to sneak into the school grounds at night... The teachers would give me \nhell for that!"
        npc_olddude "But I'm just an old practitioner. What would I know about young dumb fun?"
        npc_olddude "I'm supposed to be working at the Shrine all day. Right, kid?"

        jump returnpaulowinamallnavi

    #Entrances/Other Interactables:
    
    label clubEscapadeQuery:
        scene bg club escapade exterior

        window show

        if dayNight == 0:
            p "> Club Escapade..."
            p "> ...And it's not open yet."
            p "> It's a \"night\" club, not a \"day\" club."
            jump returnpaulowinamallnavi

        elif dayNight == 1:
            p "> Club Escapade..."
            p "> You nearly walk right in, but you stop in your tracks."
            p "> Not only are you literally a teenager, but the idea of clubbing itself weirds you out."
            p "> Why would you want to be trapped in a room full of inebriated lowkey-musty strangers?"
            p "> In a self-care win, you walk off."
            jump returnpaulowinamallnavi

    label chagallCafeQuery:
        scene bg chagall cafe exterior

        window show

        p "> Chagall Cafe..."

        if dayNight == 0:
            p "> It's too crowded right now."
            jump returnpaulowinamallnavi

        elif dayNight == 1:
            m "\"Pheremone Coffee - 500 yen\""
            m "\"A charming flavor that will turn up even the most generic \[high schooler solving supernatural mysteries\]'s {color=#2d7bb3}charm{/color}!\""
            
            p "> You somehow feel targetted by that."
            p "> It seems you can work part-time here today for some extra money."

            menu:
                "Go in as a customer":
                    if meiko.getMoney() >= 500:
                        $ meiko.decrMoney(500)

                        window hide

                        scene bg chagall cafe
                        with fade

                        window show

                        p "> The Pheremone Coffee is really good! You can just feel yourself getting cuter with every sip!"
                        $ meiko.greatlyIncrCharm()
                        p "> Your {color=#2d7bb3}Charm{/color} has increased greatly!"
                        jump endday

                    else:
                        p "> You don't have enough money for coffee... Yikes..."
                        jump returnpaulowinamallnavi

                "Work part-time":
                        window hide

                        scene bg chagall cafe
                        with fade

                        window show

                        p "> You sweat it out working as a waitress..."

                        $ meiko.incrConfidence()
                        p "> You settled an argument between two customers and became more {color=#2d7bb3}confident{/color}."

                        $ meiko.incrMoney(1000)
                        p "> You earned 1000 yen working part time!"
                        
                        if dayNight == 0:
                            jump transevening

                        elif dayNight == 1:
                            jump endday

                "Never mind":
                    jump returnpaulowinamallnavi


    label beBlueVQuery:
        scene bg bebluev exterior

        window show

        p "> Healing Shop, Be Blue V..."
        
        if dayNight == 0:
            m "\"Our special 800 yen program will send you to heaven!\""
            p "> You read the fine print on the bottom corner..."
            m "\"DISCLAIMER: Due to legal reasons, this spa treatment will NOT actually kill you.\""
            p "> It seems you can work part-time here today for some extra money."

            p "> Will you spend time here here after school?"

        elif dayNight == 1:
            p "> It seems they've closed for tonight."
            jump returnpaulowinamallnavi

        menu:
            "Go in as a customer":
                if meiko.getMoney() >= 800:
                    $ meiko.decrMoney(800)

                    window hide

                    scene bg bebluev
                    with fade

                    window show

                    p "> You begin the \"heavenly\" spa treatment."
                    p "> ..."
                    p "> ... ..."
                    p "> ... ... ...?"

                    show white
                    with dissolve
                    
                    pause 1

                    hide white
                    with dissolve

                    p "> Just before your soul leaves your mortal body, a panicked employee notices your body go cold and wakes you up."
                    p "> When you come to, you notice your skin is silky smooth!"
                    p "> You're super-exfoliated, you met God, and you feel infinitely cuter!"
                    
                    $ meiko.greatlyIncrCharm()
                    p "> Your {color=#2d7bb3}Charm{/color} has greatly increased!"
                    
                    if dayNight == 0:
                        jump transevening

                    elif dayNight == 1:
                        jump endday

                else:
                    p "> You don't have enough money for a spa day..."
                    jump returnpaulowinamallnavi

            "Work part-time":
                    window hide

                    scene bg bebluev
                    with fade

                    window show

                    p "> You sweat it out working as a cashier at the healing shop. There shall be no relaxation for you in this spa."

                    $ meiko.incrCharm()
                    p "> During your shift, you got to try some of the essential oils sold at the shop."
                    p "> Your devious lick didn't cure you of any illnesses, but you feel you became more {color=#2d7bb3}charming{/color}."

                    window hide
                    pause 1
                    window show

                    $ meiko.incrIntelligence()
                    p "> During your down time, you did some reading on the various healing items sold here to improve your sales pitch."
                    p "> Most of it seemed pretty bogus, but you certainly feel more {color=#2d7bb3}intelligent{/color} even if you actually lost some brain cells."

                    $ meiko.incrMoney(500)
                    p "> You earned 500 yen working part time!"
                    
                    if dayNight == 0:
                        jump transevening

                    elif dayNight == 1:
                        jump endday

            "Never mind":
                jump returnpaulowinamallnavi

    label enterPoliceStation:
        stop music fadeout 1.0

        show black
        with fade

        pause 1

        play music "audio/Paulownian Mall.mp3"

        scene bg shop police station interior

        show vendor_policestation neutral
        with dissolve

        window show

        kurosawa "I don't have that much, but you should be able to find what you need."

        window hide

        $ renpy.transition(dissolve)
        call screen policeshopmenu

    label mandragoraQuery:
        scene bg mandragora

        window show

        p "> Mandragora Karaoke..."
        m "\"Don't be shy! Belt your heart out like \nno one's there!\""
        m "\"Karaoke Solo - 500 Yen\""
        
        if dayNight == 0:
            p "> Will you stay here until dark?"

        elif dayNight == 1:
            p "> Will you stay here until midnight?"

        menu:
            "Yes":
                if meiko.getMoney() >= 500:
                    $ meiko.decrMoney(500)

                    show black
                    with fade
                    
                    p "> You belt your heart out. Everyone's eyes are trained on you..."
                    p "> ...And yet you keep going."
                    p "> You finish your song, fully out of breath, and..."
                    p "> ...Suddenly, the crowd is in an uproar. They're clapping just for you!"
                    
                    $ meiko.greatlyIncrConfidence()
                    p "> Your {color=#2d7bb3}Confidence{/color} has greatly increased!"

                    if dayNight == 0:
                        jump transevening

                    elif dayNight == 1:
                        jump endday

                else:
                    p "> You don't have enough money to try karaoke... That's rough buddy..."
                    jump returnpaulowinamallnavi

            "No":
                jump returnpaulowinamallnavi

    
    label enterAntiqueShop:
        stop music fadeout 1.0

        show black
        with fade

        pause 1

        play music "audio/Paulownian Mall.mp3"

        scene bg shop antiqueshop interior

        show vendor_antiqueshop neutral
        with dissolve

        window show

        antiquelady "Welcome."

        window hide

        $ renpy.transition(dissolve)
        call screen antiqueshopmenu

    label enterPharmacy:
        stop music fadeout 1.0

        show black
        with fade

        pause 1

        play music "audio/Paulownian Mall.mp3"

        scene bg shop pharmacy interior

        show vendor_pharmacy neutral
        with dissolve

        window show

        pharmacist "Welcome!"

        window hide

        $ renpy.transition(dissolve)
        call screen pharmacyshopmenu

    label powerRecordsInteract:
        scene bg power records

        window show

        p "> Power Records..."
        p "> It's a store that sells many kinds of records. Not all kinds. Just the powerful ones."
        p "> Their movies, however, are pretty weak. That's probably why they left them out \nof the name."
        p "> You recall you've actually never set foot inside the store."
        p "> You do not intend to change that today. Not after the thorough roasting you gave it."

        jump returnpaulowinamallnavi

    label gamePanicQuery:
        scene bg game panic

        window show

        p "> Game Panic..."
        p "> A wide assortment of arcade games are held captive inside."
        
        if dayNight == 0:
            p "> Will you stay here until dark?"

        elif dayNight == 1:
            p "> Will you stay here \'til midnight?"

        menu:
            "Yes":
                p "> Two games catch your eye today. Which one will you play?"

                menu:
                    "Ghostly Photography Club (800 yen)":
                        if meiko.getMoney() >= 800:
                            $ meiko.decrMoney(800)

                            show black
                            with fade

                            p "> You enter the creepy photo booth..."
                            p "> The ghosts are scary, but your will to take a good picture is scarier."
                            p "> You grip the camera and start snapping pics..."
                            p "> ...And they end up being so good, even the evil spirits are impressed."
                            p "> You leave with some cute selfies with ghosts, and some extra courage!"

                            $ meiko.greatlyIncrConfidence()
                            p "> Your {color=#2d7bb3}Confidence{/color} has greatly increased!"

                        else:
                            p "According to the arcade owner, the ghosts are extra mean to poor people..."
                            p "You don't have enough money to play so, for your own safety, you decide to leave."
                            
                            jump returnpaulowinamallnavi

                    "Quiz Game (800 yen)":
                        if meiko.getMoney() >= 800:
                            $ meiko.decrMoney(800)
                            
                            show black
                            with fade

                            p "> ..."
                            p "> ... ..."
                            p "> ... ... ..."
                            p "> You tested your knowledge of Japanese history against players across the country..."
                            p "> ...And you won the match! Was this an adequate manifestation of girl power?"

                            $ meiko.greatlyIncrIntelligence()
                            p "> Your {color=#2d7bb3}Intelligence{/color} has greatly increased!"

                        else:
                            p "You're smart but you don't have enough money to show it. Truly the problem of our times."
                            p "Just before you start considering taking out a loan, you decide today may not be a good day to play this."

                            jump returnpaulowinamallnavi

                    "Neither":
                        jump returnpaulowinamallnavi


                if dayNight == 0:
                    jump transevening

                elif dayNight == 1:
                    jump endday

            "No":
                jump returnpaulowinamallnavi


    label craneGameQuery:
        scene bg game panic

        window show

        p "> It's a crane game. A machine designed to steal money from foolhardy users."
        p "> But like, you're built different. Maybe you can win a gift for someone."
        p "> Will you give it a try? It costs 200 yen to play. You have {color=#2d7bb3}[meiko.money]{/color} yen."

        menu:

            "Yes":
                jump playCraneGame

            "No":
                jump returnpaulowinamallnavi

    label velvetalleywaynavi:
    stop music fadeout 1.0

    show black
    with fade

    pause 1

    $ naviName = "Back Alley"

    $ renpy.transition(dissolve)
    call screen velvetalleyway

    label returnpaulowinamallnavi:
        window hide
        
        show screen paulowinamall
        hide screen paulowinamall

        $ renpy.transition(dissolve)
        call screen paulowinamall

    label playCraneGame:
        if meiko.getMoney() >= 200:
            $ meiko.decrMoney(200)
            p "> You give the crane your magic touch..."

        #Generates a random number between 0 and 1, You have a 1/2 chance of winning the crane game
            $ craneGameSuccess = renpy.random.randint(0, 1)

            if craneGameSuccess == 1:
                $ jackfrostdoll.incrAmount(1)
                p "> ...And you won!"
                p "> You got a {color=#8c7a07}Jack Frost Doll{/color}. Maybe someone would like to have one of these..."
                jump returnpaulowinamallnavi
                
            else:
                p "> ...And you lost."
                jump returnpaulowinamallnavi

        else:
            p "> You're too poor to play right now..."
            jump returnpaulowinamallnavi

label transevening:

    window hide

    stop music fadeout 1.0

    show black
    with fade

    show timechng evening
    with moveinright

    $ dayNight = 1

    pause 1

    hide timechng afternoon
    with Dissolve(1)

    play music "audio/Iwatodai Dorm.mp3"

    jump fuukaDormScene

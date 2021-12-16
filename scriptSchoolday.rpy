#Contains script for school cutscenes

label schoolentrancescene: 

    play music "audio/Time.mp3"
    
    # Show a background. This uses a placeholder by default, but you can
    # add a file (named either "bg room.png" or "bg room.jpg") to the
    # images folder to show it.
    
    scene bg schoolentrance

    # This shows a character sprite. A placeholder is used by default
    # but by adding images to the images folder with a name and tag you can call them.

    show yukari neutral
    with dissolve

    # These display lines of dialogue.

    yukari "Hey, Meiko... I was thinking."

    yukari "The night before last... The 12 Shadows... Tartarus..."

    yukari "Isn't there just too much we don't understand?"

    menu:


        "\"You think so?\"":
            pass

        "\"Yeah, definitely.\"":
            pass

    yukari "It's starting to get to me..."

    ###########################
    ######################DEBUG MODE Check
    if debug == True:
        yukari "By the way... do you feel lightheaded too?"

        menu:
            "\"Nope\"":
                yukari "Oh well... I guess it's just in my head... Nevermind..."
                jump translunchtime

            "\"Yeah actually...\"":
                yukari "Yeah... I think... We should... sit down..."
                p "> Yukari blacks out without warning, and you soon follow suit..."
                
                window hide
                
                $ jackfrostdoll.setAmount(3)

                jump paulowinamallnavi
                #jump velvetroomnavi
                #jump afterschoolweird
    ##########################
    ##########################

    else:
        jump translunchtime

#lunchtime event w/ Fuuka

label translunchtime:

#Typical Transition that involves a music change
    window hide

    show black
    with fade

    #show timechng morning
    #with dissolve

    show timechng lunchtime
    with moveinright

    stop music fadeout 1.0

    pause 1

    play music "audio/Afternoon Break.mp3"

    scene bg lunch room

    # hide timechng morning

    hide timechng lunchtime
    with Dissolve(1)

    # It's very important to place window show after a window hide state as the last part of the transition (immediately before new text shows up).
    # Otherwise it'll mess the other parts/timing up (for example, the dialogue window will just pop in instead of dissolving in)
    window show

    jump fuukalunchtime

label fuukalunchtime:

    p "> It's finally time for lunch..."

    show fuuka neutral
    with dissolve

    fuuka "Oh, Meiko-chan. It's a coincidence meeting you here."

    fuuka "Oh yeah, are you free today after school?"

    menu:

        "\"I'm free.\"":
            fuuka "I see. If it's okay with you, could you come to the cooking club?"
            
        "\"I don't know yet.\"":
            fuuka "I see. Then, can you come to the cooking club if you're not busy?"

    fuuka "Oh... It's not mandatory though, just so you know."
    fuuka "If you're going to come, talk to me, or you can just come to the Home Economics room."

    p "> It seems Fuuka doesn't have much to do after school..."
    p "> Maybe you should spend some time with her..."

    hide fuuka
    with dissolve

    jump lunchtimeend

label lunchtimeend:
    p "> Lunchtime is ending. You decide to return to your classroom."

    jump transafternoon

label transafternoon:

    window hide

    show black
    with fade

    show timechng afternoon
    with moveinright

    stop music fadeout 1.0

    pause 1

    play music "audio/Time.mp3"

    scene bg class_room

    hide timechng afternoon
    with Dissolve(1)

    window show

    jump afternoonclass

label afternoonclass:
    
    show terauchi neutral
    with dissolve

    terauchi "Doesn't the octopus in this picture look creepy?"

    terauchi "Many European countries don't serve octopus, as they're feared as \"devilfish\"."

    terauchi "My darling, for example, won't touch octopus. I remember the last time I made pasta for him he..."

    p "> Mrs. Terauchi continued to talk about octopi as a food item..."

    terauchi "But octopi aren't the only undersea creatures called \"devilfish\"."

    terauchi "Now, here's a question for... Junpei."

    terauchi "Of manta rays, squid, and jellyfish..."

    terauchi "Which of these is NOT known as a \"devilfish\""

    show terauchi neutral at right
    with move

    show junpei neutral at left
    with dissolve

    junpei "I didn't even know octopi were called devilfish! How am I supposed to know?!"
    junpei "Hey Meiko, what do I say?"

    menu:
        
        "\"Manta rays.\"":
            jump goodtryjunpei

        "\"Squid\"":
            jump goodtryjunpei

        "\"Jellyfish\"":
            jump goodgoingjunpei

    label goodtryjunpei:
        terauchi "Awwwww... good try, Junpei!"
        terauchi "The answer I was looking for is \"jellyfish\"."
        terauchi "Jellyfish aren't \"devil\" fish because they're \"jelly\" fish. \"Jelly\"... get it?"
        terauchi "It was... Well, it was just a joke."
        junpei "Who cares... I'll just stay in Japan for the rest of my life."

        p "> The answer you gave was wrong..."

        jump transafterschool


    label goodgoingjunpei:
        terauchi "Good going, Junpei!"
        terauchi "Jellyfish aren't devilfish because they're a \"jelly\" fish. \"Jelly\"... get it?"
        terauchi "It was just a joke!"
        junpei "Hahah! Just plain common sense, Mrs. T!"

        hide terauchi
        with dissolve

        show junpei neutral at center
        with move

        junpei "Thanks, Meiko! I almost looked like an idiot..."

        hide junpei
        with dissolve

        p "> You hear your classmates whispering..."

        classmate "Meiko helped him out. She's really dependable!"

        p "> You became slightly more popular."

        $ meiko.incrCharm()
        p "> Your {color=#2d7bb3}Charm{/color} has increased."

        jump transafterschool

label transafterschool:

#Typical Transition without a music change

    window hide

    show black
    with fade

    show timechng afterschool
    with moveinright

    pause 1

    scene bg class_room

    hide timechng afterschool
    with Dissolve(1)

    window show

    jump afterschoolweird

label afterschoolweird:
    p "> After the final class bell rings, you, Junpei, and Yukari stay and chat after class..."
    p "> You decide to walk back to your dorm and talk, but as you make your way to the exit door..."
    p "> You feel a sense of lightheadedness overtake you..."

    window hide

    stop music fadeout 1.0

    show black
    with fade

    pause 1

    scene bg velvetroomblurred
    with Dissolve(1)

    window show

    play music "audio/Velvet Room.mp3"

    show igor neutral
    with dissolve
    igor "Meiko, I see you have finally arrived."

    show junpei neutral at left
    with moveinleft
    junpei "What the--?! Who's the freak with the long nose? Where is this place?"

    hide junpei
    with moveoutleft

    show yukari neutral at left
    with moveinleft
    yukari "And why is it so... Well decorated?"

#It's a good idea to break up long sections of dialogue with player input, like letting them answer a question/make a comment on the scene
#It doesn't have to change the story in a big way, but it adds some extra interactivity/engagement and roleplaying elements.

    menu:

        "\"It's something like a dream.\"":
            yukari "Uh, what is that supposed to mean?"

        "\"I dunno.\"":
            pass

        "\"Hell.\"":
            yukari "Excuse me?!"

    show theodore neutral at right
    with easeinright
    theodore "This is the Velvet Room."
    theodore "It is a space which exists between reality and dreams."

    igor "My name is Igor, and this here is Theodore. He serves as this room's dedicated attendant."

    theodore "I am pleased to meet you all."

    hide theodore
    with easeoutright
    
    hide yukari
    with moveoutleft

    show junpei neutral at left 
    with moveinleft
    junpei "So that answers one question. Now do you mind explaining how exactly we ended up here?"

    igor "Normally the Velvet Room serves as a space to strengthen Persona and by extension, their users."
    igor "However, a more drastic matter has necessitated we act with a heavier hand."
    
    show theodore neutral at right 
    with easeinright

    theodore "It appears the reality within your school has grown thin."
    theodore "Its halls have fallen into a liminal space between the Dark Hour and reality. Not unlike this very room."

#Also visual things like dramatic cutins provide another way of breaking up a scene and making it more interesting
#Dramatic Cutin
    show cutin_yukari at center with easeinleft:
        yalign 0.5

    pause 0.5

    hide cutin_yukari
    with easeoutright

    hide junpei 
    with moveoutleft

    show yukari neutral at left
    with moveinleft

    p "Yukari's lips purse. Something seems to be troubling her."

    hide yukari 
    with moveoutleft
    show junpei neutral at left 
    with moveinleft

    theodore "Igor has tasked me with discovering a means to free your school from this space." 
    theodore "In the meantime, Igor thought it important to rescue Meiko and her dormmate confidantes."

    junpei "Uh, and why is that?"

    hide theodore 
    with easeoutright

    igor "Why, so you do not miss the opportunity to strengthen your bonds of course."

    p "> Igor gives you a side glance with a wide grin. Wider than his resting grin at least."

    igor "The bond between friends makes your team stronger than you could ever know."
    igor "These bonds are the only way you can hope to reach the top of Tartarus some day."

    junpei "(Pssh. Can you not say something so cliché?)"

    hide junpei 
    with moveoutleft
    show yukari neutral at left 
    with moveinleft
    yukari "But... This isn't everyone from the dorm... Where's Akihiko? Mitsuru? Where is Fuuka?!"

    show theodore neutral at right 
    with easeinright

    theodore "Unfortunately, your upperclassman friends are trapped for now. We were incapable of rescuing them as well."
  
#Double Dramatic Cutin
#By loading in the images offscreen, you can have them both ease onto the screen at the same time
    show cutin_yukari at offscreenleft:
        yalign 0.80
    show cutin_junpei at offscreenright:
        yalign 0.20
    with None

    show cutin_yukari at center:
        yalign 0.80
    show cutin_junpei at center:
        yalign 0.20
    with ease

    pause 0.5

    hide cutin_yukari
    with easeoutright

    hide cutin_junpei
    with easeoutleft

    p "> Yukari and Junpei tense up."

    theodore "Being Persona users, they should be able to keep pace with any threats they encounter."
    theodore "However, I did not sense Fuuka's presence within the school when I went to rescue you."
    theodore "Perhaps she left school early today. I believe you may {color=#2d7bb3}see her around town{/color} if you're seeking her."

    igor "Please stay long as you would like. Know that the exit behind you will take you directly to Paulowina Mall."

    theodore "I will be sure to fix your school's troubled relationship with reality by the end of today."
    theodore "Be advised that Tartarus will not be accessible tonight, however."

    jump velvetroomnavi

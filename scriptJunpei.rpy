#Contains text and control for Junpei's after school events (that aren't specific to a room/navigation screen)

label junpeiSpendTime:
    window hide

    stop music fadeout 1.0

    show black
    with fade

    pause 1

    play music "audio/After School.mp3"

    scene bg octopia
    with fade

    window show

    p "> You and Junpei order takeout at Octopia: Japan's Favorite (and sketchiest) Octopus Fast Food Restaurant..."
    p "> You wait patiently outside for your order to finish..."

    show junpei neutral
    with dissolve

    junpei "You know, Meiko, I've been doing some serious thinking... About us... And..."
    junpei "...Is octopus cooked this fast really safe to eat?"

    menu:

        "\"We could eat somewhere else if you'd like.\"":
            junpei "No it's alright... I was just wondering what you thought."
            junpei "...Thanks your the concern though."
            
            $ junpeiRel.incrBondBy(5)
            p "> Junpei grins a little bit."

        "\"If it was really worth being afraid of, this place would be closed down.\"":
            junpei "I guess so..."
            $ junpeiRel.incrBond()
            p "> Junpei sits a little more comfortably."

        "\"You always seemed like the kind of guy to be scared of octopi.\"":
            junpei "Hey! What is that supposed to mean?!"
            junpei "All they have is a bunch of creepy legs. I am NOT afraid of them!"

    window hide
    
    hide junpei 
    with dissolve

    pause 1.5
    window show

    show junpei neutral
    with dissolve

    p "> Junpei is looking distant."

    junpei "Is it just me, or has Yuka-tan been acting weird lately?"

    menu:
        "\"Huh?\"":
            junpei "Dude, where have you been? We all live in the same building."

        "\"You think so too?\"":
            junpei "Oh, you noticed it too?"
            $ junpeiRel.incrBond()

    junpei "Yukari's been totally overthinking all of that Tartarus stuff."
    junpei "It's just a creepy magic mystery world full of hostile monsters..."
    junpei "I mean... Who cares? Right?"

    menu:
        "\"Well maybe it's a lot scarier for her than for you.\"":
            junpei "Hmm..."
            junpei "Yeah... I guess I can see that..."
            $ junpeiRel.incrBondBy(5)

        "\"Don't be an inconsiderate jerk.\"":
            junpei "Woah! Alright! Alright... Sorry...."
            $ junpeiRel.incrBond()

        "\"Yeah, she needs to chill out.\"":
            junpei "Woah, I kinda wasn't expecting you to agree to that so easily."

    junpei "It's just, I don't want the team to be so stressed out... and like..."
    p "> Junpei trails off."
    junpei "I mean... How are we supposed to get to the top of Tartarus if we have a panic attack every floor?"

    window hide
    
    hide junpei
    with dissolve

    pause 1.5

    window show

    p "> A waitress jingles out of the entrance with a bag full of octopus-shaped red-potatoes and calamari."
    p "> They look a bit soggy..."

    show junpei neutral
    with dissolve

    junpei "Thanks for the grub!"

    junpei "Well... Sorry for using up our time talking about Yukari behind her back."
    junpei "Let's dig in!"

    p "> Junpei bites into a handful of greasy calamari rings and swallows them without thinking..."
    p "> Almost instantly, you hear his stomach groan as if a tortured soul."

    junpei "Uh..."
    junpei "Urgh... Um... I think... I need to go inside..."

    show black
    with fade

    window show
    p "> As Junpei gets his stomach pumped by paramedics, you decide to just look for food on the way home."

    $ endingVar = "Junpei"

    jump transevening

label junpeiGiftMenu:
    $ totalGiftItems = jackfrostdoll.getAmount() + antiquekatana.getAmount()

    if totalGiftItems > 0:

        window hide

        menu:
            #Unique Responses
            "Antique Katana" if antiquekatana.getAmount() > 0:
                $ antiquekatana.decrAmount(1)
                $ giftType = antiquekatana.getAttribute()
                jump junpeiAntiqueKatanaResponse   

            #Normal Responses, Responses are based entirely on the gift's attribute
            "Jack Frost Doll" if jackfrostdoll.getAmount() > 0:
                $ jackfrostdoll.decrAmount(1)
                $ giftType = jackfrostdoll.getAttribute() 
                jump junpeiGiftResponse

    else:
        p "> You don't have any gifts to give..."
        jump junpeiSpendTimeQuery

label junpeiGiftResponse:
    window show
    p "> You present the gift to Junpei."

#Junpei only likes cool gifts. This is his response to cool but non-unique gifts
    window show

    if giftType == "Cool":

        $ junpei.incrBond()
        junpei "> This awesome! I appreciate it!"

        jump junpeiSpendTimeQuery

    else:

        junpei "Uh... That's not really my thing. But I guess that's pretty... neat."

        p "> Junpei didn't really like your gift..."
        p "> You try not to hold it against him forever and ever until time immemorial."

        jump junpeiSpendTimeQuery

label junpeiAntiqueKatanaResponse:
    window show
#Junpei's response to getting an antique katana
    p "You show Junpei the present."
    jump junpeiSpendTimeQuery
#Contains text and control for Yukari's after school events (that aren't specific to a room/navigation screen)

label yukariSpendTime:
    window hide

    stop music fadeout 1.0

    show black
    with fade

    pause 1

    play music "audio/Joy.mp3"

    scene bg chagall cafe
    with fade

    window show

    p "> You and Yukari decide to get coffee at Chagall Cafe..."

    show yukari neutral
    with dissolve

    p "> Your turn to order is approaching, yet Yukari is still pondering the menu..."
    p "> You order, then give Yukari the chance to do the same."
    p "> For a moment, she hesitates..."
    p "> Then, as if a switch flipped, Yukari gets a look of strong purpose on her face."
    
    yukari "Could I get an apple spice frapuccino? With five pumps of caramel and whipped cream. Mix it in if possible."

    p "> Yukari looks pleased with her complex order."

    yukari "You know, I'm not much of a coffee snob, but I always wondered if I'd make a good barista."

    menu:
        "\"You're a very detailed-oriented person. You'd do great.\"":
            yukari "Aw thanks! I just like to have all my facts in order is all."

            $ yukariRel.incrBond()
            p "> Yukari sits up a little straighter."

        "\"Would you really want that though?\"":
            yukari "Yeah it is kind of a demanding job. And like imagine..."

            p "> Yukari goes off about the job's massive amount of annoying-customer-potential-energy."

    window hide
    
    hide yukari
    with dissolve

    pause 1.5
    window show

    show yukari neutral
    with dissolve

    p "> Your drinks are brought to your table."
    p "> Yukari takes a slow sip of her unique apple spice latte, as if taking the whole moment in."

    yukari "It's nice to get to spend time like this, y'know?"

    yukari "Exploring Tartarus for so many nights this year is becoming stressful honestly..."

    yukari "And trying to live a normal life on top of it all... It can just be so overwhelming..."

    yukari "I mean... We aren't even \"normal\" students outside of this persona situation we've been forced into."

    menu:

        "\"I feel pretty normal.\"":
            yukari "Oh, I guess it's just me."
            yukari "Sorry... I'm getting ahead of myself."
           
            p "> Yukari looks a bit less lively."

        "\"It's not always that bad though.\"":
            yukari "Yeah... There are ups and downs to living such a strange life."
            yukari "Still, I value these moments that we get to be \"normal\" teenagers so much."

            $ yukariRel.incrBond()
            p "> Yukari gets a sentimental look on her face."


        "\"I can understand how you feel.\"":
            yukari "I'm glad it's not just me..."
            yukari "I value the moments we get to just be \"normal\" teenagers."
            yukari "Whatever \"normal\" means, right?"

            $ yukariRel.incrBondBy(5)
            p "> Yukari chuckles a little. She looks as if a weight has been lifted from her."

    window hide
    
    hide yukari
    with dissolve

    pause 1.5
    window show

    show yukari neutral
    with dissolve

    p "> Yukari takes the last sip of her latte."

    yukari "Well... I guess with that, our little moment of normalcy is over..."

    menu:
        "\"Thanks for hanging out.\"":
            yukari "Thanks, Meiko... I needed this."

            show black
            with fade

            p "> Yukari and you head your separate ways. Yours being straight home."
            
            $ endingVar = "Yukari"
            
            jump transevening

        "\"Who said it has to end now?\"":
            yukari "Aw! I didn't think you'd actually want to hang out longer."
            
            $ yukariRel.incrBondBy(5)
            p "> Yukari's body language cannot convey the force of her smile."

            yukari "I'd be glad to spend more time with you!"
            yukari "Where should we go first?"

            show black
            with fade

            p "> Yukari and you spend more time together browsing Paulowina Mall, until you decide to head home."
            
            $ endingVar = "Yukari"

            jump transevening

label yukariGiftMenu:
    $ totalGiftItems = jackfrostdoll.getAmount() + antiquekatana.getAmount()

    if totalGiftItems > 0:

        window hide

        menu:
            #Unique Responses
            "Jack Frost Doll" if jackfrostdoll.getAmount() > 0:
                $ jackfrostdoll.decrAmount(1)
                jump yukariJackFrostResponse

            #Normal Responses
            "Antique Katana" if antiquekatana.getAmount() > 0:
                $ antiquekatana.decrAmount(1)
                $ giftType = antiquekatana.getAttribute()
                jump yukariGiftResponse    

    else:
        p "> You don't have any gifts to give..."
        jump yukariSpendTimeQuery

label yukariGiftResponse:
    window show
    p "> You present your gift to Yukari."

#Cute Gift Response
    window show

    if giftType == "Cute":

        yukari "This is adorable! Thanks, Meiko!"

        $ yukariRel.incrBond()
        p "> Yukari appreciated your gift! Awesome!"

        jump yukariSpendTimeQuery

    #Anything but Cute Response
    else:

        yukari "Oh wow... Well... I appreciate the thought?"

        p "> Yukari didn't really like your gift..."

        jump yukariSpendTimeQuery

label yukariJackFrostResponse:
    window show
    
#Yukari's response to getting a jack frost doll
    p "> With a soft smile, you hand the {color=#8c7a07}Jack Frost Doll{/color} to Yukari."

    yukari "Aww! Meiko you shouldn't have!"

    p "> Yukari gives the doll a tender squeeze."

    yukari "Y'know, I actually used to have one of these as a kid."
    yukari "My dad got me one at a carnival..."

    p "> Yukari is lost in thought. Then she comes to."

    yukari "I'm so glad you thought to get me this. Thank you."

    $yukariRel.incrBondBy(5)
    p "> Yukari was delighted by your gift."

    jump yukariSpendTimeQuery
#Labels used to control game shop interactions and events within the shops (Shops: Pharmacy, Antique Shop, Police Station)

label talkPharmacy:
    scene bg shop pharmacy interior

    show vendor_pharmacy neutral
    with dissolve

    window show

    pharmacist "Gosh, it's getting hot this time of year."
    pharmacist "I didn't sell much Aojiru Sorbet last year, but I'm thinking of trying it again anyway..."
    pharmacist "Even if kids these days would only eat it on a dare. It's so bitter."

    window hide

    show screen pharmacyshopmenu
    hide screen pharmacyshopmenu

    $ renpy.transition(dissolve)
    call screen pharmacyshopmenu

label buyPharmacy:
    scene bg shop pharmacy interior

    show vendor_pharmacy neutral
    with dissolve

    window show

    pharmacist "Sorry, the sign says open but I'm on break today."
    pharmacist "Unless you really need some medical advice, I'll be here saying my thoughts to whoever will listen."

    window hide

    show screen pharmacyshopmenu
    hide screen pharmacyshopmenu

    $ renpy.transition(dissolve)
    call screen pharmacyshopmenu

label talkAntiqueShop:
    scene bg shop antiqueshop interior

    show vendor_antiqueshop neutral
    with dissolve

    window show

    antiquelady "Fusing weapons with Personas is a simple process."
    antiquelady "...What do you mean you don't need any new magic weapons today?"
    antiquelady "That's rare, but alright, kid."

    window hide

    show screen antiqueshopmenu
    hide screen antiqueshopmenu

    $ renpy.transition(dissolve)
    call screen antiqueshopmenu

label buyAntiqueShop:
    scene bg shop antiqueshop interior

    show vendor_antiqueshop neutral
    with dissolve

    window show

    antiquelady "Look, kid. All I do is fuse your Personas with weapons then pawn off the precious gemstones you give me to do it."
    antiquelady "(...I shouldn't have said that second part out loud.)"
    antiquelady "If you don't want that, I don't have much else for you besides idle chatter."

    window hide

    show screen antiqueshopmenu
    hide screen antiqueshopmenu

    $ renpy.transition(dissolve)
    call screen antiqueshopmenu

label talkPoliceStation:
    scene bg shop police station interior

    show vendor_policestation neutral
    with dissolve

    window show

    kurosawa "...Sorry I can't help you kids out more."
    p "> You think about how because adults can't fix the supernatural monster problem, suddenly teenagers have to..."
    p "> Kind've a raw deal, but alright."

    window hide

    show screen policeshopmenu
    hide screen policeshopmenu

    $ renpy.transition(dissolve)
    call screen policeshopmenu

label buyPoliceStation:
    scene bg shop police station interior

    show vendor_policestation neutral
    with dissolve

    window show

    kurosawa "So about me not having that much..."
    kurosawa "Turns out selling medieval weaponry to teenagers is a hard sell to upper-management."
    kurosawa "I'll restock later. In the meantime, I'll be on duty. Unless you want to chat."

    window hide

    show screen policeshopmenu
    hide screen policeshopmenu

    $ renpy.transition(dissolve)
    call screen policeshopmenu


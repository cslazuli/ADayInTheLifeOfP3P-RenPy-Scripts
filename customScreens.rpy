#####################################
##Area Navigation Screens
#####################################

screen velvetroom():

    viewport:
    #A viewport is like a new window opened within the game window. It can be scrolled around and objects like buttons can be added to it.

    #xpos is the x position and ypos is y position of the viewport of the window/an object.
    #Make both 0/don't include them if you want to make the viewport the full screen

    #xysize is the size of the viewport within the game window. For full screen, make it the size of the game window.
    #xalign and yalign are arguments as well, but aren't important to the function of this screen Getting rid of it didn't mess anything up so.
        xysize (1280, 720)

    #child_size essentially what are the "walls" of the viewport. Where will the "camera" stop scrolling if you move too close.
    #Generally, make this the size of the full image you will add unless you want to see the nothingness behind the image.
    #Also when it comes to the image size, you can make it larger than the screen but maybe not by too much so there isn't an overwhelming amount of content for a user to scroll through.
    #Too large of an image is overwhelming to look at/make sense of.
        child_size (1600, 900)

    #x and yinitial let you control what part of the viewport is shown right you call it
        xinitial(200)
        yinitial(100)

    #These govern what sorts of controls you can use to move the viewport. All but edgescroll aren't very smooth, so I prefer only edgescroll.
        draggable False
        mousewheel False
        arrowkeys False
        
    #edgescroll allows for the viewport to scroll at a velocity based on where your mouse cursor is and how close it is to the edge of the screen.
    #Its parameters are (how fast the "camera" scrolls when your cursor is at the edge of the screen (pixels per second), How close to the edge (in pixels) does the cursor need to be for the screen to begin scrolling at any velocity)
        edgescroll (250, 1000)
        
    #after making the parameters of the viewport itself, you can start adding objects within it.

    #add here places an image in the viewport
        add "screen velvetroom.png"

    #Junpei
        if dayNight == 0:
            imagebutton:
                #x/y pos sets where is the object (in this case, an imagebutton: a button that appears as an image) on the screen (top right pixel)
                xpos 535 ypos 327
                #auto sets the image to automatically change to another image with the same name but different last word (%s string acts as a tag: idle, hover) based on what state it is in (ex. hovered by mouse, clicked by mouse)
                auto "overworld junpei_%s.png"
                #action informs what the button will do when interacted with. In this case, when clicked on.
                #Multiple actions can be done by putting them inside of []
                action [Hide("velvetroom", "dissolve"), Jump("talkJunpei")]

    #Yukari
        if dayNight == 0:
            imagebutton:
                xpos 387 ypos 353
                auto "overworld yukari_%s.png"
                action [Hide("velvetroom", "dissolve"), Jump("talkYukari")]

    #Igor
        fixed:
            xpos 768 ypos 409 xmaximum 65 ymaximum 115
            button:
                style "button"
                action [Hide("velvetroom", "dissolve"), Jump("talkIgor")]

    #Theodore
        imagebutton:
            xpos 1220 ypos 290
            auto "overworld theodore_%s.png"
            action [Hide("velvetroom", "dissolve"), Jump("talkTheodore")]

    #Exit
        frame:
            xpos 770 ypos 830
            #Without the frame, the button will just appear as text
            button:
                style "button_text"
                text "Exit" 
                action [Hide("velvetroom", "dissolve"), SetVariable("hovObj", ""), Jump("exitQueryVelvetRoom")]
                hovered [SetVariable("hovObj", "Paulowina Mall")]
                unhovered [SetVariable("hovObj", "")]

#The Use command allows you to have a screen show up at the same time as another
    use navioverlay

screen paulowinamall():
    viewport:
        xysize (1280, 720)
        child_size (3072, 765)
        xinitial (850)
        yinitial (200)
        edgescroll (250, 1000)

        add "screen paulowinamall"

#Day NPCs
        showif dayNight == 0:
        #Blue-Haired Girl
            imagebutton:
                xpos 1050 ypos 445
                auto "overworld npc bluehair_%s.png"
                action [Hide("paulowinamall", "dissolve"), Jump("talkGirls")]

        #Girl in Green
            imagebutton:
                xpos 1110 ypos 450
                auto "overworld npc greengirl_%s.png"
                action [Hide("paulowinamall", "dissolve"), Jump("talkGirls")]

        #Old Practitioner
            imagebutton:
                xpos 1800 ypos 400
                auto "overworld npc olddude_%s.png"
                action [Hide("paulowinamall", "dissolve"), Jump("talkOldDude")]

#Entrances/Other Interactables
    #Velvet Room Alley Way (Weird Blue Glowing Alley); For buttons which change hovObj and can jump to a new screen, pass time, return to map, be sure to set hovObj to "" as action =/= unhovering
        fixed:
            xpos 1346 ypos 129 xmaximum 190 ymaximum 242
            button:
                style "button"
                action [Hide("paulowinamall", "dissolve"), SetVariable("hovObj", ""), Jump("velvetalleywaynavi")]
                hovered [SetVariable("hovObj", "Back Alley")]
                unhovered [SetVariable("hovObj", "")]

    #Escapade
        fixed:
            xpos 274 ypos 314 xmaximum 167 ymaximum 235
            button:
                style "button"
                action [Hide("paulowinamall", "dissolve"), SetVariable("hovObj", ""), Jump("clubEscapadeQuery")]
                hovered [SetVariable("hovObj", "Club Escapade")]
                unhovered [SetVariable("hovObj", "")]

    #Chagall Cafe
        fixed:
            xpos 480 ypos 270 xmaximum 174 ymaximum 211
            button:
                style "button"
                action [Hide("paulowinamall", "dissolve"), SetVariable("hovObj", ""), Jump("chagallCafeQuery")]
                hovered [SetVariable("hovObj", "Chagall Cafe")]
                unhovered [SetVariable ("hovObj", "")]
                
    #Be Blue V
        fixed:
            xpos 686 ypos 204 xmaximum 245 ymaximum 223
            button:
                style "button"
                action [Hide("paulowinamall", "dissolve"), SetVariable("hovObj", ""), Jump("beBlueVQuery")]
                hovered [SetVariable("hovObj", "Be Blue V")]
                unhovered [SetVariable ("hovObj", "")]

    #Police Station
        fixed:
            xpos 1052 ypos 181 xmaximum 245 ymaximum 223
            button:
                style "button"
                action [Hide("paulowinamall", "dissolve"), SetVariable("hovObj", ""), Jump("enterPoliceStation")]
                hovered [SetVariable("hovObj", "Police Station")]
                unhovered [SetVariable ("hovObj", "")]

    #Mandragora Karaoke
        fixed:
            xpos 1357 ypos 0 xmaximum 345 ymaximum 116
            button:
                style "button"
                action [Hide("paulowinamall", "dissolve"), SetVariable("hovObj", ""), Jump("mandragoraQuery")]
                hovered [SetVariable("hovObj", "Mandragora")]
                unhovered [SetVariable ("hovObj", "")]

    #Antique Shop
        fixed:
            xpos 1820 ypos 183 xmaximum 245 ymaximum 201
            button:
                style "button"
                action [Hide("paulowinamall", "dissolve"), SetVariable("hovObj", ""), Jump("enterAntiqueShop")]
                hovered [SetVariable("hovObj", "Shinshoudo Antiques")]
                unhovered [SetVariable ("hovObj", "")]

    #Pharmacy
        fixed:
            xpos 2146 ypos 191 xmaximum 234 ymaximum 232
            button:
                style "button"
                action [Hide("paulowinamall", "dissolve"), SetVariable("hovObj", ""), Jump("enterPharmacy")]
                hovered [SetVariable("hovObj", "Aohige Pharmacy")]
                unhovered [SetVariable ("hovObj", "")]

    #Power Records
        fixed:
            xpos 2430 ypos 242 xmaximum 167 ymaximum 229
            button:
                style "button"
                action [Hide("paulowinamall", "dissolve"), SetVariable("hovObj", ""), Jump("powerRecordsInteract")]
                hovered [SetVariable("hovObj", "Power Records")]
                unhovered [SetVariable ("hovObj", "")]

    #Game Panic
        fixed:
            xpos 2690 ypos 292 xmaximum 101 ymaximum 248
            button:
                style "button"
                action [Hide("paulowinamall", "dissolve"), SetVariable("hovObj", ""), Jump("gamePanicQuery")]
                hovered [SetVariable("hovObj", "Game Panic")]
                unhovered [SetVariable ("hovObj", "")]

    #Crane Game
        fixed:
            xpos 2598 ypos 326 xmaximum 94 ymaximum 202
            button:
                style "button"
                action [Hide("paulowinamall", "dissolve"), SetVariable("hovObj", ""), Jump("craneGameQuery")]
                hovered [SetVariable("hovObj", "Crane Game")]
                unhovered [SetVariable ("hovObj", "")]

    #Exit to Town Map
        frame:
            xpos 1502 ypos 700
            button:
                style "button_text"
                text "Exit" 
                action [Hide("paulowinamall", "dissolve"), SetVariable("hovObj", ""), Jump("townmapnavi")]
                hovered [SetVariable("hovObj", "Town Map")]
                unhovered [SetVariable("hovObj", "")]

    use navioverlay

screen velvetalleyway():
    viewport:
        xysize (1280, 720)
        child_size (1536, 765)
        xinitial (100)
        yinitial (20)
        edgescroll (250, 1000)

        add "screen velvetalleyway"

    #Door into Velvet Room
        fixed:
            xpos 642 ypos 233 xmaximum 248 ymaximum 390
            button:
                style "button"
                action [Hide("velvetalleyway", "dissolve"), SetVariable("hovObj", ""), Jump("velvetroomnavi")]
                hovered [SetVariable("hovObj", "Glowing Door")]
                unhovered [SetVariable("hovObj", "")]

    #Exit
        frame:
            xpos 740 ypos 680
            button:
                style "button_text"
                text "Exit" 
                action [Hide("velvetroom", "dissolve"), SetVariable("hovObj", "Paulowina Mall"), Jump("paulowinamallnavi")]
                hovered [SetVariable("hovObj", "Paulowina Mall")]
                unhovered [SetVariable("hovObj", "")]

    use navioverlay


screen townmap():
    
    viewport:
        xysize (1280, 720)
        child_size (1280, 720)

        add "screen townmap"

        vbox:
            spacing 20

            if dayNight == 0:
                xalign 0.04 yalign 0.9
            else:
                xalign 0.05 yalign 0.5
            
            if dayNight == 0:
                frame:
                    button:
                        style "button_text"
                        text "Gekkoukan High School" size 35
                        action [Hide("townmap", "dissolve"), Jump("interactGekkoukanHS")]

            frame:
                button:
                    style "button_text"
                    text "Paulowina Mall" size 35
                    action [Hide("townmap", "dissolve"), Jump("paulowinamallnavi")]

            frame:
                button:
                    style "button_text"
                    text "Dorm" size 35
                    
                    if dayNight == 0:
                        action [Hide("townmap", "dissolve"), Jump("returntodormearly")]

                    elif dayNight == 1:
                        action [Hide("townmap", "dissolve"), Jump("returntodormevening")]

            if dayNight == 0:

                frame:
                    button:
                        style "button_text"
                        text "Iwatodai Strip Mall" size 35
                        action [Hide("townmap", "dissolve"), Jump("visitIwatodaiStripMall")]

                frame:
                    button:
                        style "button_text"
                        text "Shrine" size 35
                        action [Hide("townmap", "dissolve"), Jump("fuukaShrineScene")]

                frame:
                    button:
                        style "button_text"
                        text "Port Island Station" size 35
                        action [Hide("townmap", "dissolve"), Jump("visitPortIslandStation")]


######Custom HUD Screens###########################################

screen navioverlay():
    fixed:
        xmaximum 395 ymaximum 634
        xalign 1.06 yalign 1.5
        add "menu_meiko"

    showif naviName != "":
        frame:
            xalign 0.03 yalign 0.96
            left_padding 50
            right_padding 50
            text "[naviName]"

    showif hovObj != "":
        frame:
            xalign 1.1 yalign 0.96
            left_padding 20
            right_padding 300
            text "[hovObj]"

    #frame:
        #$ currentSong = renpy.music.get_playing()
        #xalign 1.0 yalign 0.0
        #text "[currentSong]"

screen statusmenu():

#Stores item flavor text so it can be displayed in status menu
    default itemText = ""

    tag menu

#keysym allows you to make the button respond to a specified user input on the keyboard
#Be sure to put keysym buttons at the top of any screen you make so they're loaded first under everything else
#Otherwise they're on top of everything and make the other buttons unresponsive

#Allows player to exit the status menu. Must be under everything else, so we generate it first.
    button:
        action Return()
        keysym('m')

    add "menu_statusmenu"

    viewport:

        xysize(600, 220)
        xpos 460 ypos 110
    #If you omit childsize(), the viewport will scale based on the size of it's displayable.
    #In this case, the viewport will be however tall the vbox within it is, so it can dynamically change based on how many objects are in it
        mousewheel True
        arrowkeys True
        scrollbars "vertical"

        vbox:
            spacing 1

            frame:
                xsize(550)
                left_padding 40
                button:
                    style "button_text"
                    text "Wrapper                            x1"
                    action NullAction()
                    hovered SetScreenVariable("itemText", "Used to have candy. Now has a primitive data type in it.")
                    unhovered SetScreenVariable("itemText", "")

            showif jackfrostdoll.amount >= 1:
                frame:
                    xsize(550)
                    left_padding 40
                    button:
                        style "button_text"
                        text "Jack Frost Doll                  x [jackfrostdoll.amount]"
                        action NullAction()
                        hovered SetScreenVariable("itemText", "A cute doll that's prized... for it's cuteness.")
                        unhovered SetScreenVariable("itemText", "")

            showif antiquekatana.amount >= 1:
                frame:
                    xsize(550)
                    left_padding 40
                    button:
                        style "button_text"
                        text "Antique Katana                x [antiquekatana.amount]"
                        action NullAction()
                        hovered SetScreenVariable("itemText", "A Katana that is old.")
                        unhovered SetScreenVariable("itemText", "")

            #showif [item].amount >= 1:
                #frame:
                    #xsize(550)
                    #left_padding 40
                    #button:
                        #style "button_text"
                        #text "uh"

    showif itemText != "":
        fixed:
            xpos 500 ypos 350 xmaximum 400
            text "{color=#850042}➤ [itemText]{/color}"

#Vertical Box which contains Meiko's stats
    vbox:
        xpos 134 ypos 144

        spacing 0.5

        text "{color=#850042}[meiko.confidence]{/color}":
            size 22
        text "{color=#850042}[meiko.intelligence]{/color}":
            size 22
        text "{color=#850042}[meiko.charm]{/color}":
            size 22

#Vertical Box which contains bonds with characters and icons
    vbox:
        xpos 8 ypos 248

        hbox:
            add "menu_yukari rel icon.png"
            text "{color=#850042}Bond: [yukariRel.bond]  //  ♥: [yukariRel.romance]{/color}":
                yalign 0.5

        hbox:
            add "menu_junpei rel icon.png"
            text "{color=#850042}Bond: [junpeiRel.bond]  //   ♥: [junpeiRel.romance]{/color}":
                yalign 0.5

        hbox:
            add "menu_fuuka rel icon.png"
            text "{color=#850042}Bond: [fuukaRel.bond]  // ♥: [fuukaRel.romance]{/color}":
                yalign 0.5

        showif theodoreRel.bond > 9:
            hbox:
                add "menu_theodore rel icon.png"
                text "{color=#850042}Bond: [theodoreRel.bond]  //  ♥: [theodoreRel.romance]{/color}" :
                    yalign 0.5

############Shop Menus###########

screen moneydisplay():

    frame:
        xalign 1.1 yalign 0.1
        left_padding 20
        right_padding 140
        text "¥         [meiko.money]"

screen pharmacyshopmenu():
    
    add "screen shop pharmacy interior.png"

    use moneydisplay

    hbox:
        xalign 0.8 yalign 0.25

        frame:
            button:
                style "button_text"
                text "\nBuy     ":
                    size 42
                action [Hide("pharmacyshopmenu", "dissolve"), Jump("buyPharmacy")]

        frame:
            button:
                style "button_text"
                text "\nTalk     ":
                    size 42
                action [Hide("pharmacyshopmenu", "dissolve"), Jump("talkPharmacy")]

        frame:
            button:
                style "button_text"
                text "\nExit     ":
                    size 42
                action [Hide("pharmacyshopmenu", "dissolve"), Jump("paulowinamallnavi")]

screen antiqueshopmenu():
    
    add "screen shop antiqueshop interior.png"

    use moneydisplay

    hbox:
        xalign 0.8 yalign 0.25

        frame:
            button:
                style "button_text"
                text "\nBuy     ":
                    size 42
                action [Hide("pharmacyshopmenu", "dissolve"), Jump("buyAntiqueShop")]

        frame:
            button:
                style "button_text"
                text "\nTalk     ":
                    size 42
                action [Hide("pharmacyshopmenu", "dissolve"), Jump("talkAntiqueShop")]

        frame:
            button:
                style "button_text"
                text "\nExit     ":
                    size 42
                action [Hide("pharmacyshopmenu", "dissolve"), Jump("paulowinamallnavi")]

screen policeshopmenu():
    
    add "screen shop police station interior.png"

    use moneydisplay

    hbox:
        xalign 0.8 yalign 0.25

        frame:
            button:
                style "button_text"
                text "\nBuy     ":
                    size 42
                action [Hide("pharmacyshopmenu", "dissolve"), Jump("buyPoliceStation")]

        frame:
            button:
                style "button_text"
                text "\nTalk     ":
                    size 42
                action [Hide("pharmacyshopmenu", "dissolve"), Jump("talkPoliceStation")]

        frame:
            button:
                style "button_text"
                text "\nExit     ":
                    size 42
                action [Hide("pharmacyshopmenu", "dissolve"), Jump("paulowinamallnavi")]
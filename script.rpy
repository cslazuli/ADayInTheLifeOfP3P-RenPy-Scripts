#TODO: 

#Updates to make game cooler/practice more

    #Add a name screen, and replace instances of "Meiko" with the player's name string

    #Go back through code to clean stuff up and review comments

    #Implement Buy and Sell System/Menus in Shops; Add more gifts you can buy and have confidantes have reactions to them

    #Add secret Theodore scene if you increase your charm, smarts, and confidence by exploring around town

    #Change The Textbox Window

    #Go back and capitalize labels?

    #Fix Gift Giving and/or come up with a better system for it
    #(showing a scrollable viewport/menu screen like the status one with the items showing up only if you have them, then returning the item's ID when you click an option is smart)

    #Add animated bits to the shops

    #Find and add SFX, add SFX to some of the methods to save time by not doing it individually
    
    #See if you can implement some kind of hover gossip thing like Person 5
    
    #Start to clean up unused variables/assets/class object variables

    #Consider adding time HUD in top left corner

    #Add character emotes

    #Generalize Transitions by storing room data

#Condition Switch example
#image bg city = ConditionSwitch(
#    "time < 18", "city_daytime.png",
#    "time < 20", "city_sunset.png",
#    "True", "city_night.png")

####Consider if the unique story scenarios/scenes for your personal game should be split into different files by month

# Declare characters used by this game. The color argument colorizes the
# name of the character.

init:

    #Player/System Text
    define p = Character("")
    define m = Character("Menu", color="#0300b0")
    define q = Character("???", color="#0300b0")

    #Confidantes
    define yukari = Character("Yukari", color="#0300b0")
    define fuuka = Character("Fuuka", color="#0300b0")
    define junpei = Character("Junpei", color="0300b0")

    #School Extras
    define terauchi = Character("Mrs. Terauchi", color="0300b0")
    define classmate = Character("Classmate", color="0300b0")

    #Velvet Room Chars
    define igor = Character("Igor", color = "0300b0")
    define theodore = Character("Theodore", color = "0300b0")

    #Town NPCS
    define npc_bluehair = Character("Blue-Haired Girl", color = "0300b0")
    define npc_greengirl = Character("Girl in Green", color = "0300b0")
    define npc_detective = Character("Strange Detective", color = "0300b0")
    define npc_olddude = Character("Old Practitioner", color = "0300b0")
    define npc_redguy = Character("Guy in Red", color = "0300b0")
    define npc_punkgirl = Character("Punk Girl", color = "0300b0")

    #Shop Vendors
    define pharmacist = Character("Shopkeeper", color = "0300b0")
    define kurosawa = Character("Officer Kurosawa", color = "0300b0")
    define antiquelady = Character("Owner", color = "0300b0")

    define dayNight = 0

    image screen paulowinamall = ConditionSwitch(
        "dayNight == 0", "screen paulowinamallday",
        "dayNight == 1", "screen paulowinamallnight"
        )

    image screen townmap = ConditionSwitch(
        "dayNight == 0", "screen townmap day",
        "dayNight == 1", "screen townmap night"
        )

    image bg townmap = ConditionSwitch(
        "dayNight == 0", "bg townmap day",
        "dayNight == 1", "bg townmap night"
        )

    image black = "#000"
    image white = "#fff"

    #Navigation Screen Heads Up Display (HUD) Variables 
    define hovObj = ""

    define naviName = ""

    #Debug Flag
    define debug = False

#Python Block run at program initialization
init python:

#Class which contains and allows changes to the player's stats in one place
    class LifeStats:
        def __init__(self, Charm, Intelligence, Confidence, Money):
            self.charm = Charm
            self.intelligence = Intelligence
            self.confidence = Confidence
            self.money = Money

    #Getters
        def getCharm(self):
            return self.charm
        
        def getIntelligence(self):
            return self.intelligence

        def getConfidence(self):
            return self.confidence

        def getMoney(self):
            return self.money

    #Setters
        def setCharm(self, newCharm):
            self.charm = newCharm

        def setIntelligence(self, newIntelligence):
            self.intelligence = newIntelligence

        def setConfidence(self, newConfidence):
            self.confidence = newConfidence

        def setMoney(self, newMoney):
            self.money = newMoney

    #Other Methods/Functions

        def incrCharm(self):
            self.charm = self.getCharm() + 1

        def greatlyIncrCharm(self):
            self.charm = self.getCharm() + 5

        def incrIntelligence(self):
            self.intelligence = self.getIntelligence() + 1

        def greatlyIncrIntelligence(self):
            self.intelligence = self.getIntelligence() + 5

        def incrConfidence(self):
            self.confidence = self.getConfidence() + 1

        def greatlyIncrConfidence(self):
            self.confidence = self.getConfidence() + 5

        def incrMoney(self, howMuch):
            self.money = self.getMoney() + howMuch

        def decrMoney(self, howMuch):
            self.money = self.getMoney() - howMuch

#Class which contains various aspects about your relationships to other characters

    class Relationship:
        def __init__(self, Bond, Romance, ContextBond):
        #Bond is how close they are you in general. A platonic bond/general affinity for you as a person.
        #Romance is how interested they are in you based on if you've shown them romantic interest.
        #ContextBond gives me the flexibility to have a character react a certain way based on player actions within a given conversation/scenario.
            #This way, NPCs are a bit more human. 
            #Even if you have a strong bond or high romance stat, they can still get mad at you and can do it in different ways by checking this stat and the other ones.
            self.bond = Bond
            self.romance = Romance
            self.contextBond = ContextBond

    #Getters
        def getBond(self):
            return self.bond
        
        def getRomance(self):
            return self.romance

        def getContextBond(self):
            return self.contextBond

    #Setters
        def setBond(self, newBond):
            self.bond = newBond

        def setRomance(self, newRomance):
            self.romance = newRomance

        def setContextBond(self, newContextBond):
            self.contextBond = newContextBond

    #Other Methods
        def incrBond(self):
            self.bond = self.getBond() + 1

        def incrBondBy(self, howMuch):
            self.bond = self.getBond() + howMuch

        def incrRomance(self):
            self.romance = self.getRomance() + 1

        def incrRel(self):
            self.bond = self.getBond() + 1
            self.romance = self.getRomance() + 1

        def resetContextBond(self):
            self.contextBond = 0

#Inventory Class
    class Inventory:
        def __init__(self, ID, Amount, Type, Attribute):
            #Types: "Health", "Battle", "Other"
            #Attributes: "NotGift", "Cute", "Cool", "Interesting"
                self.id = ID
                self.amount = Amount
                self.type = Type
                self.attribute = Attribute

            #Getters
        def getID(self):
            return self.id
        
        def getAmount(self):
            return self.amount

        def getType(self):
            return self.type

        def getAttribute(self):
            return self.attribute

    #Setters
        def setAmount(self, newAmount):
            self.amount = newAmount

    #Other Methods
        def incrAmount(self, howMuch):
            self.amount = self.getAmount() + howMuch

        def decrAmount(self, howMuch):
            self.amount = self.getAmount() - howMuch

# The game starts here.

label start:

#In order to ensure player progress variables are stored when a player saves, you must define them outside of the init python block.

#Determines What Ending Player has Earned
    define endingVar = ""

#Event Flags
    define metFuukaAtShrine = False

    python:
        meiko = LifeStats(0, 0, 0, 1200)

        yukariRel = Relationship(10, 0, 0)
        junpeiRel = Relationship(8, 0, 0)
        fuukaRel = Relationship(10, 0, 0)
        theodoreRel = Relationship(10, 2, 0)

        jackfrostdoll = Inventory(1, 0, "Other", "Cute")
        antiquekatana = Inventory(2, 0, "Other", "Cool")

#morning event

    if persistent.finishedGame:

        p "Finished game data detected."
        p "Would you like to skip straight to the Velvet Room?"

        menu:

            "Yes":
                $ meiko.incrCharm()
                $ persistent._clear()
                jump velvetroomnavi

            "No":
                pass

    jump schoolentrancescene
    
    # Show a background. This uses a placeholder by default, but you can
    # add a file (named either "bg room.png" or "bg room.jpg") to the
    # images directory to show it.
import os
import platform

####VARIABLES
####VARIABLES
####VARIABLES
name = "Gravelorde"

class Being:
    def __init__(self, name):
        #Basic stats
        self.name = name
        self.hp = 1
        self.job_class = "initialized"
        self.level = 1
        self.max_hp = 1
        #Magicks and skills
        self.animal_control = False
        self.bone_alteration = False
        self.illusion_magic = False
        self.light_magic = False
        self.lunar_gift = False
        self.tactics = False
        #Used to initialize to center of screen + keep track of "player" (creature)
        self.x = 0
        self.y = 0
        #Physical representations
        #self.char = "@"
        #self.color = color_white
        #Only used to do the looping in character creation, then useless.
        self.still_deciding = True
            
    #Creates a character with these job classes    
    def character_classes(self):
        def are_you_sure(hp, job_class, level, max_hp, animal_control, 
        bone_alteration, illusion_magic, light_magic, lunar_gift, tactics):
            print "Do you wish to follow this path?"
            choice = raw_input(">")
            choice = choice.upper()                    
            if (choice[0] == "Y"):
                self.hp = hp
                self.job_class = job_class
                self.level = level
                self.max_hp = max_hp
                
                if animal_control == True:
                    self.skill = "Animal Control"
                    #self.color = color_brethren
                elif bone_alteration == True:
                    self.skill = "Bone Alteration"
                    #self.color = color_bone
                elif illusion_magic == True:
                    self.skill = "Illusion Magic"
                    #self.color = color_illusion
                elif light_magic == True:
                    self.skill = "Sun Magic"
                    #self.color = color_light_magic
                elif lunar_gift == True:
                    self.skill = "Lunar Gift"
                    #self.color = color_lunar
                elif tactics == True:
                    self.skill = "Ancient Tactics"
                    #self.color = color_olde
                    
                self.still_deciding = False
                
            elif (choice[0] == "N"):
                raw_input("Very well.")
            while (choice[0] != "Y" and choice[0] != "N"):
                print "Yes or no."
                choice = raw_input(">")
                choice = choice.upper()
      
        while (self.still_deciding == True):                    
            clear_reset()
            print "||CLASS MENU||"
            print "Choose class: "
            print "(A)nimal Brethren"
            print "(B)one Armourer"
            print "(I)llusionist"
            print "(S)un Magician"
            print "(L)unar Knight"
            print "(W)arrior of Olde"
            
            choice = raw_input(">")
            choice = choice.upper()
            
            if (choice == "A"):
                clear_reset()
                print ">-~^ANIMAL BRETHREN^~-<"
                print "The path of the animal brother." 
                print "Attuned to nature."
                print "Guides beasts to attack the enemies of creation."
                print "Spiritual Warrior."
                are_you_sure(10, "Animal Brethren", 1, 10, True, 0, 0, 0, 0, 0)
                
            elif (choice == "B"):
                clear_reset()
                print ">-~^BONE ARMOURER^~-<"
                print "The path of the hunter."
                print "Fashions bones from the fallen into weaponry and armour."
                print "Enchants using earth magics."
                print "Nomadic Survivor."
                are_you_sure(12, "Bone Armourer", 1, 12, 0, True, 0, 0, 0, 0)

            elif (choice == "D"):
                clear_reset()
                print ">-~^ILLUSIONIST^~-<"
                print "Path of the illusionist."
                print "Uses the power of logic to obfuscate."
                print "Sleight of Hand Master."
                print "Secret tradesman."
                are_you_sure(8, "Illusionist", 1, 8, 0, 0, True, 0, 0, 0)

            elif (choice == "N"):
                clear_reset()
                print ">-~^SUN MAGICIAN^~-<"
                print "The path of the sun magician."
                print "Draws extreme power from the sun."
                print "Body has become one with flame."
                print "Formidable Fire Thaumaturge."
                are_you_sure(6, "Sun Magician", 1, 6, 0, 0, 0, True, 0, 0)

            elif (choice == "L"):
                clear_reset()
                print ">-~^LUNAR KNIGHT^~-<"
                print "The path of the twilight breed."
                print "Pays homage to nature."
                print "Derives strength from the moon."
                print "Powerful Midnight Battler."
                are_you_sure(14, "Lunar Knight", 1, 14, 0, 0, 0, 0, True, 0)

            elif (choice == "W"):
                clear_reset()
                print ">-~^WARRIOR OF OLDE^~-<"
                print "The path of the strategist."
                print "Studies ancient forgotten tactics."
                print "Relys on quick wit and sheer strength."
                print "Master Swordsman."
                are_you_sure(16, "Warrior of Olde", 1, 16, 0, 0, 0, 0, 0, True)

            else:
                print "Huh?"
                raw_input()

def begin():
    clear_reset()
    name = raw_input("What is your name, ancient one?\n>")
    player.name = name
    clear_reset()
    print "What is your path, %s?" % player.name
    print "(C)reate new character"
    choice = raw_input("(E)xit this world\n>")
    choice = choice.upper()
    if (choice == "C"):
        player.character_classes()
    elif(choice == "E"):
        print "Be seeing you..."
        

def clear_reset():
    if platform.system() == "Windows":
        os.system('cls')
    else:
        os.system('clear') ## same command for Linux and Mac



####INSTANCES
####INSTANCES
####INSTANCES
player = Being(name)

####BEGIN HERE
####BEGIN HERE
####BEGIN HERE
begin()

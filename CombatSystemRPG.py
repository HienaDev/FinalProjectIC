import random

#Function to create a character
def createCharacter(name, health, mana, armor, damage, iniative):

    character = (name, health, mana, armor, damage, iniative)
    return (character)

#Function to create an array of characters
def allCharacters(characters):

    return (characters)

#Function to roll iniative of each character
def rollInitiative(character):

    d20 = random.randrange(1, 20)
    print(character[0] + " rolled a " + str(d20) + " his turn order is: " + str(d20 + character[5]))
    return (d20 + character[5])

#Function that creates a tuple with the order of each character
def turnOrder(characters):

    order = tuple()

    for character in characters:

        order += (rollInitiative(character), )
    return(order)

#def magicspells():
#    spells = ['rushdown', 'exorcism', 'mend']
#    if input ('rushdown')


#ola sou o henrique
player = createCharacter("PLAYER", 25, 10, 2, 5, 10)   
monster = createCharacter("MONSTER", 30, 20, 23, 5, 6)   
characters = allCharacters((player, monster))
print(str(characters[0]) + "\n" + str(characters[1]))
print(str(turnOrder(characters)))

spells = ['rushdown', 'exorcism', 'mend']
#se escolher o spell e possior mp sufecientes
#spellefectvalue = -1 * (wd + d4)
#if input('rushdown') and (mpplayer >= SpellMPcost):
#   (player[2]) - 




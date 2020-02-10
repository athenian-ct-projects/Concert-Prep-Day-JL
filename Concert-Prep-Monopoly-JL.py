#art fact function
def fact():
    import random
    x = random.randint(1,10)
    if x == 1:
        print("Bob Ross's 'Joy of Painting' TV series lasted for 31 seasons")
    if x == 2:
        print("In 1911 when the Mona Lisa was stolen from the Louvre, Pablo Picasso was one of the two primary suspects in the investigation \nbefore it was found out that an employee did it")
    if x == 3:
        print("Salvador Dalí thinks that he is a re-incarnation of his brother that died before he was born")
    if x == 4:
        print("Vincent van Gogh only ever sold one painting in his life")
    if x == 5:
        print("'The Last Supper' by Leonardo da Vinci originally featured Jesus's feet, but in 1652 when installing a door in the refectory where the painting is, \nthe feet were cut off")
    if x == 6:
        print("Vincent van Gogh's painting 'The Starry Night' is the view from a psychiatric hospital in France where van Gogh was staying when he painted it")
    if x == 7:
        print("The marble that was used for Michelangelo's 'David' was used by two other sculptors before Michelangelo")
    if x == 8:
        print("There are five versions of Edvard Munch’s 'The Scream'")
    if x == 9:
        print("Auguste Rodin’s 'The Thinker' originally was only 70cm until he later made an enlarged version")
    if x == 10:
        print("Andy Warhol's Campbell's Soup cans came in a set of thirty-two cans")
#Rainbow paint bucket function
def paint():
    import random
    y = random.randint(1,10)
    if y == 1:
        print("HOORAY, advance to go collect $200")
    if y == 2:
        print("You commited tax fraud - go to jail. If you pass go do not collect $200.")
    if y == 3:
        print("You are a guest star on a game show. Collect $100 from the bank.")
    if y == 4:
        print("You drink a Sprite cranbery. Suddenly your door falls down and Lebron James walks in and hands you a fat stack of cash. Collect $500 from the bank.")
    if y == 5:
        print("Some guy blows up your house with a grenade launcher like in John Wick 2. Pay the bank $200.")
    if y == 6:
        print("The Great Depression happens again and your bank fails. Pay the bank all of your money (you can mortgage your artists to avoid going bankrupt).")
    if y == 7:
        print("You get in a car crash while wearng a VR headset and playing a flight simulator in the car, saying 'it will be like I am flying in a plane'. \nPay the bank $200 in medical fees")
    if y == 8:
        print("Your grandfather dies and he leaves you an inheritance. You assume his massive debt and pay the bank $500.")
    if y == 9:
        print("Your favorite NFL team wins the Super Bowl! Pay the bank $50 for the jersey you bought.")
    if y == 10:
        print("You win the lottery but spend it all on worthless stuff. Roll the dice again")
#Instructions
print("Welcome to Artist Monopoly!")
print("This is just like regular monopoly but with some IMPORTANT twists:")
print("To roll dice just ask siri to roll a pair of dice")
print("*there are more spaces, and railroads have been replaced with more modern airlines")
print("*there are auction spaces now. If you land on one you can buy any artist on the board but you have to pay double (only one artist each time you land on the spot).")
print("*trading artists for money and other artists are encoureged but you can only propose a trade on your turn.")
print("*chance spaces have been replaced by artist facts. If you land on that space, type the word 'fact' into the computer.")
print("*community chests have been replaced by rainbow paint buckets. If you land on that space, type the word 'paint' into the computer.\n")
print("IMPORTANT: When someone goes bankrupt, type the word 'player' into the computer.\n")
player = int(input("How many people are playing today? "))
print("Alright you're ready to play. Everyone starts with $1500")

#Gameplay while loop
while player > 1:
    tip = input()
    if tip == "fact":
        fact()
    elif tip == "paint":
        paint()
    elif tip == "player":
        player = player - 1
    else:
        print("You must have spelled somthing wrong. Try again.")

#Final score calculating
print("Looks like we have a winner! Now lets calculate your final score.")
pig = int(input("How much money did the winner have in the end? "))
fig = 0
for z in range(1,pig):
  fig = fig + z
print("The final score of the winner is:")
print(fig)
print("Thanks for playing!")

#imports random library ready to be utilized by the file
import random 

# creates lists of values in accordance to their respective names
suits = ["Clubs", "Spades", "Hearts","Diamonds"]
faces = ["Jack", "Queen", "King", "Ace"]
numbered = ["2","3","3","4","5","6","7","8","9","10"]

# creates a function that draws each suit or card randomly, from the lists provided, and 
# then returns a tuple
def draw():
    the_suit = random.choice(suits)
    the_card = random.choice(faces)
    return the_card, "of", the_suit

# creates on tuple for each enquiry
print(suits)
print()

print(draw())
print(draw())
print(draw())
print()

for _ in range(5):
    print(draw())

deck = set()

for suit in suits:
    for card in faces + numbered:
        deck.add((card, "of", suit))

card = ("4", "of", "Clubs")

if card in deck:
    print("yes")
else:
    print("no")
    
for card in deck:
    print(card)
    
    
    
    
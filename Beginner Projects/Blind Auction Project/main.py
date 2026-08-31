import art
print(art.logo)
# TODO-1: Ask the user for input
# TODO-2: Save data into dictionary {name: price}
# TODO-3: Whether if new bids need to be added
# TODO-4: Compare bids in dictionary
dictionary={}
def add_bidder():
     name=input("Enter your name: ")
     bid=int(input("Enter your bid: "))
     dictionary[name]=bid
add_bidder()
next_decision=input("Another bidder wants to Particpate? Yes or No").lower()
while next_decision == "yes":
    add_bidder()
    print("\n" * 100)
    next_decision = input("Another bidder wants to participate? Yes or No: ").lower()
highest_bidder=0
for bidder in dictionary:
    if dictionary[bidder]>highest_bidder:
        highest_bidder=dictionary[bidder]
        winner=bidder
print("The Winner is ",winner)




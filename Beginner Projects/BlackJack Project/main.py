import random
cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]
def deal_card():
    return random.choice(cards)
def calculate_score(cards):
    if sum(cards) == 21 and len(cards) == 2:
        return 0
    if 11 in cards and sum(cards) > 21:
        cards.remove(11)
        cards.append(1)
    return sum(cards)
def compare(user_score, computer_score):
    if user_score == computer_score:
        return "Draw "
    elif computer_score == 0:
        return "You Lose! Dealer has Blackjack "
    elif user_score == 0:
        return "You Win with Blackjack! "
    elif user_score > 21:
        return "You went over 21. You Lose! "

    elif computer_score > 21:
        return "Dealer went over 21. You Win! "

    elif user_score > computer_score:
        return "You Win! "

    else:
        return "You Lose! "
def play_game():

    user_cards = []
    computer_cards = []

    for _ in range(2):
        user_cards.append(deal_card())
        computer_cards.append(deal_card())

    game_over = False
    while not game_over:
        user_score = calculate_score(user_cards)
        computer_score = calculate_score(computer_cards)

        print(f"\nYour cards: {user_cards}")
        print(f"Your current score: {user_score}")

        print(f"Computer's first card: {computer_cards[0]}")

        # Check Blackjack or bust
        if user_score == 0 or computer_score == 0 or user_score > 21:
            game_over = True
        else:
            user_should_deal = input(
                "Type 'y' to get another card, type 'n' to pass: "
            )

            if user_should_deal == "y":
                user_cards.append(deal_card())
            else:
                game_over = True
    while computer_score != 0 and computer_score < 17:
        computer_cards.append(deal_card())
        computer_score = calculate_score(computer_cards)
    user_score = calculate_score(user_cards)
    computer_score = calculate_score(computer_cards)

    print(f"\nYour final hand: {user_cards}")
    print(f"Your final score: {user_score}")
    print(f"Computer's final hand: {computer_cards}")
    print(f"Computer's final score: {computer_score}")
    print(compare(user_score, computer_score))
while input(
    "\nDo you want to play a game of Blackjack? Type 'y' or 'n': "
) == "y":
     print("\n" * 20)
     play_game()
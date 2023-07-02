from art import logo
import random
from replit import clear


def deal_card():
    cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]
    return random.choice(cards)


def calculate_score(hand):
    score = sum(hand)
    if score > 21 and 11 in hand:
        score -= 10
    return score


def compare(user_score, cpu_score, cpu_cards, user_cards):
    print(f"\nUser hand: {user_cards}")
    print(f"CPU hand: {cpu_cards}")
    print(f"CPU score is {cpu_score} and user score is {user_score}")
    if user_score == cpu_score:
        print("It is a draw!")
    elif cpu_score == 21:
        print("CPU wins!")
    elif cpu_score != 21 and user_score == 21:
        print("User wins!")
    elif user_score > 21:
        print("CPU wins!")
    elif cpu_score > 21:
        print("User wins!")
    elif cpu_score > user_score:
        print("CPU wins!")
    else:
        print("User wins!")


def play_again():
    return input(
        "\nDo you want to play again? Type 'y' or 'n': ").lower() == "y"


def blackjack_game():
    clear()
    print(logo)
    print("Welcome to the BlackJack Game\n")
    user_cards = []
    cpu_cards = []

    for _ in range(2):
        user_cards.append(deal_card())
        cpu_cards.append(deal_card())

    print(f"Your initial hand is {user_cards[0]} and {user_cards[1]}")
    print(f"CPU initial hand is {cpu_cards[0]} and X")

    if calculate_score(cpu_cards) == 21 or calculate_score(user_cards) == 21:
        compare(calculate_score(user_cards), calculate_score(cpu_cards),
                cpu_cards, user_cards)
        if play_again():
            blackjack_game()
        else:
            print("Goodbye")
            return

    while calculate_score(user_cards) < 21:
        another_card = input(
            "\nDo you want another card? Type 'y' or 'n': ").lower()
        if another_card == "y":
            user_cards.append(deal_card())
            print(f"User hand: {user_cards}")
            print(f"User score is {calculate_score(user_cards)}")

            if calculate_score(user_cards) == 21:
                break
        else:
            break

    while calculate_score(cpu_cards) < 17 and calculate_score(user_cards) < 21:
        cpu_cards.append(deal_card())

    print("\n=== Final result ===")
    compare(calculate_score(user_cards), calculate_score(cpu_cards), cpu_cards,
            user_cards)

    if play_again():
        blackjack_game()
    else:
        print("Goodbye")


blackjack_game()

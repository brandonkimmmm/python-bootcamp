from random import choice

from art import logo
from replit import clear

hands = {"player": {"cards": [], "score": 0}, "house": {"cards": [], "score": 0}}


def clear_hands():
    hands["player"]["cards"] = []
    hands["player"]["score"] = 0
    hands["house"]["cards"] = []
    hands["house"]["score"] = 0


def display_board(show_house_cards=False):
    if show_house_cards:
        print(
            f"\tYour final hand: {hands['player']['cards']}, final score: {hands['player']['score']}"
        )
        print(
            f"\tComputer's final hand: {hands['house']['cards']}, final score: {hands['house']['score']}"
        )
    else:
        print(
            f"\tYour cards: {hands['player']['cards']}, current score: {hands['player']['score']}"
        )
        print(f"\tComputer's first card: {hands['house']['cards'][0]}")


def calculate_hand_score(hand_owner):
    score = sum(hands[hand_owner]["cards"])

    if score > 21 and 11 in hands[hand_owner]["cards"]:
        ace_index = hands[hand_owner]["cards"].index(11)
        hands[hand_owner]["cards"][ace_index] = 1
        score -= 10
    hands[hand_owner]["score"] = score


def draw_card(hand_owner):
    cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]

    card = choice(cards)
    hands[hand_owner]["cards"].append(card)
    calculate_hand_score(hand_owner)


def get_game_result(is_playing=True):
    player_score = hands["player"]["score"]
    house_score = hands["house"]["score"]

    if not is_playing:
        if house_score > 21:
            return "Opponent went over. You win 😁"
        elif player_score == house_score:
            return "Draw 🙃"
        elif player_score == 21:
            return "Blackjack! You win 😁"
        elif house_score == 21:
            return "Oppenent has Blackjack. You lose 😤"
        elif player_score < house_score:
            return "You lose 😤"
        elif player_score > house_score:
            return "You win 😁"
    else:
        if player_score > 21:
            return "You went over. You lose 😤"
    return None


def hand_owner_can_draw(hand_owner):
    if (hand_owner == "player" and hands["player"]["score"] < 21) or (
        hand_owner == "house" and hands["house"]["score"] < 17
    ):
        return True
    return False


def play_game():
    start_game = input("Do you want to play a game of Blackjack? Type 'y' or 'n': ")

    while start_game == "y":
        clear()
        clear_hands()
        is_player_turn = True

        print(logo)
        draw_card("player")
        draw_card("house")
        draw_card("player")
        draw_card("house")

        display_board()

        if hand_owner_can_draw("player"):
            while is_player_turn:
                draw_player_card = input(
                    "Type 'y' to get another card, type 'n' to pass: "
                )
                if draw_player_card == "y":
                    draw_card("player")
                    if not hand_owner_can_draw("player"):
                        is_player_turn = False
                    else:
                        display_board()
                else:
                    is_player_turn = False

        result = get_game_result()

        if result == None:
            while hand_owner_can_draw("house"):
                draw_card("house")
            result = get_game_result(False)

        display_board(True)
        print(result)

        start_game = input("Do you want to play a game of Blackjack? Type 'y' or 'n': ")


play_game()

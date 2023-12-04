def calculate_card_points(winning_numbers, player_numbers):
    points = 0
    for num in winning_numbers:
        if num in player_numbers:
            points = 1 if points == 0 else points * 2
    return points


def main():
    filename = (
        "/Users/arthur/Documents/GitHub/LeetcodeAdventure/AdventOfCode/day4input.txt"
    )
    total_points = 0

    with open(filename, "r") as file_object:
        for line in file_object:
            _, game_data = line.strip().split(":")
            winning_numbers, player_numbers = game_data.split("|")

            # Convert these numbers from strings to integers
            winning_numbers = [int(n) for n in winning_numbers.split()]
            player_numbers = [int(n) for n in player_numbers.split()]

            # Calculate points for each card
            total_points += calculate_card_points(winning_numbers, player_numbers)

    print(f"Total points: {total_points}")


def count_matches(winning_numbers, player_numbers):
    return sum(1 for num in winning_numbers if num in player_numbers)


def process_cards(cards):
    card_copies = [1] * len(cards)  # Number of copies of each card

    for i in range(len(cards)):
        _, game_data = cards[i].split(":")
        winning_numbers, player_numbers = game_data.split("|")

        winning_numbers = [int(n) for n in winning_numbers.split()]
        player_numbers = [int(n) for n in player_numbers.split()]

        matches = count_matches(winning_numbers, player_numbers)

        for j in range(i + 1, min(i + 1 + matches, len(cards))):
            card_copies[j] += card_copies[i]

    return sum(card_copies)


def main2():
    filename = (
        "/Users/arthur/Documents/GitHub/LeetcodeAdventure/AdventOfCode/day4input.txt"
    )
    cards = []

    with open(filename, "r") as file_object:
        for line in file_object:
            cards.append(line.strip())

    total_scratchcards = process_cards(cards)
    print(f"Total scratchcards: {total_scratchcards}")


if __name__ == "__main__":
    main2()

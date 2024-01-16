from collections import Counter


def classify_hand(hand):
    # Count frequencies of each card and sort
    frequencies = Counter(hand[:-1]).most_common()
    sorted_frequencies = sorted(frequencies, key=lambda x: (-x[1], x[0]))

    # Identify hand type
    if sorted_frequencies[0][1] == 5:
        hand_type = 7  # Five of a kind
    elif sorted_frequencies[0][1] == 4:
        hand_type = 6  # Four of a kind
    elif sorted_frequencies[0][1] == 3:
        if len(sorted_frequencies) > 1 and sorted_frequencies[1][1] == 2:
            hand_type = 5  # Full house
        else:
            hand_type = 3  # Three of a kind
    elif sorted_frequencies[0][1] == 2:
        if len(sorted_frequencies) > 1 and sorted_frequencies[1][1] == 2:
            hand_type = 4  # Two pair
        else:
            hand_type = 2  # One pair
    else:
        hand_type = 1  # High card

    # Return a tuple that includes the hand type and sorted card frequencies for comparison
    return (hand_type,) + tuple((freq, card) for card, freq in sorted_frequencies)


def calculate_winnings(hands):
    # Parse and sort the hands based on their strength
    sorted_hands = sorted(
        [(classify_hand(hand), bid, hand) for hand, bid in hands], reverse=True
    )

    # Calculate winnings
    total_winnings = sum(
        rank * bid for rank, (_, bid, _) in enumerate(sorted_hands, start=1)
    )
    return total_winnings, sorted_hands


def main():
    filename = (
        "/Users/arthur/Documents/GitHub/LeetcodeAdventure/AdventOfCode/day7input.txt"
    )

    with open(filename, "r") as file_object:
        hands = []
        for line in file_object:
            # Assuming each line is in the format "hand bid"
            parts = line.strip().split()
            if len(parts) == 2:
                hand, bid = parts
                hands.append((hand, int(bid)))

    total_winnings, sorted_hands = calculate_winnings(hands)

    print(f"Total Winnings: {total_winnings}")
    for rank, (_, _, hand) in enumerate(sorted_hands, start=1):
        print(f"Rank {rank}: {hand}")


if __name__ == "__main__":
    main()

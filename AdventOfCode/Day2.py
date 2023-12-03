# only 12 red cubes, 13 green cubes, and 14 blue cubes
from itertools import product


def main():
    filename = (
        "/Users/arthur/Documents/GitHub/LeetcodeAdventure/AdventOfCode/day2input.txt"
    )
    File_object = open(filename, "r")
    possible_games = []

    for line in File_object:
        # Split the line into game number and details
        game_number, game_details = line.split(":")

        # Split the details into segments by ';'
        game_segments = game_details.split(";")

        parsed_data = []
        for segment in game_segments:
            # Split each segment into color-number pairs by ','
            color_number_pairs = segment.split(",")

            # Strip spaces and append to parsed_data
            for pair in color_number_pairs:
                parsed_data.append(pair.strip())

        # Summarize data
        color_max = {}
        for item in parsed_data:
            number, color = item.split()
            number = int(number)
            if color not in color_max or color_max[color] < number:
                color_max[color] = number

        print(f" {game_number.strip()}: {parsed_data}")
        print("Color Totals:", color_max)

        if (
            color_max["red"] <= 12
            and color_max["green"] <= 13
            and color_max["blue"] <= 14
        ):
            possible_games.append(game_number.strip())
    print(possible_games)

    answer = sum([int(game.split()[1]) for game in possible_games])
    print(answer)


def mainfindpowermin():
    filename = (
        "/Users/arthur/Documents/GitHub/LeetcodeAdventure/AdventOfCode/day2input.txt"
    )
    with open(filename, "r") as file_object:
        answer = 0

        for line in file_object:
            # Split the line into game number and details
            game_number, game_details = line.split(":")

            # Split the details into segments by ';'
            game_segments = game_details.split(";")

            parsed_data = []
            for segment in game_segments:
                # Split each segment into color-number pairs by ','
                color_number_pairs = segment.split(",")

                # Strip spaces and append to parsed_data
                for pair in color_number_pairs:
                    parsed_data.append(pair.strip())

            # Summarize data
            color_max = {}
            for item in parsed_data:
                number, color = item.split()
                number = int(number)
                if color not in color_max or color_max[color] < number:
                    color_max[color] = number

            # Calculate game_max for each game
            game_max = 1
            for value in color_max.values():
                game_max *= value

            print(f"Game {game_number.strip()}: {parsed_data}")
            print("Maximum cubes needed:", color_max)
            print(f"Product for Game {game_number.strip()}: {game_max}")

            # Accumulate the sum of maximum numbers for each game
            answer += game_max

        print("Final Answer:", answer)


mainfindpowermin()


if __name__ == "__main__":
    mainfindpowermin()

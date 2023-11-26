#'Problem specification for Taylor Problem:'
#'1. only allowed to add two songs'
# 2. the total duration of the two songs we choose is less than 7 minutes  (s1 + s2 < 7)
# 3. Given a List of List, each List contains the song name and duration
# 4. Return every possible combination of songs that satisfy the above two conditions

convert_to_seconds = lambda x: int(x.split(":")[0]) * 60 + int(x.split(":")[1])


def build_hash(album: list[list[str]], maxtime: int):
    hash_table = {}

    for song in album:
        print(song[0], convert_to_seconds(song[1]))
        if convert_to_seconds(song[1]) < maxtime:
            hash_table[song[0]] = convert_to_seconds(song[1])
    return hash_table


def find_songs(album: list[list[str]], maxtime: int):
    result = []
    maxtime = convert_to_seconds(maxtime)
    hash_table = sorted(build_hash(album, maxtime).items(), key=lambda x: x[1])
    print(hash_table, "maxtime: ", maxtime)

    pointer = 0
    pointer2 = 0

    get_complement = lambda x: (maxtime - 1) - int(
        x
    )  # Gets the max size the other song can be
    for _ in range(len(hash_table)):  # O(n)
        if (
            pointer == pointer2 and pointer2 == len(hash_table) - 1
        ):  # Only true if the list is one element long
            break

        while get_complement(hash_table[pointer][1]) > hash_table[pointer2][1]:
            pointer2 += 1
            if (
                get_complement(hash_table[pointer2][1]) < hash_table[pointer][1]
            ):  # if the next song is too long
                pointer2 -= 1
                break

            if (
                pointer2 == len(hash_table) - 1
            ):  # if no complement is found (all songs are too long)
                break
        print(pointer, pointer2)
        for i in range(pointer, pointer2 + 1):
            if i != pointer:
                result.append([hash_table[pointer][0], hash_table[i][0]])
        pointer += 1
        pointer2 = pointer

    return result


if __name__ == "__main__":
    maxtime = "7:00"

    album = [
        ["song1", "1:00"],
        ["song2", "2:00"],
        ["song3", "3:00"],
        ["song4", "4:00"],
        ["song5", "5:00"],
        ["song6", "6:00"],
        ["song7", "7:00"],
        ["song8", "5:00"],
        ["song9", "4:00"],
        ["song10", "8:00"],
    ]

    print(find_songs(album, maxtime))

    # Test scripts:
    album0 = [
        ["Welcome to New York", "3:32"],
        ["Blank Space", "3:51"],
        ["Style", "3:51"],
        ["Out of the Woods", "3:55"],
        ["All You Had to Do Was Stay", "3:13"],
        ["Shake It Off", "3:39"],
        ["I Wish You Would", "3:27"],
        ["Bad Blood", "3:31"],
        ["Wildest Dreams", "3:40"],
        ["How You Get the Girl", "4:07"],
    ]
    print("\n")
    print("\n")
    print("\n")

    print(find_songs(album0, maxtime))

    [
        ("All You Had to Do Was Stay", "Welcome to New York"),
        ("All You Had to Do Was Stay", "Shake It Off"),
        ("All You Had to Do Was Stay", "I Wish You Would"),
        ("All You Had to Do Was Stay", "Bad Blood"),
        ("All You Had to Do Was Stay", "Wildest Dreams"),
        ("I Wish You Would", "Welcome to New York"),
        ("Bad Blood", "I Wish You Would"),
    ]

    album1 = [
        ["Song 1", "0:32"],
        ["Song 2", "4:51"],
        ["Song 3", "2:09"],
        ["Song 4", "6:27"],
    ]

    print(find_songs(album1, maxtime))

    [
        ("Song 1", "Song 2"),
        ("Song 1", "Song 3"),
        ("Song 1", "Song 4"),
    ]

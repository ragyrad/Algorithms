#Kevin and Stuart want to play the 'The Minion Game'.

# Game Rules:
# Both players are given the same string, S.
# Both players have to make substrings using the letters of the string S.

# Stuart has to make words starting with consonants.
# Kevin has to make words starting with vowels.
# The game ends when both players have made all possible substrings.
#
# Scoring
# A player gets +1 point for each occurrence of the substring in the string S

# For Example:
# String = BANANA
# Kevin's vowel beginning word = ANA
# Here, ANA occurs twice in BANANA. Hence, Kevin will get 2 Points.

# Constraints: 0 < len(S) <= 10^6


def my_count(string, substring):
    """Function for counting how many times a substring occurs in a string"""
    result = 0
    while substring in string:
        i = string.index(substring)
        string = string[i + 1:]
        result += 1
    return result


def check_letter(string, letter, i, words, score):
    if letter not in words:
        score += my_count(string, letter)
    words.append(letter)
    substring_len = 2
    while i + substring_len <= len(string):
        substring = string[i:i + substring_len]
        if substring not in words:
            words.append(substring)
            score += my_count(string, substring)
        substring_len += 1
    return words, score


def minion_game(string):
    # FIXME: Need to optimize
    string = string.upper()
    if 0 < len(string) <= 10**6:
        vowels = [*"AEIUO"]
        vowels_words = []
        consonants_words = []
        vowels_score = 0
        consonants_score = 0

        for i, letter in enumerate(string):
            if letter in vowels:
                vowels_words, vowels_score = check_letter(string, letter, i, vowels_words, vowels_score)
            else:
                consonants_words, consonants_score = check_letter(string, letter, i, consonants_words, consonants_score)
        result = ""
        if consonants_score != vowels_score:
            result = f"Stuart {consonants_score}" if consonants_score > vowels_score else f"Kevin {vowels_score}"
        else:
            result = "Draw"
        print(result)
    else:
        raise ValueError("len(string) must be > 0 and <= 10^6")


minion_game("BANANA")
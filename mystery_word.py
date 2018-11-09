play = True
while play:
    play_mystery_word()
    play = input_yn("Do you want to play again?")

def play_mystery_word():
    difficulty = ask_user_for_difficulty
    word = choose_word(difficulty)
    bad_choices = 0
    good_choices = []
    while bad_choices < 8 and not word_guessed(word, good_choices):
        #ask user for input

def word_with_guesses(word, guesses):
    """
    Should print the word using underscores for letters not guessed and the actual letters for letters in guesses.
    """
    output_list = []
    guesses = [letter.lower() for letter in guesses]
    for letter in word:
        if letter in guesses:
            output_list.append(letter.upper())
        else:
            output_list.append("_")

    return " ".join(output_list)

def filter_words_by_length(wordlist, min, max):
    return [word for word in wordlist if len(word) in range(min, max +1)]

def easy_words(wordlist):
    """
    Given a list of words, return just the ones of length 4-6.
    """
    return [word for word in wordlist if len(word) in range(4, 7)]

def medium_words(wordlist):
    """
    Given a list of words, return just the ones of length 6-8.
    """
    return [word for word in wordlist if len(word) in range(6, 9)]

def hard_words(wordlist):
    """
    Given a list of words, return just the ones of length 8+
    """
    return [word for word in wordlist if len(word) in range(8, 20)]


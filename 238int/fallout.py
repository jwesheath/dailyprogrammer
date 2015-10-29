import random
import re


def check(guess, correct_word):
    count = 0
    for i in range(len(guess)):
        if guess[i] == correct_word[i]:
            count += 1
    return count


def load_word_list(word_len):
    with open('/usr/share/dict/words') as infile:
        words = infile.read().splitlines()
    words = [word for word in words if re.fullmatch(r'[A-Za-z0-9]+', word)]
    word_choices = random.sample(list(filter(lambda x: len(x) == word_len, words)), word_len)
    word_choices = [word.upper() for word in word_choices]
    return word_choices


def main():
    diff_to_len = {'1': 4, '2': 8, '3': 11, '4': 13, '5': 15}
    word_len = diff_to_len[input('Difficulty (1-5)?')]
    word_choices = load_word_list(word_len)
    correct_word = random.choice(word_choices)
    guesses = 4
    print('\n'.join(word_choices))
    while guesses:
        guess = input('Guess (' + str(guesses) + ' left)?').upper()
        if guess not in word_choices:
            print('Illegal guess')
            continue
        guesses -= 1
        num_correct = check(guess, correct_word)
        print(str(num_correct) + '/' + str(word_len) + ' correct')
        if num_correct == word_len:
            print('You win!')
            break
        if guesses == 0:
            print('You lose!')
            break

if __name__ == '__main__':
    main()

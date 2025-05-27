import random
a = ['asim','hello','python','java']
word = random.choice(a)
word_letter = set(word)
guess_letter = set()
attempt = 6
print('welcome to Hangman!')
print('_ '*len(word))

while attempt>0 and word_letter:
    print('Gussed letter : ', ' '.join(sorted(guess_letter)))
    guess = input('guess a letter : ').lower()
    
    if len(guess) != 1 or not guess.isalpha():
        print('❗plz enter a single or valid letter')
        continue

    if guess in guess_letter:
        print('already guessed')
        continue    

    guess_letter.add(guess)

    if guess in word_letter:
        word_letter.remove(guess)
        print('Good guess!')
    else:
        attempt -=1
        print('wrong guess!')

    current_display = [letter if letter in guess_letter else "_" for letter in word]
    print(' '.join(current_display))

if not word_letter:
    print(f"\n🎉 Congratulations! You guessed the word: {word}")
else:
    print(f"\n💀 Out of attempts! The word was: {word}")


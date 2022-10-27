import pandas

data = pandas.read_csv('nato_phonetic_alphabet.csv')
data = {row.letter: row.code for (index, row) in data.iterrows()}


def start():
    word = input("Enter name: ").upper()
    try:
        output = [data[letter] for letter in word]
        print(output)

    except KeyError:
        print('Sorry, only letters in the alphabet please.')
        start()


start()

import pandas
data_dict = pandas.read_csv("../python-projects/PROJECT-26/nato_phonetic_alphabet.csv")
# print(type(data_dict))
new_dict = {row.letter: row.code for (index, row) in data_dict.iterrows()}
# print(new_dict)

def generate_phonetic():
    user_input = input("Enter your name:").upper()
    try:
        nato_list = [new_dict[letter] for letter in user_input]
    except KeyError:
        print("Sorry, only letters in the alphabet please.")
        generate_phonetic()
    else:
        print(nato_list)
generate_phonetic()
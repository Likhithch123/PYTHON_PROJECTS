import pandas
data_dict = pandas.read_csv("nato_phonetic_alphabet.csv")
# print(type(data_dict))
new_dict = {row.letter: row.code for (index, row) in data_dict.iterrows()}
# print(new_dict)
user_input = input("Enter your name:").upper()
nato_list = [new_dict[letter] for letter in user_input]
print(nato_list)

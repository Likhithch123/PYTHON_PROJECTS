with open("./Input/Names/invited_names.txt") as names_file:
    names_list=names_file.readlines()

with open("./Input/Letter/starting_letter.txt") as letter_file:
    letter_format=letter_file.read()

for name in names_list:
    with open(f"letter_for_{name.strip()}.txt","w") as letters:
        new_letter=letter_format.replace("[name]",f"{name.strip()}")
        letters.write(new_letter)
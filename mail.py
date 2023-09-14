FIX_NAME = "[name]"



# Opening a text file 
with open("./names.txt") as names_file:
    names = names_file.readlines() # puting the text content in a list using the 'readlines' methods



with open("./Letters/letter.txt") as letter_file:
    letter_contents = letter_file.read() # Saving the contents of the letter.txt file in the variable letter_contents
    for name in names:
        stripped_name = name.strip() # strip to help remove the spacing and new lines in the list 
        letter_update = letter_contents.replace(FIX_NAME, stripped_name) # replacing the "[name]" in the default letter with an actual name from the names.txt
        with open(f"./Letters/ReadyLetter/letter_for_{stripped_name}.txt", mode="w") as complete_letter: # open a file and save it with each person's name.
            complete_letter.write(letter_update) # write the new updates made to file
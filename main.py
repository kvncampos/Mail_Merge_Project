#TODO: Create a letter using starting_letter.txt 
#for each name in invited_names.txt
#Replace the [name] placeholder with the actual name.
#Save the letters in the folder "ReadyToSend".

#Hint1: This method will help you: https://www.w3schools.com/python/ref_file_readlines.asp
    #Hint2: This method will also help you: https://www.w3schools.com/python/ref_string_replace.asp
        #Hint3: THis method will help you: https://www.w3schools.com/python/ref_string_strip.asp


# Open the invited_names.txt and store it in a list
with open("Input/Names/invited_names.txt") as r:
    temp_guest_list = r.read().splitlines()
    guest_list = []
    for guest in temp_guest_list:
        guest_list.append(guest)

# Open the starting_letter.txt as a template, replace placeholder name with each person
# in the NEW guest_list and Save each invite to ReadyToSend Folder
with open("Input/Letters/starting_letter.txt") as r:
    letter_template = r.read()
    for name in guest_list:
        new_letter = letter_template.replace("[name]", name)
        with open(f"Output/ReadyToSend/{name}", "w") as person:
            person.write(new_letter)

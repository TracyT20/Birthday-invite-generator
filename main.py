#TODO: Create a letter using starting_letter.txt
with open("./Input/Letters/starting_letter.txt","r") as letter:
    text=letter.read()


# Extract each name in invited_names.txt
with open("./Input/Names/invited_names.txt","r") as names:
    guests=names.read()
guest_list=guests.split("\n")

#for each name in invited_names.txt
#Replace the [name] placeholder with the actual name and Save the letters in the folder "ReadyToSend".
for guest in guest_list:
    new_letter=text.replace("[name]",guest)
    with open(f"./Output/ReadyToSend/letter_for_{guest}.txt",
              "w") as f:
        f.write(new_letter)

#Hint1: This method will help you: https://www.w3schools.com/python/ref_file_readlines.asp
    #Hint2: This method will also help you: https://www.w3schools.com/python/ref_string_replace.asp
        #Hint3: THis method will help you: https://www.w3schools.com/python/ref_string_strip.asp
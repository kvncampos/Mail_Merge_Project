# Letter Generation Script
This Python script generates personalized letters by replacing a placeholder in a template with actual names from a list. The letters are then saved in the "ReadyToSend" folder.

# Prerequisites
Before running the script, ensure that you have the following files in the specified directories:

Input/Names/invited_names.txt: This file should contain a list of names, with each name on a separate line.

Input/Letters/starting_letter.txt: This file should serve as a template for the generated letters. It should contain the placeholder "[name]", which will be replaced with each person's name.

# Usage
Clone or download the repository to your local machine.

Navigate to the project directory.

Install any necessary dependencies.

Place the names of the intended recipients in the Input/Names/invited_names.txt file, with each name on a separate line.

Customize the contents of the letter by modifying the Input/Letters/starting_letter.txt file. Replace the placeholder "[name]" with the desired text.

Run the script using the following command:

Copy code
python generate_letters.py
The generated letters will be saved in the Output/ReadyToSend folder. Each letter will be named after the respective recipient.

# Acknowledgements
w3schools - Python File readlines() method
w3schools - Python String replace() method
w3schools - Python String strip() method
Feel free to customize the script and adapt it to your specific needs!

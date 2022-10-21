# Shardkiller

In an attempt to help solve the FF:06:B5 mystery within Cyberpunk 2077, this program was created using Python (3.0+) to analyze "Shards", 
which are in-game text entries of lore, scattered around the game's map. The current functionality is limited, and imperfect, but serves
as an effective tool in quickly accessing these data entries, and breaking them down all within a single program.

Please keep in mind that there is no GUI for this program, and it is operated through a CLI.

# Usage

You do not need to understand Python to use this program; however, you will need Python installed on your machine. You can download [here](https://www.python.org/downloads/) if you do not. As previously stated, it is operated through a CLI with a basic menu navigated with numeric inputs. Bad inputs should not crash the program, if they do, please report it in the issues section. The intended behavior when a bad input is entered is to send the user back to the main menu.

# Dependencies

The only dependency within the program is [PySpellchecker](https://pypi.org/project/pyspellchecker/) which is used for finding misspelled words that are not
notated with a [sic], which represents when the text is true to it's source material and purposefully misspelled. If you plan on forking this program, I suggest reading the 
documentation and installing this module.

# Source

The Shards in this program are all sourced from the [Cyberpunk 2077 Wiki](https://cyberpunk.fandom.com/wiki/Cyberpunk_2077_Shards). 

# Adding Categories

To add a new category, the process is admittedly hacky, but easy to implement with an entry level understanding of Python. 

Assuming you have already created a folder with text files inside of it and placed it in the folder containing the program, the next steps are as follows:

Locate the **"OpenMenu"** function and copy any of the **"elif catChoice ="** statements from top to the bottom of the **"if relAndPhilCommand ="** statement.
You will then paste it below the bottom-most **"elif catChoice ="** statment and change the **"currentPath ="** in each **elif catChoice** to the name of the new folder/category
you have added. Lastly, you will start the program and change each of the **"elif catChoice ="** statements to match the numbered list of categories shown in the output.
Restart the program, and you should now be able to perform functions on text files in the new category.


# Licensing
This program is open source and available to anyone whon wishes to fork the repo and improve on it.


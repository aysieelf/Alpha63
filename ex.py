The dictionary will support the following functionality:
- adding a new word to the dictionary - updating existing word's meaning - searching for a word in the dictionary

1. Console Dictionary Module
must be in a separate file, for example console_dictionary.py
must store words along with their meaning
you can keep the word in a two-dimensional list; example: python dictionary = [ ['word', 'meaning of the word'], ['hello', 'hello is a common greeting'], ['bye', 'bye is not a common greeting'] ]
must define the following functions:
add_word(word, meaning) - creates a new entry in the dictionary
update_meaning(word, meaning) - replaces the word in the dictionary with a new meaning
find_word(word) - returns the meaning of the word or None, if no such word
2. Instruction Runner Module
file: instruction_runner.py
must import the functions defined in the console-dictionary module
must define a function execute_instruction(line), handling several possible instructions
parse the input and execute one of the possible console-dictionary functions:
add:word:meaning for word - uses the add_word imported function
returns Added word msg
update:word:new meaning for word - uses the update_meaning imported function
returns Meaning updated msg
find:keyword - uses the find_word imported function
returns No such word or word: "meaning of word" message
3. Main module
file: main.py
imports the instruction_runner module
reads input until it reaches the exit instruction
passes the line to the function defined by the instruction_runner module
Sample input
add:keyword:word with special meaning in a language
add:while:keyword that repeats code
update:while:keyword that repeats code until condition is true
find:keyword
find:while
find:for
exit
Sample output
Added word
Added word
Meaning updated
keyword: "word with special meaning in a language"
while: "keyword that repeats code until condition is true"
No such word

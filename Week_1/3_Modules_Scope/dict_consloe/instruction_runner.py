import console_dictionary

def execute_instruction(line):
    if ':' in line:
        line = line.split(':')
        if line[0] == "add":
            console_dictionary.add_word(line[1], line[2])
            print("Added word")
        elif line[0] == "update":
            console_dictionary.update_meaning(line[1], line[2])
            print("Meaning updated")
        elif line[0] == "find":
            msg = console_dictionary.find_word(line[1])
            if msg is None:
                print("No such word")
            else:
                print(f"{line[1]}: {msg}")


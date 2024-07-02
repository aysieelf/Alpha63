import instruction_runner


while True:
    line = input()
    if line == "exit":
        break
    else:
        instruction_runner.execute_instruction(line)

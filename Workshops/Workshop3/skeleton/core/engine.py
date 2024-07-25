
from core.command_factory import CommandFactory


class Engine:
    def __init__(self, factory: CommandFactory):
        self._command_factory = factory

    def start(self) -> None:
        all_output_strings = []
        while True:
            input_line = input()
            if input_line.lower() == "end":
                break

            command = self._command_factory.create(input_line)
            all_output_strings.append(command.execute())

        print('\n'.join(all_output_strings))
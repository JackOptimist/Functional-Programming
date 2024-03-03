from abc import ABC, abstractmethod

class Command(ABC):
    @abstractmethod
    def execute(self):
        pass
    
    @abstractmethod
    def undo(self):
        pass

class AddCommand(Command):
    def __init__(self, receiver, value):
        self.receiver = receiver
        self.value = value
    
    def execute(self):
        self.receiver.add(self.value)
    
    def undo(self):
        self.receiver.remove(self.value)

class Receiver:
    def __init__(self):
        self.data = []
    
    def add(self, value):
        self.data.append(value)
        print(f"Added: {value}")
    
    def remove(self, value):
        if value in self.data:
            self.data.remove(value)
            print(f"Removed: {value}")
        else:
            print(f"Doesn't contain: {value}")
    
    def display(self):
        print(f"Current list: {self.data}")

class Invoker:
    def __init__(self):
        self.history = []
    
    def execute_command(self, command):
        command.execute()
        self.history.append(command)
    
    def undo_last_command(self):
        if self.history:
            last_command = self.history.pop()
            last_command.undo()

receiver = Receiver()
add_command1 = AddCommand(receiver, 10)
add_command2 = AddCommand(receiver, 20)

invoker = Invoker()
invoker.execute_command(add_command1)
invoker.execute_command(add_command2)
receiver.display()

invoker.undo_last_command()
receiver.display()

import os
import errno
import time


class TaskProvider:
    bufferSize = 100

    def getTask(self):

        fifo_name = 'mypipe'

        if not os.path.exists(fifo_name):
            os.mkfifo(fifo_name)
        pipe = os.open(fifo_name, os.O_RDONLY | os.O_NONBLOCK)
        input = os.read(pipe, self.bufferSize)

        if input:
            try:
                name, explanation, position = input.decode().split()
                task = Task(name, explanation)
                tasks.insert(int(position), task)
                if int(position) <= last_instruction:
                    next(gen)
                return tasks[next(gen)]
            except ValueError:
                return command_template(input)
        else:
            return tasks[next(gen)]


class Task:
    def __init__(self, name, explanation):
        self.name = name
        self.explanation = explanation

    def __repr__(self):
        return f"{self.name}, {self.explanation}"


def index_generator():
    global last_instruction
    i = 0
    while i <= len(tasks):
        if i == len(tasks):
            i = 0
            last_instruction = 0
        last_instruction += 1
        yield i
        i += 1


def command_template(command):
    command_list = command.decode().split()
    if command_list[0] == 'break':
        return -1

    if len(command_list) != 3:
        return 'Suppose to be 3 parts in command !'

    try:
        checker = int(command_list[-1])
    except ValueError:
        return 'Last command element is not int!'


tasks = []

task1 = Task('Instruction1', 'grabbing')
task2 = Task('Instruction2', 'carving')
task3 = Task('Instruction3', 'rotating')
task4 = Task('Instruction4', 'pushing')

tasks.insert(1, task1)
tasks.insert(2, task2)
tasks.insert(3, task3)
tasks.insert(4, task4)

last_instruction = -1
gen = index_generator()

if __name__ == '__main__':
    some = TaskProvider()
    while True:
        print(some.getTask())
        time.sleep(1)

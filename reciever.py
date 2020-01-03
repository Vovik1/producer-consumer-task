from TaskProvider import TaskProvider
from time import sleep

task_provider = TaskProvider()


class Robot:

    @staticmethod
    def run():
        while True:
            task = task_provider.getTask()
            if task == -1:
                break
            print(f" Doing {task} ")
            sleep(1)


robot = Robot()
robot.run()

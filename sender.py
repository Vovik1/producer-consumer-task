import os


def task_creator():

    fifo_name = 'mypipe'

    if not os.path.exists(fifo_name):
        os.mkfifo(fifo_name)

    while True:
        inp = input('>>')
        if len(inp) < 1:
            break
        bts = inp.encode()
        pipe = os.open(fifo_name, os.O_WRONLY)
        os.write(pipe, bts)
        os.close(pipe)


if __name__ == '__main__':
    task_creator()
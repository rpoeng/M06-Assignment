#15.1 Use "multiprocessing" to create three seperate process. Make each one wait a random number of seconds between
# zero and one, print the current time, and then exit.
import multiprocessing

def now(seconds): #Function to sleep after a certain amount of time.
    from datetime import datetime
    from time import sleep
    sleep(seconds)
    print('wait', seconds, 'seconds, time is', datetime.utcnow())


if __name__ == '__main__':
    import random
    for n in range(3): #Range for three seperate processes.
        seconds = random.random()
        proc = multiprocessing.Process(target=now, args=(seconds,)) #starts new process and calls "now" function
        proc.start()


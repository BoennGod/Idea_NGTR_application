import sys
import random


def A():
    for line in sys.stdin:
        command = line.rstrip()
        if command == 'Hi':
            print("Hi")
        elif command == 'GetRandom':
            print(random.randint(1, 100))
        elif command == 'Shutdown':
            print("ok, shutting down")
            break
    return 0


if __name__ == "__main__":
    A()


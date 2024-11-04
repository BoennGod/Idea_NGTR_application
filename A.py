import sys
import random


def A():
    for line in sys.stdin:
        command = line.rstrip()
        if command == 'Hi':
            print("Hi", flush=True)
        elif command == 'GetRandom':
            print(random.randint(1, 100), flush=True)
        elif command == 'Shutdown':
            print("ok, shutting down", flush=True)
            break
    return 0


if __name__ == "__main__":
    A()


import subprocess


def B():
    process = subprocess.Popen(
        ["python3", "A.py"],
        stdin=subprocess.PIPE,
        stdout=subprocess.PIPE,
        universal_newlines=True,
        bufsize = 1
    )

    def send_command(command):
        process.stdin.write(command + "\n")
        process.stdin.flush()
        return process.stdout.readline().strip()

    response = send_command("Hi")
    if response != "Hi":
        print("oh, A did not reply to my Hi :(")
        process.terminate()
        return

    print("A responded to my hi :)")

    numbers = []
    for i in range(100):
        response = send_command("GetRandom")
        try:
            numbers.append(int(response))
        except ValueError:
            print("Error: Received a non-integer response from Program A.")
            process.terminate()
            return

    send_command("Shutdown")
    process.wait()

    numbers.sort()

    median = (numbers[49] + numbers[50]) / 2
    average = sum(numbers)/100

    print(numbers)
    print(median)
    print(average)
    return 0


if __name__ == "__main__":
    B()

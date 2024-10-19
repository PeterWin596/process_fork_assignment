import os
import time

def process_a():
    print(f"10 I AM PROCESS A whose id is : {os.getpid()}")

def process_b():
    print(f"20 I AM PROCESS B whose id is : {os.getpid()}")

def process_c():
    print(f"30 I AM PROCESS C whose id is : {os.getpid()}")

if __name__ == "__main__":
    # Parent process (Process A)
    process_a()

    # Fork to create Process B
    pid_b = os.fork()

    if pid_b == 0:
        # This is Process B (child process)
        process_b()
        os._exit(0)
    else:
        # Parent process (Process A) waits for Process B to finish
        os.wait()

        # Fork to create Process C
        pid_c = os.fork()

        if pid_c == 0:
            # This is Process C (child process)
            process_c()
            os._exit(0)
        else:
            # Parent process waits for Process C to finish
            os.wait()

    # Parent process (Process A) finishes
    print("Good Bye World, I am Done!!")

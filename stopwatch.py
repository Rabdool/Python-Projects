import time

def format_time(seconds):
    mins = int(seconds // 60)
    secs = int(seconds % 60)
    return f"{mins:02d}:{secs:02d}"

def stopwatch():
    print("⏱️ Stopwatch Controls:")
    print("s = Start, p = Pause, r = Reset, q = Quit")

    running = False
    start_time = 0
    elapsed = 0

    while True:
        command = input("Command (s/p/r/q): ").lower()

        if command == 's':
            if not running:
                start_time = time.time() - elapsed
                running = True
                print("Stopwatch started.")
            else:
                print("Already running.")

        elif command == 'p':
            if running:
                elapsed = time.time() - start_time
                running = False
                print(f"Paused at {format_time(elapsed)}.")
            else:
                print("Stopwatch is not running.")

        elif command == 'r':
            elapsed = 0
            start_time = time.time()
            print("Stopwatch reset.")

        elif command == 'q':
            if running:
                elapsed = time.time() - start_time
            print(f"⏹️ Final Time: {format_time(elapsed)}")
            print("Goodbye!")
            break

        else:
            print("Invalid command. Use s, p, r, or q.")

        if running:
            current = time.time() - start_time
            print(f"⏳ Elapsed: {format_time(current)}")

if __name__ == "__main__":
    stopwatch()

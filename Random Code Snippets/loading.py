import time
import sys

def loading_bar(iterations, length=40):
    for i in range(iterations):
        percent = (i + 1) / iterations
        filled_length = int(length * percent)
        bar = '#' * filled_length + '-' * (length - filled_length)
        sys.stdout.write(f'\r[{bar}] {percent*100:.1f}%')
        sys.stdout.flush()
        time.sleep(0.1)  # Simulate work

    sys.stdout.write('\r' + ' ' * (length + 10) + '\r')
    sys.stdout.flush()
    # sys.stdout.write('\n')  # Newline at the end

if __name__ == "__main__":
    loading_bar(100)
import sys

class bcolors:
    HEADER = '\033[95m'
    OKBLUE = '\033[94m'
    OKCYAN = '\033[96m'
    OKGREEN = '\033[92m'
    WARNING = '\033[93m'
    FAIL = '\033[91m'
    ENDC = '\033[0m'
    BOLD = '\033[1m'
    UNDERLINE = '\033[4m'

_spinner_state = 0
_spinner_items = list('▙▛▜▟')
_len = len(_spinner_items)

# spinner - Just a simple spinner for the console
def spinner():
    global _spinner_state
    # spinner = ['◐' ,'◓', '◑', '◒']
    _spinner_state = (_spinner_state + 1) % _len
    return _spinner_items[_spinner_state]

# demo
if __name__ == "__main__":
    import time
    for i in range(100):
        print(f" Spinner test {spinner()}", end='\r', file=sys.stderr)
        time.sleep(0.1)
    print("\nDone!")

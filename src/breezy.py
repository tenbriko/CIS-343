import sys
from scanner import Scanner


def run(source):
    scanner = Scanner(source)
    tokens = scanner.scan_tokens()

    for token in tokens:
        print(token)


def run_file(path):
    with open(path, "r") as file:
        source = file.read()

    run(source)


def run_prompt():
    while True:
        try:
            line = input("> ")
            run(line)
        except KeyboardInterrupt:
            print()
            break


def main():
    if len(sys.argv) > 2:
        print("Usage: breezy [script]")
    elif len(sys.argv) == 2:
        run_file(sys.argv[1])
    else:
        run_prompt()


if __name__ == "__main__":
    main()
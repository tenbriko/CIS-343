import sys
from scanner import Scanner
from parser import Parser, ParseError
from ast_printer import AstPrinter


def run(source):
    scanner = Scanner(source)
    tokens = scanner.scan_tokens()
    
    if scanner.had_error:
        return

    try:
        parser = Parser(tokens)
        expression = parser.parse()

        printer = AstPrinter()
        print(printer.print(expression))

    except ParseError as error:
        print(error)


def run_file(path):
    with open(path, "r") as file:
        source = file.read()

    run(source)


def run_prompt():
    while True:
        try:
            line = input("> ")
            run(line)
        except (KeyboardInterrupt, EOFError):
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
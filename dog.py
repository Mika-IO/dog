import sys
from pygments import highlight
from pygments.lexers import get_lexer_for_filename
from pygments.formatters import TerminalFormatter


def main():
    if len(sys.argv) != 2:
        print("Use: dog <file_name>")
        sys.exit(1)

    filename = sys.argv[1]

    try:
        with open(filename, "r") as file:
            content = file.read()
            lexer = get_lexer_for_filename(filename)
            highlighted = highlight(content, lexer, TerminalFormatter())
            print(highlighted)
    except Exception as e:
        print(f"Error to open: {e}")
        sys.exit(1)


if __name__ == "__main__":
    main()

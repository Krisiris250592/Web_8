from models import Author, Quote
from connect import connect


def parsing(string: str):
    command, *args = string.split(":")
    return command, args


def find_quotes_by_author(args: list):
    author_name = args[0]
    author = Author.objects(fullname=author_name.strip()).first()
    quotes = Quote.objects(author=author).all()
    result = "".join(set([f"{quote.quote}\n" for quote in quotes]))
    return result


def find_quotes_by_tag(args: list):
    tag = args[0]
    quotes = Quote.objects(tags=tag).all()
    result = "".join(set([f"{quote.quote}\n" for quote in quotes]))
    return result


def find_quotes_by_tags(args: list):
    tags = args[0].split(",")
    quotes = Quote.objects(tags__in=tags).all()
    result = "".join(set([f"{quote.quote}\n" for quote in quotes]))
    return result


def main():
    while True:
        input_str = input("Please enter <command>:<text> ")
        command, args = parsing(input_str)
        if command in ("close", "exit"):
            break
        if command == "name":
            print(find_quotes_by_author(args))
        elif command == "tag":
            print(find_quotes_by_tag(args))
        elif command == "tags":
            print(find_quotes_by_tags(args))
        else:
            print("invalid comment")


if __name__ == "__main__":
    main()

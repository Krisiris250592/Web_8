import json
from models import Author, Quote
from connect import connect


def add_author(path: str):
    with open(path, "r", encoding="utf-8") as file:
        authors = json.load(file)
    for author in authors:
        fullname = author.get('fullname')
        born_date = author.get('born_date')
        born_location = author.get('born_location')
        record = Author(fullname=fullname, born_date=born_date, born_location=born_location, description=description)
        record.save()


def add_quotes(path: str):
    with open(path, "r", encoding="utf-8") as file:
        quotes = json.load(file)
    for quote in quotes:
        author_name = quote.get("author")
        author = Author.objects(fullname=author_name).first()
        tags = quote.get("tags")
        quote_ = quote.get("quote")
        record = Quote(author=author, tags=tags, quote=quote_)
        record.save()


if __name__ == "__main__":
    add_quotes("quotes.json")
    add_author("authors.json")

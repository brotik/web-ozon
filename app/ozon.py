import uuid


def create_book(title, author, tags):
    tags = convert_tags_from_str_to_set(tags)

    return {
        'title': title,
        'author': author,
        'tags': tags
    }


def convert_tags_from_str_to_set(tags):
    if not tags:
        return set()

    tags = set(map(str.strip, tags.split(',')))
    return tags


def add_book(container, book):
    copy = container[:]
    copy.append(book)
    return copy


def search_books(container, search):  # search - строка поиска
    search_lowercased = search.strip().lower()
    result = []
    for book in container:
        if search_lowercased in book['title'].lower():
            result.append(book)
            continue

        if search_lowercased in book['author'].lower():
            result.append(book)
            continue

        if search_lowercased in book['tags']:
            result.append(book)
            continue

    return result


def search_book_by_id(container, book_id):
    for book in container:
        if book['id'] == book_id:
            return book


def remove_book_by_id(container, book_id):
    result = []
    for book in container:
        if book['id'] != book_id:
            result.append(book)
    return result


def create_empty_book():
    return {
        'id': 'new',
        'title': '',
        'author': '',
    }


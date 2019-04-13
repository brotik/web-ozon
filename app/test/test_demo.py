from app.ozon import create_book, add_book, search_books
import uuid


def test_create_book():
    data = {
        'id': str(uuid.uuid4()),
        'title': 'Война и мир',
        'author': 'Толстой',
    }
    result = {'title': 'Война и мир', 'author': 'Толстой'}
    assert 'id' in data
    assert data['title'] == result['title']
    assert data['author'] == result['author']


def test_add_book():
    container = []
    wp = create_book('Война и мир', 'Толстой', '#война, #любовь, #толстой')
    expected = add_book(container, wp)
    result = add_book(container, wp)

    assert expected == result


def test_search_books():
    books = [{'title': 'Война и мир', 'author': 'Толстой', 'tags': {'#война', '#любовь', '#толстой'}},
             {'title': 'Анна каренина', 'author': 'Толстой', 'tags': {'#поезд', '#любовь', '#толстой'}}
             ]
    search = 'Война и мир'
    expected = search_books(books, search)
    result = search_books(books, search)

    assert expected == result




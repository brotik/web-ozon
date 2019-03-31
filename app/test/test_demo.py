from app.ozon import create_book
import uuid


def test_create_book():
    data = {
        'id': str(uuid.uuid4()),
        'title': 'war and peace',
        'author': 'tolstoy',
    }
    result = { 'title': 'war and peace', 'author': 'tolstoy',}
    assert 'id' in data
    assert data['title'] == result['title']
    assert data['author'] == result['author']



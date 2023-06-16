from flask import Flask, jsonify, request

app = Flask(__name__)

books = [
    {
        'id': 1,
        'title': 'The Great Gatsby',
        'author': 'F. Scott Fitzgerald',
        'published': 1925
    },
    {
        'id': 2,
        'title': 'The Kill',
        'author': 'Lee',
        'published': 1960
    },
    {
        'id': 3,
        'title': '1985',
        'author': 'George',
        'published': 1941
    }
]

@app.route('/books', methods=['GET'])
def get_books():
    return jsonify(books)


@app.route('/books', methods=['POST'])
def create_book():
    book = {
        'id': max([book['id'] for book in books]) + 1,
        'title': request.json['title'],
        'author': request.json['author'],
        'published': request.json['published']
    }
    books.append(book)
    return jsonify(book), 201

if __name__ == '__main__':
    app.run(debug=True, host='127.0.0.1', port = 5000)

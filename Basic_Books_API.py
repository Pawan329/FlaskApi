from flask import Flask, jsonify, request

app = Flask(__name__)

# Using list intead of database
books_db = [
    {
        "name": "Alchemist",
        "price": 250,
        "author": "Paulo Coelho"
    },
    {
        "name": "Love side by side",
        "price": 150,
        "author": "Partha sarthi sen sharma"
    }
]

# Return all books GET METHOD
@app.route("/AllBooks", methods=["GET"])
def all_books():
    return jsonify({"AllBooks": books_db})


# retrieve a single book
@app.route("/find/<string:name>")
def get_book(name):
    for book in books_db:
        if book['name'] == name:
            return jsonify({"your book": book})

    return jsonify({"message":"your book not found"})


# add a book using post method POST METHOD
@app.route("/addbook", methods=["POST"])
def add_book():
    new_book = request.get_json()
    books_db.append(new_book)

    return jsonify({"message": "New book added successfully!!"})


# Default api
@app.route("/", methods=["GET"])
def blank():
    return jsonify({"message": "This is a home page"},
    {"Available APIs":["/AllBooks","/find","/addbook"]})


app.run(debug=True, port=5000)

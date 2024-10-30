from flask import jsonify, request
from models.BookModel import Book
from models.CategoryModel import Category
from config import db


def get_all_books():
    books = Book.query.all()
    books_with_categories = []

    for book in books:
        category = Category.query.get(book.category_id)
        book_with_category = {
            "id": book.id,
            "title": book.title,
            "author": book.author,
            "year": book.year,
            "category": category.name if category else "No Category",
        }
        books_with_categories.append(book_with_category)

    return jsonify(books_with_categories)


def get_book_by_id(book_id):
    book = Book.query.get(book_id)
    if not book:
        return jsonify({"status": "error", "message": "Book not found"}), 404

    category = Category.query.get(book.category_id)
    book_data = {
        "id": book.id,
        "title": book.title,
        "author": book.author,
        "year": book.year,
        "category": category.name if category else "No Category",
    }

    return jsonify(book_data)


def add_book():
    new_book_data = request.get_json()
    new_book = Book(
        title=new_book_data["title"],
        author=new_book_data["author"],
        year=new_book_data["year"],
        category_id=new_book_data["category_id"],
    )

    db.session.add(new_book)
    db.session.commit()
    return (
        jsonify({"message": "Book added successfully", "book": new_book.to_dict()}),
        201,
    )


def update_book(book_id):
    book = Book.query.get(book_id)
    if not book:
        return jsonify({"status": "error", "message": "Book not found"}), 404

    updated_book_data = request.get_json()
    book.title = updated_book_data.get("title", book.title)
    book.author = updated_book_data.get("author", book.author)
    book.year = updated_book_data.get("year", book.year)
    book.category_id = updated_book_data.get("category_id", book.category_id)

    db.session.commit()
    return jsonify({"message": "Book updated successfully", "book": book.to_dict()})


def patch_book(book_id):
    book = Book.query.get(book_id)
    if not book:
        return jsonify({"status": "error", "message": "Book not found"}), 404

    updated_book_data = request.get_json()
    if "title" in updated_book_data:
        book.title = updated_book_data["title"]
    if "author" in updated_book_data:
        book.author = updated_book_data["author"]
    if "year" in updated_book_data:
        book.year = updated_book_data["year"]
    if "category_id" in updated_book_data:
        category = Category.query.get(updated_book_data["category_id"])
        if category:
            book.category_id = updated_book_data["category_id"]
        else:
            return jsonify({"status": "error", "message": "Category not found"}), 404

    db.session.commit()
    return jsonify({"message": "Book patched successfully", "book": book.to_dict()})


def delete_book(book_id):
    book = Book.query.get(book_id)
    if not book:
        return jsonify({"status": "error", "message": "Book not found"}), 404

    db.session.delete(book)
    db.session.commit()
    return jsonify({"message": "Book deleted successfully"})

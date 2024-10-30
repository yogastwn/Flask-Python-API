from flask import Blueprint
from controllers.BookController import *

book_bp = Blueprint("book_bp", __name__)

book_bp.route("/api/books", methods=["GET"])(get_all_books)
book_bp.route("/api/books", methods=["POST"])(add_book)
book_bp.route("/api/books/<int:book_id>", methods=["GET"])(get_book_by_id)
book_bp.route("/api/books/<int:book_id>", methods=["PUT"])(update_book)
book_bp.route("/api/books/<int:book_id>", methods=["PATCH"])(patch_book)
book_bp.route("/api/books/<int:book_id>", methods=["DELETE"])(delete_book)

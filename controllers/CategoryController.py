from flask import jsonify, request
from models.CategoryModel import Category
from config import db


def get_all_categories():
    categories = Category.query.all()
    return jsonify([category.to_dict() for category in categories])


def get_category_by_id(category_id):
    category = Category.query.get(category_id)
    if not category:
        return jsonify({"status": "error", "message": "Category not found"}), 404
    return jsonify(category.to_dict())


def add_category():
    new_category_data = request.get_json()
    new_category = Category(name=new_category_data["name"])
    db.session.add(new_category)
    db.session.commit()
    return (
        jsonify(
            {
                "message": "Category added successfully",
                "category": new_category.to_dict(),
            }
        ),
        201,
    )


def update_category(category_id):
    category = Category.query.get(category_id)
    if not category:
        return jsonify({"status": "error", "message": "Category not found"}), 404
    updated_category_data = request.get_json()
    category.name = updated_category_data.get("name", category.name)
    db.session.commit()
    return jsonify(
        {"message": "Category updated successfully", "category": category.to_dict()}
    )


def delete_category(category_id):
    category = Category.query.get(category_id)
    if not category:
        return jsonify({"status": "error", "message": "Category not found"}), 404
    db.session.delete(category)
    db.session.commit()
    return jsonify({"message": "Category deleted successfully"})

from flask import Blueprint
from controllers.CategoryController import *


category_bp = Blueprint("category_bp", __name__)


category_bp.route("/api/category", methods=["GET"])(get_all_categories)
category_bp.route("/api/category", methods=["POST"])(add_category)
category_bp.route("/api/category/<int:category_id>", methods=["GET"])(get_category_by_id)
category_bp.route("/api/category/<int:category_id>", methods=["PUT"])(update_category)
category_bp.route("/api/category/<int:category_id>", methods=["DELETE"])(delete_category)
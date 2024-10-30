from flask import Blueprint
from controllers.UserController import *

user_bp = Blueprint("user_bp", __name__)

user_bp.route("/api/users", methods=["GET"])(get_all_users)
user_bp.route("/api/users", methods=["POST"])(add_user)
user_bp.route("/api/users/<int:user_id>", methods=["GET"])(get_user_by_id)
user_bp.route("/api/users/<int:user_id>", methods=["PUT"])(update_user)
user_bp.route("/api/users/<int:user_id>", methods=["PATCH"])(patch_user)
user_bp.route("/api/users/<int:user_id>", methods=["DELETE"])(delete_user)

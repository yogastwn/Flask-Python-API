from flask import Blueprint
from controllers.LevelController import *


level_bp = Blueprint("level_bp", __name__)


level_bp.route("/api/level", methods=["GET"])(get_all_levels)
level_bp.route("/api/level", methods=["POST"])(add_level)
level_bp.route("/api/level/<int:level_id>", methods=["GET"])(get_level_by_id)
level_bp.route("/api/level/<int:level_id>", methods=["PUT"])(update_level)
level_bp.route("/api/level/<int:level_id>", methods=["DELETE"])(delete_level)
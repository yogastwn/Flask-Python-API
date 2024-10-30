from flask import jsonify, request
from models.UserModel import User
from models.LevelModel import Level
from config import db
from werkzeug.security import generate_password_hash, check_password_hash


def get_all_users():
    users = User.query.all()
    users_with_levels = []

    for user in users:
        level = Level.query.get(user.level_id)
        user_with_level = {
            "id": user.id,
            "full_name": user.full_name,
            "username": user.username,
            "password": user.password,
            "status": user.status,
            "level": level.name if level else "No Level",
        }
        users_with_levels.append(user_with_level)

    return jsonify(users_with_levels)


def get_user_by_id(user_id):
    user = User.query.get(user_id)
    if not user:
        return jsonify({"status": "error", "message": "User not found"}), 404

    level = Level.query.get(user.level_id)
    user_data = {
        "id": user.id,
        "full_name": user.full_name,
        "username": user.username,
        "password": user.password,
        "status": user.status,
        "level": level.name if level else "No Level",
    }

    return jsonify(user_data)


def add_user():
    new_user_data = request.get_json()
    hashed_password = generate_password_hash(new_user_data["password"])

    new_user = User(
        full_name=new_user_data["full_name"],
        username=new_user_data["username"],
        # password=new_user_data["password"],
        password=hashed_password,
        status=new_user_data["status"],
        level_id=new_user_data["level_id"],
    )

    db.session.add(new_user)
    db.session.commit()

    return (
        jsonify(
            {
                "message": "User added successfully",
                "user": new_user.to_dict(),
            }
        ),
        201,
    )


def update_user(user_id):
    user = User.query.get(user_id)
    if not user:
        return jsonify({"status": "error", "message": "User not found"}), 404

    updated_user_data = request.get_json()
    user.full_name = updated_user_data.get("full_name", user.full_name)
    user.username = updated_user_data.get("username", user.username)
    # user.password = updated_user_data.get("password", user.password)
    if "password" in updated_user_data:
        user.password = generate_password_hash(updated_user_data["password"])
    user.status = updated_user_data.get("status", user.status)
    user.level_id = updated_user_data.get("level_id", user.level_id)

    db.session.commit()

    return jsonify({"message": "User updated successfully", "user": user.to_dict()})


def patch_user(user_id):
    user = User.query.get(user_id)
    if not user:
        return jsonify({"status": "error", "message": "User not found"}), 404

    updated_user_data = request.get_json()
    if "full_name" in updated_user_data:
        user.full_name = updated_user_data["full_name"]
    if "username" in updated_user_data:
        user.username = updated_user_data["username"]
    # if "password" in updated_user_data:
    #     user.password = updated_user_data["password"]
    if "password" in updated_user_data:
        user.password = generate_password_hash(updated_user_data["password"])
    if "status" in updated_user_data:
        user.status = updated_user_data["status"]
    if "level_id" in updated_user_data:
        level = Level.query.get(updated_user_data["level_id"])
        if level:
            user.level_id = updated_user_data["level_id"]
        else:
            return jsonify({"status": "error", "message": "Invalid level ID"}), 400

    db.session.commit()

    return jsonify({"message": "User patched successfully", "user": user.to_dict()})


def delete_user(user_id):
    user = User.query.get(user_id)
    if not user:
        return jsonify({"status": "error", "message": "User not found"}), 404

    db.session.delete(user)
    db.session.commit()

    return jsonify({"message": "User deleted successfully"})

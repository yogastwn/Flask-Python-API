from flask import render_template
from config import app, db
from routes.Book_bp import book_bp
from routes.Category_bp import category_bp
from routes.User_bp import user_bp
from routes.Level_bp import level_bp

app.register_blueprint(book_bp)
app.register_blueprint(category_bp)

app.register_blueprint(user_bp)
app.register_blueprint(level_bp)


@app.route("/")
def index():
    return render_template("index.html")


# if __name__ == "__main__":
#     db.create_all()
#     app.run(port=5001, debug=True)

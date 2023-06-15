from CompanyPanel.adminBlueprint import admin_bp
from flask import Flask
from CompanyPanel.models import db




app = Flask(__name__)
app.config["SECRET_KEY"] = "arunisto"
app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///new_database.db"
db.init_app(app)

with app.app_context():
    db.create_all()


app.register_blueprint(admin_bp)

if __name__ == "__main__":
    app.run(debug=True)
from flask import Flask, jsonify
from flask_cors import CORS


from api.education import education_bp
app = Flask(__name__)

CORS(app, supports_credentials=True, origins=["http://76.13.134.224:8080/"])

app.register_blueprint(education_bp)
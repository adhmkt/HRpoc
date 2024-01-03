from flask import Flask
from .file_service import file_service

app = Flask(__name__)
app.register_blueprint(file_service, url_prefix='/file_service')
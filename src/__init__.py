from flask import Flask
from src.blueprints import mangayeh

app = Flask(__name__)

app.register_blueprint(mangayeh.bp)
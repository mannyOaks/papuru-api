from flask import Flask
from src.blueprints import sources

app = Flask(__name__)


app.register_blueprint(sources.bp)

from flask import Flask
from src.blueprints import sources, mangayeh

app = Flask(__name__)


app.register_blueprint(sources.bp)
app.register_blueprint(mangayeh.bp)

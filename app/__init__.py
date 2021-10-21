from flask import Flask
from flask_qrcode import QRcode
from .views import views


app = Flask(__name__)
app.config.from_object('config')
app.register_blueprint(views)
QRcode(app)

from flask import Blueprint, flash, g, redirect, render_template, request, session, url_for
from .wallet_gen import wallet_gen


views = Blueprint('auth', __name__, url_prefix='')


@views.route('/', methods=['GET','POST'])
def home():
    if request.method == "POST":
        data = request.form['salt']
        session['data'] = data
        return redirect(url_for('auth.wallet'))
    return render_template("home.html")



@views.route('/wallet')
def wallet():
    wallgen = wallet_gen()
    private_key, public_key, address = wallgen.genrate(session['data'])
    return render_template("wallet.html", address = address, private_key = private_key)
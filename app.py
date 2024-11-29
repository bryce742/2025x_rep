from flask import Flask, render_template, redirect, request
from blueprints.home.home import home_bp
from blueprints.buy.buy import buy_bp
from blueprints.chart.chart import chart_bp
from config import config

app = Flask(__name__, template_folder='templates')
app.config.update(config)

"""
@app.before_request
def before_request():
    if request.headers.get('X-Forwarded-Proto') == 'http':
        return redirect(request.url.replace('http://', 'https://', 1))
"""

# Register blueprints with url_prefixes from config
app.register_blueprint(home_bp, url_prefix='/')
app.register_blueprint(buy_bp, url_prefix=f'/{app.config["tab1_route"]}')
app.register_blueprint(chart_bp, url_prefix=f'/{app.config["tab2_route"]}')

if __name__ == '__main__':
    app.run()


from flask import render_template
from application import app

@app.route('/')
@app.route('/index')
def index():
    user = {'username' : 'William'}
    exoplanets = [
        {
            'name': 'AU Mic b',
            'system': 'AU Mic',
            'discovery_method': 'Transit',
            'discover_facility': 'TESS',
            'confirmed': True,
            'reference': '',
            'year': 2020
        },
        {
            'name': 'test1',
            'system': 'test_system'
        }
    ]
    return render_template('index.html', title='Home', user=user, exoplanets=exoplanets)
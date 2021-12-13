from flask import render_template, flash, redirect
from application import app
from forms import Exoplanet_Form

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

@app.route('/entry', methods=['GET', 'POST'])
def entry():
    form = Exoplanet_Form()
    if form.validate_on_submit():
        flash(f'New exoplanet data for {form.name.data}')
        return redirect('/index')
    return render_template('entry.html', title='Enter Exoplanets', form=form)
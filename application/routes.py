from flask import render_template, flash, redirect, url_for, request
from application import app, db
from forms import Exoplanet_Form
from application.models import Exoplanet

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

    if request.method == 'POST':
        if form.validate_on_submit():
            exoplanet = Exoplanet(
                name = form.name.data,
                system = form.system.data,
                method = form.method.data,
                year = form.year.data
            )
            db.session.add(exoplanet)
            db.session.commit()
            flash(f'New exoplanet data for {form.name.data}')
            return redirect(url_for('index'))
    return render_template('entry.html', title='Enter Exoplanets', form=form)
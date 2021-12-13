from flask import render_template, flash, redirect, url_for, request
from application import app, db
from forms import EditEntry, Exoplanet_Form
from application.models import Exoplanet

# This route has READ functionality
@app.route('/')
@app.route('/index')
def index():
    user = {'username' : 'William'}
    exoplanets = Exoplanet.query.all()
    return render_template('index.html', title='Home', user=user, exoplanets=exoplanets)

# This route has CREATE functionality
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

# This route has UPDATE functionality
@app.route('/update/<int:id>', methods = ['GET', 'POST'])
def update(id):
    form = EditEntry()
    planet = Exoplanet.query.get(id)
    if request.method == 'POST' and form.validate_on_submit():
        planet.name = form.name.data
        planet.system = form.system.data
        planet.method = form.method.data
        planet.year = form.year.data
        db.session.commit()
        return(redirect(url_for('index')))
    return render_template('update.html', title='Update Exoplanets', form=form)
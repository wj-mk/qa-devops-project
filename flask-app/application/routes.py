from flask import render_template, flash, redirect, url_for, request
from application import app, db
from forms import EditEntry, Exoplanet_Form, DeleteEntry
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

# Navigation link to update is not possible without adding a route 
# for just /update. It could be improved, but it works so lets move on.

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
        flash(f'Updated exoplanet data for {form.name.data}')
        return(redirect(url_for('index')))
    return render_template('update.html', title='Update Exoplanets', form=form, planet=planet)

# This route has DELETE functionality
@app.route('/delete', methods = ['GET', 'POST'])
def delete():
    exoplanets = Exoplanet.query.all()
    form = DeleteEntry()
    if request.method == 'POST' and form.validate_on_submit():
        id = form.id.data
        planet = Exoplanet.query.get(id)
        deletion = planet.name
        db.session.delete(planet)
        db.session.commit()
        flash(f'Deleted {deletion}')
        return redirect(url_for('index'))
    return render_template('delete.html', form=form, exoplanets=exoplanets)


# for running tests, run this 
# python3 -m pytest --cov --cov-report term-missing

from flask_testing import TestCase
from werkzeug.wrappers import response
from application import app, db
from application.models import Exoplanet
from flask import url_for

class TestBase(TestCase):
    def create_app(self):
        app.config.update(
            SQLALCHEMY_DATABASE_URI='sqlite:///test.db',
            SECRET_KEY='TEST_SECRET_KEY',
            DEBUG=True,
            WTF_CSRF_ENABLED=False  
        )
        return app
    
    def setUp(self):
        # Create table schema
        db.create_all()

        # Create test exoplanet
        earth = Exoplanet(
                name = 'Earth',
                system = 'Solar',
                method = 'Existing',
                year = 0
        )

        # save sample date to database
        db.session.add(earth)
        db.session.commit()
    
    def tearDown(self):
        db.session.remove()
        db.drop_all()
    
class TestViews(TestBase):
    def test_get_index(self):
        response = self.client.get(url_for('index'))
        self.assert200
        self.assertIn(b'Earth', response.data)

class TestEntry(TestBase):
    def test_entry_page(self):
        response = self.client.get(url_for('entry'))
        self.assert200
        self.assertIn(b'Exoplanet', response.data)
    
    def test_post_entry(self):
        response = self.client.post(
            url_for('entry'),
            data = dict(
                name = 'Kepler 16b',
                system = 'Kepler 16',
                method = 'Transit',
                year = 2005
            ),
            follow_redirects = True
        )
        self.assert200
        self.assertIn(b'Kepler', response.data)

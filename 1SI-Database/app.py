import psycopg2
from database_manager import *
from flask import Flask, render_template

app = Flask(__name__)


@app.route('/')
def index():
    return render_template('index.html')


@app.route('/mentors')
def mentors():
    query = ("""SELECT concat(mentors.first_name, ' ', mentors.last_name), schools.name, schools.country
            FROM mentors
            INNER JOIN schools
                ON mentors.city = schools.city
            ORDER BY mentors.id""")
    asked_parameters = database_manager(query)
    return render_template('mentors.html', asked_parameters=asked_parameters)


@app.route('/all-school')
def all_school():
    query = ("""SELECT concat(mentors.first_name, ' ', mentors.last_name), schools.name, schools.country
            FROM mentors
            RIGHT JOIN schools
                ON mentors.city = schools.city
            ORDER BY mentors.id""")
    asked_parameters = database_manager(query)
    return render_template('all_school.html', asked_parameters=asked_parameters)


if __name__ == '__main__':
    app.run(debug=True)

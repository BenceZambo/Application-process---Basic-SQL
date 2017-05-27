import psycopg2
from database_manager import *
from flask import Flask, render_template

app = Flask(__name__)


@app.route('/')
def index():
    asked_parameters = []
    return render_template('results.html', asked_parameters=asked_parameters)


@app.route('/mentors')
def mentors():
    query = ("""SELECT concat(mentors.first_name, ' ', mentors.last_name), schools.name, schools.country
            FROM mentors
            INNER JOIN schools
                ON mentors.city = schools.city
            ORDER BY mentors.id""")
    asked_parameters = database_manager(query)
    return render_template('results.html', asked_parameters=asked_parameters)


@app.route('/all-school')
def all_school():
    query = ("""SELECT concat(mentors.first_name, ' ', mentors.last_name), schools.name, schools.country
            FROM mentors
            RIGHT JOIN schools
                ON mentors.city = schools.city
            ORDER BY mentors.id""")
    asked_parameters = database_manager(query)
    return render_template('results.html', asked_parameters=asked_parameters)


@app.route('/mentors-by-country')
def mentors_by_country():
    query = ("""SELECT  schools.country, COUNT(mentors.first_name)
            FROM mentors
            INNER JOIN schools
                ON mentors.city = schools.city
            GROUP BY schools.country
            ORDER BY schools.country""")
    asked_parameters = database_manager(query)
    return render_template('results.html', asked_parameters=asked_parameters)


@app.route('/contacts')
def contacts():
    query = ("""SELECT concat(mentors.first_name, ' ', mentors.last_name), schools.name
            FROM mentors
            INNER JOIN schools
                ON mentors.city = schools.city
            ORDER BY schools.name""")
    asked_parameters = database_manager(query)
    return render_template('results.html', asked_parameters=asked_parameters)


@app.route('/applicants')
def applicants():
    query = ("""SELECT applicants.first_name, applicants.application_code, applicants_mentors.creation_date
            FROM applicants
            INNER JOIN applicants_mentors
                ON applicants.id = applicants_mentors.applicant_id
            WHERE applicants_mentors.creation_date  > '2016-01-01'
            ORDER BY applicants_mentors.creation_date DESC""")
    asked_parameters = database_manager(query)
    return render_template('results.html', asked_parameters=asked_parameters)


@app.route('/applicants-and-mentors')
def applicants_and_mentors():
    query = ("""SELECT applicants.first_name, applicants.application_code, mentors.first_name, mentors.last_name
            FROM applicants
            LEFT JOIN applicants_mentors
                ON applicants.id = applicants_mentors.applicant_id
            LEFT JOIN mentors
                ON mentors.id = applicants_mentors.mentor_id""")
    asked_parameters = database_manager(query)
    return render_template('results.html', asked_parameters=asked_parameters)


if __name__ == '__main__':
    app.run(debug=True)

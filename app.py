from flask import Flask, jsonify, render_template,jsonify

app = Flask(__name__)

JOBS = [
    {
        'id': 1,
        'title': 'Data Scientist',
        'location': 'Bengaluru',
        'salary': 'Rs. 16,00,000'
    },
    {
        'id': 2,
        'title': 'Data Engineer',
        'location': 'Remote',
        'salary': 'Rs. 15,00,000'
    },
    {
        'id': 3,
        'title': 'AI Engineer',
        'location': 'Kochi',
        'salary': 'Rs. 17,00,000'
    },
]

@app.route("/")
def steps_home():
    return render_template('home.html', jobs=JOBS , company_name='Steps')


@app.route("/jobs")
def steps_jobs():
    return jsonify(JOBS)

if __name__ == "__main__":
    app.run(host='0.0.0.0', debug=True)

    

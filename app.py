from flask import Flask,render_template

app = Flask(__name__)
JOBS=[{'id':1,
    'Title':'Data Scientist',
    'Location':'Delhi,India',
'Salary': '15,00,000'},
{'id':2,
'Title':'Data Analyst',
'Location':'San Fransisco,USA',
'Salary':'$120,000'},
{'id':3,
'Title':'Data Engineer',
'Location':'Bengaluru,India',
'Salary':'12,00,000'}
]
@app.route("/")
def hello():
    return render_template('home.html',jobs=JOBS)

if __name__ == "__main__":
    app.run(host="0.0.0.0",debug=True)  

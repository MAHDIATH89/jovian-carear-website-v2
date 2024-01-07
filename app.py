from flask import Flask, render_template ,jsonify



app = Flask(__name__)

""" JOBS = [
  {
    'Id' : 1,
    'title': 'Data Analyst',
    'location': 'Bengaluru, India',
    'salary': 'Rs. 10,00,000'

  },
  {
    'Id' : 2,
    'title': 'Data Scientist',
    'location': 'Delhi, India',
    'salary': 'Rs. 15,00,000'
  },
  {
    'Id' : 3,
    'title': 'Frontend Engineer',
    'location': 'Remote',
  },
  {
    'Id' : 4,
    'title': 'Backend Engineer',
    'location': 'San Francisco, USA',
    'salary': '$120,000'
  }
]   """

def load_jobs_from_db():
  with engine.connect() as conn:
    result = conn.execute(text(" select * from jobs "))
    jobs = []
    for row in result.all():
      jobs.append(dict(row))
      return jobs

@app.route("/")
def hello_world():
  jobs = load_jobs_from_db()
  return render_template("home.html" ,jobs=jobs ,company_name ='Jovian')

@app.route("/api/jobs")
def list_jobs():
  return jsonify(JOBS)
  
if __name__ == "__main__":
  app.run(host='0.0.0.0', debug=True)





from flask import Flask, render_template, request
from run import randomforest
from scraper import scrapeDetails
from scraper import scrapeDoctors
app = Flask(__name__)

@app.route('/')
def student():
   mobile = ""
   email = ""
   return render_template('login.html', mobile = mobile, email = email)

@app.route('/details', methods = ['POST', 'GET'])
def details():
   if request.method == 'POST':
      mobile = request.form['Name']
      email = request.form['Name2']
      result = ""
      return render_template("details.html")

@app.route('/symptoms', methods = ['POST', 'GET'])
def symptoms():
   if request.method == 'POST':
      height = request.form['Name3']
      weight = request.form['Name4']
      bmi = int(weight)/((int(height)/100)**2)
      bmi = round(bmi)
      return render_template("index.html", result = result, bmi = bmi)

@app.route('/result', methods = ['POST', 'GET'])
def result():
   if request.method == 'POST':
      symptom1 = request.form['Name']
      symptom2 = request.form['Name2']
      symptom3 = request.form['Name3']
      symptom4 = request.form['Name4']
      symptom5 = request.form['Name5']
      result = randomforest(symptom1, symptom2, symptom3, symptom4, symptom5)
      detail = scrapeDetails(result)[0]
      disease = scrapeDetails(result)[1]
      meds = scrapeDetails(result)[2]
      procedure = scrapeDetails(result)[-1]
      return render_template("result.html", result = result, detail = detail, disease = disease, meds =  meds, procedure = procedure)

@app.route('/suggestion', methods = ['POST', 'GET'])
def suggestion():
      docname1 = scrapeDoctors()[0]
      docdetails1 = scrapeDoctors()[1]
      patientexp1 = scrapeDoctors()[-1]

      docname2 = scrapeDoctors()[3]
      docdetails2 = scrapeDoctors()[4]
      patientexp2 = scrapeDoctors()[2]

      docname3 = scrapeDoctors()[6]
      docdetails3 = scrapeDoctors()[7]
      patientexp3 = scrapeDoctors()[5]
      return render_template("suggestion.html", docname1 = docname1, docdetails1 = docdetails1, patientexp1 = patientexp1, docname2 = docname2, docdetails2 = docdetails2, patientexp2 = patientexp2, docname3 = docname3, docdetails3 = docdetails3, patientexp3 = patientexp3)

if __name__ == '__main__':
   app.run(debug=True)

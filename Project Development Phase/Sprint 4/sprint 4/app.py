from flask import Flask, render_template, redirect, request, url_for, flash, session
from markupsafe import escape
import requests
import json
from turtle import st
import ibm_db



conn = ibm_db.connect("DATABASE=bludb;HOSTNAME=6667d8e9-9d4d-4ccb-ba32-21da3bb5aafc.c1ogj3sd0tgtu0lqde00.databases.appdomain.cloud;PORT=30376;SECURITY=SSL;SSLServerCertificate=DigiCertGlobalRootCA.crt;UID=xcg19604;PWD=4Kk8jwgnitagt74M",'','')
print(conn)
print("connection successful...")


app = Flask(__name__)

app.secret_key = 'gtvhfryj123#@%'

@app.route('/')
def home():
    return render_template('index.html')


url = "https://jsearch.p.rapidapi.com/search"

querystring = {"query":" Web Developer , USA","num_pages":"1"}

headers = {
	"X-RapidAPI-Key": "",
	"X-RapidAPI-Host": "jsearch.p.rapidapi.com"
}



@app.route("/api", methods=['GET'])
def api():
    response = requests.request("GET", url, headers=headers, params=querystring)
    data = json.loads(response.text)
    return render_template('index.html',data=data)



@app.route('/signup', methods =['GET', 'POST'])
def signup():
    return render_template('sign-up.html')

@app.route('/dashboard')
def dashboard():
    return render_template('dashboard.html')

@app.route('/about')
def about():
    return render_template('about.html')

@app.route('/bookmark')
def bookmark():
    return render_template('bookmark-jobs.html')

@app.route('/candidatedetails')
def candidatedetails():
    return render_template('candidate-details.html')

@app.route('/candidategird')
def candidategird():
    return render_template('candidate-gird.html')

@app.route('/candidatelist')
def candidatelist():
    return render_template('candidate-list.html')

@app.route('/companydetails')
def companydetails():
    return render_template('company-details.html')

@app.route('/companylist')
def companylist():
    return render_template('company-list.html')

@app.route('/contact')
def contact():
    return render_template('contact.html')

@app.route('/faqs')
def faqs():
    return render_template('faqs.html')

@app.route('/jobcategories')
def jobcategories():
    return render_template('job-categories.html')

@app.route('/jobdetails')
def jobdetails():
    return render_template('job-details.html')

@app.route('/jobgrid')
def jobgrid():
    return render_template('job-gird.html')

@app.route('/joblist')
def joblist():
    return render_template('job-list.html')

@app.route('/managejobpost')
def managejobpost():
    return render_template('manage-jobs-post.html')

@app.route('/managejobs')
def managejobs():
    return render_template('manage-jobs.html')

@app.route('/privacypolicy')
def privacypolicy():
    return render_template('privacy-policy.html')

@app.route('/profile')
def profile():
    return render_template('profile.html')

@app.route('/resetpassword')
def resetpassword():
    return render_template('reset-password.html')

@app.route('/services')
def services():
    return render_template('services.html')

@app.route('/signin', methods =['GET','POST'])
def signin():
    return render_template('sign-in.html')

@app.route('/signout')
def signout():
    return render_template('sign-out.html')

@app.route('/team')
def team():
    return render_template('team.html')



@app.route('/register', methods=['GET', 'POST'])
def register():
    if request.method == 'POST':
        username = request.form['username']
        email = request.form['email']
        password = request.form['password']
        phonenumber = request.form['phonenumber']


        sql = "SELECT * FROM users WHERE email = ?"
        stmt = ibm_db.prepare(conn, sql)
        ibm_db.bind_param(stmt,1,email)
        ibm_db.execute(stmt)
        account = ibm_db.fetch_assoc(stmt)
        
        if account:
            return render_template('about.html', msg="already members")
        else:
            insert_sql = "INSERT INTO users VALUES (?,?,?,?)"
            prep_stmt = ibm_db.prepare(conn, insert_sql)
            ibm_db.bind_param(prep_stmt, 1, username)
            ibm_db.bind_param(prep_stmt, 2, email)
            ibm_db.bind_param(prep_stmt, 3, password)
            ibm_db.bind_param(prep_stmt, 4, phonenumber)
            ibm_db.execute(prep_stmt)

            return "hello"
            
               
@app.route('/login', methods=['GET', 'POST'])
def login():
    app.secret_key = 'qwerty:098765'
    if request.method == 'POST':
        
        email = request.form['email']
        password = request.form['password']
        print(email,password)

        sql = f"SELECT * FROM  users WHERE email='{escape(email)}' and password='{escape(password)}'"
        stmt = ibm_db.exec_immediate(conn, sql)
        data = ibm_db.fetch_both(stmt)
                       
        if data:
            session["email"] = escape(email)
            session["password"] = escape(password)
            return redirect(url_for('dashboard'))

        else:
            return render_template('sign-in.html')
    
    






if __name__ == "__main__":
    app.run(debug=True, port=5050)
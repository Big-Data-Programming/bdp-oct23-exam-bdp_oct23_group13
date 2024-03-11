from flask import Flask, render_template, redirect, url_for, request


app = Flask(__name__)

users = {
    'Recruiter@gmail.com': {'password': 'password@123', 'dashboard': 'dashboard'},
    'HRecruiter@gmail.com': {'password': 'password@1234', 'dashboard': 'dashboard2'},
    'student@gmail.com': {'password': 'student@123', 'dashboard': 'coding'},
}




@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        username = request.form.get('username')
        password = request.form.get('password')
        
        # Check credentials and redirect to the correct dashboard
        user_info = users.get(username)
        if user_info and user_info['password'] == password:
            if user_info['dashboard'] == 'dashboard':
                return redirect(url_for('dashboard'))
            elif user_info['dashboard'] == 'dashboard2':
                return redirect(url_for('dashboard2'))
            elif user_info['dashboard'] == 'coding':
                return redirect(url_for('coding'))
        
       
        return render_template('login.html', error='Invalid credentials')
        
    return render_template('login.html')


@app.route('/dashboard')
def dashboard():
    return render_template('dashboard.html')


@app.route('/dashboard2')
def dashboard2():
    return render_template('dashboard2.html')

@app.route('/Eligible_Candidate_lists')
def Eligible_Candidate_lists():
    return render_template('Eligible_Candidate_lists.html')

@app.route('/overview')
def overview():
    return render_template('overview.html')

@app.route('/candidate_requirements')
def candidate_requirements():
    return render_template('candidate_requirements.html')

@app.route('/candidate_results')
def candidate_results():
    return render_template('candidate_results.html')

@app.route('/requirement_demands_list')
def requirement_demands_list():
    return render_template('requirement_demands_list.html')



if __name__ == '__main__':
    app.run(debug=True)
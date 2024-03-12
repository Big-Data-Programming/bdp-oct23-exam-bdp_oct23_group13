# Doodle, hushhush Recruiter

-- Project Structure and basic gist
  - Data Fetching and Preparation:
  1. Fetch user profile links via API calls.
  2. Perform web scraping on fetched data.
  3. Convert and save data into a CSV file.
  4. Store CSV data in an SQL Lite database.

  - Model Training and Testing:
  1. Divide data from SQL Lite database into training, testing, and unseen data.
  2. Train and test a model using the training and testing data.
  3. Save trained model for each job role in a Pickle file.

  - Candidate Selection and Assessment Process:
  1. Load trained model for each job role from Pickle file into 'selector.py'.
  2. Process 'selected candidates' data using the model.
  3. Manager selects candidates (Yes/No) through Manager Interface.
  4. Manager-set requirements passed to HR Interface.
  5. HR Interface generates list of eligible candidates.
  6. Eligible candidates receive email for coding test.
  7. Candidate Interface updates candidate status.
  8. Candidates receive confirmation email and access to coding test.

  - Candidate Evaluation and Feedback:
  1. Save candidates' coding test answers and Q&A in a database table.
  2. Evaluate answers using OpenAI API.
  3. Provide feedback based on coding test evaluation.
   
-- Initial Setup Procedure 
   - Navigate to desired directory for project setup.
  1. Clone project using: git clone https://github.com/Big-Data-Programming/bdp-oct23-exam-bdp_oct23_group13.git
  2. Install requirements by running: pip install -r requirements.txt
      - Execute this command whenever requirements.txt changes.

-- Product Application Flow
  1. Run app.py file.
  2. Open the localhost URL provided after running app.py in a browser.
  3. Access the login page at https://{url}/loginpage using static login credentials for Recruiting Manager or HR Manager.
  4. Upon logging in, Recruiting Manager is redirected to https://{url}/dashboard and HR Manager to https://{url}/dashboard2.
  5. In the Recruiting Manager dashboard, select candidate requirements based on Job Role, Years of Experience, and Number of Candidates required.
  6. In the HR Manager dashboard, view the Latest Job Requirement and access the Eligible Candidate List through a button.
  7. On the Eligible Candidate List page, an option to send emails to all eligible candidates is available.
  8. Selected candidates receive an email with a link to a coding challenge, valid for 48 hours. After submission, candidates are redirected to the login page.
  9. Accessing the coding challenge link displays three coding questions for the candidate to solve.
  10. Candidates who pass the challenge receive an email for further rounds, while failed candidates receive a rejection page.
  11. In the Recruiting Manager's dashboard, feedback for each coding question is displayed for each candidate.

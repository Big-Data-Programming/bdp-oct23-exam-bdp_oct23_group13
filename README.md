# Doodle, hushhush Recruiter

1. Project Structure and basic gist
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
   
3. Initial Setup Procedure 
    - Navigate to the directory where you want to set up this project.
    - git clone this project using the following command git clone https://github.com/Big-Data-Programming/bdp-oct23-exam-              bdp_oct23_group13.git
    - To install all the requirements run the below command. Execute this command whenever there is a change in requirements.txt file.
      On Mac/Win: pip install -r requirements.txt

4. Product Application Flow

    - Navigate to the app.py file and run it
    - While running app.py, the code provides a localhost url, run the url in the browser.
    - For accessing the login page, navigate to https://{url}/loginpage. Enter static login credentials either for Recruiting Manager or HR         Manager.
    - For Recruiting Manager, you will be redirected to https://{url}/dashboard. For HR Manager, you will be redirected to https://{url}/          dashboard2.
    - Suppose you are in the Recruiter manager dashboard, user selects the Candidate requirements based on Job Role, Years of Experience and       Number of Candidates required.
    - Now, in the HR Manager dashboard, user views the Latest Job Requirement, with a button prompting Eligible Candidate List. Upon               pressing the button, user is redirected to page displaying Eligible Candidate List.
    - In the Eligible Candidate List page, Send Email option is avaialble to all eligible candidates.
    - Selected candidates will recieve an email, which contains the link to a coding challenge which has an expiry window of 48 Hours. After       submitting the coding challenge it will redirect the user to the login page.
    - When the candidate accesses the coding challenge link, three coding questions are displayed for the candidate to solve.
    - Candidates who pass this challenge will receive an email for further round and those who fail will get a page diplaying rejection.
    - In the Recruiting Manager's dashboard, for each candidate, feedback for each coding question is displayed.

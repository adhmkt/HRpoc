from flask import Flask, render_template, request, redirect, url_for, flash, send_from_directory
import os
from app.file_handling import save_file, list_files, delete_file  # Updated function names

app = Flask(__name__)
app.secret_key = 'your_secret_key'  # Replace with a real secret key
resume_folder = 'resume_folder'  # Path for resume uploads
job_folder = 'job_folder'  # Path for job uploads


@app.route('/')
def home():
    return render_template('home.html')

@app.route('/login', methods=['GET', 'POST'])
def login():
    # Logic for login (to be implemented)
    return render_template('login.html')

@app.route('/dashboard')
def dashboard():
    # Logic for dashboard (to be implemented)
    return render_template('dashboard.html')

@app.route('/resume_bank', methods=['GET', 'POST'])
def resume_bank():
    if not os.path.exists(resume_folder):
        os.makedirs(resume_folder, mode=0o755)

    if request.method == 'POST':
        files = request.files.getlist('resumes')
        for file in files:
            result = save_file(file, resume_folder)  # Make sure this is save_file
            flash(result)

    resumes = list_files(resume_folder)  # Make sure this is list_files
    return render_template('resume_bank.html', resumes=resumes)  # Always return a response


@app.route('/download_resume/<filename>')
def download_resume(filename):
    return send_from_directory(resume_folder, filename, as_attachment=True)

@app.route('/delete_resume/<filename>', methods=['POST'])
def delete_resume_route(filename):
    result = delete_file(filename, resume_folder)  # Using delete_file function
    flash(result)
    return redirect(url_for('resume_bank'))

@app.route('/delete_job/<filename>', methods=['POST'])
def delete_job_route(filename):
    result = delete_file(filename, job_folder)  # Corrected to use delete_file
    flash(result)
    return redirect(url_for('job_bank'))

@app.route('/job_bank', methods=['GET', 'POST'])
def job_bank():
    if not os.path.exists(job_folder):
        os.makedirs(job_folder, mode=0o755)

    if request.method == 'POST':
        files = request.files.getlist('jobs')
        for file in files:
            result = save_file(file, job_folder)
            flash(result)

    jobs = list_files(job_folder)
    return render_template('job_bank.html', jobs=jobs)



@app.route('/download_job/<filename>')
def download_job(filename):
    return send_from_directory(job_folder, filename, as_attachment=True)



if __name__ == '__main__':
    app.run(debug=True)

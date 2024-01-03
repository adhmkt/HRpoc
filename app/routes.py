from flask import Flask, render_template, request, redirect, url_for, flash, send_from_directory
import os
from app.file_handling import save_resume, list_resumes, delete_resume  # Assuming these functions are defined

app = Flask(__name__)
app.secret_key = 'your_secret_key'  # Replace with a real secret key in a production environment
resume_folder = 'resume_folder'  # Update with the actual path for resume uploads

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
        os.makedirs(resume_folder)

    if request.method == 'POST':
        files = request.files.getlist('resumes')
        for file in files:
            result = save_resume(file, resume_folder)
            flash(result)

    resumes = list_resumes(resume_folder)  # Make sure this function returns a list of file names
    return render_template('resume_bank.html', resumes=resumes)

@app.route('/download_resume/<filename>')
def download_resume(filename):
    return send_from_directory(resume_folder, filename, as_attachment=True)

@app.route('/delete_resume/<filename>', methods=['POST'])
def delete_resume_route(filename):
    result = delete_resume(filename, resume_folder)
    flash(result)
    return redirect(url_for('resume_bank'))

# Add other routes as necessary

if __name__ == '__main__':
    app.run(debug=True)  # Set debug=False in a production environment

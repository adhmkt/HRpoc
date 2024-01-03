import os
from werkzeug.utils import secure_filename

# Assuming you have these constants defined
ALLOWED_EXTENSIONS = {'pdf', 'docx'}
MAX_FILE_SIZE = 5 * 1024 * 1024  # 5 MB limit

def allowed_file(filename):
    """ Check if the file has an allowed extension """
    return '.' in filename and filename.rsplit('.', 1)[1].lower() in ALLOWED_EXTENSIONS

def save_resume(file, upload_folder):
    """ Save a resume file to the specified upload folder """
    if not file:
        return "No file provided."
    
    if file.content_length > MAX_FILE_SIZE:
        return "File size exceeds the limit."

    if not allowed_file(file.filename):
        return "File type is not allowed."

    filename = secure_filename(file.filename)
    file_path = os.path.join(upload_folder, filename)

    try:
        file.save(file_path)
        return f"File {filename} uploaded successfully."
    except IOError as e:
        return f"An error occurred: {e}"

def list_resumes(upload_folder):
    """ List all resume files from the specified upload folder """
    return os.listdir(upload_folder)

def delete_resume(filename, upload_folder):
    file_path = os.path.join(upload_folder, filename)
    if os.path.exists(file_path):
        try:
            os.remove(file_path)
            return f"File {filename} successfully deleted."
        except Exception as e:
            return f"An error occurred: {e}"
    else:
        return "File not found."

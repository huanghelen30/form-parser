from flask import Blueprint, render_template, request
from app.utils.pdf_parser import parse_pdf  # we'll define this soon

main = Blueprint('main', __name__)

@main.route('/')
def index():
    return render_template('index.html')

@main.route('/upload', methods=['POST'])
def upload():
    if 'pdf_file' not in request.files:
        return "No file uploaded", 400

    file = request.files['pdf_file']
    if file.filename == '':
        return "No selected file", 400

    file.save(f"uploads/{file.filename}")
    parsed_data = parse_pdf(f"uploads/{file.filename}")
    
    return render_template("result.html", data=parsed_data)

# buy.py
import json
import os
from flask import Blueprint, render_template, request, redirect, url_for, current_app

buy_bp = Blueprint('buy', __name__, template_folder='templates')

SUBMISSIONS_FILE = 'submissions.json'

def load_submissions():
    if os.path.exists(SUBMISSIONS_FILE):
        with open(SUBMISSIONS_FILE, 'r') as f:
            return json.load(f)
    return []

def save_submissions(submissions):
    with open(SUBMISSIONS_FILE, 'w') as f:
        json.dump(submissions, f)

def save_submission(username, content):
    submissions = load_submissions()
    submissions.append({"username": username, "content": content, "likes": 0})
    save_submissions(submissions)

@buy_bp.route('/')
def getData():
    submissions = load_submissions()

    page_config = {
        "main_heading": "Help us reach 2025X before New Years Eve!",                  
        "heading_color": "gold",                            
        "heading_font": "Arial, sans-serif",                  
        "heading_font_size": "3em",                           
        "heading_font_weight": "bold",                        
        "heading_alignment": "center", 
        "heading_background_color": "black",                                              
        "paragraphs": "Start of 2025 RICH!",  
        "paragraph_color": "gold",                           
        "paragraph_font": "Georgia, serif",                   
        "paragraph_font_size": "3em",
        "paragraph_background": "rgba(0, 0, 0, .7)",     # Background color for paragraph container                       
        "paragraph_alignment": "center",                      
        "background_image": "/static/media/square.jpg", 

        # Styling for success message, blog form, and submissions
        "success_text": "Thanks for doing your part, now HOLD!",
        "success_text_color": "gold",
        "success_background_color": "black",
        "success_image": "/static/media/success.gif",
        "success_image_width": "100%",  

        # Blog form title and styling
        "blog_title": "What are your goals for 2025?",
        "blog_title_color": "gold",
        "blog_title_font_size": "2em",

        # Form labels and styling for input fields
        "form_label_username": "Username:",
        "form_label_content": "Username:",
        "form_label_text_color": "gold",
        "form_label_font_size": "3em",
        "button_background_color": "#444",
        "button_text_color": "#fff",

        # Submissions title and styling
        "submissions_title": "Submissions:",
        "submissions_title_color": "gold",
        "submissions_font_size": "2em",
        "submissions_background_color": "black",

        # Alignment for blog, form, and submissions content
        "blog_alignment": "center"
    }

    merged_config = {**current_app.config, **page_config}
    return render_template('tab1.html', **merged_config, submissions=submissions)

@buy_bp.route('/submit_blog', methods=['POST'])
def submit_blog():
    username = request.form.get('username')
    content = request.form.get('content')
    save_submission(username, content)
    return redirect(url_for('buy.getData'))

@buy_bp.route('/like_submission/<int:index>', methods=['POST'])
def like_submission(index):
    submissions = load_submissions()
    if 0 <= index < len(submissions):
        submissions[index]['likes'] += 1
        save_submissions(submissions)
    return redirect(url_for('buy.getData'))

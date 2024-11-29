from flask import Blueprint, render_template, current_app

home_bp = Blueprint('home', __name__, template_folder='templates')

@home_bp.route('/')
def home():
    page_config = {
        "main_heading": "2025X BEFORE NEW YEAR'S EVE!",
        "heading_color": "gold",
        "heading_font": "Arial, sans-serif",
        "heading_font_size": "4em",
        "heading_font_weight": "bold",
        "heading_padding": "0px 0",
        "heading_alignment": "center",
        "heading_background": "rgba(0, 0, 0, 0.5)",
        "heading_border": "1px solid white",
        "heading_container_padding": ".5%",
        "heading_display": "inline-block",
        "heading_margin": "auto" if "center" else "0",
        "heading_bottom_padding": "20px",
        
        "paragraphs": "Possible only through community. We can do this!",
        "paragraph_color": "gold",
        "paragraph_font": "Georgia, serif",
        "paragraph_font_size": "2em",
        "paragraph_font_weight": "",
        "paragraph_padding": "5px 0",
        "paragraph_alignment": "center",
        "paragraph_background": "rgba(0, 0, 0, 0.5)",
        "paragraph_border": "1px solid #ddd",
        "paragraph_container_padding": "10px",
        "paragraph_display": "inline-block",
        "paragraph_margin": "auto" if "center" else "0",
        "paragraph_bottom_padding": "20px",

        "content_boxed": True,
        "box_background": "transparent",
        "box_border": "transparent",
        "box_padding": "0px",
        "box_margin": "0px auto",

        "background_image": "/static/media/square.jpg"
    }
    merged_config = {**current_app.config, **page_config}
    return render_template('home.html', **merged_config)

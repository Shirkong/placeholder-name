from flask import Flask, render_template, request, redirect, url_for
import pandas as pd

web = Flask(__name__)

# Load the CSV file once at startup
try:
    df = pd.read_csv("framedata.csv")
except FileNotFoundError:
    # Fallback placeholder if your CSV file isn't created yet
    df = pd.DataFrame(columns=["Attack", "Notation", "Damage"])

@web.route("/")
def home():
    return render_template("website.html")

# FIXED: Changed app to web, and added "GET" to methods so the page can actually load
@web.route("/wiki", methods = ["GET", "POST"])
def wiki():
    # Convert dataframe into a dynamic Pico CSS compatible table block
    table_html = df.to_html(
        index=False,
        classes="striped",
        border=0,
        justify="left"
    )
    # Pass the table directly into your beautiful template shell
    return render_template("website_wiki.html", table_html=table_html)

# FIXED: Changed @app.route to @web.route
@web.route('/submit-feedback', methods=['POST'])
def submit_feedback():
    # Capture the data from the form
    liked = request.form.get('liked_game')
    comments = request.form.get('feedback_text')
    return render_template("Thanks.html")
    
    # Example: Print to python console (Replace this with database storage or log saving)
    print(f"Feedback Received! Liked: {liked} | Comments: {comments}")
    
    # Redirect user back to the wiki page
    return redirect(url_for('wiki'))

if __name__ == "__main__":
    web.run(debug=True)

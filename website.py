from flask import Flask, render_template
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


@web.route("/wiki")
def wiki():
    # Convert dataframe into a dynamic Pico CSS compatible table block
   # table_html = df.to_html(
    #    index=False, classes="striped", border=0, justify="left"
    #)
    return render_template("website_wiki.html",
                            move = Move,
                           startup = Startup,
                           active = Active,
                           recovery = Recovery,
                           des = Description
                          )
    
    # Pass the table directly into your beautiful template shell
    return render_template("website_wiki.html", table_html=table_html)


if __name__ == "__main__":
    web.run(debug=True)

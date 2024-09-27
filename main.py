from flask import Flask, request, render_template

app = Flask(__name__)

@app.route("/")
def index():
    image_url = "/workspaces/Hangout_Planner/templates/index.html" 
    return render_template("index.html", image_url = image_url)

@app.route("/input_page")
def input_page():
    return render_template("input_page.html")


if __name__ == "__main__":
    app.run()
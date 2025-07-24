from flask import Flask, render_template, request
from trait_cost_calculator import process_traits  # Use the full-featured one

app = Flask(__name__)

@app.route("/", methods=["GET", "POST"])
def index():
    input_text = ""
    output = ""
    if request.method == "POST":
        input_text = request.form.get("trait_input", "")
        output = process_traits(input_text)
    return render_template("index.html", input_text=input_text, output=output)

if __name__ == "__main__":
    app.run(debug=True)
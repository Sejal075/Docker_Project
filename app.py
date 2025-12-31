from flask import Flask, render_template, request

app = Flask(__name__)

@app.route("/", methods=["GET", "POST"])
def index():
    student = None

    if request.method == "POST":
        student = {
            "name": request.form.get("name"),
            "email": request.form.get("email"),
            "course": request.form.get("course")
        }

    return render_template("index.html", student=student)

if __name__ == "__main__":
    app.run(debug=True, host="0.0.0.0", port=8080)

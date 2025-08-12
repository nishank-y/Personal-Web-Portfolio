from flask import Flask, render_template, request

app = Flask(__name__)

@app.route("/", methods=["GET", "POST"])
def home():
    if request.method == "POST":
        name = request.form.get("name")
        email = request.form.get("email")
        message = request.form.get("message")
        print(f"Message from {name} ({email}): {message}")
        return render_template("index.html", success=True)
    return render_template("index.html", success=False)

if __name__ == "__main__":
    app.run(debug=True)

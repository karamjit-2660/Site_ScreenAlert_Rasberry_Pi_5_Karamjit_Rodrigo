from flask import Flask, render_template

app = Flask(__name__)

@app.route("/")
def home():
    return render_template("screen_alert.html")

@app.route("/historico")
def historico():
    return render_template("historico.html")

if __name__ == "__main__":
    app.run(debug=True)
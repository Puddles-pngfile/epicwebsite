from flask import Flask, render_template
import random  

app = Flask(__name__)



@app.route("/")
def home():
    return render_template("home.html")

@app.route("/generator")
def number():
    return render_template("number.html", rand = random.randint(0,100)





if __name__ == "__main__":
    app.run(debug=True)




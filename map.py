from flask import Flask, render_template

app = Flask(__name__)

#mapping url
@app.route("/")
@app.route("/<users>")
def index(users=None):
  return render_template("user.html", users=users)

#Passing Objects into Templates
@app.route("/shoping")
def shoping():
  food = ["chicken", "tuna", "kebab"]
  return render_template("shoping.html", food=food)

if __name__ == '__main__':
  app.run(debug=True)
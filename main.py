from flask import Flask, render_template

app = Flask(__name__)

#basic html templates
@app.route("/profile/<name>")
def profile(name):
	return render_template("profile.html", name=name)

#mapping url
@app.route("/<users>")
def index(user=None):
  return render_template("user.html", user=user)
if __name__ == '__main__':
  app.run(debug=True)
from flask import Flask, request

app = Flask(__name__)

#basic routing
@app.route('/')
def index():
  return 'this is methos %s' % request.method

#http request
@app.route('/blog', methods=['GET','POST'])
def blog():
  if request.method == 'POST':
    return "you arre using post"
  else:
    return "you are probably using get" 

#basic routing with user
@app.route('/andre')
def andre():
  return '<h2>andre you are good</h2>'

#routing with username
@app.route('/profile/<username>')
def profil(username):
  return "<h2>hey there %s</h2>" % username

#routing with params id
@app.route('/post/<int:post_id>')
def show_post(post_id):
  return "<h2>post id %s</h2>" % post_id

if __name__ == '__main__':
  app.run(debug=True)
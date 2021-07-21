from flask import Flask
  
app = Flask(__name__)
  
@app.route("/")
def home_view():
    script=server_document("http://localhost:5006/flaskbokeh1")
    return render_template('flaskbokeh1.html',bokS=script)

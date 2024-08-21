from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def principal():
    return render_template("home.html")

if __name__=="__main__":
    app.run(host='127.0.0.9',port=4455,debug=True)

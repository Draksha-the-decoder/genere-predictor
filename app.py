from flask import Flask, request, render_template

app = Flask(__name__)

@app.route('/')
def index():
    return render_template("home.html")

@app.route('/result',methods=['POST'])
def result():
    message = request.form['message']
    # hasil "Sekian"
    return render_template('result.html',text=message)
 
if __name__ == "__main__":
    app.run(debug=True)
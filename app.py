output =['alt.atheism', 'comp.graphics', 'comp.os.ms-windows.misc', 'comp.sys.ibm.pc.hardware', 'comp.sys.mac.hardware', 'comp.windows.x', 'misc.forsale', 'rec.autos', 'rec.motorcycles', 'rec.sport.baseball', 'rec.sport.hockey', 'sci.crypt', 'sci.electronics', 'sci.med', 'sci.space', 'soc.religion.christian', 'talk.politics.guns', 'talk.politics.mideast', 'talk.politics.misc', 'talk.religion.misc']

from flask import Flask, request, render_template
import pickle
app = Flask(__name__)

@app.route('/')
def index():
    return render_template("home.html")

@app.route('/result',methods=['POST'])
def result():
    message = request.form['message']
    article =[message]
    model = pickle.load(open("model.pkl", "rb"))
    result = model.predict(article)       
    return render_template('home.html',text=output[result[0]],myarticle=message)
 
if __name__ == "__main__":
    app.run(debug=True)
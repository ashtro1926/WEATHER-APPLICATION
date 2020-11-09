from flask import Flask,request,render_template
from Weather import Weather

app=Flask(__name__)

@app.route('/')
def Index():
    return render_template('Index.html')

@app.route('/Success',methods=["GET", "POST"])
def Success():
    if request.method == 'POST':
        City=request.form['City']
        App=Weather(str(City))
        Data=App.Find_Data()
        return render_template('Success.html',Data=Data)
    return render_template('Index.html')

if __name__=='__main__':
    app.run(debug=True)

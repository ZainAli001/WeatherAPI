from flask import Flask,render_template,request,redirect, url_for, render_template
from weather import main as get_weather

app = Flask(__name__)

@app.route('/',methods=['GET','POST'])
def index():
    data = None
    if request.method == 'POST':
        city = request.form['cityName']
        state = request.form['stateName']
        country = request.form['countryName']
        data = get_weather(city,state,country)
        return redirect(url_for('index', data=data))
    data = request.args.get('data')
    return render_template('index.html', data=data)

if __name__ == "__main__":
    app.run(debug=True)
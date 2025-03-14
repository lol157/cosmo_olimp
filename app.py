from flask import Flask, render_template, request

app = Flask(__name__)


@app.route('/')
def home():
    days = 3
    credits = 3
    return render_template('base.html', days=days, credits=credits)


@app.route('/input', methods=['GET', 'POST'])
def input():
    if request.method == 'POST':
        return 'post'
    return render_template('input.html')


@app.route('/waypoints', methods=['GET', 'POST'])
def waypoints():
    if request.method == 'POST':
        return 'отдельная точка'
    return render_template('waypoints.html')


@app.route('/days', methods=['GET', 'POST'])
def days():
    if request.method == 'POST':
        return 'отдельный день'
    return render_template('days.html')


app.run(debug=True)

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
        from_api = False
        data = request.form["user_input"]

        if not data:
            from_api = True
        # бд

    return render_template('input.html')


@app.route('/waypoints', methods=['GET', 'POST'])
def waypoints():
    if request.method == 'POST':
        waypoint = request.form['waypoint']
        # данные от бд
        data = {'waypoint': waypoint, 'fuel': 3, 'o2': 3}
        return render_template('waypoint.html', data=data)

    # данные от бд
    waypoints_number = 4
    return render_template('waypoints.html', waypoints=waypoints_number)


@app.route('/days', methods=['GET', 'POST'])
def days():
    if request.method == 'POST':
        day = request.form['day']
        # данные от бд
        data = {'day': day, 'fuel': 4, 'o2': 4, 'power_for_engine': 4,
                'power_for_electricity': 5, 'T': 3, 'sh': 5}
        return render_template('day.html', data=data)

    # данные от бд
    days_number = 6
    return render_template('days.html', days=days_number)


app.run(debug=True)

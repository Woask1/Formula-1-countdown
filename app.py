from datetime import datetime
from flask import Flask, render_template, url_for

app = Flask(__name__)

@app.route('/')
def index():
    currentTime = datetime.now()
    lightsOutTime = datetime(2019, 3, 17, 6, 10)
    timeLeft = lightsOutTime - currentTime
    days = timeLeft.days
    hours, remainder = divmod(timeLeft.seconds, 3600)
    minutes, seconds = divmod(remainder, 60)
    returnString = str(days) + " Days, " + str(hours) + " Hours, " + str(minutes) + " Minutes, " + str(seconds) + " Seconds."
    url_for('static', filename='style.css')
    url_for('static', filename='verstappen.gif')
    return render_template('index.html', timeLeft=returnString)

if __name__ == "__main__":
    app.run(host='0.0.0.0', port=80)

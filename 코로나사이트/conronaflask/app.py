from flask import Flask, render_template
import corona_data
from datetime import date, timedelta

app = Flask(__name__)

@app.route('/')
def index():
    now = date.today()
    now_str = now.strftime("%Y%m%d")
    print(now_str)

    data = corona_data.get_corona_data(now_str,now_str)
    print(data)

    if not data :
        yesterday = now - timedelta(days=1)
        yesterday_str = yesterday.strftime("%Y%m%d")
        print(yesterday_str)

        data= corona_data.get_corona_data(yesterday_str,yesterday_str)
        print(data)

    return render_template('index.html', data=data[1:])

if __name__ == "__main__" :
    app.run(debug=True)

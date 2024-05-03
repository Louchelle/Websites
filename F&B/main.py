from flask import Flask, render_template
import folium
app = Flask(__name__)


def mapview():
    mymap = folium.Map(location=[0, 0], zoom_start=3)
    return mymap._repr_html_()

@app.route('/')
def home():
  return render_template("home.html")

@app.route("/hours")
def hours():
  return render_template("hours.html")

@app.route("/prices")
def prices():
  return render_template("prices.html")
  
@app.route("/AfricanKidsAtire")
def aka():
  return render_template("aka.html")


@app.route("/contact")
def contact():
  return render_template("contact.html")


if __name__ == "__main__":
  app.run(host='0.0.0.0', debug=True, port=8080)

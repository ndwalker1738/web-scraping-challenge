from flask import Flask, render_template, redirect
from flask_pymongo import PyMongo
import scrape 
app=Flask(__name__)
mongo=PyMongo(app,uri="mongodb://localhost:27017/mars_app")

@app.route("/")
def home():

    mars_data = mongo.db.mars.find_one()
    return render_template("index.html", mars=mars_data)

@app.route("/scrape")
def scrape_all():

    mars_data = scrape.scrape_all()
    mongo.db.mars.update({},mars_data,upsert=True)
    return redirect("/")

if __name__ == "__main__":
    app.run(debug=True)


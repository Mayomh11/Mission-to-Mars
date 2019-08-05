from flask import Flask, render_template, redirect 
from flask_pymongo import PyMongo
import pymongo
import scrape_mars

#Create an instance of Flask
app = Flask(__name__)

#Use PyMongo to establish Mongo connection 
conn ='mongodb://localhost:27017'
client = pymongo.MongoClient(conn)

db = client.mars_data_db
collection = db.mars





#Route to render template using the data from Mongo
@app.route("/")
def home():

    mars_scraping = collection.find_one({'_id':'5d333eb54862101974484a09'})

    return render_template('mars.html', mars=mars_scraping)







#import python function from mars_scraping.py
from scrape_mars import scraped_info

# Route that will trigger scrape function.
@app.route("/scrape")
def scrape():
    # Run scrape function.
    mars_mission_data = scraped_info()
    #print (f'in scrape function. will take a few min to  execute  - {type(mars_mission_data)}')
    print (f'>>>>>>>>>>>>> {mars_mission_data}<<<<<<<<<<<<')  

    # Insert mars_mission_data into database
    collection.update_one({"_id": '5d333eb54862101974484a09'}, {"$set": mars_mission_data}, upsert = True)

    # Redirect back to home page
    #return redirect("/", code=302)
    return redirect("http://localhost:5000/", code=302)


if __name__ == "__main__":
    app.run(debug=True)

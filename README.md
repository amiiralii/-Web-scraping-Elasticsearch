Simple Web Scrapping Project

Scraping Data from Bama.ir
Iranian website for buying and selling cars.

The scrap.py file loads the webpage, extract the useful data, and export them into a Json file. The Json file contains 6 values per each post.
+ Car Model
+ Car Name
+ Mileage
+ Production Year
+ City Posted
+ Car Price

The other file, inserttoelastic.py, import the downloaded data from Json file and add it to the local elastic search database. The mentioned dataset will be added to an index called 'Cars'.

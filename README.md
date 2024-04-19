# python-api-challenge

Instructions

This activity is broken down into two deliverables, WeatherPy and VacationPy.

                                                                                      Part 1: WeatherPy

In this deliverable, you'll create a Python script to visualize the weather of over 500 cities of varying distances from the equator. You'll use the citipy Python libraryLinks to an external site., the OpenWeatherMap APILinks to an external site., and your problem-solving skills to create a representative model of weather across cities. For this part, you'll use the WeatherPy.ipynb Jupyter notebook provided in the starter code ZIP file. 


Requirement 1: 

Create Plots to Showcase the Relationship Between Weather Variables and Latitude
To fulfill the first requirement, you'll use the OpenWeatherMap API to retrieve weather data from the cities list generated in the starter code. Next, you'll create a series of scatter plots to showcase the following relationships:

  - Latitude vs. Temperature

  - Latitude vs. Humidity

  - Latitude vs. Cloudiness

  - Latitude vs. Wind Speed


Requirement 2: 

Compute Linear Regression for Each Relationship
To fulfill the second requirement, compute the linear regression for each relationship. Separate the plots into Northern Hemisphere (greater than or equal to 0 degrees latitude) and Southern Hemisphere (less than 0 degrees latitude). You may find it helpful to define a function in order to create the linear regression plots. Next, create a series of scatter plots with the linear regression line, the model's formula, and the r values. 

  - Northern Hemisphere: Temperature vs. Latitude

  - Southern Hemisphere: Temperature vs. Latitude

  - Northern Hemisphere: Humidity vs. Latitude

  - Southern Hemisphere: Humidity vs. Latitude

  - Northern Hemisphere: Cloudiness vs. Latitude

  - Southern Hemisphere: Cloudiness vs. Latitude

  - Northern Hemisphere: Wind Speed vs. Latitude

  - Southern Hemisphere: Wind Speed vs. Latitude

After each pair of plots, explain what the linear regression is modeling. Describe any relationships that you notice and any other findings you may uncover.


                                                                      Part 2: VacationPy
In this deliverable, you'll use your weather data skills to plan future vacations. Also, you'll use Jupyter notebooks, the geoViews Python library, and the Geoapify API.
Your main tasks will be to use the Geoapify API and the geoViews Python library and employ your Python skills to create map visualizations.Create a map that displays a point for every city in the city_data_df DataFrame as shown in the following image. The size of the point should be the humidity in each city.



  ****NOTE

  
  Feel free to adjust your specifications but make sure to set a reasonable limit to the number of rows returned by your API requests.

  Create a new DataFrame called hotel_df to store the city, country, coordinates, and humidity.

  For each city, use the Geoapify API to find the first hotel located within 10,000 meters of your coordinates.

  Add the hotel name and the country as additional information in the hover message for each city on the map as in the following image: Hotel map



    ***Hints and Considerations***
    The city data that you generate is based on random coordinates and different query times, so your outputs will not be an exact match to the provided starter notebook.

    If you'd like a refresher on the geographic coordinate system, this siteLinks to an external site. has great information.

    Take some time to study the OpenWeatherMap API. Based on your initial study, you should be able to answer basic questions about the API: Where do you request the API key? Which Weather API in particular will you need? What URL endpoints does it expect? What     JSON structure does it respond with? Before you write a line of code, you should have a crystal-clear understanding of your intended outcome.

    A starter code for citipy has been provided. However, if you're craving an extra challenge, push yourself to learn how it works by using the citipy Python libraryLinks to an external site.. Before you try to incorporate the library in your analysis, start       with simple test cases outside of your main script to confirm that you are using it correctly. Often, when introduced to a new library, learners spend hours trying to figure out errors in their code when a simple test case can save you a lot of time and         frustration.


    While building your script, pay attention to the cities you are using in your query pool. Are you covering the full range of latitudes and longitudes? Or are you choosing 500 cities from one region of the world? Even if you were a geography genius, simply       listing 500 cities based on your personal selection would create a biased dataset. Try to think of ways that you can counter these selection issues.




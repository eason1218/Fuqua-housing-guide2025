# Fuqua_housing_guide

## Project Overview

The Fuqua Housing Map is an interactive map application developed using Python and Folium. It serves prospective and current Duke Fuqua MBA students by providing detailed visualizations of recommended housing options around Duke University's Fuqua School of Business in Durham, North Carolina. The map integrates data sourced directly from the official Duke Fuqua MBA Housing Guide, featuring apartment ratings and reviews provided by current MBA students.

## Features

Interactive Map Interface: Intuitive navigation powered by Folium.

Durham City Boundaries: Visual outline of Durham city limits.

Road Networks: Clear depiction of major roads for easier orientation.

Apartment Markers: Interactive markers featuring detailed property information.

Comprehensive Ratings: Displays overall ratings, price levels, management quality, amenities, value, social engagement, and safety, directly sourced from Fuqua MBA student reviews.

Embedded Images: Visual previews of properties embedded within map pop-ups.

## Dataset Description

The application uses datasets from the official Duke Fuqua MBA Housing Guide:

Apartment Listings (33 properties)

Attributes: Property Name, Overall Rating (scale 1-10), Price Range ($ to $$$$), Geographic Coordinates, Property Website URL.

Additional Ratings CSV (Apartment_Ratings.csv)

Attributes: Property Name, Management, Amenities, Value, Social Engagement, Safety (rated from 1 to 4 stars based on student feedback).

Geospatial Data:

City_of_Durham_Boundary.geojson: Durham city boundary.

Roads.geojson: Road network within Durham.

Property Images:

Images stored in the images/ directory, embedded directly into interactive property markers through base64 encoding.

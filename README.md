# Fuqua Housing Map

## Overview

The **Fuqua Housing Map** is an interactive Python application designed for Duke Fuqua MBA students to easily visualize and explore recommended housing options near Duke University's Fuqua School of Business in Durham, North Carolina. Built using Folium, the application leverages data from the official Duke Fuqua MBA Housing Guide, including apartment ratings and student reviews.

---

## Features

- **Interactive Map**: Easy-to-use interface powered by Folium.
- **Durham Boundaries**: Clearly defined city limits.
- **Road Network**: Visible major roads for convenient navigation.
- **Property Markers**: Detailed apartment information accessible through interactive markers.
- **Apartment Ratings**: Comprehensive details including overall ratings, price range, management quality, amenities, value, social interactions, and safety.
- **Embedded Property Images**: Visual previews directly within the interactive markers.

---

## Data Sources

This project utilizes data from the official **Duke Fuqua MBA Housing Guide**, specifically:

- **Apartment Listings (33 properties)**
  - Attributes: Name, Overall Rating (1-10), Price ($ to $$$$), Coordinates, URL.

- **Additional Ratings (`Apartment_Ratings.csv`)**
  - Attributes: Management, Amenities, Value, Social Engagement, Safety (1-4 stars).

- **Geospatial Files**
  - `City_of_Durham_Boundary.geojson`: Durham city boundaries.
  - `Roads.geojson`: Durham road network.

- **Images**
  - Stored in the `images/` directory; embedded in the map using base64 encoding.


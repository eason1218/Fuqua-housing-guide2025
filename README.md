# Fuqua_housing_guide

## Overview

The **Fuqua Housing Map** is an interactive application developed with Python and Folium. It is designed to serve both prospective and current Duke Fuqua MBA students by providing detailed visualizations of recommended housing options near Duke University's Fuqua School of Business in Durham, North Carolina. The map leverages data directly sourced from the official Duke Fuqua MBA Housing Guide, incorporating apartment ratings and reviews from current MBA students.

## Features

- **Interactive Map Interface:**  
  Intuitive navigation powered by Folium.

- **Durham City Boundaries:**  
  Visual outlines of Durham's city limits.

- **Road Networks:**  
  Clear depiction of major roads for enhanced orientation.

- **Apartment Markers:**  
  Interactive markers that provide detailed property information.

- **Comprehensive Ratings:**  
  Displays overall ratings, price levels, management quality, amenities, value, social engagement, and safety—all based on Fuqua MBA student reviews.

- **Embedded Images:**  
  Visual previews of properties are embedded directly within map pop-ups.

## Dataset Description

The application utilizes datasets from the official Duke Fuqua MBA Housing Guide:

### Apartment Listings (33 Properties)

- **Attributes:**
  - Property Name
  - Overall Rating (scale 1–10)
  - Price Range (from $ to $$$$)
  - Geographic Coordinates
  - Property Website URL

### Additional Ratings (CSV: `Apartment_Ratings.csv`)

- **Attributes:**
  - Property Name
  - Management
  - Amenities
  - Value
  - Social Engagement
  - Safety (rated on a scale of 1 to 4 stars, based on student feedback)

### Geospatial Data

- **City Boundary:**  
  `City_of_Durham_Boundary.geojson` – outlines the boundaries of Durham.

- **Road Networks:**  
  `Roads.geojson` – details the road network within Durham.

### Property Images

- **Storage:**  
  Images are stored in the `images/` directory and are embedded directly into interactive property markers via base64 encoding.

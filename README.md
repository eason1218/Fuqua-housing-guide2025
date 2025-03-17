# Fuqua Housing Guide2025

## Project Overview

The **Fuqua Housing Guide2025** is an interactive Python-based application designed for prospective and current Duke Fuqua students. Utilizing Folium, this map visually presents recommended housing options near Duke University's Fuqua School of Business in Durham, North Carolina. The application incorporates data directly from the official Duke Fuqua Housing Guide, providing detailed apartment ratings and student reviews.

---

## Features

- **Interactive Map Interface:** User-friendly navigation powered by Folium.
- **Durham City Boundaries:** Clearly outlined city boundaries.
- **Road Networks:** Easily navigable representation of major roads.
- **Apartment Markers:** Detailed property information through interactive markers.
- **Comprehensive Ratings:** Includes overall ratings, pricing, management quality, amenities, value, social environment, and safety based on Fuqua MBA student feedback.
- **Embedded Images:** Property images integrated within interactive map pop-ups.

---

## Dataset Description

Datasets used in this application are sourced from the official Duke Fuqua MBA Housing Guide and include:

### Apartment Listings (33 properties)

- **Attributes:** Property Name, Overall Rating (1-10 scale), Price Range (\$ to \$\$\$\$), Geographic Coordinates, Website URL.

### Additional Ratings (`Apartment_Ratings.csv`)

- **Attributes:** Property Name, Management, Amenities, Value, Social Engagement, Safety (ratings from 1 to 4 stars).

### Geospatial Data

- `City_of_Durham_Boundary.geojson`: Durham city boundary outlines.
- `Roads.geojson`: Detailed Durham road network.

### Property Images

- Images stored in the `images/` directory and embedded via base64 encoding.


# Fuqua_housing_guide

\documentclass{article}
\usepackage[margin=1in]{geometry}
\usepackage{hyperref}
\usepackage{listings}
\usepackage{xcolor}

\lstset{
basicstyle=\ttfamily\small,
backgroundcolor=\color{gray!10},
frame=single,
breaklines=true
}

\begin{document}

\section*{Fuqua Housing Map}

\subsection*{Overview}

The \textbf{Fuqua Housing Map} is an interactive Python application designed for Duke Fuqua MBA students to easily visualize and explore recommended housing options near Duke University's Fuqua School of Business in Durham, North Carolina. Built using Folium, the application leverages data from the official Duke Fuqua MBA Housing Guide, including apartment ratings and student reviews.

\section*{Features}

\begin{itemize}
\item \textbf{Interactive Map}: Easy-to-use interface powered by Folium.
\item \textbf{Durham Boundaries}: Clearly defined city limits.
\item \textbf{Road Network}: Visible major roads for convenient navigation.
\item \textbf{Property Markers}: Detailed apartment information accessible through interactive markers.
\item \textbf{Apartment Ratings}: Comprehensive details including overall ratings, price range, management quality, amenities, value, social interactions, and safety.
\item \textbf{Embedded Property Images}: Visual previews directly within the interactive markers.
\end{itemize}

\section*{Data Sources}

This project utilizes data from the official \textbf{Duke Fuqua MBA Housing Guide}, specifically:

\begin{itemize}
\item \textbf{Apartment Listings (33 properties)}
\begin{itemize}
\item Attributes: Name, Overall Rating (1-10), Price ($ to $$$$), Coordinates, URL.
\end{itemize}

\item \textbf{Additional Ratings (\texttt{Apartment_Ratings.csv})}
\begin{itemize}
\item Attributes: Management, Amenities, Value, Social Engagement, Safety (1-4 stars).
\end{itemize}

\item \textbf{Geospatial Files}
\begin{itemize}
\item \texttt{City_of_Durham_Boundary.geojson}: Durham city boundaries.
\item \texttt{Roads.geojson}: Durham road network.
\end{itemize}

\item \textbf{Images}
\begin{itemize}
\item Stored in the \texttt{images/} directory; embedded in the map using base64 encoding.
\end{itemize}
\end{itemize}

\section*{Installation}

Clone the repository and install the necessary Python dependencies:

\begin{lstlisting}[language=bash]
git clone 
cd 
pip install folium geopandas shapely pandas
\end{lstlisting}

\section*{Usage}

Run the script to generate the interactive housing map:

\begin{lstlisting}[language=bash]
python fuqua_housing_map.py
\end{lstlisting}

This creates the map as \texttt{durham_properties_with_base64_images.html}.

\section*{Future Improvements}

\begin{itemize}
\item Include real-time property availability and pricing updates.
\item Add advanced filters tailored to user preferences.
\item Expand map functionality with community-sourced reviews and ratings.
\end{itemize}

\end{document}

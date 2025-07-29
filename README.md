🏅 OlympiTrack

OlympiTrack is a dynamic data analysis and visualization web app for exploring Summer and Winter Olympics data across years. Built using Streamlit, this project offers users an interactive way to analyze country performance, athlete dominance, participation trends, and more from 1896 to 2024.

📊 About the Data

Summer Olympics: Data from 1896 to 2024

Winter Olympics: Data from 1900 to 2014

The dataset includes 1906 Olympics, which are not officially recognized in modern medal tallies. This results in minor differences in medal counts compared to official records.

🎯 Features

Medal tally viewer by year and country

Historical trends: Participating countries, athletes, and events over time

Interactive heatmaps of country-wise sports performance

Insights into most successful athletes, globally and by country

Separate exploration modes for Summer and Winter Olympics

Smooth performance through modular code and optimized data access

🚀 Live Demo

You can access the deployed app here: [olympitrack.onrender.com](https://olympitrack.onrender.com)

🛠️ Technologies Used

Python 3.11+

Pandas for data manipulation

Matplotlib & Seaborn for plotting

Streamlit for web UI

Render for deployment

🧠 Challenges Faced

🔁 Heavy heatmap loading time: Optimized by reducing DataFrame size using drop_duplicates, using pivot_table, and simplifying visuals.

🔧 Slow app startup: Reduced load time by removing redundant preprocessing and modularizing logic into helper.py.

⚙️ Render file path issues: Adjusted relative paths and kept only essential files for production.

🔄 Data discrepancies due to inclusion of 1906 Olympics, which are typically omitted from official records.

🧪 How to Run Locally

Clone the repository:

git clone https://github.com/deeprao03/olympics_analysis.git

Install dependencies:

pip install -r requirements.txt

Run the app:

cd App
streamlit run app.py

✅ Future Improvements

Add event-based filtering (e.g. swimming, athletics)

Include athlete bio integration from public APIs

Add map-based visualizations

Incorporate real-time Olympic updates

👤 Author  
[Deepanshu Rao](https://github.com/deeprao03)

# 🏅 OlympiTrack

**OlympiTrack** is an interactive and insightful data analysis web app for exploring **Summer** and **Winter Olympics** over the years. Built using **Streamlit**, it provides dynamic visualizations and deep insights into athlete dominance, country performance, participation trends, and more — spanning from **1896 to 2024**.

---

## 📊 About the Data

- **Summer Olympics:** 1896 to 2024  
- **Winter Olympics:** 1900 to 2014  
- The dataset **includes the 1906 Intercalated Games**, which are not officially recognized in modern medal counts — leading to **minor discrepancies** from official records.

---

## 🎯 Key Features

- 🥇 View **medal tallies** by year and country  
- 📈 Explore **historical trends** in participating countries, events, and athletes  
- 🌍 Generate **interactive heatmaps** of country-wise performance  
- 👑 Discover the **most successful athletes**, globally and by country  
- ☀️ Separate analysis for **Summer** and ❄️ **Winter** Olympics  
- ⚙️ **Modular code** structure and **optimized data loading** for better performance  

---

## 🚀 Live Demo

Check out the deployed app here:  
🔗 [https://olympitrack.onrender.com](https://olympitrack.onrender.com)

---

## 🛠️ Tech Stack

- **Python 3.11+**
- **Pandas** for data manipulation
- **Matplotlib** and **Seaborn** for visualizations
- **Streamlit** for the web interface
- **Render** for deployment

---

## 🧠 Challenges Faced

- 🐢 **Slow heatmap rendering:** Solved by reducing DataFrame size using `drop_duplicates()`, `pivot_table()`, and simplifying the visuals  
- 🕓 **App load time:** Improved by removing redundant preprocessing and modularizing logic into `helper.py`  
- 📁 **File path issues on Render:** Fixed by using relative paths and keeping only production-critical files  
- 📉 **Medal count discrepancy:** Due to inclusion of 1906 games (not part of official Olympic records)

---

## 🧪 How to Run Locally

1. **Clone the repo:**
   ```bash
   git clone https://github.com/deeprao03/olympics_analysis.git

2. **Install dependencies:**
    ```bash
    pip install -r requirements.txt

3.  **Run the app:**
    ```bash
    streamlit run App/app.py

---

✅ Future Improvements
🎯 Add event-specific filters (e.g., swimming, gymnastics)

🧑‍💼 Integrate athlete bios from public APIs

🗺️ Include map-based visualizations

📡 Add real-time Olympic updates (when API available)

---

👤 Author
Deepanshu Rao
🔗 GitHub Profile
---

### ✅ How to Use It
1. Copy the above code into your `README.md` file.
2. Make sure the deployment link and repo link are correct.
3. If you have screenshots, you can insert them like this:
   ```markdown
   ![App Screenshot](link-to-screenshot.png)
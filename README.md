# government-housing-expenditure-map-World-Bank-Data-
Interactive choropleth map visualizing government housing expenditure by country and year using Python, Pandas, and Plotly.
# Government Housing Expenditure – Interactive World Map

This project visualizes **government expenditure on housing** across countries using an **interactive choropleth map with a year slider**.  
The visualization allows users to explore how public housing expenditure changes **over time and across countries**.

---

## 📊 What This Project Does

- Cleans and filters raw government expenditure data
- Removes ratio-based values and zero observations
- Converts expenditure values into **billion USD** for readability
- Aggregates data by **country and year**
- Creates an **interactive animated world map** with a **time slider**

---

## 🌍 Output

- Interactive choropleth map
- Hover to view country-level expenditure
- Year slider to visualize changes over time
- Exported as a standalone **HTML file** (`output_map.html`)

---

## 🛠️ Tools & Libraries Used

- **Python**
- **Pandas** – data cleaning and aggregation
- **NumPy** – numerical operations
- **Plotly Express** – interactive geospatial visualization
- **GeoPandas** (imported for potential spatial extensions)

---


---

## 🧠 Methodology

1. Selected relevant columns:
   - Country
   - Year
   - Expenditure value
   - Unit type
2. Removed missing values and ratio-based observations
3. Converted expenditure values to **billions**
4. Grouped data by country and year
5. Generated an animated choropleth map using Plotly

---

## 🚀 How to Run

1. Install dependencies:
   ```bash
   pip install pandas numpy plotly geopandas matplotlib




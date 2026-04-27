#  PM2.5 Emissions Dashboard

## Project Overview
This project presents an interactive dashboard developed using Streamlit to analyse PM2.5 emissions data. The dashboard converts complex environmental data into clear and easy-to-understand visualisations, helping users explore pollution patterns and support sustainability decision-making.

The analysis is based on the *Greenhouse Gas and Air Pollutant Emissions* dataset, which includes information on emissions across sectors, subsectors, regions, and geographical locations.


## Objectives
- Analyse PM2.5 emission trends over time  
- Identify high-emission sectors and subsectors  
- Compare emissions across regions  
- Visualise geographical distribution of emissions  
- Provide an interactive dashboard for data exploration  

---

## Dataset
- Source: Humanitarian Data Exchange 
- Dataset: Greenhouse Gas and Air Pollutant Emissions  
- Focus: Spain  
- Format: CSV (cleaned dataset used for dashboard)  

---

## Technologies Used
- Python  
- Streamlit  
- Pandas  
- Plotly  

---

## Dashboard Features

### KPI Metrics
- Total Emissions  
- Average Emissions  
- Maximum Emissions  

### Filters
- Sector  
- Year  

### Visualisations
- Emissions Trend Over Time  
- Top 10 Regions by Emissions  
- Top Contributing Subsectors   
- Geographical Distribution   

### Additional Feature
- Dataset preview table  

---

##  How to Run the Project

### 1. Clone the Repository
```bash
git clone https://github.com/your-username/pm25-dashboard.git
cd pm25-dashboard

Install Required Libraries
pip install -r requirements.txt

Run the Application
python -m streamlit run app.py

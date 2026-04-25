import streamlit as st
import pandas as pd
import plotly.express as px

# -----------------------------
# TITLE
st.title("PM2.5 Emissions Dashboard")

# -----------------------------
# LOAD DATA
df = pd.read_csv("Cleaned_PM2.5_dataset.csv")

# FIX: Ensure year is integer (avoids 2024.5 issue)
df["year"] = df["year"].astype(int)

# -----------------------------
# SIDEBAR FILTERS
st.sidebar.header("Filter Data")

sector = st.sidebar.selectbox(
    "Select Sector",
    sorted(df["sector"].dropna().unique())
)

year = st.sidebar.selectbox(
    "Select Year",
    ["All"] + sorted(df["year"].dropna().unique())
)

# Apply filters
if year == "All":
    filtered_df = df[df["sector"] == sector]
else:
    filtered_df = df[
        (df["sector"] == sector) &
        (df["year"] == year)
    ]

# -----------------------------
# KPI SECTION (RED BORDER STYLE)
# KPI SECTION (IMPROVED VISIBILITY)
st.subheader("Key Performance Indicators")

st.markdown("""
<style>
.kpi-card {
    padding: 18px;
    border-radius: 12px;
    text-align: center;
    background-color: #b1cee6;
    box-shadow: 2px 2px 10px rgba(0,0,0,0.15);
    color: black;
}

.kpi-title {
    font-size: 15px;
    font-weight: bold;
    color: #696969;
    margin-bottom: 8px;
}

.kpi-value {
    font-size: 24px;
    font-weight: bold;
    color: black;
}
</style>
""", unsafe_allow_html=True)

col1, col2, col3 = st.columns(3)

with col1:
    st.markdown(f"""
    <div class="kpi-card">
        <div class="kpi-title"> Total Emissions</div>
        <div class="kpi-value">{filtered_df['PM25_Emissions'].sum():,.2f}</div>
    </div>
    """, unsafe_allow_html=True)

with col2:
    st.markdown(f"""
    <div class="kpi-card">
        <div class="kpi-title"> Average Emissions</div>
        <div class="kpi-value">{filtered_df['PM25_Emissions'].mean():,.2f}</div>
    </div>
    """, unsafe_allow_html=True)

with col3:
    st.markdown(f"""
    <div class="kpi-card">
        <div class="kpi-title"> Max Emissions</div>
        <div class="kpi-value">{filtered_df['PM25_Emissions'].max():,.2f}</div>
    </div>
    """, unsafe_allow_html=True)

# -----------------------------
# VISUAL 1 - TREND LINE
st.subheader("1. Emissions Trend Over Time")

trend_data = df[df["sector"] == sector]
trend_data = trend_data.groupby("year", as_index=False)["PM25_Emissions"].sum()

fig1 = px.line(
    trend_data,
    x="year",
    y="PM25_Emissions",
    markers=True
)

fig1.update_xaxes(type='category')

st.plotly_chart(fig1, use_container_width=True)

# -----------------------------
# VISUAL 2 - REGION BAR
st.subheader("2. Top 10 Regions by PM2.5 Emissions")

region_data = filtered_df.groupby("Region", as_index=False)["PM25_Emissions"].sum()
region_data = region_data.sort_values("PM25_Emissions", ascending=False).head(10)

fig2 = px.bar(
    region_data,
    x="Region",
    y="PM25_Emissions",
    color="PM25_Emissions",
    text="PM25_Emissions"
)

fig2.update_traces(texttemplate='%{text:.2s}', textposition='outside')

st.plotly_chart(fig2, use_container_width=True)

# -----------------------------
# VISUAL 3 - SUBSECTOR BAR
st.subheader("3. Top Contributing Subsectors")

sub_data = filtered_df.groupby("subsector", as_index=False)["PM25_Emissions"].sum()
sub_data = sub_data.sort_values("PM25_Emissions", ascending=False).head(10)

fig3 = px.bar(
    sub_data,
    x="subsector",
    y="PM25_Emissions",
    color="PM25_Emissions"
)

st.plotly_chart(fig3, use_container_width=True)

# -----------------------------
# VISUAL 4 - MAP
st.subheader("4. Geographical Distribution of Emissions")

fig4 = px.scatter_mapbox(
    filtered_df,
    lat="latitude",
    lon="longitude",
    size="PM25_Emissions",
    color="PM25_Emissions",
    color_continuous_scale="YlOrRd",
    zoom=5,
    mapbox_style="carto-positron",
    hover_name="Region",
    hover_data=["sector", "subsector"]
)

st.plotly_chart(fig4, use_container_width=True)

# -----------------------------
# DATA TABLE
st.subheader("Dataset Preview")
st.dataframe(filtered_df)
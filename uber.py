import pandas as pd
import plotly.express as px
import streamlit as st

st.set_page_config(page_title="Uber Trips NYC", page_icon="🚕", layout="wide")

DAYS = ["Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday", "Sunday"]


@st.cache_data
def load_data():
    df = pd.read_csv("uber-raw-data-sep14.csv")
    df["Date/Time"] = pd.to_datetime(df["Date/Time"], format="%m/%d/%Y %H:%M:%S")
    df["Hour"] = df["Date/Time"].dt.hour
    df["Day"] = df["Date/Time"].dt.day
    df["Weekday"] = df["Date/Time"].dt.day_name()
    return df


df = load_data()

st.title("🚕 Uber Trips in New York City")
st.caption("Exploratory analysis of Uber pickups, September 2014.")

# Sidebar filters
bases = st.sidebar.multiselect("Base", sorted(df.Base.unique()), default=sorted(df.Base.unique()))
days = st.sidebar.slider("Day of month", 1, 30, (1, 30))
d = df[df.Base.isin(bases) & df.Day.between(*days)]

# KPIs
c1, c2, c3 = st.columns(3)
c1.metric("Total trips", f"{len(d):,}")
c2.metric("Busiest hour", f"{d.Hour.mode()[0]}:00" if len(d) else "-")
c3.metric("Busiest weekday", d.Weekday.mode()[0] if len(d) else "-")

tab1, tab2, tab3, tab4 = st.tabs(["Time patterns", "Locations", "Bases", "Data"])

with tab1:
    col1, col2 = st.columns(2)
    hourly = d.Hour.value_counts().sort_index().rename_axis("Hour").reset_index(name="Trips")
    col1.plotly_chart(px.bar(hourly, x="Hour", y="Trips", title="Trips by hour"), use_container_width=True)
    weekly = d.Weekday.value_counts().reindex(DAYS).rename_axis("Weekday").reset_index(name="Trips")
    col2.plotly_chart(px.bar(weekly, x="Weekday", y="Trips", title="Trips by weekday"), use_container_width=True)

    heat = pd.crosstab(d.Weekday, d.Hour).reindex(DAYS)
    st.plotly_chart(px.imshow(heat, aspect="auto", color_continuous_scale="YlGnBu",
                              title="Weekday vs hour heatmap"), use_container_width=True)
    daily = d.Day.value_counts().sort_index().rename_axis("Day").reset_index(name="Trips")
    st.plotly_chart(px.bar(daily, x="Day", y="Trips", title="Trips by day of month"), use_container_width=True)

with tab2:
    nyc = d[d.Lat.between(40.5, 41.0) & d.Lon.between(-74.2, -73.7)]
    st.subheader("Pickup hotspots (10,000 random trips)")
    st.map(nyc.sample(min(10000, len(nyc)), random_state=42).rename(columns={"Lat": "lat", "Lon": "lon"}))
    top = d.groupby([d.Lat.round(2), d.Lon.round(2)]).size().nlargest(10).reset_index(name="Trips")
    top["Area"] = top.Lat.astype(str) + ", " + top.Lon.astype(str)
    fig = px.bar(top, x="Trips", y="Area", orientation="h", title="Top 10 pickup areas")
    fig.update_yaxes(autorange="reversed")
    st.plotly_chart(fig, use_container_width=True)

with tab3:
    col1, col2 = st.columns(2)
    base_counts = d.Base.value_counts().rename_axis("Base").reset_index(name="Trips")
    col1.plotly_chart(px.bar(base_counts, x="Base", y="Trips", title="Trips by base"), use_container_width=True)
    share = d.Weekday.isin(["Saturday", "Sunday"]).map({True: "Weekend", False: "Weekday"}).value_counts()
    col2.plotly_chart(px.pie(values=share.values, names=share.index, hole=0.6, title="Weekday vs weekend"),
                      use_container_width=True)

with tab4:
    st.dataframe(d.head(1000), use_container_width=True)
    st.caption("Showing the first 1,000 rows of the filtered data.")
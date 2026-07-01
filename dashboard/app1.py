import streamlit as st
import pandas as pd
import joblib
import plotly.express as px
import plotly.graph_objects as go
from datetime import datetime

# PAGE CONFIG
st.set_page_config(
    page_title="LogisChain AI",
    page_icon="🚚",
    layout="wide",
    initial_sidebar_state="expanded"
)

# LOAD MODEL
model = joblib.load("models/financial_risk_model.pkl")

try:
    data = pd.read_csv("data/Financial_Risk_Dataset.csv")
except:
    data = pd.read_csv("data/smart_logistics_dataset.csv")

# CUSTOM CSS
st.markdown("""
<style>

.main{
background:#f4f8fb;
}

.block-container{
padding-top:2rem;
padding-left:2rem;
padding-right:2rem;
}

div[data-testid="metric-container"]{
background:white;
padding:20px;
border-radius:18px;
box-shadow:0px 8px 20px rgba(0,0,0,.10);
border-left:6px solid #1f77b4;
}

.stButton>button{
background:linear-gradient(90deg,#0072ff,#00c6ff);
color:white;
height:55px;
border:none;
border-radius:12px;
font-size:18px;
font-weight:bold;
width:100%;
}

.stButton>button:hover{
background:linear-gradient(90deg,#005bea,#00a8ff);
}

section[data-testid="stSidebar"]{
background:#eef5ff;
}

</style>
""",unsafe_allow_html=True)

# -------------------------------------------------
# HEADER
# -------------------------------------------------

st.title("🚚 LogisChain AI")

st.markdown(
"""
### AI Powered Supply Chain Financial Risk Dashboard

Modern analytics dashboard for predicting financial risk using Machine Learning.
"""
)

st.divider()

# KPI CARDS
c1,c2,c3,c4=st.columns(4)

with c1:
    st.metric(
        "📦 Total Shipments",
        len(data)
    )

with c2:
    st.metric(
        "🎯 Model Accuracy",
        "92%"
    )

with c3:
    st.metric(
        "🤖 Algorithm",
        "Random Forest"
    )

with c4:
    st.metric(
        "⚠️ Current Prediction",
        "Waiting..."
    )

st.divider()

# SIDEBAR
st.sidebar.title("🚚 Logistics Details")

st.sidebar.markdown("Enter shipment information")

latitude = st.sidebar.number_input(
    "Latitude",
    value=22.57
)

longitude = st.sidebar.number_input(
    "Longitude",
    value=88.36
)

inventory = st.sidebar.slider(
    "Inventory Level",
    0,
    500,
    250
)

temperature = st.sidebar.slider(
    "Temperature",
    0.0,
    50.0,
    35.0
)

humidity = st.sidebar.slider(
    "Humidity",
    0.0,
    100.0,
    75.0
)

waiting_time = st.sidebar.slider(
    "Waiting Time",
    0,
    60,
    20
)

transaction = st.sidebar.number_input(
    "User Transaction Amount",
    value=450
)

purchase = st.sidebar.slider(
    "Purchase Frequency",
    1,
    10,
    5
)

asset = st.sidebar.slider(
    "Asset Utilization",
    0,
    100,
    85
)

demand = st.sidebar.slider(
    "Demand Forecast",
    0,
    1000,
    700
)

year = st.sidebar.number_input(
    "Year",
    value=2024
)

month = st.sidebar.slider(
    "Month",
    1,
    12,
    6
)

day = st.sidebar.slider(
    "Day",
    1,
    31,
    30
)

hour = st.sidebar.slider(
    "Hour",
    0,
    23,
    10
)

day_week = st.sidebar.selectbox(
    "Day Of Week",
    [0,1,2,3,4,5,6]
)

detour = st.sidebar.selectbox(
    "Traffic Detour",
    [0,1]
)

heavy = st.sidebar.selectbox(
    "Heavy Traffic",
    [0,1]
)

st.sidebar.divider()

predict = st.sidebar.button(
    "🚀 Predict Financial Risk"
)

# CREATE INPUT DATAFRAME
sample = pd.DataFrame({

"Latitude":[latitude],

"Longitude":[longitude],

"Inventory_Level":[inventory],

"Temperature":[temperature],

"Humidity":[humidity],

"Waiting_Time":[waiting_time],

"User_Transaction_Amount":[transaction],

"User_Purchase_Frequency":[purchase],

"Asset_Utilization":[asset],

"Demand_Forecast":[demand],

"Year":[year],

"Month":[month],

"Day":[day],

"Hour":[hour],

"Day_of_Week":[day_week],

"Traffic_Status_Detour":[detour],

"Traffic_Status_Heavy":[heavy]

})

# PREDICTION
prediction = None

if predict:

    prediction = model.predict(sample)[0]
    st.success("Prediction Completed Successfully ✅")

# MAIN DASHBOARD
if prediction is not None:

    st.divider()

    # Updated KPI Cards
    k1, k2, k3, k4 = st.columns(4)
    with k1:
        st.metric(
            "📦 Total Shipments",
            len(data)
        )

    with k2:
        st.metric(
            "🎯 Model Accuracy",
            "92%"
        )

    with k3:
        st.metric(
            "🤖 Algorithm",
            "Random Forest"
        )

    with k4:
        st.metric(
            "⚠️ Current Prediction",
            prediction
        )

    st.divider()

    # Prediction + Gauge
    left, right = st.columns([2,1])

    with left:

        st.subheader("🎯 Prediction Result")

        if prediction == "Low":

            st.success("""
### 🟢 LOW RISK

Shipment is financially safe.

No immediate action required.
""")

            gauge_value = 20

        elif prediction == "Medium":

            st.warning("""
### 🟡 MEDIUM RISK

Shipment requires monitoring.

Some operational improvements are recommended.
""")

            gauge_value = 60

        else:

            st.error("""
### 🔴 HIGH RISK

Immediate attention required.

Financial loss probability is high.
""")

            gauge_value = 95

    with right:

        gauge = go.Figure(go.Indicator(

            mode="gauge+number",

            value=gauge_value,

            title={"text":"Risk Score"},

            gauge={

                "axis":{"range":[0,100]},

                "bar":{"color":"darkblue"},

                "steps":[

                    {"range":[0,40],"color":"green"},

                    {"range":[40,70],"color":"gold"},

                    {"range":[70,100],"color":"red"}

                ]

            }

        ))

        gauge.update_layout(height=350)
        st.plotly_chart(
            gauge,
            use_container_width=True
        )

    st.divider()

    # Shipment Summary
    st.subheader("📦 Shipment Summary")

    s1, s2, s3 = st.columns(3)

    with s1:

        st.info(f"""
Inventory

### {inventory}
""")

        st.info(f"""
Temperature

### {temperature} °C
""")

    with s2:

        st.info(f"""
Humidity

### {humidity} %
""")

        st.info(f"""
Waiting Time

### {waiting_time} min
""")

    with s3:

        st.info(f"""
Demand

### {demand}
""")

        st.info(f"""
Traffic

### {"Heavy" if heavy else "Normal"}
""")

    st.divider()

    # AI Recommendation
    st.subheader("🤖 AI Recommendation")

    if prediction=="Low":

        st.success("""
✅ Continue current logistics strategy.

* Maintain inventory

* Regular monitoring

* No action required
""")

    elif prediction=="Medium":

        st.warning("""
⚠️ Suggested Improvements

* Reduce waiting time

* Increase inventory optimization

* Monitor traffic

* Improve transport scheduling
""")

    else:

        st.error("""
🚨 Immediate Action Required

* Reduce logistics delays

* Increase warehouse efficiency

* Optimize traffic routes

* Allocate emergency resources

* Investigate financial bottlenecks
""")

# ANALYTICS DASHBOARD
st.divider()
st.header("📊 Analytics Dashboard")

tab1, tab2, tab3 = st.tabs([
    "📈 Risk Analysis",
    "📦 Operations",
    "🌍 Dataset"
])

# TAB 1
with tab1:
    col1, col2 = st.columns(2)
    with col1:

        st.subheader("Financial Risk Distribution")

        risk_count = data["Financial_Risk"].value_counts()

        fig = px.pie(
            values=risk_count.values,
            names=risk_count.index,
            hole=.45,
            color=risk_count.index,
            color_discrete_map={
                "Low":"green",
                "Medium":"orange",
                "High":"red"
            }
        )

        fig.update_layout(height=420)

        st.plotly_chart(
            fig,
            use_container_width=True
        )

    with col2:

        st.subheader("Waiting Time")

        fig = px.histogram(
            data,
            x="Waiting_Time",
            nbins=20,
            color_discrete_sequence=["royalblue"]
        )

        fig.update_layout(height=420)

        st.plotly_chart(
            fig,
            use_container_width=True
        )

# TAB 2
with tab2:

    c1,c2=st.columns(2)

    with c1:

        st.subheader("Inventory Level")

        fig = px.histogram(
            data,
            x="Inventory_Level",
            nbins=25,
            color_discrete_sequence=["teal"]
        )

        st.plotly_chart(
            fig,
            use_container_width=True
        )

    with c2:

        st.subheader("Demand Forecast")

        fig = px.histogram(
            data,
            x="Demand_Forecast",
            nbins=25,
            color_discrete_sequence=["purple"]
        )

        st.plotly_chart(
            fig,
            use_container_width=True
        )

    st.divider()

    c3,c4=st.columns(2)

    with c3:

        st.subheader("Temperature")

        fig = px.box(
            data,
            y="Temperature",
            color_discrete_sequence=["red"]
        )

        st.plotly_chart(
            fig,
            use_container_width=True
        )

    with c4:

        st.subheader("Humidity")

        fig = px.box(
            data,
            y="Humidity",
            color_discrete_sequence=["dodgerblue"]
        )

        st.plotly_chart(
            fig,
            use_container_width=True
        )

# TAB 3
with tab3:

    st.subheader("Dataset Preview")

    st.dataframe(
        data.head(20),
        use_container_width=True
    )

    st.divider()

    st.subheader("Dataset Statistics")

    s1,s2,s3,s4=st.columns(4)

    with s1:
        st.metric("Rows",len(data))

    with s2:
        st.metric("Columns",len(data.columns))

    with s3:
        st.metric(
            "Missing Values",
            int(data.isnull().sum().sum())
        )

    with s4:
        st.metric(
            "Duplicates",
            int(data.duplicated().sum())
        )

    st.divider()

    st.subheader("Sample Data")

    st.dataframe(
        data.sample(10),
        use_container_width=True
    )

# FEATURE IMPORTANCE
st.divider()

st.header("🔥 Model Insights")

try:

    feature_names = sample.columns

    importance = pd.DataFrame({

        "Feature": feature_names,

        "Importance": model.feature_importances_

    })

    importance = importance.sort_values(
        by="Importance",
        ascending=False
    )

    fig = px.bar(
        importance,
        x="Importance",
        y="Feature",
        orientation="h",
        color="Importance",
        color_continuous_scale="Blues",
        title="Feature Importance"
    )

    fig.update_layout(height=500)

    st.plotly_chart(
        fig,
        use_container_width=True
    )

except:

    st.info("Feature importance not available for this trained model.")

# SHIPMENT MAP
st.divider()

st.header("🌍 Shipment Location")

map_df = pd.DataFrame({

    "lat":[latitude],

    "lon":[longitude]

})

st.map(map_df)

# DOWNLOAD BUTTON
st.divider()
st.header("📥 Download Prediction")
csv = sample.to_csv(index=False)

st.download_button(

    label="⬇️ Download Shipment Details",

    data=csv,

    file_name="shipment_prediction.csv",

    mime="text/csv"

)

# PROJECT INFORMATION
st.divider()

st.header("📌 Project Information")

col1,col2=st.columns(2)

with col1:

    st.markdown("""

### 🚚 LogisChain AI

AI Powered Supply Chain Financial Risk Prediction Dashboard.

### Technologies

- Python

- Pandas

- Scikit-learn

- Streamlit

- Plotly

- Random Forest

""")

with col2:

    st.markdown("""

### Model

Random Forest Classifier

### Accuracy

92%

### Target

- Low

- Medium

- High

### Dataset

1000 Logistics Records

""")

# FOOTER
st.divider()

st.markdown(
"""
<center>

<h3>🚚 LogisChain AI</h3>

Machine Learning Internship Project

Developed by <b>Manish Parihar</b>

Made with ❤️ using Python, Streamlit & Scikit-learn

</center>
""",
unsafe_allow_html=True
)
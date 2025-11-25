import streamlit as st
import pandas as pd
import plotly.express as px
import plotly.graph_objects as go

# -----------------------------------------------------------------------------
# 1. APP CONFIGURATION
# -----------------------------------------------------------------------------
st.set_page_config(
    page_title="ForgeFlow Command Center", 
    layout="wide", 
    initial_sidebar_state="collapsed"
)

# -----------------------------------------------------------------------------
# 2. DATA LOADING
# -----------------------------------------------------------------------------
@st.cache_data
def load_data():
    # We only really need the granular predictions file, as it has everything
    predictions = pd.read_csv("data/processed/forgeflow_predictions.csv")
    return predictions

try:
    df_preds = load_data()
except FileNotFoundError:
    st.error("CRITICAL ERROR: 'forgeflow_predictions.csv' not found in 'data/processed/'.")
    st.stop()

# -----------------------------------------------------------------------------
# 3. HEADER SECTION
# -----------------------------------------------------------------------------
st.title("🏭 ForgeFlow Manufacturing Analytics")
st.markdown("### Real-time Defect Detection & Supply Chain Risk Monitoring")
st.markdown("---")

# -----------------------------------------------------------------------------
# 4. ROW 1: THE EXECUTIVE HOOK (Volume vs. Quality)
# -----------------------------------------------------------------------------
st.subheader("1. Network Performance (Volume vs. Quality)")

# FIX: Aggregate the granular data on the fly to get the Summary
# This avoids the "KeyError: units" because we calculate it right here.
df_chart_data = df_preds.groupby('plant').agg({
    'units': 'sum',
    'defect_rate': 'mean'
}).reset_index()

# Convert rate to percentage for the chart
df_chart_data['defect_pct'] = df_chart_data['defect_rate'] * 100

# Using Plotly Graph Objects for the Dual Axis Chart
fig_dual = go.Figure()

# Left Axis: Production Volume (Grey Bars)
fig_dual.add_trace(go.Bar(
    x=df_chart_data['plant'], 
    y=df_chart_data['units'],
    name='Production Volume',
    marker_color='#4A4A4A', # Professional Grey
    opacity=0.8
))

# Right Axis: Defect Rate (Red Line)
fig_dual.add_trace(go.Scatter(
    x=df_chart_data['plant'], 
    y=df_chart_data['defect_pct'],
    name='Defect Rate (%)',
    yaxis='y2',
    line=dict(color='#FF4B4B', width=4), # Alert Red
    mode='lines+markers',
    marker=dict(size=10)
))

# Layout: Define the Dual Axis and Dark Mode Template
fig_dual.update_layout(
    xaxis=dict(title="Manufacturing Facility"),
    yaxis=dict(title="Volume (Units)", showgrid=False),
    yaxis2=dict(
        title="Defect Rate (%)", 
        overlaying='y', 
        side='right', 
        range=[2.3, 2.6], # ZOOM IN to show the spike!
        showgrid=True,
        gridcolor='#333333'
    ),
    template="plotly_dark",
    height=400,
    legend=dict(orientation="h", y=1.1, x=0),
    margin=dict(l=0, r=0, t=40, b=0)
)

# Add the Threshold Line (2.5%)
fig_dual.add_shape(
    type="line", 
    x0=-0.5, x1=2.5, 
    y0=2.5, y1=2.5, 
    yref='y2',
    line=dict(color="White", dash="dash", width=2),
)
# Add Annotation
fig_dual.add_annotation(
    x=0, y=2.55, yref='y2',
    text="Quality Tolerance (2.5%)",
    showarrow=False,
    font=dict(color="White", size=12)
)

st.plotly_chart(fig_dual, use_container_width=True)

# -----------------------------------------------------------------------------
# 5. ROW 2: PREDICTIVE INSIGHTS
# -----------------------------------------------------------------------------
st.markdown("---")
col1, col2 = st.columns([1, 2])

# LEFT COLUMN: The Risk Heatmap
with col1:
    st.subheader("2. Predictive Risk Heatmap")
    st.caption("Avg. Failure Probability by Segment")
    
    # Aggregate data for the heatmap
    heatmap_data = df_preds.groupby(['plant', 'product'])['defect_probability'].mean().reset_index()
    
    fig_heat = px.density_heatmap(
        heatmap_data, 
        x="product", 
        y="plant", 
        z="defect_probability",
        color_continuous_scale="Redor", # Red-Orange Scale
        text_auto=".0%"
    )
    fig_heat.update_layout(
        template="plotly_dark", 
        height=400,
        coloraxis_colorbar=dict(title="Risk Score")
    )
    st.plotly_chart(fig_heat, use_container_width=True)

# RIGHT COLUMN: The "Kill List" (Action Table)
with col2:
    st.subheader("3. Actionable Kill List")
    st.caption("Batches with **High Failure Probability** (> 50%)")
    
    # Filter: Only show predicted failures
    bad_batches = df_preds[df_preds['predicted_outcome'] == 1].copy()
    
    # Sort: Worst offenders first
    bad_batches = bad_batches.sort_values('defect_probability', ascending=False)
    
    # Select & Rename Columns for the Manager
    display_cols = ['batch_id', 'plant', 'product', 'defect_probability', 'sensor_pressure', 'sensor_temp']
    clean_table = bad_batches[display_cols].rename(columns={
        'batch_id': 'Batch ID',
        'defect_probability': 'Risk Score',
        'sensor_pressure': 'Pressure (PSI)',
        'sensor_temp': 'Temp (°C)'
    })
    
    # Render Interactive Table using Streamlit's new Column Config
    st.dataframe(
        clean_table,
        column_config={
            "Batch ID": st.column_config.TextColumn("Batch ID", width="small"),
            "Risk Score": st.column_config.ProgressColumn(
                "Risk Score",
                help="Model Confidence",
                format="%.2f",
                min_value=0,
                max_value=1,
            ),
            "Pressure (PSI)": st.column_config.NumberColumn("Pressure", format="%d PSI"),
            "Temp (°C)": st.column_config.NumberColumn("Temp", format="%d °C"),
        },
        use_container_width=True,
        height=400,
        hide_index=True
    )
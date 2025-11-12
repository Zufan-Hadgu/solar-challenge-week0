"""
Solar Data Analysis Dashboard
10 Academy: Artificial Intelligence Mastery - Week 0 Challenge
"""

import streamlit as st
import pandas as pd
import plotly.express as px
from datetime import datetime, timedelta
import utils

# Page Configuration
st.set_page_config(
    page_title="Solar Data Analysis Dashboard",
    page_icon="☀️",
    layout="wide",
    initial_sidebar_state="expanded"
)

# Custom CSS
st.markdown("""
<style>
    .main-header {
        font-size: 2.5rem;
        font-weight: bold;
        color: #FF6B35;
        text-align: center;
        padding: 1rem 0;
    }
    .metric-card {
        background-color: #f0f2f6;
        padding: 1rem;
        border-radius: 0.5rem;
        border-left: 5px solid #FF6B35;
    }
    .stTabs [data-baseweb="tab-list"] {
        gap: 2rem;
    }
</style>
""", unsafe_allow_html=True)

# Title and Description
st.markdown('<div class="main-header">☀️ Solar Data Analysis Dashboard</div>', unsafe_allow_html=True)
st.markdown("""
<div style='text-align: center; padding-bottom: 2rem;'>
    <p><strong>10 Academy: Artificial Intelligence Mastery - Week 0 Challenge</strong></p>
    <p>Exploring solar radiation datasets from Benin, Sierra Leone, and Togo</p>
</div>
""", unsafe_allow_html=True)

# Sidebar
st.sidebar.title("🎛️ Dashboard Controls")
st.sidebar.markdown("---")

# Country Selection
view_option = st.sidebar.radio(
    "Select View",
    ["Single Country", "Compare All Countries"],
    help="Choose to view one country or compare all three"
)

if view_option == "Single Country":
    selected_country = st.sidebar.selectbox(
        "Select Country",
        ["Benin", "Sierra Leone", "Togo"],
        help="Choose a country to analyze"
    )
    df = utils.load_data(selected_country)
else:
    selected_country = "All Countries"
    df = utils.load_all_countries()

# Metric Selection
selected_metric = st.sidebar.selectbox(
    "Select Solar Metric",
    ["GHI", "DNI", "DHI"],
    help="GHI: Global Horizontal Irradiance, DNI: Direct Normal Irradiance, DHI: Diffuse Horizontal Irradiance"
)

# Date Range Filter
st.sidebar.markdown("---")
st.sidebar.subheader("📅 Date Filter")

if df is not None and 'Timestamp' in df.columns:
    min_date = df['Timestamp'].min().date()
    max_date = df['Timestamp'].max().date()
    
    use_date_filter = st.sidebar.checkbox("Enable Date Range Filter", value=False)
    
    if use_date_filter:
        date_range = st.sidebar.date_input(
            "Select Date Range",
            value=(min_date, max_date),
            min_value=min_date,
            max_value=max_date
        )
        
        if len(date_range) == 2:
            df = utils.filter_by_date_range(df, date_range[0], date_range[1])
            st.sidebar.success(f"Filtered: {date_range[0]} to {date_range[1]}")

# Additional Options
st.sidebar.markdown("---")
show_statistics = st.sidebar.checkbox("Show Statistical Tests", value=False)
show_raw_data = st.sidebar.checkbox("Show Raw Data Table", value=False)

# Main Dashboard
if df is not None and len(df) > 0:
    
    # Key Performance Indicators (KPIs)
    st.header("📊 Key Performance Indicators")
    
    col1, col2, col3, col4 = st.columns(4)
    
    with col1:
        mean_val = df[selected_metric].mean()
        st.metric(
            label=f"Average {selected_metric}",
            value=f"{mean_val:.2f} W/m²",
            delta=None
        )
    
    with col2:
        max_val = df[selected_metric].max()
        st.metric(
            label=f"Peak {selected_metric}",
            value=f"{max_val:.2f} W/m²",
            delta=None
        )
    
    with col3:
        std_val = df[selected_metric].std()
        st.metric(
            label="Std Deviation",
            value=f"{std_val:.2f} W/m²",
            delta=None
        )
    
    with col4:
        count_val = len(df)
        st.metric(
            label="Total Records",
            value=f"{count_val:,}",
            delta=None
        )
    
    st.markdown("---")
    
    # Tabs for Different Visualizations
    tab1, tab2, tab3, tab4 = st.tabs(["📈 Time Series", "📦 Comparison", "🔗 Correlation", "🌡️ Environmental"])
    
    with tab1:
        st.subheader(f"Time Series Analysis - {selected_metric}")
        
        col1, col2 = st.columns([2, 1])
        
        with col1:
            # Time Series Plot
            fig_ts = utils.create_time_series_plot(df, selected_metric)
            if fig_ts:
                st.plotly_chart(fig_ts, use_container_width=True)
        
        with col2:
            # Hourly Pattern
            st.markdown("**Average by Hour of Day**")
            fig_hourly = utils.create_hourly_pattern(df, selected_metric)
            if fig_hourly:
                st.plotly_chart(fig_hourly, use_container_width=True)
        
        # Statistics
        stats = utils.calculate_statistics(df, selected_metric)
        if stats:
            st.markdown("**Summary Statistics**")
            stats_df = pd.DataFrame([stats]).T
            stats_df.columns = ['Value']
            st.dataframe(stats_df, use_container_width=True)
    
    with tab2:
        st.subheader(f"Country Comparison - {selected_metric}")
        
        if view_option == "Compare All Countries":
            # Boxplot
            fig_box = utils.create_comparison_boxplot(df, selected_metric)
            if fig_box:
                st.plotly_chart(fig_box, use_container_width=True)
            
            # Summary Table
            st.markdown("**Summary Statistics by Country**")
            summary_table = utils.get_summary_stats_table(df)
            if summary_table is not None:
                # Filter for selected metric
                metric_table = summary_table[summary_table['Metric'] == selected_metric]
                st.dataframe(metric_table.style.format({
                    'Mean': '{:.2f}',
                    'Median': '{:.2f}',
                    'Std Dev': '{:.2f}',
                    'Max': '{:.2f}'
                }), use_container_width=True)
            
            # Statistical Tests
            if show_statistics:
                st.markdown("---")
                st.markdown("**Statistical Tests**")
                test_results = utils.perform_anova_test(df, selected_metric)
                if test_results:
                    col1, col2 = st.columns(2)
                    with col1:
                        st.markdown("**ANOVA Test**")
                        st.write(f"F-statistic: {test_results['ANOVA']['F-statistic']:.4f}")
                        st.write(f"P-value: {test_results['ANOVA']['p-value']:.6f}")
                    with col2:
                        st.markdown("**Kruskal-Wallis Test**")
                        st.write(f"H-statistic: {test_results['Kruskal-Wallis']['H-statistic']:.4f}")
                        st.write(f"P-value: {test_results['Kruskal-Wallis']['p-value']:.6f}")
                    
                    if test_results['Significant']:
                        st.success("✅ Significant difference detected (p < 0.05)")
                    else:
                        st.info("ℹ️ No significant difference detected (p ≥ 0.05)")
        else:
            st.info("Switch to 'Compare All Countries' view to see comparisons")
    
    with tab3:
        st.subheader("Correlation Analysis")
        
        col1, col2 = st.columns([3, 2])
        
        with col1:
            # Correlation Heatmap
            fig_corr = utils.create_correlation_heatmap(df)
            if fig_corr:
                st.plotly_chart(fig_corr, use_container_width=True)
        
        with col2:
            st.markdown("**Key Correlations**")
            # Calculate correlations with selected metric
            corr_cols = ['GHI', 'DNI', 'DHI', 'Tamb', 'RH', 'WS']
            available_cols = [col for col in corr_cols if col in df.columns]
            
            if selected_metric in available_cols:
                correlations = df[available_cols].corr()[selected_metric].sort_values(ascending=False)
                correlations = correlations[correlations.index != selected_metric]
                
                st.dataframe(correlations.to_frame('Correlation').style.format('{:.3f}'), 
                           use_container_width=True)
    
    with tab4:
        st.subheader("Environmental Factors")
        
        # Scatter plots
        col1, col2 = st.columns(2)
        
        with col1:
            if 'Tamb' in df.columns:
                fig_temp = utils.create_scatter_plot(df, 'Tamb', selected_metric)
                if fig_temp:
                    st.plotly_chart(fig_temp, use_container_width=True)
        
        with col2:
            if 'RH' in df.columns:
                fig_rh = utils.create_scatter_plot(df, 'RH', selected_metric)
                if fig_rh:
                    st.plotly_chart(fig_rh, use_container_width=True)
        
        # Environmental Statistics
        env_vars = ['Tamb', 'RH', 'WS', 'BP']
        available_env = [var for var in env_vars if var in df.columns]
        
        if available_env:
            st.markdown("**Environmental Variables Summary**")
            env_stats = df[available_env].describe().T
            st.dataframe(env_stats.style.format('{:.2f}'), use_container_width=True)
    
    # Raw Data Table
    if show_raw_data:
        st.markdown("---")
        st.header("📋 Raw Data")
        
        # Select columns to display
        display_cols = ['Timestamp', 'GHI', 'DNI', 'DHI', 'Tamb', 'RH', 'WS']
        if 'Country' in df.columns:
            display_cols = ['Country'] + display_cols
        
        available_display_cols = [col for col in display_cols if col in df.columns]
        
        st.dataframe(df[available_display_cols].head(1000), use_container_width=True)
        
        # Download button
        csv = df[available_display_cols].to_csv(index=False).encode('utf-8')
        st.download_button(
            label="📥 Download Data as CSV",
            data=csv,
            file_name=f"solar_data_{selected_country.replace(' ', '_')}_{datetime.now().strftime('%Y%m%d')}.csv",
            mime="text/csv"
        )

else:
    st.error("❌ Unable to load data. Please check that the data files exist in the '../data/' directory.")
    st.info("""
    Expected files:
    - ../data/benin_clean.csv
    - ../data/sierraleone_clean.csv
    - ../data/togo-dapaong_qc.csv
    """)

# Footer
st.markdown("---")
st.markdown("""
<div style='text-align: center; color: #666; padding: 2rem 0;'>
    <p><strong>Solar Data Analysis Dashboard</strong> | 10 Academy AI Mastery Program</p>
    <p>Week 0 Challenge: Solar Data Discovery</p>
</div>
""", unsafe_allow_html=True)
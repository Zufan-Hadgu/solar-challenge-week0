"""
Utility functions for Solar Data Analysis Dashboard
"""

import pandas as pd
import numpy as np
import plotly.express as px
import plotly.graph_objects as go
from plotly.subplots import make_subplots
from scipy import stats
import streamlit as st

@st.cache_data
def load_data(country):
    """Load cleaned CSV data for specified country"""
    try:
        import os
        # Get the project root directory
        current_dir = os.path.dirname(os.path.abspath(__file__))
        project_root = os.path.dirname(current_dir)
        
        file_mapping = {
            "Benin": os.path.join(project_root, "data", "benin_clean.csv"),
            "Sierra Leone": os.path.join(project_root, "data", "sierraleone_clean.csv"),
            "Togo": os.path.join(project_root, "data", "togo-dapaong_qc.csv")
        }
        
        if country not in file_mapping:
            return None
            
        df = pd.read_csv(file_mapping[country])
        df['Country'] = country
        
        # Convert Timestamp to datetime
        if 'Timestamp' in df.columns:
            df['Timestamp'] = pd.to_datetime(df['Timestamp'])
        
        return df
    except Exception as e:
        st.error(f"Error loading data for {country}: {str(e)}")
        return None

@st.cache_data
def load_all_countries():
    """Load and combine all country data"""
    countries = ["Benin", "Sierra Leone", "Togo"]
    dfs = []
    
    for country in countries:
        df = load_data(country)
        if df is not None:
            dfs.append(df)
    
    if dfs:
        combined = pd.concat(dfs, ignore_index=True)
        return combined
    return None

def calculate_statistics(df, metric='GHI'):
    """Calculate summary statistics for a metric"""
    if df is None or metric not in df.columns:
        return {}
    
    stats_dict = {
        'Mean': df[metric].mean(),
        'Median': df[metric].median(),
        'Std Dev': df[metric].std(),
        'Min': df[metric].min(),
        'Max': df[metric].max(),
        'Count': len(df)
    }
    return stats_dict

def filter_by_date_range(df, start_date, end_date):
    """Filter dataframe by date range"""
    if df is None or 'Timestamp' not in df.columns:
        return df
    
    mask = (df['Timestamp'] >= pd.to_datetime(start_date)) & (df['Timestamp'] <= pd.to_datetime(end_date))
    return df[mask]

def create_time_series_plot(df, metric='GHI'):
    """Create interactive time series plot"""
    if df is None or metric not in df.columns:
        return None
    
    # Resample to hourly for better performance
    if 'Timestamp' in df.columns:
        df_plot = df.set_index('Timestamp').resample('1H')[metric].mean().reset_index()
    else:
        return None
    
    fig = px.line(df_plot, x='Timestamp', y=metric,
                  title=f'{metric} Over Time',
                  labels={metric: f'{metric} (W/m²)', 'Timestamp': 'Date'})
    
    fig.update_layout(
        hovermode='x unified',
        height=400
    )
    
    return fig

def create_comparison_boxplot(df, metric='GHI'):
    """Create country comparison boxplot"""
    if df is None or metric not in df.columns or 'Country' not in df.columns:
        return None
    
    fig = px.box(df, x='Country', y=metric, color='Country',
                 title=f'{metric} Distribution by Country',
                 labels={metric: f'{metric} (W/m²)'})
    
    fig.update_layout(height=400, showlegend=False)
    
    return fig

def create_correlation_heatmap(df):
    """Create correlation heatmap"""
    if df is None:
        return None
    
    # Select numeric columns
    numeric_cols = ['GHI', 'DNI', 'DHI', 'Tamb', 'RH', 'WS']
    available_cols = [col for col in numeric_cols if col in df.columns]
    
    if len(available_cols) < 2:
        return None
    
    corr_matrix = df[available_cols].corr()
    
    fig = px.imshow(corr_matrix,
                    labels=dict(color="Correlation"),
                    x=available_cols,
                    y=available_cols,
                    color_continuous_scale='RdBu_r',
                    zmin=-1, zmax=1,
                    title='Correlation Matrix')
    
    fig.update_layout(height=500)
    
    return fig

def create_hourly_pattern(df, metric='GHI'):
    """Create hourly average pattern plot"""
    if df is None or 'Timestamp' not in df.columns or metric not in df.columns:
        return None
    
    df['Hour'] = df['Timestamp'].dt.hour
    hourly_avg = df.groupby('Hour')[metric].mean().reset_index()
    
    fig = px.line(hourly_avg, x='Hour', y=metric,
                  title=f'Average {metric} by Hour of Day',
                  labels={metric: f'{metric} (W/m²)', 'Hour': 'Hour of Day'},
                  markers=True)
    
    fig.update_layout(height=400)
    
    return fig

def create_scatter_plot(df, x_metric='Tamb', y_metric='GHI'):
    """Create scatter plot between two metrics"""
    if df is None or x_metric not in df.columns or y_metric not in df.columns:
        return None
    
    # Sample data for performance (every 100th point)
    df_sample = df.iloc[::100]
    
    fig = px.scatter(df_sample, x=x_metric, y=y_metric,
                     color='Country' if 'Country' in df.columns else None,
                     title=f'{y_metric} vs {x_metric}',
                     labels={x_metric: f'{x_metric}', y_metric: f'{y_metric} (W/m²)'},
                     opacity=0.6)
    
    fig.update_layout(height=400)
    
    return fig

def perform_anova_test(df, metric='GHI'):
    """Run ANOVA test across countries"""
    if df is None or metric not in df.columns or 'Country' not in df.columns:
        return None
    
    countries = df['Country'].unique()
    groups = [df[df['Country'] == country][metric].dropna() for country in countries]
    
    # Perform ANOVA
    f_stat, p_value = stats.f_oneway(*groups)
    
    # Perform Kruskal-Wallis
    h_stat, p_value_kw = stats.kruskal(*groups)
    
    result = {
        'ANOVA': {'F-statistic': f_stat, 'p-value': p_value},
        'Kruskal-Wallis': {'H-statistic': h_stat, 'p-value': p_value_kw},
        'Significant': p_value < 0.05
    }
    
    return result

def get_summary_stats_table(df):
    """Get summary statistics table for all countries"""
    if df is None or 'Country' not in df.columns:
        return None
    
    metrics = ['GHI', 'DNI', 'DHI']
    available_metrics = [m for m in metrics if m in df.columns]
    
    summary_data = []
    
    for country in df['Country'].unique():
        country_df = df[df['Country'] == country]
        for metric in available_metrics:
            summary_data.append({
                'Country': country,
                'Metric': metric,
                'Mean': country_df[metric].mean(),
                'Median': country_df[metric].median(),
                'Std Dev': country_df[metric].std(),
                'Max': country_df[metric].max()
            })
    
    summary_df = pd.DataFrame(summary_data)
    return summary_df
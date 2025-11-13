# Scripts Directory

This directory contains utility scripts for data processing and analysis in the Solar Data Discovery project.

## Purpose

The scripts folder is designed to house reusable Python scripts that support:
- Data preprocessing and cleaning
- Statistical analysis functions
- Data transformation utilities
- Helper functions for the Streamlit dashboard

## Structure

```
scripts/
├── __init__.py       # Makes this a Python package
└── README.md         # This file
```

## Usage

Scripts in this directory can be imported by the Streamlit dashboard or Jupyter notebooks:

```python
# Example import
from scripts import data_processor
```

## Current Implementation

Currently, utility functions are located in `app/utils.py` and are used by the Streamlit dashboard in `app/main.py`. 

### Key Functions Available:

**Data Loading:**
- `load_data(country)` - Load cleaned CSV data for a specific country
- `load_data_from_upload(uploaded_file, country_name)` - Load data from uploaded file
- `load_all_countries()` - Load and combine all country datasets

**Data Processing:**
- `calculate_statistics(df, metric)` - Calculate summary statistics
- `filter_by_date_range(df, start_date, end_date)` - Filter data by date
- `get_summary_stats_table(df)` - Generate summary statistics table

**Visualization:**
- `create_time_series_plot(df, metric)` - Create interactive time series
- `create_comparison_boxplot(df, metric)` - Generate country comparison boxplots
- `create_correlation_heatmap(df)` - Create correlation heatmap
- `create_hourly_pattern(df, metric)` - Plot hourly average patterns
- `create_scatter_plot(df, x_metric, y_metric)` - Generate scatter plots

**Statistical Analysis:**
- `perform_anova_test(df, metric)` - Run ANOVA and Kruskal-Wallis tests

## Future Enhancements

Potential scripts to add:
- `data_validator.py` - Data quality checks and validation
- `feature_engineering.py` - Create derived features
- `seasonal_analysis.py` - Seasonal decomposition tools
- `energy_modeling.py` - PV system output simulation
- `export_utils.py` - Data export in various formats

## Contributing

When adding new scripts:

1. **Create meaningful function names** that clearly describe their purpose
2. **Add docstrings** to all functions explaining parameters and return values
3. **Include error handling** for robust operation
4. **Write unit tests** in the `tests/` directory
5. **Update this README** with new script descriptions

## Example Script Template

```python
"""
Module Name: example_script.py
Purpose: Brief description of what this script does
Author: Your Name
Date: YYYY-MM-DD
"""

import pandas as pd
import numpy as np

def example_function(data, param1, param2=None):
    """
    Brief description of the function.
    
    Parameters:
    -----------
    data : pd.DataFrame
        Input dataframe
    param1 : str
        Description of param1
    param2 : int, optional
        Description of param2
        
    Returns:
    --------
    pd.DataFrame
        Description of return value
        
    Examples:
    ---------
    >>> result = example_function(df, "GHI")
    """
    try:
        # Function implementation
        result = data.copy()
        # ... processing ...
        return result
    except Exception as e:
        print(f"Error in example_function: {e}")
        return None

if __name__ == "__main__":
    # Test code
    pass
```

## Dependencies

Scripts may require the following packages (from `requirements.txt`):
- pandas
- numpy
- matplotlib
- seaborn
- scipy
- plotly
- streamlit

## Testing

To test scripts:

```bash
# Run all tests
pytest tests/

# Run specific test file
pytest tests/test_utils.py
```

## Notes

- All scripts should be Python 3.8+ compatible
- Follow PEP 8 style guidelines
- Use type hints where appropriate
- Keep functions modular and reusable
- Document all assumptions and limitations

---

For more information about the project, see the main [README.md](../README.md) in the project root.


# ☀️ Solar Data Discovery - Week 0 Challenge

**10 Academy: Artificial Intelligence Mastery Program**

A comprehensive exploratory data analysis (EDA) and visualization project analyzing solar irradiance data from three West African countries: Benin, Sierra Leone, and Togo.

---

## 📋 Table of Contents

- [Project Overview](#project-overview)
- [Live Dashboard](#live-dashboard)
- [Features](#features)
- [Installation](#installation)
- [Usage](#usage)
- [Project Structure](#project-structure)
- [Data Analysis](#data-analysis)
- [Technologies Used](#technologies-used)
- [Key Findings](#key-findings)
- [Contributing](#contributing)
- [License](#license)

---

## 🎯 Project Overview

This project analyzes solar radiation datasets from Benin, Sierra Leone, and Togo to identify high-potential regions for solar farm installation. The analysis includes:

- **Data Cleaning**: Handling missing values, outliers, and negative irradiance values
- **Exploratory Data Analysis**: Statistical analysis and pattern identification
- **Cross-Country Comparison**: ANOVA and Kruskal-Wallis tests to compare solar potential
- **Interactive Dashboard**: Streamlit-based visualization platform

**Dataset Details:**
- **Records per Country**: 525,600 (1 year of minute-resolution data)
- **Total Data Points**: 1.5+ million
- **Variables**: 19 (including GHI, DNI, DHI, temperature, humidity, wind)

---

## 🌐 Live Dashboard

**🚀 Interactive Dashboard:** [https://Zufan-Hadgu-solar-challenge-week0.streamlit.app](https://Zufan-Hadgu-solar-challenge-week0.streamlit.app)

### Dashboard Features:

- 📊 **Real-time KPI Metrics**
  - Average GHI, Peak Irradiance, Standard Deviation, Total Records
  
- 📈 **Time Series Analysis**
  - Interactive plots with hourly aggregation
  - Daily pattern analysis
  
- 📦 **Country Comparison**
  - Side-by-side boxplots
  - Statistical tests (ANOVA, Kruskal-Wallis)
  - Summary statistics tables
  
- 🔗 **Correlation Analysis**
  - Heatmaps showing variable relationships
  - Key correlation insights
  
- 🌡️ **Environmental Factors**
  - Scatter plots (GHI vs Temperature, GHI vs Humidity)
  - Environmental variables summary
  
- 📥 **Data Export**
  - Download filtered data as CSV
  - Upload custom datasets

---

## ✨ Features

### Data Analysis
- ✅ Comprehensive data cleaning and preprocessing
- ✅ Outlier detection using Z-score method (|Z| > 3)
- ✅ Missing value imputation (median strategy)
- ✅ Statistical testing (ANOVA, Kruskal-Wallis)
- ✅ Correlation analysis

### Visualizations
- ✅ Time series plots with interactive zooming
- ✅ Boxplots for cross-country comparison
- ✅ Correlation heatmaps
- ✅ Scatter plots (environmental factors)
- ✅ Hourly pattern analysis
- ✅ Summary statistics tables

### Interactive Dashboard
- ✅ Country selector (Single or Compare All)
- ✅ Metric selector (GHI, DNI, DHI)
- ✅ Date range filtering
- ✅ File upload capability
- ✅ Statistical test toggle
- ✅ Raw data viewer
- ✅ CSV export functionality

---

## 🛠️ Installation

### Prerequisites

- Python 3.8+
- pip or conda

### Setup

1. **Clone the repository:**

```bash
git clone https://github.com/Zufan-Hadgu/solar-challenge-week0.git
cd solar-challenge-week0
```

2. **Create a virtual environment:**

```bash
# Using venv
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate

# Or using conda
conda create -n solar-env python=3.9
conda activate solar-env
```

3. **Install dependencies:**

```bash
pip install -r requirements.txt
```

4. **Data Files:**

Place your data files in the `data/` directory:
- `benin_clean.csv`
- `sierraleone_clean.csv`
- `togo-dapaong_qc.csv`

> **Note:** Data files are not included in the repository (.gitignored). You can upload them via the dashboard interface.

---

## 🚀 Usage

### Running the Dashboard Locally

```bash
streamlit run app/main.py
```

The dashboard will open in your browser at `http://localhost:8501`

### Running Jupyter Notebooks

```bash
jupyter notebook
```

Navigate to the `notebooks/` directory and open:
- `benin_eda.ipynb` - Benin analysis
- `sierraleone.ipynb` - Sierra Leone analysis
- `compare_countries.ipynb` - Cross-country comparison

### Using the Dashboard

1. **Choose Data Source:**
   - **Local Files**: Use pre-loaded data files
   - **Upload Files**: Upload your own CSV files

2. **Select View:**
   - **Single Country**: Analyze one country at a time
   - **Compare All Countries**: See side-by-side comparisons

3. **Explore Tabs:**
   - **Time Series**: View irradiance trends over time
   - **Comparison**: Compare countries with statistical tests
   - **Correlation**: Analyze variable relationships
   - **Environmental**: Explore environmental factor impacts

4. **Apply Filters:**
   - Enable date range filter
   - Select specific metrics (GHI, DNI, DHI)
   - Toggle statistical tests

5. **Export Data:**
   - Check "Show Raw Data Table"
   - Click "Download Data as CSV"

---

## 📁 Project Structure

```
solar-challenge-week0/
├── app/
│   ├── __init__.py
│   ├── main.py              # Main Streamlit dashboard
│   └── utils.py             # Utility functions for data processing
│
├── data/                    # Data files (gitignored)
│   ├── benin_clean.csv
│   ├── sierraleone_clean.csv
│   └── togo-dapaong_qc.csv
│
├── notebooks/               # Jupyter notebooks
│   ├── benin_eda.ipynb
│   ├── sierraleone.ipynb
│   └── compare_countries.ipynb
│
├── scripts/                 # Utility scripts
│   ├── __init__.py
│   └── README.md
│
├── tests/                   # Unit tests
│
├── .streamlit/              # Streamlit configuration
│   └── config.toml
│
├── .gitignore
├── requirements.txt
└── README.md
```

---

## 📊 Data Analysis

### Data Cleaning Process

1. **Negative Irradiance Correction**
   - ~50% of records had negative values (nighttime measurements)
   - Corrected by setting negative GHI, DNI, DHI to 0
   - Impact: +1-2% change in mean values

2. **Outlier Detection**
   - Z-score method with |Z| > 3 threshold
   - <1% outliers in daytime irradiance
   - ~2% outliers in environmental variables

3. **Missing Value Imputation**
   - Median imputation for numeric variables
   - <1% missing data (except Comments: 100%)

4. **Physical Constraints**
   - Relative Humidity clipped to [0, 100]%
   - Wind Speed negative values set to 0

### Statistical Analysis

**ANOVA Testing:**
- Null Hypothesis (H₀): No significant difference in GHI across countries
- Alternative (H₁): At least one country differs significantly
- Significance level: α = 0.05

**Kruskal-Wallis Test:**
- Non-parametric alternative to ANOVA
- Validates findings without normality assumption

---

## 🔧 Technologies Used

### Programming & Analysis
- **Python 3.9+**
- **pandas** - Data manipulation
- **numpy** - Numerical computing
- **scipy** - Statistical testing

### Visualization
- **matplotlib** - Static plots
- **seaborn** - Statistical graphics
- **plotly** - Interactive visualizations

### Dashboard
- **Streamlit** - Web application framework

### Development Tools
- **Jupyter Notebook** - Interactive analysis
- **Git** - Version control
- **GitHub** - Repository hosting

---

## 💡 Key Findings

### Solar Potential Assessment

1. **All three countries are viable for solar energy development**
   - Peak irradiance: 1,300-1,500 W/m²
   - Average GHI: ~200-205 W/m²
   - Year-round solar availability

2. **Country Rankings:**
   - 🥇 **Highest Peak**: Sierra Leone (1,499 W/m²)
   - 🥈 **Highest Average**: Sierra Leone (204.41 W/m²)
   - 🥉 **Most Consistent**: All within 2% of each other

### Environmental Insights

1. **Humidity Impact:**
   - Strong negative correlation (r = -0.79)
   - High humidity reduces solar output
   - **Recommendation**: Anti-soiling coatings

2. **Cleaning Effectiveness:**
   - **32-40% improvement** in sensor readings after cleaning
   - **Recommendation**: Bi-weekly to monthly cleaning schedule

3. **Temperature Effects:**
   - Positive correlation with irradiance (r > 0.7)
   - Operating range suitable for standard PV modules

4. **Wind Conditions:**
   - Low average speeds (<2 m/s)
   - Minimal structural requirements
   - Low risk of wind damage

### Data Quality

**Strengths:**
- ✅ High-resolution (1-minute intervals)
- ✅ Full year coverage
- ✅ Multiple irradiance components
- ✅ Strong sensor correlations (r > 0.99)

**Limitations:**
- ⚠️ Single location per country
- ⚠️ One-year duration (long-term trends unknown)
- ⚠️ Some outliers in environmental sensors (~2%)

---

## 📈 Results Summary

| Country | Mean GHI (W/m²) | Max GHI (W/m²) | Std Dev | Records |
|---------|-----------------|----------------|---------|---------|
| **Benin** | 203.85 | 1,308 | Moderate | 525,600 |
| **Sierra Leone** | 204.41 | 1,499 | Moderate | 525,600 |
| **Togo** | ~200-210 | ~1,400 | Moderate | 525,600 |

**Statistical Significance:** ANOVA and Kruskal-Wallis tests confirm differences between countries (p < 0.05)

---

## 🤝 Contributing

Contributions are welcome! Please follow these steps:

1. Fork the repository
2. Create a feature branch (`git checkout -b feature/AmazingFeature`)
3. Commit your changes (`git commit -m 'Add some AmazingFeature'`)
4. Push to the branch (`git push origin feature/AmazingFeature`)
5. Open a Pull Request

---

## 📝 License

This project is part of the 10 Academy AI Mastery Program - Week 0 Challenge.

---

## 👥 Author

**Zufan Hadgu**

- GitHub: [@Zufan-Hadgu](https://github.com/Zufan-Hadgu)
- Project: [Solar Challenge Week 0](https://github.com/Zufan-Hadgu/solar-challenge-week0)

---

## 🙏 Acknowledgments

- **10 Academy** for the AI Mastery Program
- **Data Sources**: Solar irradiance data from Benin, Sierra Leone, and Togo monitoring stations
- **Streamlit Community** for the excellent dashboard framework

---

## 📞 Contact

For questions or feedback, please open an issue in the GitHub repository.

---

**⭐ If you find this project useful, please consider giving it a star!**

---

*Last Updated: November 2025*


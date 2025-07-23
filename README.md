<h1>Life Expectancy Analysis</h1>

<p><strong>🔬 Domain:</strong> Healthcare Analytics / Data Science</p>
<p><strong>🧠 Techniques:</strong> Machine Learning, Deep Learning, EDA</p>
<p><strong>📅 Years Covered:</strong> 2000–2015</p>
<p><strong>🌍 Countries:</strong> 193</p>

<h2>📁 Project Structure</h2>
<pre>
life_expectancy_analysis/
│
├── data/
│   └── life_expectancy_dataset.csv           # Cleaned and merged WHO & UN data (2000–2015)
│
├── notebooks/
│   ├── life_expectancy_analysis.ipynb        # EDA, preprocessing, feature engineering
│   ├── LifeExpectancy_ML.ipynb               # Machine Learning models
│   └── life_expectancy_DL.ipynb              # Deep Learning model
│
├── models/
│   └── trained_models.pkl                     # Serialized ML models (joblib)
│
├── outputs/
│   ├── plots/                                # Visualizations (heatmaps, trends, etc.)
│   └── reports/                              # Model evaluation metrics, CV results
│
├── README.md                                 # GitHub ReadMe file (this one)
└── requirements.txt                          # Python dependencies
</pre>

<h2>📊 Project Overview</h2>
<p>
This project investigates global life expectancy determinants using data from WHO and UN for the years 2000–2015. It aims to identify key health, economic, social, and immunization factors affecting life expectancy across 193 countries.
</p>

<h2>🧪 Methodology</h2>
<ul>
  <li>Data Cleaning: Missing value imputation, outlier handling</li>
  <li>EDA: Trends, correlation heatmaps, status-wise analysis (developed vs developing)</li>
  <li>Feature Engineering: Label encoding, standardization</li>
  <li>Modeling:
    <ul>
      <li>ML Models: Random Forest, XGBoost, Extra Trees, Gradient Boost</li>
      <li>DL Model: Deep Neural Network using Keras</li>
    </ul>
  </li>
  <li>Model Evaluation: R² Score, RMSE, Cross-validation</li>
</ul>

<h2>📌 Key Questions</h2>
<ul>
  <li>Which factors significantly influence life expectancy?</li>
  <li>What is the impact of immunization, GDP, and schooling?</li>
  <li>Are there major differences between developed and developing nations?</li>
</ul>

<h2>📈 Results</h2>
<ul>
  <li><strong>Best Model:</strong> XGBoost (R² ≈ 0.96, RMSE ≈ 1.98)</li>
  <li><strong>Top Features:</strong> Adult Mortality, Schooling, HIV/AIDS, BMI</li>
  <li><strong>Insight:</strong> Countries with higher schooling and lower adult mortality tend to have higher life expectancy.</li>
</ul>

<h2>📎 References</h2>
<ul>
  <li><a href="https://www.who.int/data/gho">WHO Global Health Observatory</a></li>
  <li><a href="https://github.com/kiranshahi/Life-expectancy-prediction">Inspiration GitHub Repo</a></li>
</ul>

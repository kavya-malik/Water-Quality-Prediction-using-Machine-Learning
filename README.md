# 💧 Water Quality Prediction 

This project predicts whether water is **potable (drinkable)** or not using ML techniques on the Kaggle [Water Potability Dataset](https://www.kaggle.com/datasets/adityakadiwal/water-potability).

---

## 📌 Steps Performed

### 1. Data Loading
- Uploaded `water_potability.csv` in Google Colab.  
- Dataset Shape: **3276 rows × 10 columns**

### 2. Data Cleaning
- Missing values detected in:
  - `ph` (491), `Sulfate` (781), `Trihalomethanes` (162)  
- Handled using **mean imputation** (`df.fillna(df.mean(), inplace=True)`).

### 3. Exploratory Data Analysis (EDA)
- **Correlation Heatmap** – checked relationships between features.  
- **Outlier Detection** – used boxplots to visualize extreme values.  
- **Class Balance** – `0 = Not Potable (1998)`, `1 = Potable (1278)` → dataset is imbalanced.  
- **Distribution Plots** – histograms of all features.  
- **Feature vs Target** – scatterplot (`pH` vs `Potability`).

### 4. Observations
- Data has strong variation in `Solids` (up to 61,227).  
- Dataset slightly imbalanced (60% non-potable, 40% potable).  
- Correlation heatmap shows weak correlations → all features retained.  
- No dimensionality reduction required.

---


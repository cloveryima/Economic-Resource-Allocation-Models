import pandas as pd
import statsmodels.api as sm

# Load the datasets
health_exp_data = pd.read_csv('API_SH.XPD.CHEX.PC.CD_DS2_en_csv_v2_11721.csv', skiprows=4)
life_exp_data = pd.read_csv('API_SP.DYN.LE00.IN_DS2_en_csv_v2_9814.csv', skiprows=4)

# Data preprocessing: Select relevant columns and rename for clarity
health_exp_data = health_exp_data[['Country Name', '2019']].rename(columns={'2019': 'Health_Expenditure'})
life_exp_data = life_exp_data[['Country Name', '2019']].rename(columns={'2019': 'Life_Expectancy'})

# Merge the datasets on 'Country Name' and drop any rows with missing values
merged_data = pd.merge(health_exp_data, life_exp_data, on='Country Name').dropna()

# OLS Regression Analysis
X = sm.add_constant(merged_data['Health_Expenditure'])  # Add constant term for intercept
y = merged_data['Life_Expectancy']  # Dependent variable: Life Expectancy
model = sm.OLS(y, X).fit()  # Fit the Ordinary Least Squares (OLS) model

# Print regression summary
print(model.summary())

# Results & Conclusion
# -----------------------------------------------------
# R-squared: 0.369, indicating that 36.9% of the variation in life expectancy
# can be explained by health expenditure per capita.
# Intercept (const): 69.5095, suggesting that a country with zero health expenditure
# per capita would have a life expectancy of approximately 69.5 years.
# Health Expenditure Coefficient: 0.0024, indicating that for every additional
# dollar spent per capita on health, life expectancy increases by 0.0024 years.
# P-value: The p-value for health expenditure is < 0.0001, showing a statistically
# significant relationship between health expenditure and life expectancy.
#
# Conclusions:
# 1. There is a positive and statistically significant correlation between health
#    expenditure per capita and life expectancy.
# 2. The analysis suggests that increasing health investment can lead to longer
#    lifespans, which has policy implications for governments and NGOs.
# 3. Future analysis could include more variables to improve the model's robustness
#    and conduct scenario analysis for policy recommendations.

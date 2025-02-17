
# Schizophrenia Diagnosis and Symptom Prediction
---

# Project Overview


This project focuses on developing machine learning models to classify individuals as either having schizophrenia or not based on various demographic, clinical, and psychosocial attributes. Additionally, regression models (with a focus on regularization techniques) will be implemented to predict positive symptom severity scores, negative symptom score, and GAF score. Using the schizophrenia dataset, the objective is to build accurate predictive models while performing exploratory data analysis (EDA) to understand key factors associated with schizophrenia diagnosis and symptom severity.

---

# Background

Schizophrenia is a complex psychiatric disorder that affects cognition, emotion, and behavior affecting everyday life. Predictive modeling can assist in better understanding factors associated with the disorder and potentially aid in early detection or symptom severity estimation.

---

# Objectives 

1. Perform exploratory data analysis (EDA) to understand dataset characteristics and distributions.
2. Preprocess and clean the data to prepare it for machine learning models.
3. Build and evaluate classification models to predict schizophrenia diagnosis.
4. Develop regression models to predict symptom scores.
5. Interpret model results and assess key factors influencing schizophrenia prediction.
6. Optimize models using regularization techniques for improved performance.

---

# Dataset

The schizophrenia dataset contains 10,000 instances and 20 features, including demographic information, clinical history, and symptom severity scores. Key features include:

* Demographic Factors: Age, Gender, Education Level, Marital Status, Occupation, Income Level, Living Area
* Clinical Factors: Disease Duration, Hospitalizations, Family History, Substance Use, Suicide Attempt
* Symptom Scores: Positive Symptom Score, Negative Symptom Score, GAF Score
* Social & Treatment Factors: Social Support, Stress Factors, Medication Adherence

Source: [Schizophrenia Dataset](https://www.kaggle.com/datasets/asinow/schizohealth-dataset)

---

# Workflow

# Exploratory Data Analysis (EDA)

* Visualizing data distributions
* Identifying correlations between features
* Checking for class balance for schizophrenia diagnosis

---

# Data Preprocessing

* Handling categorical variables and encoding them appropriately
* Normalization or scaling for numerical features if needed
* Feature Selection

---

# Model Development

* Implementing classification models 
* Applying regularization techniques (Lasso, Ridge) for regression models

----

# Model Evaluation

* Selecting evaluation metrics: Recall over precision for classification
* Using RMSE and R-squared for regression models
* Analyzing feature importance and model performance


---

# Model Results

* Comparing different models and their performance
* Analyzing trade-offs between recall and precision

---

# Results


---

# Conclusions


---

# Tools and Libraries

* Python
* Pandas, NumPy'
* Scikit-Learn
* Matplotlib, Seaborn


----

# Future Work

TBA

---

# License

This project is licensed under the MIT License.


---

# References 

* McCutcheon RA, Reis Marques T, Howes OD. Schizophrenia—An Overview. JAMA Psychiatry. 2020;77(2):201–210. [doi:10.1001/jamapsychiatry.2019.3360](https://jamanetwork.com/journals/jamapsychiatry/article-abstract/2753514)

* Robinson N and Bergen SE (2021) Environmental Risk Factors for Schizophrenia and Bipolar Disorder and Their Relationship to Genetic Risk: Current Knowledge and Future Directions. Front. Genet. 12:686666. [doi: 10.3389/fgene.2021.686666](https://www.frontiersin.org/journals/genetics/articles/10.3389/fgene.2021.686666/full)
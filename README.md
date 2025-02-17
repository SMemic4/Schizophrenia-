
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


## Dataset Features

| Feature Name              | Type        | Description                                      | Values (if categorical)                                         |
|---------------------------|------------|--------------------------------------------------|-----------------------------------------------------------------|
| Patient_ID               | Numerical  | Unique identifier assigned to each patient      | Unique ID                                                      |
| Age                      | Numerical  | Patient's age                                   | 18-80                                                          |
| Gender                   | Categorical| Gender of the patient                           | 0: Female, 1: Male                                             |
| Education_Level          | Categorical| Highest level of education completed           | 1: Primary, 2: Middle, 3: High School, 4: University, 5: Postgraduate |
| Marital_Status          | Categorical| Marital status of the patient                  | 0: Single, 1: Married, 2: Divorced, 3: Widowed                 |
| Occupation              | Categorical| Employment status of the patient               | 0: Unemployed, 1: Employed, 2: Retired, 3: Student             |
| Income_Level            | Categorical| Income level category                          | 0: Low, 1: Medium, 2: High                                     |
| Living_Area             | Categorical| Living area classification                     | 0: Rural, 1: Urban                                            |
| Diagnosis               | Categorical| Schizophrenia diagnosis status                 | 0: Not schizophrenic, 1: Schizophrenic                         |
| Disease_Duration        | Numerical  | Duration of illness (years)                    | 1-40                                                           |
| Hospitalizations        | Numerical  | Number of hospital admissions                  | 0-10                                                           |
| Family_History         | Categorical| Family history of schizophrenia                | 0: No, 1: Yes                                                 |
| Substance_Use          | Categorical| Substance use history (tobacco, alcohol, drugs)| 0: No, 1: Yes                                                 |
| Suicide_Attempt        | Categorical| History of suicide attempts                    | 0: No, 1: Yes                                                 |
| Positive_Symptom_Score | Numerical  | Positive symptom severity                      | 0-100                                                          |
| Negative_Symptom_Score | Numerical  | Negative symptom severity                      | 0-100                                                          |
| GAF_Score              | Numerical  | Global assessment of functioning               | 0-100                                                          |
| Social_Support         | Categorical| Level of social support                        | 0: Low, 1: Medium, 2: High                                     |
| Stress_Factors         | Categorical| Level of stress factors                        | 0: Low, 1: Medium, 2: High                                     |
| Medication_Adherence   | Categorical| Adherence to medication regimen                | 0: Poor, 1: Moderate, 2: Good                                  |


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
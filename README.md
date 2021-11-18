# Final Project
![fig3](https://github.com/retroxsky06/Final_Project/blob/main/images/Kerfin7-NEA-2134.jpg)
## Project Overview
For the final project of this course, the primary goal is to tell a cohesive story using a dataset. The topic of selection is stroke and the dataset is sourced from Kaggle. A csv file is downloaded, cleaned, and analyzed using Python’s Pandas and Numpy, and then stored in a PostgreSQL database.  The data is then trained, tested, and evaluated in a machine learning algorithm to predict if a patient is likely to suffer a stroke based on their demographics and health records. Lastly, the machine learning algorithm is integrated into an interactive web-application using Flask, HTML, and CSS. Findings are displayed through Tableau and Google Slides.

### Visualizations
- **Tableau:**
- **Presentation:** [Google Slides]()

### Software & Resources
- Data Cleaning and Analysis: Python
- Database: PostgreSQL 11.1, SQLAlchemy
- Machine Learning: Scikit-learn
- Vizualizations: Tableau, Flask, HTML, CSS
- Presentation: Google Slides
- Data source: [train_strokes.csv]() from [Kaggle](www.kaggle.com)

## Outline of Project
- **Selected Topic:** Stroke
- **Reason for Selected topic:** The topic was selected due to interest in examining potential risk factors that may cause strokes, the second leading cause of death worldwide, and a major cause of severe disability.
- **Source of data:** The dataset was sourced from Kaggle. This dataset contains 43,400 observations with 11 attributes. Each row in the data provides relevant patient information. The initial source of the data is unknown.
  - train_strokes.csv: contains data specific to patients (age, gender, heart disease, hypertension, etc.)
- **Questions I hope to answer with the data:**
  - What are the significant risk factors for a stroke?
  - Can machine learning predict whether a patient is likely to suffer a stroke based on one's demographics (age, gender, marital status) and health records (presence of hypertension and/or heart disease, smoking status, and experience of stroke)?
- **Algorithm:** Logistic Regression Model

## Project Phases
![fig1]()
### Phase 1. Data Review and Cleaning
The first part of our Analysis involved looking at the raw data to ensure it was usable for our analysis. The dataset was relatively clean; however, two columns, body mass index (BMI) and smoking status had missing values. 1,458 records had shown NaN (null values) in the column, and initially, I thought about removing the records as it represented a small portion of the dataset.  With further investigation, it contained 140 records of patients who suffered a stroke.  As the dataset had 738 patients who suffered from a stroke compared to 42,00 that did not, the information was valuable to retain.  The NaN values in the BMI column were instead replaced with the mean of BMI.  Additionally, 13,292 records of the dataset had missing values under the smoking status column, accounting for 30.6% of the data.  As the records are a significant portion of the dataset, a new category “unknown” was created to account for the missing values. Python’s Pandas and Numpy were used to clean the dataset. 

After conducting an initial exploratory data analysis, additional cleaning of the data occurred in which four columns- residence type, work type,  average glucose level, and bmi were removed to be used for the machine learning algorithm.  
 
**Integration of Database:** Once the data was cleaned, it was connected and stored in a local PostgresSQL server using SQLAlchemy. The cleaned data was accessed using a Postgres query through Jupyter Notebook to connect to the Machine Learning Model. 

### Phase 2. Exploratory Data Analysis
Once the preliminary data cleaning was complete, initial investigations to discover any patterns and correlation among features (all variables except stroke) and target variable (stroke).  Insights are highlighted below:
- There is a significant difference between patients that suffered from a stroke (783 or 1.8%), compared to those that did not (42,617 or 98.2%). The dataset is extremely unbalanced, which will need to be amended prior to the machine learning phase.
- Age: The risk of experiencing a stroke increases as a patient's age advances.
- Gender: 
- Marriage status: Married people have a higher chance of suffering a stroke compared to those who are not married.
- Smoking status: Formerly smoked people have a higher chance of suffering a stroke followed by those who smoke, then people who never smoke.
- Hypertension: People who have hypertension have a higher chance of suffering a stroke.
- Heart disease: People who have heart disease are more prone to suffering a stroke.

### Phase 3. Machine Learning Model
**Explanation of Model Choice:**
**Data Preprocessing**
**How the data was split**

### Phase 4. Results of Analysis
## Summary

## Recommendations for Future Analysis



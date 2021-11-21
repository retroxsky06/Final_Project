# Stroke Risk Analytics
![fig1](https://github.com/retroxsky06/Final_Project/blob/main/images/Kerfin7-NEA-2134.jpg)

##### UC Berkeley Extension Data Analytics Bootcamp Final Project
*** 
## Project Overview
For the final project of this course, the primary goal is to tell a cohesive story using a dataset. The topic of selection is stroke and the dataset is sourced from Kaggle. A csv file is downloaded, cleaned, and analyzed using Python’s Pandas and Numpy, and then stored in a PostgreSQL database.  The data is then trained, tested, and evaluated in a machine learning algorithm to predict if a patient is likely to suffer a stroke based on their demographics and health records. Lastly, the machine learning algorithm is integrated into an interactive web-application using Flask, HTML, and CSS. Findings are displayed through Tableau and Google Slides.

### Visualizations & Presentation
- [Tableau](https://public.tableau.com/app/profile/vanessa.aczon/viz/StrokeVisualizations/Story1?publish=yes) 
- [Google Slides Presentation](https://docs.google.com/presentation/d/1LFhhYaabJc8rippfvuhxt_4OcxhvujPh_i00uDQa6iU/edit?usp=sharing)

### Software & Resources
- Data Cleaning and Analysis: Python
- Database: PostgreSQL 11.1, SQLAlchemy
- Machine Learning: Scikit-learn
- Visualizations: Tableau, Flask, HTML, CSS
- Presentation: Google Slides
- Data source: [Kaggle](https://kaggle.com/datasets)

## Outline of Project
- **Selected Topic:** Stroke
- **Reason for Selected topic:** The topic was selected due to interest in examining six assumptions about risk factors that lead to a stroke, the second leading cause of death worldwide, and a major cause of severe disability.
- **Source of data:** The dataset was sourced from Kaggle. This dataset contains 43,400 observations with 11 attributes. Each row in the data provides relevant patient information. The initial source of the data is unknown.
  - [train_strokes.csv](https://github.com/retroxsky06/Final_Project/blob/main/Resources/train_strokes.csv): contains data specific to patients (age, gender, heart disease, hypertension, etc.)
- **Questions I hope to answer with the data:**
  - Are only older adults impacted by strokes?
  - Do males have a higher chance of suffering from a stroke than females?
  - People who have hypertension have a higher chance of suffering from a stroke?
  - People who have heart disease are more prone to stroke?
  - Do married people have a higher chance of getting a stroke than unmarried people?
  - Are people who smoke are more prone to stroke?
- **Algorithm:** Logistic Regression Model

## Project Phases
![fig1](2)
### Phase 1. Data Review and Cleaning
The first part of the analysis involved looking at the raw data to ensure it was usable for the analysis. The dataset was relatively clean; however, two columns, body mass index (BMI) and smoking status had missing values. 1,458 records had shown NaN (null values) in the column, and initially, I thought about removing the records as it represented a small portion of the dataset.  With further investigation, it contained 140 records of patients who suffered a stroke.  As the dataset had 738 patients who suffered from a stroke compared to 42,00 that did not, the information was valuable to retain.  The NaN values in the BMI column were instead replaced with the mean of BMI.  Additionally, 13,292 records of the dataset had missing values under the smoking status column, accounting for 30.6% of the data.  As the records are a significant portion of the dataset, a new category “unknown” was created to account for the missing values. Python’s pandas and numpy were used to clean the dataset. 

After conducting an initial exploratory data analysis, additional cleaning of the data occurred in which four columns- residence type, work type, average glucose level, and BMI were removed.  
 
**Integration of Database:** Once the data was cleaned, it was connected and stored in a local PostgreSQL server using SQLAlchemy. The cleaned data was accessed using a Postgres query through Jupyter Notebook to connect to the Machine Learning Model. 

### Phase 2. Exploratory Data Analysis
Once the preliminary data cleaning was complete, initial investigations to discover any patterns and correlations among features. Observations are highlighted below:
- There is a significant difference between patients that suffered from a stroke (783 or 1.8%), compared to those that did not (42,617 or 98.2%). The dataset is extremely unbalanced, which will need to be amended prior inputting the data into a machine learning algorithm.
- Age: The risk of experiencing a stroke increases as a patient's age advances.
- Gender: Gender is not a variable that discriminates between a person having a stroke or not.
- Marriage status: Married people have a higher chance of suffering a stroke compared to those who are not married.
- Smoking status: Formerly smoked people have a higher chance of suffering a stroke followed by those who do smoke, then people who never smoke.
- Hypertension: People who have hypertension have a higher chance of suffering a stroke.
- Heart disease: People who have heart disease have a higher chance of suffering a stroke.

The findings of this data exploration can be found [here](https://github.com/retroxsky06/Final_Project/blob/main/data_cleaning_and_analysis/exploratory_data_analysis.ipynb) and was adapted into a Tableau story.

##### Fig. 2. Bivariate Analysis: Hypertension, Heart Disease, & Marriage status
![fig3](https://github.com/retroxsky06/Final_Project/blob/main/images/bivar_analysis.png)

### Phase 3. Machine Learning Model
**Data Processing, Scaling & Normalizing, & Oversampling:**
- To further prepare the data for a machine learning algorithm, categorical datatypes were transformed into numerical data using **one hot encoding** process (LabelEncoder).
- Once data has been encoded, it is then scaled and normalized. Since the ‘age’ column holds larger numbers, it is best to scale and normalize so they would not disproportionately impact the model. Scikit-learn's StandardScaler is applied to scale the data, and all numerical columns are transformed to have a mean of 0 and a standard deviation of 1, reducing the likelihood that large values will not influence the model. 
- Another technique applied to the dataset was **Random Oversampling** to resolve the class imbalance.  Scikit-learn’s RandomOverSampler is applied so the minority class is randomly selected and added to the training set until the majority and minority classes are balanced. This process occurs after training/splitting the data.

**Feature Selection & Training & Testing sets:**

The dataset was separated into two categories: 6 features (input) and 1 target (output):
- Features: age, gender, hypertension, heart disease, smoking status
- Target: stroke

For all models, a 75/25 testing/training split was used to achieve the results. 75% was used to train the model, while 25% was used to evaluate it.

**Explanation of Model Choice:**  Several models were tried, and it was the Logistic Regression (random_state=42) that was chosen due to its outperformance against the other models. Additionally, the Logistic Regression was chosen as it's easier to implement, interpret, and train.

The results for each model is displayed below:

![fig3](https://github.com/retroxsky06/Final_Project/blob/main/images/ml_trials.png)

#### Results of Analysis
The model ran successfully with a 76% accuracy; however, the percentage can be misleading due to a high class imbalance.  The precision, recall, and f1 scores are reviewed to better evaluate the model. Results of the model is displayed below in a confusion matrix, where 0 equals 'No Stroke,' and 1 equals 'Stroke.'

![fig5](https://github.com/retroxsky06/Final_Project/blob/main/images/model_run.png)

- Out of 10,642 no stroke outcomes (Actual 0), 7,788 were predicted to be no stroke (Predicted 0), which are true positives. 
- Out of 10,642 no stroke outcomes (Actual 0), 2,854 were predicted to have stroke (Predicted 1), which are considered false negatives.
- Out of 208 stroke outcomes (Actual 1), 44 were predicted to be no stroke (Predicted 0) and are considered false positives.
- Out of 208  stroke outcomes (Actual 1), 164 were predicted to be strokes (Predicted 1) and are considered true negatives.

## Recommendations for Future Analysis
- Run different train and test sets: A 75/25 train/test was only attempted in this analysis and in the future it would be helpful to try other size parameters, such as a 67% train and a 33% test, and a 50% train and 50% test set.
- Add more variables: Instead of only using seven variables (including target), all variables could be applied to see if the accuracy results, and precision, recall, and f1 scores improve. 
- Revisit the tried models to fine tune them to get a better fitting model.
- Explore different machine models and datasets.

### Improvements
An area that could have improved my project is taking more time to do statistical analysis to attain a better understanding of the risk factors and its significance. Additionally, as there are many factors that may impact one’s risk of suffering a stroke, I could have used all the variables for the machine learning algorithm.




import pandas as pd
from sklearn.linear_model import LogisticRegression
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler
from imblearn.over_sampling import RandomOverSampler

def predictions(age, gender, hypertension, heart_disease, ever_married, smoking_status):

    stroke_df = pd.read_csv('flktwo_data.csv')
    X = stroke_df[['age', 'gender', 'hypertension', 'heart_disease', 'ever_married', 'smoking_status']]
    y = stroke_df['stroke']

    data_scaler = StandardScaler()
    X_train, X_test, y_train, y_test = train_test_split(X, y, random_state=42)    
    data_scaler.fit_transform(stroke_df)

    ros = RandomOverSampler(random_state=42)
    X_resampled, y_resampled = ros.fit_resample(X_train, y_train)

    model = LogisticRegression(random_state=42)
    model.fit(X_resampled, y_resampled)
    y_pred = model.predict(X_test)
    print(f"Training Data Score: {model.score(X_resampled, y_resampled)}")
    print(f"Testing Data Score: {model.score(X_test, y_test)}")

    return(model.predict([[age, gender, hypertension, heart_disease, ever_married, smoking_status]]))
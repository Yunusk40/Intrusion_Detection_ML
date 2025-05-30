import joblib
from imblearn.over_sampling import SMOTE
from sklearn.ensemble import RandomForestClassifier
from sklearn.linear_model import LogisticRegression
from sklearn.naive_bayes import GaussianNB
from sklearn.neighbors import KNeighborsClassifier

import pandas as pd
from sklearn.tree import DecisionTreeClassifier


def train_ml_model_multiclass(X_train, y_train):

    # Apply SMOTE to balance the training data
    print("Applying SMOTE to balance training data...")
    smote = SMOTE(random_state=42)
    X_train_balanced, y_train_balanced = smote.fit_resample(X_train, y_train)
    print("Class distribution after SMOTE:")
    print(pd.Series(y_train_balanced).value_counts())

    # Random Forest
    print("Training Random Forest...")
    rf_model = RandomForestClassifier(n_estimators=100, random_state=42)
    rf_model.fit(X_train_balanced, y_train_balanced)
    joblib.dump(rf_model, 'models/random_forest_model.pkl')
    print("Random Forest trained successfully.")

    # K-Nearest Neighbors
    print("Training KNN...")
    knn_model = KNeighborsClassifier(n_neighbors=5)
    knn_model.fit(X_train_balanced, y_train_balanced)
    joblib.dump(knn_model, 'models/knn_model.pkl')
    print("KNN trained successfully.")

    # Decision Tree
    print("Training Decision Tree...")
    dt_model = DecisionTreeClassifier(random_state=42)
    dt_model.fit(X_train_balanced, y_train_balanced)
    joblib.dump(dt_model, 'models/decision_tree_model.pkl')
    print("Decision Tree trained successfully.")

    # Logistic Regression
    print("Training Logistic Regression...")
    lr_model = LogisticRegression(max_iter=1000, random_state=42)
    lr_model.fit(X_train_balanced, y_train_balanced)
    joblib.dump(lr_model, 'models/logistic_regression_model.pkl')
    print("Logistic Regression trained successfully.")

    # Naive Bayes
    print("Training Naive Bayes...")
    nb_model = GaussianNB()
    nb_model.fit(X_train_balanced, y_train_balanced)
    joblib.dump(nb_model, 'models/naive_bayes_model.pkl')
    print("Naive Bayes trained successfully.")

    print("All models trained and saved successfully.")

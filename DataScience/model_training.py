from sklearn.ensemble import RandomForestClassifier
from imblearn.over_sampling import SMOTE, RandomOverSampler
from sklearn.model_selection import train_test_split

from feature_selection import feature_selection

def train_model():
    df_model = feature_selection()

    X = df_model.drop(columns=['had_heart_attack'])
    y = df_model['had_heart_attack']

    # smote = SMOTE(random_state=42)
    ros = RandomOverSampler()
    X_resampled, y_resampled = ros.fit_resample(X, y)

    X_train, X_test, y_train, y_test = train_test_split(X_resampled, y_resampled, test_size=0.2, stratify=y_resampled, random_state=42)

    rf_clf = RandomForestClassifier(n_estimators=100, random_state=42)

    rf_clf.fit(X_train, y_train)

    return rf_clf, X_test, y_test
    
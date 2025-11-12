from typing import Tuple
import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.metrics import f1_score, roc_auc_score
from sklearn.ensemble import RandomForestClassifier

def train_quality_classifier(df: pd.DataFrame, target: str) -> Tuple[RandomForestClassifier, dict]:
    X = df.drop(columns=[target])
    y = df[target]
    X_train, X_test, y_train, y_test = train_test_split(X, y, stratify=y, test_size=0.2, random_state=42)
    clf = RandomForestClassifier(n_estimators=200, random_state=42, n_jobs=-1)
    clf.fit(X_train, y_train)
    preds = clf.predict(X_test)
    probas = clf.predict_proba(X_test)[:,1] if hasattr(clf, "predict_proba") else None
    metrics = {"f1": f1_score(y_test, preds)}
    if probas is not None:
        try:
            metrics["roc_auc"] = roc_auc_score(y_test, probas)
        except Exception:
            pass
    return clf, metrics

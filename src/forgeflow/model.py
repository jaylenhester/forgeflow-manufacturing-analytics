from typing import Dict, Tuple

import pandas as pd
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import f1_score, roc_auc_score
from sklearn.model_selection import train_test_split


def train_quality_classifier(
    df: pd.DataFrame,
    target: str,
    test_size: float = 0.2,
    random_state: int = 42,
) -> Tuple[RandomForestClassifier, Dict[str, float]]:
    """
    Train a RandomForest classifier for a binary quality target.

    Returns:
        model: fitted RandomForestClassifier
        metrics: dict with at least 'f1', and 'roc_auc' when possible
    """
    X = df.drop(columns=[target])
    y = df[target]

    X_train, X_test, y_train, y_test = train_test_split(
        X,
        y,
        stratify=y,
        test_size=test_size,
        random_state=random_state,
    )

    clf = RandomForestClassifier(
        n_estimators=200,
        random_state=random_state,
        n_jobs=-1,
    )
    clf.fit(X_train, y_train)

    preds = clf.predict(X_test)
    metrics: Dict[str, float] = {"f1": f1_score(y_test, preds)}

    if hasattr(clf, "predict_proba"):
        probas = clf.predict_proba(X_test)[:, 1]
        try:
            metrics["roc_auc"] = roc_auc_score(y_test, probas)
        except Exception:
            # e.g., if test split has only one class
            pass

    return clf, metrics
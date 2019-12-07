import joblib
import pandas as pd
from sklearn.metrics import classification_report, recall_score, precision_score, \
                            accuracy_score, roc_auc_score, f1_score


def generate_report(y_test, y_pred):
    report = pd.DataFrame(classification_report(y_true=y_test, y_pred=y_pred, output_dict=True)).T
    return report


def save_model(model, filename):
    joblib.dump(model, filename)


def confusion_matrix(y_test, y_pred):
    table = pd.crosstab(y_test, y_pred, rownames=['Actual'], colnames=['Predicted'])
    return table


def metrics_summary(y_test, y_pred):
    print(f'El área bajo la curva ROC es: {roc_auc_score(y_test, y_pred)}')
    print(f'La exactitud es: {accuracy_score(y_test, y_pred)}')
    print(f'La precisión es: {precision_score(y_test, y_pred)}')
    print(f'El recall es: {recall_score(y_test, y_pred)}')
    print(f'El puntaje F1 es: {f1_score(y_test, y_pred)} \n')


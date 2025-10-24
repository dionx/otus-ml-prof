import sys

import seaborn as sns
import numpy as np
import matplotlib.pyplot as plt
from sklearn.metrics import (
    r2_score, 
    root_mean_squared_error,
    mean_squared_error, 
    mean_absolute_error,
    accuracy_score,
    precision_score,
    recall_score,
    f1_score,
    roc_curve,
    roc_auc_score
)
from typing import List

def corr_matrix_plot(corr_df, title):
    # Визуализируем матрицу корреляции с помощью тепловой карты
    figsize = (corr_df.shape[1] / 2 + 2, corr_df.shape[1] / 2)
    plt.figure(figsize = figsize)
    sns.heatmap(corr_df, annot=True, cmap='coolwarm', fmt='.2f', linewidths=0.5)
    plt.title(title)
    plt.show()


def quality_classification(y_pred, y_true) -> None:
    """
    Стандартный набор метрик качества для моделей классификации

    Parameters:
    -----------
    y_pred : 1d array-like, or label indicator array / sparse matrix
        Predicted labels, as returned by a classifier.
    y_true : 1d array-like, or label indicator array / sparse matrix
        Ground truth (correct) labels.

    Returns:
    --------
    None
    """
    accuracy = accuracy_score(y_true, y_pred)
    precision = precision_score(y_true, y_pred)
    recall = recall_score(y_true, y_pred)
    f1 = f1_score(y_true, y_pred)
    print("Accuracy:  {:.3f}\nPrecision: {:.3f}\nRecall:    {:.3f}\nF1-score:  {:.3f}".format(
        accuracy, precision, recall, f1
    ))

def quality_regress(y_pred, y_true) -> None:
    """
    Стандартный набор метрик качества для регресс-моделей 
    Список всех скорей: get_scorer_names()

    Parameters:
    -----------
    y_pred : 1d array-like, or label indicator array / sparse matrix
        Predicted labels, as returned by a classifier.
    y_true : 1d array-like, or label indicator array / sparse matrix
        Ground truth (correct) labels.

    Returns:
    --------
    None
    """
    # Среднеквадратичная ошибка: (y-ŷ)²
    mse = mean_squared_error(y_true, y_pred)
    # Средняя абсолютная ошибка: y-ŷ
    mae = mean_absolute_error(y_true, y_pred)
    # Объяснённая доля дисперсии: 1 - SSres/SStot. 1.0 — идеально, 0 — нет пользы, < 0 — хуже среднего.
    r2 = r2_score(y_true, y_pred)
    rmse = root_mean_squared_error(y_true, y_pred)
    # Средняя ошибка в процентах y-ŷ
    mape = np.mean(np.abs((np.array(y_true) - np.array(y_pred)) / np.array(y_true)))

    print("MSE:  {:.4f}\nMAE: {:.4f}\nRMSE: {:.4f}\nR2 Score: {:.4f}\nMAPE: {:.4f}".format(
        mse, mae, rmse, r2, mape
    ))

if __name__ == "__main__":
    sys.exit(1)

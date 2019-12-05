import pandas as pd
from sklearn.base import BaseEstimator, TransformerMixin

numerical_features = []
categorical_features = []
features = []


class ColumnsSelector(BaseEstimator, TransformerMixin):
    def __init__(self, columns: list = None, variables: str = 'all') -> None:
        if columns is None and variables == 'all':
            columns = features
        if variables == 'numerical':
            columns = numerical_features
        if variables == 'categorical':
            columns = categorical_features
        if not isinstance(columns, list):
            self.columns = [columns]
        else:
            self.columns = columns
        if not isinstance(variables, str):
            self.variables = str(variables)
        else:
            self.variables = variables

    def fit(self, X: pd.DataFrame, y: pd.Series = None):
        return self

    def transform(self, X: pd.DataFrame) -> pd.DataFrame:
        X = X.loc[:, self.columns]
        return X


class ConvertDtypes(BaseEstimator, TransformerMixin):
    def __init__(self, numerical: list = None, categorical: list = None):
        if numerical is None:
            numerical = numerical_features
        if categorical is None:
            categorical = categorical_features
        if not isinstance(numerical, list):
            self.numerical = [numerical]
        else:
            self.numerical = numerical
        if not isinstance(categorical, list):
            self.categorical = [categorical]
        else:
            self.categorical = categorical

    def fit(self, X: pd.DataFrame, y: pd.Series = None):
        return self

    def transform(self, X: pd.DataFrame) -> pd.DataFrame:
        for numeric in self.numerical:
            X[numeric] = pd.to_numeric(X[numeric])
        for category in self.categorical:
            X[category] = pd.Categorical(X[category], categories=[])
        return X


class GetDummies(BaseEstimator, TransformerMixin):
    def fit(self, X: pd.DataFrame, y: pd.Series = None):
        return self

    def transform(self, X: pd.DataFrame):
        X = pd.get_dummies(X, drop_first=True)
        return X


class GetDataFrame(BaseEstimator, TransformerMixin):
    def __init__(self, columns: list = None, variables: str = 'all'):
        if columns is None and variables == 'all':
            columns = features
        if variables == 'numerical':
            columns = numerical_features
        if variables == 'categorical':
            columns = categorical_features
        if not isinstance(columns, list):
            self.columns = [columns]
        else:
            self.columns = columns
        if not isinstance(variables, str):
            self.variables = str(variables)
        else:
            self.variables = variables

    def fit(self, X: pd.DataFrame, y: pd.Series = None):
        return self

    def transform(self, X: pd.DataFrame) -> pd.DataFrame:
        X = pd.DataFrame(X, columns=self.columns)
        return X

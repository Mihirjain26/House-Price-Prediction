import matplotlib.pyplot as plt
import seaborn as sns
from pandas.api.types import is_numeric_dtype

class DataVisualizer:
    def plot_histogram(self,dataframe,column):
        if column not in dataframe.columns:
            raise ValueError(f"Column '{column}' does not exist.")
        if not is_numeric_dtype(dataframe[column]):
            raise ValueError(f"'{column}' must be a numeric column.")
        plt.figure(figsize=(8, 5))
        sns.histplot(data=dataframe,x=column,kde=True)
        plt.title(f"Distribution of {column}")
        plt.xlabel(column)
        plt.ylabel("Count")
        plt.show()

    def plot_boxplot(self,dataframe,column):
        if column not in dataframe.columns:
            raise ValueError(f"Column '{column}' does not exist.")
        if not is_numeric_dtype(dataframe[column]):
            raise ValueError(f"'{column}' must be a numeric column.")
        plt.figure(figsize=(8, 5))
        sns.boxplot(data=dataframe,y=column)
        plt.title(f"Box Plot of {column}")
        plt.show()

    def plot_countplot(self,dataframe,column):
        if column not in dataframe.columns:
            raise ValueError(f"Column '{column}' does not exist.")
        plt.figure(figsize=(10, 5))
        sns.countplot(data=dataframe,x=column)
        plt.xticks(rotation=45)
        plt.title(f"Count Plot of {column}")
        plt.show()

    def plot_scatterplot(self,dataframe,x_column,y_column):
        if x_column not in dataframe.columns:
            raise ValueError(f"Column '{x_column}' does not exist.")
        if y_column not in dataframe.columns:
            raise ValueError(f"Column '{y_column}' does not exist.")
        plt.figure(figsize=(8, 5))
        sns.scatterplot(data=dataframe,x=x_column,y=y_column)
        plt.title(f"{y_column} vs {x_column}")
        plt.show()

    def plot_lineplot(self,dataframe,x_column,y_column):
        if x_column not in dataframe.columns:
            raise ValueError(f"Column '{x_column}' does not exist.")
        if y_column not in dataframe.columns:
            raise ValueError(f"Column '{y_column}' does not exist.")
        plt.figure(figsize=(8, 5))
        sns.lineplot(data=dataframe,x=x_column,y=y_column)
        plt.title(f"{y_column} vs {x_column}")
        plt.show()

    def plot_barplot(self,dataframe,x_column,y_column):
        if x_column not in dataframe.columns:
            raise ValueError(f"Column '{x_column}' does not exist.")
        if y_column not in dataframe.columns:
            raise ValueError(f"Column '{y_column}' does not exist.")
        plt.figure(figsize=(10, 5))
        sns.barplot(data=dataframe,x=x_column,y=y_column)
        plt.xticks(rotation=45)
        plt.title(f"{y_column} by {x_column}")
        plt.show()

    def plot_heatmap(self,dataframe):
        numeric_dataframe = dataframe.select_dtypes(include=["number"])
        plt.figure(figsize=(12, 8))
        sns.heatmap(numeric_dataframe.corr(),annot=True,cmap="coolwarm")
        plt.title("Correlation Heatmap")
        plt.show()
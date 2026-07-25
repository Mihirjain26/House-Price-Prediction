class DataCleaner:
    def remove_duplicates(self,dataframe):
        return dataframe.drop_duplicates()

    def remove_missing_values(self,dataframe):
        return dataframe.dropna()

    def fill_missing_values(self,dataframe,fill_value):
        return dataframe.fillna(fill_value)

    def clean_column_names(self,dataframe):
        dataframe.columns=(dataframe.columns.str.strip().str.lower().str.replace(" ", "_"))
        return dataframe

    def drop_columns(self,dataframe,columns):
        if isinstance(columns,str):
            columns=[columns]
        missing_columns=[column for column in columns if column not in dataframe.columns]
        if missing_columns:
            raise ValueError(f"Columns not found: {missing_columns}")
        return dataframe.drop(columns=columns)

    def drop_null_columns(self,dataframe):
        null_columns=dataframe.columns[dataframe.isnull().all()]
        return dataframe.drop(columns=null_columns)
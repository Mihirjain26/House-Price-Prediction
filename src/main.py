from data_loader import DataLoader
from data_analyzer import DataAnalyzer
from data_cleaner import DataCleaner
from data_visualization import DataVisualizer


def analyze_menu(dataframe,analyzer):
    while True:
        print("\n====== Analyze Dataset ======")
        print("1. Shape")
        print("2. Columns")
        print("3. Data Types")
        print("4. Missing Values")
        print("5. Summary Statistics")
        print("6. Correlation Matrix")
        print("7. Value Counts")
        print("8. Unique Values")
        print("9. Memory Usage")
        print("10. Back")
        choice=input("Enter your choice: ")

        if choice=="1":
            print(analyzer.get_shape(dataframe))

        elif choice=="2":
            print(analyzer.get_columns(dataframe))

        elif choice=="3":
            print(analyzer.get_dtypes(dataframe))

        elif choice=="4":
            print(analyzer.get_missing_values(dataframe))

        elif choice=="5":
            print(analyzer.get_summary_statistics(dataframe))

        elif choice=="6":
            print(analyzer.get_correlation_matrix(dataframe))

        elif choice=="7":
            try:
                column=input("Enter column name: ")
                print(analyzer.get_value_counts(dataframe,column))
            except Exception as error:
                print(error)

        elif choice=="8":
            column=input("Enter column name: ")
            print(analyzer.get_unique_values(dataframe,column))

        elif choice=="9":
            print(analyzer.get_memory_usage(dataframe))
            print(f"\nTotal Memory Usage: {analyzer.get_total_memory_usage(dataframe)} bytes")

        elif choice=="10":
            break

        else:
            print("Invalid choice.")



def cleaning_menu(dataframe,cleaner):
    while True:
        print("\n====== Clean Dataset ======")
        print("1. Remove Duplicates")
        print("2. Remove Missing Values")
        print("3. Fill Missing Values")
        print("4. Clean Column Names")
        print("5. Drop Columns")
        print("6. Drop Null Columns")
        print("7. Back")
        choice=input("Enter your choice: ")

        if choice=="1":
            dataframe=cleaner.remove_duplicates(dataframe)
            print("Duplicates removed.")

        elif choice=="2":
            dataframe=cleaner.remove_missing_values(dataframe)
            print("Missing values removed.")

        elif choice=="3":
            value=input("Enter fill value: ")
            dataframe=cleaner.fill_missing_values(dataframe,value)
            print("Missing values filled.")

        elif choice=="4":
            dataframe=cleaner.clean_column_names(dataframe)
            print("Column names cleaned.")

        elif choice=="5":
            columns=input("Enter column names separated by commas: ")
            columns=[column.strip() for column in columns.split(",")]
            try:
                dataframe=cleaner.drop_columns(dataframe,columns)
                print("Columns dropped.")
            except Exception as error:
                print(error)

        elif choice=="6":
            dataframe=cleaner.drop_null_columns(dataframe)
            print("Null columns removed.")

        elif choice=="7":
            return dataframe

        else:
            print("Invalid choice.")




def visualization_menu(dataframe,visualizer):
    while True:
        print("\n====== Visualize Dataset ======")
        print("1. Histogram")
        print("2. Box Plot")
        print("3. Count Plot")
        print("4. Scatter Plot")
        print("5. Line Plot")
        print("6. Bar Plot")
        print("7. Heatmap")
        print("8. Back")
        choice=input("Enter your choice: ")

        if choice=="1":
            column=input("Enter column name: ")
            try:
                visualizer.plot_histogram(dataframe,column)
            except Exception as error:
                print(error)

        elif choice=="2":
            column=input("Enter column name: ")
            visualizer.plot_boxplot(dataframe,column)

        elif choice=="3":
            column=input("Enter column name: ")
            visualizer.plot_countplot(dataframe,column)

        elif choice=="4":
            x_column=input("Enter X column: ")
            y_column=input("Enter Y column: ")
            visualizer.plot_scatterplot(dataframe,x_column,y_column)

        elif choice=="5":
            x_column=input("Enter X column: ")
            y_column=input("Enter Y column: ")
            visualizer.plot_lineplot(dataframe,x_column,y_column)

        elif choice=="6":
            x_column=input("Enter X column: ")
            y_column=input("Enter Y column: ")
            visualizer.plot_barplot(dataframe,x_column,y_column)

        elif choice=="7":
            visualizer.plot_heatmap(dataframe)

        elif choice=="8":
            break

        else:
            print("Invalid choice.")


                       

def main():

    loader=DataLoader()
    analyzer=DataAnalyzer()
    cleaner=DataCleaner()
    visualizer=DataVisualizer()
    dataframe=None

    while True:
        print("\n========== Data Analysis Toolkit ==========")
        print("1. Load Dataset")
        print("2. Analyze Dataset")
        print("3. Clean Dataset")
        print("4. Visualize Dataset")
        print("5. Save Dataset")
        print("6. Exit")
        choice=input("Enter your choice: ")

        if choice=="1":
            file_path=input("Enter CSV file path: ")
            try:
                dataframe=loader.load_csv(file_path)
                print("\nDataset loaded successfully.")
                print(f"Shape: {dataframe.shape}")
            except Exception as error:
                print(error)

        elif choice=="2":
            if dataframe is None:
                print("\nPlease load a dataset first.")
            else:
                analyze_menu(dataframe,analyzer)

        elif choice=="3":
            if dataframe is None:
                print("\nPlease load a dataset first.")
            else:
                dataframe=cleaning_menu(dataframe,cleaner)

        elif choice=="4":
            if dataframe is None:
                print("\nPlease load a dataset first.")
            else:
                visualization_menu(dataframe,visualizer)

        elif choice=="5":
            if dataframe is None:
                print("\nNo dataset available to save.")
            else:
                output_path=input("Enter output file path: ")
                try:
                    loader.save_csv(dataframe,output_path)
                    print("\nDataset saved successfully.")
                except Exception as error:
                    print(error)

        elif choice=="6":
            print("\nThank you for using Data Analysis Toolkit.")
            break

        else:
            print("\nInvalid choice. Please try again.")


if __name__=="__main__":
    main()
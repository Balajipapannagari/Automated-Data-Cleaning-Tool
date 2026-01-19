import pandas as pd

def clean_data(input_file, output_file):
    try:
        # Read CSV file
        df = pd.read_csv(input_file)
        print("Original Data:")
        print(df)

        # Remove duplicate rows
        df = df.drop_duplicates()

        # Handle missing values
        df['Age'] = pd.to_numeric(df['Age'], errors='coerce')
        df['Age'] = df['Age'].fillna(df['Age'].mean())

        df['Salary'] = pd.to_numeric(df['Salary'], errors='coerce')
        df['Salary'] = df['Salary'].fillna(df['Salary'].median())

        df['Join_Date'] = pd.to_datetime(df['Join_Date'], errors='coerce')
        df['Join_Date'] = df['Join_Date'].fillna(method='ffill')

        # Strip extra spaces from string columns
        df['Name'] = df['Name'].str.strip()

        # Save cleaned data
        df.to_csv(output_file, index=False)

        print("\nCleaned Data:")
        print(df)
        print(f"\nCleaned file saved as: {output_file}")

    except FileNotFoundError:
        print("CSV file not found. Please check the file path.")
    except Exception as e:
        print("Error:", e)


if __name__ == "__main__":
    input_csv = "messy_data.csv"
    output_csv = "cleaned_data.csv"
    clean_data(input_csv, output_csv)

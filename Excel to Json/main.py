import pandas as pd
import os

# Define the file paths
excel_file_path = "D:\\Study\\Programs\\Projects\\Excel to Json\\example.xlsx"  # Replace with your Excel file path
json_file_path = "D:\\Study\\Programs\\Projects\\Excel to Json\\output.json"  # Replace with your desired JSON file path

try:
    # Verify if the Excel file exists
    if not os.path.exists(excel_file_path):
        raise FileNotFoundError(f"The file '{excel_file_path}' does not exist.")

    # Load the Excel file
    data = pd.read_excel(excel_file_path)
    print("Excel file loaded successfully!")
    print(data.head())

    # Convert the DataFrame to JSON
    data_json = data.to_json(orient="records", indent=4)

    # Write the JSON to a file
    with open(json_file_path, "w") as json_file:
        json_file.write(data_json)

    print(f"JSON file created successfully at '{os.path.abspath(json_file_path)}'!")
except FileNotFoundError as fnf_error:
    print(f"Error: {fnf_error}")
except PermissionError:
    print(f"Error: Permission denied when trying to write to '{json_file_path}'.")
except Exception as e:
    print(f"An unexpected error occurred: {e}")

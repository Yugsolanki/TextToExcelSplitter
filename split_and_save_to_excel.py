import pandas as pd
import os

def split_and_save_to_excel(input_file, delimiter=',', max_rows_per_sheet=1_048_576):
    # Read the input file into a DataFrame with custom delimiter
    df = pd.read_csv(input_file, delimiter=delimiter)
    
    # Check if the header is present and set it
    header = df.iloc[0]
    df = df[1:]
    df.columns = header

    # Get unique values from the second column (index 1)
    unique_values = df.iloc[:, 1].unique()

    for value in unique_values:
        # Filter rows based on the unique value in the second column
        filtered_df = df[df.iloc[:, 1] == value]

        # Split the data into multiple Excel files if necessary
        num_sheets = (len(filtered_df) - 1) // max_rows_per_sheet + 1
        for i in range(num_sheets):
            start_row = i * max_rows_per_sheet
            end_row = min(start_row + max_rows_per_sheet, len(filtered_df))
            
            sheet_data = filtered_df.iloc[start_row:end_row]

            # Determine the output file name
            base_name, ext = os.path.splitext(os.path.basename(input_file))
            output_file = f"{base_name}_{value}_part{i+1}.xlsx"

            # Save the data to an Excel file
            with pd.ExcelWriter(output_file, engine='openpyxl') as writer:
                sheet_data.to_excel(writer, index=False)

            print(f"Saved {output_file} with {len(sheet_data)} rows.")

if __name__ == "__main__":
    input_file = "path_to_your_input_file.txt"
    delimiter = ','  # Change this to your custom delimiter if needed
    split_and_save_to_excel(input_file, delimiter)

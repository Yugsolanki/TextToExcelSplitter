A Python script that reads a text file with a custom delimiter, splits the data based on unique values in the second column, and writes each split to an Excel file. If the data is too big for a single Excel file, multiple files are 
created.

## Prerequisites

1. **Python 3.x**: Make sure you have Python installed on your system.
2. **Install Required Libraries**:
   ```bash
   pip install pandas openpyxl
   ```

## Usage

1. **Clone the Repository**:
   ```bash
   git clone https://github.com/Yugsolanki/TextToExcelSplitter.git
   cd TextToExcelSplitter
   ```

2. **Prepare Your Input File**:
   - Ensure your input file is a text file where rows are separated by newline characters (`\n`).
   - Values in each row should be separated by your specified delimiter (e.g., comma `,`, tab `\t`, etc.).

3. **Run the Script**:
   ```bash
   python split_and_save_to_excel.py --input_file path/to/your/input.txt --delimiter , --max_rows_per_sheet 1048576
   ```

   - `--input_file`: Path to your input text file.
   - `--delimiter`: Delimiter used in the input file. Default is `,`.
   - `--max_rows_per_sheet`: Maximum number of rows per Excel sheet. Default is `1,048,576`.

## Example

Given an input file `data.txt` with content:
```
Header1,Header2,Header3
Value1,CategoryA,Data1
Value2,CategoryB,Data2
Value3,CategoryA,Data3
```

Running the script:
```bash
python split_and_save_to_excel.py --input_file data.txt
```

Will produce two Excel files:
- `data_CategoryA_part1.xlsx`
- `data_CategoryB_part1.xlsx`

## Notes

- The first line of the input file is assumed to be a header.
- If the filtered data exceeds the maximum number of rows per sheet, it will be split across multiple sheets within a single Excel file or multiple files.
- Adjust the `max_rows_per_sheet` parameter if you need different limits for rows per sheet.

## Contributing

Feel free to fork this repository and contribute! Please create an issue if you encounter any bugs or have feature requests.

## License

This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for details.

### Directory Structure
```
TextToExcelSplitter/
├── split_and_save_to_excel.py
├── README.md
└── LICENSE
```

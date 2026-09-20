# Bank Marketing Data Cleaning

A Python data-cleaning project that transforms a raw bank marketing dataset into three structured CSV files for further analysis or database storage.

## Project Overview

The script uses pandas and NumPy to clean, transform, and separate the source data into:

- `client.csv` — client demographics, education, credit default, and mortgage data.
- `campaign.csv` — contact history, campaign outcomes, and formatted contact dates.
- `economics.csv` — consumer price index and three-month Euribor rate.

Key transformations include handling missing values, standardizing text, converting categorical values to booleans, assigning correct data types, and creating dates in `YYYY-MM-DD` format.

## Technologies

- Python
- pandas
- NumPy

## Run the Project

```bash
pip install pandas numpy
python project/code.py
```

The processed CSV files are generated in the `project` directory.

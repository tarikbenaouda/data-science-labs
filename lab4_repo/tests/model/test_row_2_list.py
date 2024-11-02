import sys
from pathlib import Path

# Add the src directory to sys.path
sys.path.append(str(Path(__file__).resolve().parents[2] / "src/model"))

from row_2_list import row_to_list
import csv
import pytest

def test_for_clean_row():
    assert row_to_list ("2,081\t314,942\n") == ["2,081","314,942"]

# def test_for_missing_area():
#     assert row_to_list ("\t314,942\n") is None

# def test_for_missing_tab():
#     assert row_to_list ("2,081314,942\n") is None


# Load your dataset from the CSV file
dataset = []
with open('lab4_repo/data/house_price.csv', 'r') as csvfile:
    csvreader = csv.reader(csvfile)
    for row in csvreader:
        dataset.append(row)

# Test if the function correctly handles rows with missing values
# Parametrize the test function to iterate through each row in the dataset
@pytest.mark.parametrize("row_number, input_row", enumerate(dataset, 1))
def test_row_to_list_with_missing_values(row_number, input_row):
    input_string = ' '.join(input_row)  # Convert list to string
    result = row_to_list(input_string, ";")  # Call your function to convert input_string to a list
    # Check if the result contains any missing values (empty elements)
    missing_values = any(value == '' for value in result)
    assert not missing_values, f"Missing value found in the row no.{row_number}: {input_row}"
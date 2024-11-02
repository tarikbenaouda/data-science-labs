import sys
from pathlib import Path

# Add the src directory to sys.path
sys.path.append(str(Path(__file__).resolve().parents[2] / "src/model"))

from sentiment import extract_sentiment

from textblob import TextBlob
import pytest
import csv

testdata =["Borussia Dortmund’s loss was heartbreaking as they failed to gain momentums from their  two goals advance. Very disappointing results for our Algerian player Bensebaini.",\
           "Barcelona played brilliantly last Wednesday. Rafinia’s hat-trick was pure magic. Visca Barça!"]


with open('lab4_repo/data/soccer_sentiment_analysis.csv', 'r') as csvfile:
    csvreader = csv.reader(csvfile)
    for row in csvreader:
        testdata.append(''.join(row))

@pytest.mark.parametrize('sample', testdata)
def test_extract_sentiment(sample):

    neg_sentiment = extract_sentiment(sample)

    assert neg_sentiment <= 0
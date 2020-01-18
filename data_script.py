""" Script used to import CSV data from a publicly accessible URL or relative file path.

Usage:
  load_data.py <csv_file>

"""
from docopt import docopt
import pandas as pd

arguments = docopt(__doc__)
df = pd.read_csv(arguments['<csv_file>'])
df.to_csv("src/data/data.csv")

""" Script used to import CSV data from a publicly accessible URL or relative file path.

Usage:
  data_script.py <csv_file>

Example:
  python src/data_script.py https://opendatatc.blob.core.windows.net/opendatatc/NCDB_2017.csv

"""
from docopt import docopt
import pandas as pd

arguments = docopt(__doc__)
df = pd.read_csv(arguments['<csv_file>'])
df.to_csv("data/data.csv")

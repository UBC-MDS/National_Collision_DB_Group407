all: data/raw_data.csv data/cleaned_test_data.csv results/fatal_features.png

data/raw_data.csv : src/data_read.R
	Rscript src/data_read.R --filepath='https://opendatatc.blob.core.windows.net/opendatatc/NCDB_2017.csv'
data/cleaned_test_data.csv : data/raw_data.csv src/data_clean.py
	python src/data_clean.py --read_path=data/raw_data.csv --write_path=data/
results/fatal_features.png : data/cleaned_train_data.csv src/eda.py
	python src/eda.py --read_path=data/cleaned_train_data.csv --write_path=results/
results/rf_classification.csv : src/ml_lgr_rf.py
	python src/ml_lgr_rf.py 

clean :
	rm -f data/*.csv
	rm -f results/*.png
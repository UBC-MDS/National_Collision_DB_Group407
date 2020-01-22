# author: DSCI_522_Group_207
# date: 2020-01-22
#
"This script is used to download data from a 
publicly accessible URL and split the data into 80% traning and 20% testing data.
 
Usage: read_data.R --filepath=<filepath>
 
Example:
   Rscript read_data.R --filepath='https://opendatatc.blob.core.windows.net/opendatatc/NCDB_2017.csv'

Options:
<filepath>        Takes a file path (this is a required positional argument)
" -> doc

library(tidyverse)
library(docopt)
library(caTools)

opt <- docopt(doc)

download.file(url = opt$filepath, destfile = "../data/raw_data.csv")

data <- read.csv("../data/raw_data.csv")

set.seed(407)   #  set seed to ensure you always have same random numbers generated

sample = sample.split(data,SplitRatio = 0.8) # splits the data in the ratio mentioned in SplitRatio. After splitting marks these rows as logical TRUE and the the remaining are marked as logical FALSE
train_data=subset(data,sample ==TRUE) # creates a training dataset named train1 with rows which are marked as TRUE
test_data=subset(data, sample==FALSE)

write.csv(train_data, "../data/train_data.csv")
write.csv(test_data, "../data/test_data.csv")


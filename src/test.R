library(caTools)
data <- read.csv("../data/raw_data.csv")
set.seed(407)   #  set seed to ensure you always have same random numbers generated

sample = sample.split(data,SplitRatio = 0.8) # splits the data in the ratio mentioned in SplitRatio. After splitting marks these rows as logical TRUE and the the remaining are marked as logical FALSE
train_data=subset(data,sample ==TRUE) # creates a training dataset named train1 with rows which are marked as TRUE
test_data=subset(data, sample==FALSE)

write.csv(train_data, "../data/train_data.csv")
write.csv(test_data, "../data/test_data.csv")

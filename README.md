# National_Collision_DB_Group407

### Proposal

The data we are using is from the National Collision Database and can be found on the [Government of Canada website](https://open.canada.ca/data/en/dataset/1eb9eba7-71d1-4b30-9fb1-30cbdab7e63a). It’s a database that contains all police-reported motor vehicle collisions on public roads in Canada. The data is from 1999 to 2017. Each row provides several data points for a passenger with the detailed summary statistics of the collision.

**Research question 01**
Our first research question is: “Is the injury rate of sitting in the front row passenger seat different from sitting on the second row left seat?” This is an inferential question. We will be doing hypothesis testing with a 95% confidence interval. The null and alternative hypothesis are included as follows:

`H_0`: The injury rate of sitting in the front row passenger seat has no difference from sitting in the second row left seat.
`H_1`: The injury rate of sitting in the front row passenger seat is different from sitting in the second row left seat.

We will begin our project by first wrangling and cleaning our dataset. In the wrangling stage, we will limit the vehicle type to light-duty vehicle (passenger car, passenger van, light utility vehicles and light duty pick up trucks). Then, we will further filter the data - keeping only passengers sitting at front row, right outboard and passengers sitting at second row, left outboard in the same vehicle and label them as ‘passenger seat’ and ‘behind driver’, respectively. Doing this will help us to make sure each data points are independent and the sample sizes are equal. This will help us with performing the z-test after.

After wrangling the data, we will be doing a two tailed proportion z-test to compare if there is a significant difference between the fatality rate between the two groups.

We looked into our dataset to identify potential data imbalance issue by looking at the data points in each class and created a stacked bar chart to visualize the result. The two class: "injury" and "non-injury" seem to be pretty balanced in our dataset, which is an important aspect to keep in mind in our future analysis.

![RQ1](https://raw.githubusercontent.com/schepal/National_Collision_DB_Group407/master/src/eda/md_file/output_24_0.png)


**Research Question 02**: What features are indicative of a person not surviving in a car accident?

The `P_ISEV` feature provides the fatality of the accident. After splitting the data into train and test sets, we would like to predict which features strongly predict the fatality. Using a decision tree and/or random forest, we would like to understand the contribution of the features and predict if an accident would result in fatality or not. This would be useful for driving license agencies to investigate further on sensitive spots in the country and improve driver safety.

![Roadway Configuration Chart](https://raw.githubusercontent.com/schepal/National_Collision_DB_Group407/master/src/eda/md_file/output_16_0.png)


**Research Question 03**: Given the features(weather, time of the day, road surface, etc.) determine if emergency services would be needed for an accident.

In this question, we would like to explore which accidents would require emergency medical services. Unlike in the previous case, emergency services will be needed. This question would help build staffing abilities for hospitals during appropriate hours so that accidents are immediately tended to. We would transform the target variables into 1 and 0 for the severity of the emergency. After training the model, we would like to be able to predict the staffing requirements for the test set.

![Medical Service Needs](https://raw.githubusercontent.com/schepal/National_Collision_DB_Group407/master/src/eda/md_file/output_18_0.png)

## Usage

To run the download script file, clone this GitHub repository, install the
[dependencies](#dependencies) listed below, and run the following
commands at the command line/terminal from the root directory of this
project:

    Rscript src/data_read.R --filepath='https://opendatatc.blob.core.windows.net/opendatatc/NCDB_2017.csv'
    python src/data_clean.py --read_path= data/file.csv --write_path= data/
    python src/eda.py --read_path= data/cleaned_train_data.csv --write_path= results/
    Rscript -e "rmarkdown::render('doc/eda_report.Rmd')"
    python src/ml_lgr_rf.py
    Rscript -e "rmarkdown::render('doc/final_report.Rmd')"

## Dependencies
Python 3.7.3 and Python packages:
- docopt==0.6.2
- pandas==0.25.1
- matplotlib==3.1.1
- altair==3.2.0
- numpy==1.17.2
- sklearn==0.0
- pandas-profiling==2.4.0

## License
National Collision Database documents are licensed under the
Open Government Licence - Canada. If re-using/re-mixing please provide attribution and link to this webpage.

## References
<div id="refs" class="references">
<div id="ref-Transport Canada 2017">

Transport Canada. 2017. “National Collision Database.”
Government of Canada; <https://open.canada.ca/data/en/dataset/1eb9eba7-71d1-4b30-9fb1-30cbdab7e63a>.

</div>

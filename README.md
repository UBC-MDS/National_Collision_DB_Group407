# National_Collision_DB_Group407

### Proposal

The data we are using is from the National Collision Database and can be found on the [Government of Canada website](https://open.canada.ca/data/en/dataset/1eb9eba7-71d1-4b30-9fb1-30cbdab7e63a). It’s a database that contains all police-reported motor vehicle collisions on public roads in Canada. The data is from 1999 to 2017. Each row provides several data points for a passenger with the detailed summary statistics of the collision.

Our research question is: “Is the injury rate of sitting in the front row passenger seat different from sitting on the second row left seat?” This is an inferential question. We will be doing hypothesis testing with a 95% confidence interval. The null and alternative hypothesis are included as follows:

`H_0`: The injury rate of sitting in the front row passenger seat has no difference from sitting in the second row left seat.
`H_1`: The injury rate of sitting in the front row passenger seat is different from sitting in the second row left seat.

We will begin our project by first wrangling and cleaning our dataset. In the wrangling, we will filter out the vehicle types of light-duty vehicle (passenger car, passenger van, light utility vehicles and light duty pick up trucks). Then, we will filter out passengers with the seat position in the front row, right outboard and passengers with seat position in the second row, left outboard in the same vehicle and divide them into ‘front row’ and ‘second row’ group. 

After wrangling the data, we will be doing a two tailed proportion z-test to compare if there is a significant difference between the fatality rate between the two groups.


## Usage

To run the download script file, clone this GitHub repository, install the
[dependencies](#dependencies) listed below, and run the following
commands at the command line/terminal from the root directory of this
project:

    python src/download_data.py https://opendatatc.blob.core.windows.net/opendatatc/NCDB_2017.csv


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



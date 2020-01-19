# National_Collision_DB_Group407

### Proposal

The data we are using is from the National Collision Database and can be found on the [Government of Canada website](https://open.canada.ca/data/en/dataset/1eb9eba7-71d1-4b30-9fb1-30cbdab7e63a). It’s a database that contains all police-reported motor vehicle collisions on public roads in Canada. The data is from 1999 to 2017. Each row is a passenger data with the detailed information of the collision, car and the passenger.

Our research question is: “Is the injury rate of sitting on the front row passenger seat different from sitting on the second row left seat?” This is an inferential question. We will be doing hypothesis testing with a 95% confidence interval. The null and alternative hypothesis are included as follow:
`H_0`: The injury rate of sitting on the front row passenger seat has no difference from sitting on the second row left seat.
`H_1`: The injury rate of sitting on the front row passenger seat is different from sitting on the second row left seat.

We will be wrangling the data first. In the wrangling, we will filter out the vehicle type of light-duty vehicle (passenger car, passenger van, light utility vehicles and light duty pick up trucks). Then, we will filter out passengers with seat position in the front row, right outboard and passengers with seat position in the second row, left outboard in the same vehicle and divide them into ‘front row’ and ‘second row’ group. 

After wrangling the data, we will be doing a two-proportion Z test to compare if there is a significant difference between the fatality rate in the two groups.


Resources:
[Noational Collision Database from Government of Canada website](https://open.canada.ca/data/en/dataset/1eb9eba7-71d1-4b30-9fb1-30cbdab7e63a)


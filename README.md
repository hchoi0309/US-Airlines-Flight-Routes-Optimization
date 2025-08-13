# US-Airlines-Flight-Routes-Optimization
Effective allocation of resources for different flights is pivotal for airline companies to maximize their profit. This project considers operational constraints and variations in passenger demand over time to suggest an optimal sales strategy for different US airlines. By leveraging two comprehensive datasets that each contain historical information about the number of passengers [1] and the costs incurred [2], a Mixed-Integer Nonlinear Programming (MINLP) problem was modelled to capture the revenue generated depending on the amounts of daily seats sold for American flight routes.

In this model, companies are expected to provide information about their operating cities of each origin and destination, as well as the size and capacity of their fleet. Gradient descent was used in the objective function to find the parameter values that would accurately represent the dynamic relationship between the supply of tickets sold and the demand of customers. In addition, different algorithms, such as linear regression, random forests, gradient boosting, and a multilayer-preceptron model, were tested to forecast the total number of passengers for varying routes. These values were then used as upper limits to constrain the amount of seats sold by the airline company.

## References
[1]https://www.kaggle.com/datasets/amitzala/us-airline-flight-routes-and-fares?select=US+Airline+Flight+Routes+and+Fares.csv </br>
[2]https://www.kaggle.com/datasets/xan3011/airline-data-project-mit-1995-2019?select=Original+MIT+data

# Machine Learning 

A python Implementation for Machine Learning 

This is a part of a series of HyperionDev Capstone Projects, I will implement a k-means algorithm and run it on the provided dataset with the python language.

# HyperionDev Capstone Projects Instrctions 

Your task is to implement the k-means algorithm and run it on the provided data using the following steps as guidance:

			■ Open the file kmeans.py, in which comments have been included to help guide you. 
                    Take a look at the data provided, which consists of the two variables 
                    (life expectancy, birth rate) measured for each country, and note that 
                    there is one dataset for 2008 and one from 1953. This data is in csv 
                    file format, which can be opened just like a text file. Open each file 
                    and take a look at how the data is laid out. 
                    Your algorithm should work on either data set. 
				
				● Find the distance to each of the centroids from each of the points. Ie. 
                              If you have 15 points and 3 centroids, you need to calculate the distance 
                              from each of the 15 points to each of the 3 centroids. 
				
				● Compute the two-dimensional mean. To compute the mean (or average) of 
                              a number of observations, you simply add all the observations together 
                              and then divide by the number of observations you added together. 
                              Thus, to compute the two-dimensional mean (ie. the mean coordinate point (𝑥, 𝑦)), 
                              calculate the mean of the x values and the mean of the y values of all the points.
				
				● Read in the data from either of the provided csv files. Remember that BirthRate is the ‘x’ value and 
                              LifeExpectancy is the ‘y’ value. Hint: after reading in the data from the csv file, the data should be 
                              in a form where you should easily be able to plot all the data as a scatter plot to get an idea of what 
                              the data distribution looks like. 
				
				● Visualise the data as a scatter plot, with the points in each cluster shown in a different colour.
				
			■ After doing this, implement the k-means algorithm using the steps described in the ‘Specifications 
                    of k-means’ section above. You should let the user decide how many clusters (k) there should be 
                    (although it might make sense to begin with just two clusters, and generalize later. I.e. k=2). 
                    The algorithm will need to run for a user-specified number of iterations, though to begin you 
                    can hard-code this in with the value 6 and update this later. 
                    You do not need to monitor the algorithm for convergence at this point.
			
			■ Try enter 20 years and 8 (%) and see what the difference is
			depending on the type of interest rate! 
			
		3. If the user selects ‘bond’, do the following: 
			■ Ask the user to input:
			 
				● The present value of the house. E.g. 100000 
				● The interest rate. E.g. 7 
				● The number of months they plan to take to repay the
				bond. E.g. 120
				
			■ Calculate how much money the user will have to repay each
			month and output the answer.

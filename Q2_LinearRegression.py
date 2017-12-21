#simple linear regression model > y = b0 + b1 * x

#calculate the mean value of a list of numbers
#sum of the numbers divided by total count of the numbers
def mean(values):
	return sum(values) / float(len(values))

#calculate the variance of a list of numbers
#sum squared difference for each value compared to the mean
def variance(values, mean):
	return sum([(x-mean)**2 for x in values])

#calculate covariance between two groups of number
#describe changes in relationship between x and y
def covariance(x, mean_x, y, mean_y):
	covar = 0.0
	for i in range(len(x)):
		covar += (x[i] - mean_x) * (y[i] - mean_y)
	return covar

#calculate estimated coefficients
def coefficients(dataset):
	x = [row[0] for row in dataset]
	y = [row[1] for row in dataset]
	x_mean, y_mean = mean(x), mean(y)
	b1 = covariance(x, x_mean, y, y_mean) / variance(x, x_mean)
	b0 = y_mean - b1 * x_mean
	return [b0, b1]

#calculate root mean squared error
def rmse_metric(actual, predicted):
	sum_error = 0.0
	for i in range(len(actual)):
		prediction_error = predicted[i] - actual[i]
		sum_error += (prediction_error ** 2)
	mean_error = sum_error / float(len(actual))
    # find the squareroot
	return (mean_error ** 0.5)

#evaluate regression algorithm on training dataset using root mean squared error
def evaluate_algorithm(dataset, algorithm):
	test_set = list()
	for row in dataset:
		row_copy = list(row)
		row_copy[-1] = None
		test_set.append(row_copy)
	predicted = algorithm(dataset, test_set)
	print(predicted)
	actual = [row[-1] for row in dataset]
	rmse = rmse_metric(actual, predicted)
	return rmse

#simple linear regression algorithm for prediction
def simple_linear_regression(train, test):
	predictions = list()
	b0, b1 = coefficients(train)
	for row in test:
		yhat = b0 + b1 * row[0]
		predictions.append(yhat)
	return predictions

#test simple linear regression
dataset = [[2, 1], [5, 3], [2, 3], [3, 2], [4, 4]]
rmse = evaluate_algorithm(dataset, simple_linear_regression)
print('RMSE: %.3f' % (rmse))
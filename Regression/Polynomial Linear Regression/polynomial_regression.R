#dataset preprocessing

dataset = read.csv('Position_Salaries.csv')
dataset = dataset[2:3]

#splitting of dataset into training and test data is not required

#feature scaling is also not required

#fitting linear regression model
lin_reg = lm(formula = Salary ~ .,
             data = dataset)

#fitting polynomial regression model
dataset$Level2 = dataset$Level^2
dataset$Level3 = dataset$Level^3

poly_reg = lm(formula = Salary ~ .,
              data = dataset)

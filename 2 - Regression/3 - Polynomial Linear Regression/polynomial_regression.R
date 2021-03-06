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
dataset$Level4 = dataset$Level^4

poly_reg = lm(formula = Salary ~ .,
              data = dataset)

#adding visualisations for linear regression model
library(ggplot2)
ggplot()+
  geom_point(aes(x = dataset$Level, y = dataset$Salary),
             color = 'red')+
  geom_line(aes(x = dataset$Level, y = predict(lin_reg, newdata = dataset)),
            color = 'blue')+
  ggtitle('Linear Regression')+
  xlab('Level')+
  ylab('Salary')


x_grid = seq(min(dataset$Level), max(dataset$Level), 0.1)
ggplot()+
  geom_point(aes(x = dataset$Level, y = dataset$Salary),
             color = 'red')+
  geom_line(aes(x = x_grid, y = predict(poly_reg,
                                        newdata = data.frame(Level = x_grid,
                                                             Level2 = x_grid^2,
                                                             Level3 = x_grid^3,
                                                             Level4 = x_grid^4))),
            color = 'blue')+
  ggtitle('Polynomial Regression')+
  xlab('Level')+
  ylab('Salary')

#predicting a new result with linear regression model
y_pred = predict(lin_reg, data.frame(Level = 6.5))

#predicting the new result using the polynomial regression model
y_pred = predict(poly_reg, data.frame(Level = 6.5,
                                      Level2 = 6.5^2,
                                      Level3 = 6.5^3,
                                      Level4 = 6.5^4))


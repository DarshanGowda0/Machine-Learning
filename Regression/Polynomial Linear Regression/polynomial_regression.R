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

ggplot()+
  geom_point(aes(x = dataset$Level, y = dataset$Salary),
             color = 'red')+
  geom_line(aes(x = dataset$Level, y = predict(poly_reg, newdata = dataset)),
            color = 'blue')+
  ggtitle('Polynomial Regression')+
  xlab('Level')+
  ylab('Salary')

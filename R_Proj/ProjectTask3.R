# Conrad Ibanez
# DSC640 Winter 2020
# Project Task 1: Dashboard

#https://plotly.com/r/bar-charts/#stacked-bar-chart

#install.packages("plotly")
#install.packages("tidyverse")
#install.packages("Rcpp")
#install.packages("broom")
#install.packages("dplyr")

library(readxl)
library(plotly)
library(dplyr)

#Set working directory
setwd("C:/Users/kryp_/Documents/conrad/MSDSC/DSC640/project/R_proj/")

#Import the data
fatalities <- read_excel("../data/Fatalities_and_Fatality_Rates_1899-2018_Clean.xls")

#Basic line chart
fig <- plot_ly(fatalities, x = ~Year, y = ~Total_Fatalities, type = 'scatter', mode = 'lines', line = list(color = 'red'))
fig <- fig %>% layout(title = 'U.S. Vehicle Fatalities from 2000 - 2014',
                      yaxis = list(title = 'Fatalities', showticklabels = TRUE, tickprefix="<b>",ticksuffix ="</b><br>"),xaxis=list(title = 'Year', range=c('2000', '2014')))

print(fig)

#Import the data
fatalities <- read_excel("../data/table9_2014-accidents_ntsb-classification-1995-2014-for-u-s-air-carriers_Clean.xls")

#Basic line chart
fig <- plot_ly(fatalities, x = ~Year, y = ~Fatalities_Total, type = 'scatter', mode = 'lines', line = list(color = 'grey'))
fig <- fig %>% layout(title = 'U.S. Airline Fatalities from 2000 - 2014',
                      yaxis = list(title = 'Fatalities', showticklabels = TRUE, tickprefix="<b>",ticksuffix ="</b><br>"),xaxis=list(title = 'Year', range=c('2000', '2014')))

list(title = "Soil grouping",
     ticktext = sprintf("<i>%s</i>", levels(factor(iris$Species))),
     tickvals = levels(factor(iris$Species))
)
print(fig)


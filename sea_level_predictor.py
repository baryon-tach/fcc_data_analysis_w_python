import pandas as pd
import matplotlib.pyplot as plt
from scipy.stats import linregress

def draw_plot():
    # Read data from file
    sea = pd.read_csv('epa-sea-level.csv')

    # Create scatter plot
    x = sea.Year
    y = sea['CSIRO Adjusted Sea Level']

    plt.figure(figsize=(7,5))
    plt.scatter(x,y, label='data')

    # Create first line of best fit
    sea1 = sea.copy
    x2 = pd.Series([i for i in range(1880,2051)])

    res = linregress(x,y )
    plt.plot(x2 , res.intercept + res.slope*x2, 'red', linewidth=2, label = 'fitted line')


    # Create second line of best fit
    sea1 = sea.loc[(sea.Year >= 2000)]
    x3 = sea1.Year
    y3 = sea1['CSIRO Adjusted Sea Level']
    res2 = linregress(x3, y3)

    x4 = pd.Series([i for i in range(2000,2051)])

    plt.plot(x4, res2.intercept + res2.slope*x4, 'orange', linewidth=3, label='fitted line 2')

    # Add labels and title
    plt.xlabel('Year')
    plt.ylabel('Sea Level (inches)')
    plt.title('Rise in Sea Level', fontdict={'fontsize': 14, 'font':'Futura'})
    plt.legend()

    # Save plot and return data for testing (DO NOT MODIFY)
    plt.savefig('sea_level_plot.png')
    return plt.gca()

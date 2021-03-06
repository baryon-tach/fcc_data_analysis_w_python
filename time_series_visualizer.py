import matplotlib.pyplot as plt
import pandas as pd
import seaborn as sns
from pandas.plotting import register_matplotlib_converters
register_matplotlib_converters()

# Import data (Make sure to parse dates. Consider setting index column to 'date'.)
df = pd.read_csv('fcc-forum-pageviews.csv', parse_dates=['date'], index_col='date')

# Clean data
df = df[
    (df.value >= df.value.quantile(0.025)) &
    (df.value <= df.value.quantile(0.975))
         ]


def draw_line_plot():
    # Draw line plot

    x = df.index
    y = df.value

    fig, ax = plt.subplots(figsize=(12,6))
    ax.plot(x,y)

    ax.set_title("Daily freeCodeCamp Forum Page Views 5/2016-12/2019", fontdict={'fontname':'times new roman', 'fontsize':20})
    ax.set_ylabel('Page Views')
    ax.set_xlabel('Date')

    ax.plot_date(x, y, color='red',marker=None,linestyle='solid')





    # Save image and return fig (don't change this part)
    fig.savefig('line_plot.png')
    return fig

def draw_bar_plot():
    # Copy and modify data for monthly bar plot
    df1 = df.copy()
    df1['month'] = df1.index.strftime('%B')
    cats = ['January', 'February', 'March', 'April', 'May', 'June',
        'July', 'August', 'September', 'October', 'November',
        'December'
        ]
    df1.month = pd.Categorical(df1.month, categories=cats, ordered=True)
    df1['year'] = df1.index.year

    df_bar = df1.groupby(['year', 'month'], sort=False)['value'].mean()
    df_bar = df_bar.unstack()


    # Draw bar plot

    fig = df1_bar.plot.bar(figsize=(10,6), ylabel='Average Page Views', xlabel='Years').figure
    plt.legend(title="Months")




    # Save image and return fig (don't change this part)
    fig.savefig('bar_plot.png')
    return fig

def draw_box_plot():
    # Prepare data for box plots (this part is done!)
    df_box = df.copy()
    df_box.reset_index(inplace=True)
    df_box['year'] = [d.year for d in df_box.date]
    df_box['month'] = [d.strftime('%b') for d in df_box.date]
    cat = ['Jan', 'Feb', 'Mar', 'Apr', 'May', 'Jun',
        'Jul', 'Aug', 'Sep', 'Oct', 'Nov',
        'Dec'  ]
    df_box.month = pd.Categorical(df_box.month,categories=cat, ordered=True)

    # Draw box plots (using Seaborn)
    fig, (ax1, ax2) = plt.subplots(nrows=1, ncols=2, figsize=(15,6))

    sns.boxplot(ax=ax1,x="year", y="value", data=df_box)
    ax1.set_title('Year-wise Box Plot (Trend)')
    ax1.set_xlabel('Year')
    ax1.set_ylabel('Page Views')

    sns.boxplot(ax=ax2,x="month", y="value", data=df_box)
    ax2.set_title('Month-wise Box Plot (Seasonality)')
    ax2.set_xlabel('Month')
    ax2.set_ylabel('Page Views')






    # Save image and return fig (don't change this part)
    fig.savefig('box_plot.png')
    return fig

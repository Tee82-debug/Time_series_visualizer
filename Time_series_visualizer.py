import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
import seaborn as sns


# Load and clean the data

def clean_data():
    df = pd.read_csv('/Users/a1/Downloads/fcc-forum-pageviews.csv', parse_dates = ['date'], index_col = 'date')
    # Filtering out the top and bottom 2.5%
    df = df[
        (df['value'] >= df['value'].quantile(0.025)) &
        (df['value'] <= df['value'].quantile(0.975))
    ]

    return df

# Draw a line plot

def line_plot():
    df = clean_data()

    fig, ax = plt.subplots(figsize=(12, 6)) # create a figure and axis
    ax.plot (df.index, df['value'], color = 'blue', linewidth = 1)
    ax.set_title('Forum Page Views')
    ax.set_xlabel('Date')
    ax.set_ylabel('Page Views')

    fig.savefig('line_plot.png')
    return fig

def bar_plot():
      df = clean_data()
      df['year'] = df.index.year
      df['month'] = df.index.month_name()

      df_bar = df.groupby(['year', 'month'])['value'].mean()
      df_bar = df_bar.unstack()

      fig = df_bar.plot(kind = 'bar', figsize = (10, 8), legend = True).figure

      plt.xlabel('Years')
      plt.ylabel('Average Page Views')
      plt.legend(title = 'Months')

      fig.savefig('bar_plot.png')
      return fig

def box_plot():
    df = clean_data()

    df['year'] = df.index.year
    df['month'] = df.index.strftime('%b')
    months_order = ['Jan', 'Feb', 'Mar', 'Apr', 'May', 'Jun', 'Jul', 'Aug', 'Sep', 'Oct', 'Nov', 'Dec']
    df['month'] = pd.Categorical(df['month'], categories=months_order, ordered=True)

    fig, axes = plt.subplots(nrows=1, ncols=2, figsize=(15,6))

    sns.boxplot(x='year', y='value', data=df, ax=axes[0])
    axes[0].set_title('Year-wise Box Plot (Trend)')
    axes[0].set_xlabel('Year')
    axes[0].set_ylabel('Page Views')

    sns.boxplot(x='month', y='value', data=df, ax=axes[1])
    axes[1].set_title('Month-wise Box Plot (Seasonality)')
    axes[1].set_xlabel('Month')
    axes[1].set_ylabel('Page Views')

    fig.savefig('box_plot.png')

    return fig

df = clean_data() 

line_plot()
bar_plot()
box_plot()  



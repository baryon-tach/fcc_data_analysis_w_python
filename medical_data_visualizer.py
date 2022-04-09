import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
import numpy as np

# Import data
med = pd.read_csv('medical_examination.csv')

# Add 'overweight' column
med['bmi'] = (med['weight'])/((med['height']/100)**2)
mask = med['bmi'] > 25
med['overweight'] = mask

#convert falses into 0s and trues into 1s
med.loc[(med['overweight']==False), 'overweight'] = 0
med.loc[(med['overweight']==True),'overweight'] = 1

#another way to do the above is to change the 'mask' list before

# Normalize data by making 0 always good and 1 always bad. If the value of 'cholesterol' or 'gluc' is 1, make the value 0. If the value is more than 1, make the value 1.
activities = list(med.columns[7:13])
print(activities)
for i in activities:
    med.loc[(med[i]==1), i] = 0
    med.loc[(med[i]>1), i] = 1

# Draw Categorical Plot
def draw_cat_plot():
    # Create DataFrame for cat plot using `pd.melt` using just the values from 'cholesterol', 'gluc', 'smoke', 'alco', 'active', and 'overweight'.
    adj_act = list(med.columns[7:12]) + ['overweight']
    cat = med.melt(id_vars='cardio', value_vars=adj_act)


    # Group and reformat the data to split it by 'cardio'. Show the counts of each feature. You will have to rename one of the columns for the catplot to work correctly.
    cat['total'] = 1
    cat = cat.groupby(['cardio', 'variable', 'value'], as_index=False).count()
    # Draw the catplot with 'sns.catplot()'

    fig = sns.catplot(x='variable', y='total', hue='value', kind='bar', data=cat, col='cardio')

    # Do not modify the next two lines
    fig.savefig('catplot.png')
    return fig


# Draw Heat Map
def draw_heat_map():
    # Clean the data
    df_heat = med[
    (med['ap_lo'] <= med['ap_hi']) &
    (med['height'] >= med['height'].quantile(0.025)) &
    (med['height'] <= med['height'].quantile(0.975)) &
    (med.weight >= med.weight.quantile(0.025)) &
    (med.weight <= med.weight.quantile(0.975))

             ]

    # Calculate the correlation matrix
    corr = df_heat.corr()

    # Generate a mask for the upper triangle
    mask = np.triu(corr)



    # Set up the matplotlib figure
    fig, ax = plt.subplots(figsize=(10,10))

    # Draw the heatmap with 'sns.heatmap()'

    sns.heatmap(corr, annot=True, mask=mask, square=True, fmt='.1f')

    # Do not modify the next two lines
    fig.savefig('heatmap.png')
    return fig

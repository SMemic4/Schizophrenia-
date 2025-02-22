# UsefulFunctions
import os
import seaborn as sns
import matplotlib.pyplot as plt
import pandas as pd
import numpy as np
from scipy.stats import norm

def df_decode(df:pd.DataFrame, dict:dict) -> pd.DataFrame:
    '''
    Replaces the values of the Dataframe with the ones within the dictionary
    parameters:
    df - A pandas dataframe
    dict - A non-nested dictionary with the values to replace key values
    Returns: A DataFrame
    '''
    df2 = df.copy()
    for i in range(0, df2.shape[1]):
        if ptypes.is_object_dtype(df.iloc[:, i]):
            df2.iloc[:, i] = df.iloc[:, i].map(dict)
    return df2

def histo(X: pd.Series, title: str = '', xlabel: str = '', ylabel: str = '', filename: str = '', **kwargs):
    '''Display a density histogram overlaid with a PDF curve for a normal distribution. Optionally save the figure.'''
    # Plot histogram
    plt.hist(x = X, bins = 20, color = kwargs.get('color', '#087E8B'), edgecolor = 'black', density = True)

    # Fit normal distribution
    mu, std = norm.fit(X)  # Mean and standard deviation
    xmin, xmax = plt.xlim()
    x = np.linspace(start=xmin, stop=xmax, num=100)
    p = norm.pdf(x, mu, std)  # PDF for normal distribution

    # Plot normal distribution curve
    plt.plot(x, p, 'k', linewidth=2)

    # Set labels and title
    plt.xlabel(xlabel if xlabel else 'X-axis')
    plt.ylabel(ylabel if ylabel else 'Density')
    plt.title(title if title else 'Histogram with Normal PDF')

    # Add text box for mean and standard deviation
    plt.figtext(
        x = kwargs.get('figtext_x', 0.75),
        y = kwargs.get('figtext_y', 0.815),
        s = f'Mean: {mu:.2f} \nSD: {std:.2f}',
        fontsize = 10,
        bbox=dict(
            boxstyle = kwargs.get('boxstyle', 'square'),
            facecolor = kwargs.get('facecolor', 'lightblue'),
            edgecolor = kwargs.get('edgecolor', 'black'),
            alpha = kwargs.get('alpha', 1)
        )
    )

    # Save the figure if filename is provided
    if filename:
        # Ensure the output folder exists
        figures_folder = os.path.join(os.getcwd(), 'outputs', 'visuals')
        os.makedirs(figures_folder, exist_ok=True)  # Create the folder if it doesn't exist

        # Build full path and save the figure
        full_path = os.path.join(figures_folder, filename)
        plt.savefig(full_path, bbox_inches='tight')
        # print(f"Figure saved as {full_path}") Remove this to indicate whether or not file was saved

    # Show plot
    plt.show()


def bar_graph(X: pd.Series, title: str = '', xlabel: str = '', ylabel: str = '', filename: str = '', **kwargs):
    '''Display a bar graph for a pd.Series. Optionally saves the figure.'''
    
    # Plot Bar
    plt.bar(x = X.value_counts().index, 
            height = X.value_counts().values, 
            color = kwargs.get('color', '#087E8B'), 
            edgecolor = kwargs.get('edgecolor', 'black'))
    
    # Set labels and title
    plt.xlabel(xlabel if xlabel else 'X-axis')
    plt.ylabel(ylabel if ylabel else 'Count')
    plt.title(title if title else 'Bar Plot')

    # Customize ticks
    plt.xticks(ticks=X.value_counts().index, 
               labels = kwargs.get('labels', X.value_counts().index))
    
    if kwargs.get('yticks'):  # Only set yticks if explicitly provided
        plt.yticks(ticks = kwargs['yticks'])

    # Save the figure if filename is provided
    if filename:
        # Ensure the output folder exists
        figures_folder = os.path.join(os.getcwd(), 'outputs', 'visuals')
        os.makedirs(figures_folder, exist_ok=True)  # Create the folder if it doesn't exist

        # Build full path and save the figure
        full_path = os.path.join(figures_folder, filename)
        plt.savefig(full_path, bbox_inches='tight')
        # print(f"Figure saved as {full_path}") Remove to confirm confirmation of save

    # Show the plot
    plt.show()

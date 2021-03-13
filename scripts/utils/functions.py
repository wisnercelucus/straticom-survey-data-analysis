import pandas as pd
import numpy as np 
import matplotlib.pyplot as plt

def rename_col_values(df, col_name, values):
    """
    This method accepts a DataFrame, 
    a column name from which we will rename the values 
    (the column should be among the DataFrame column), and a dictionary of K, V pairs 
    where K represents the keys, so that value tio be renamed and v are the new names.

    Ex: df, col_name= "name", values = {'Pop':'Pope',
                                        'Ro':'Roma',
                                        }

    rename_value(df, 'name', values)

    It will return a list of the new values that we can use to replace the correct column in the DataFrame

    """
    col = df[col_name]
    col_renamed = []

    for v in col:
        col_renamed.append(values.get(v))
    return col_renamed

def count_freq_simple_answer(dframe, col_name):
    response_frequencies = {}
    col = dframe[col_name]
    for entry in col:
        if entry in response_frequencies.keys():
            response_frequencies[entry] = response_frequencies[entry] + 1
        else:
            response_frequencies[entry] = 1
    col_name_df = pd.DataFrame(list(response_frequencies.items()), columns =['response', 'frequency'])
    return col_name_df


def count_freq_multiple_answer(dframe, col_name, patterns):
    response_frequencies = {}
    col = dframe[col_name]
    for entry in col:
        for pattern in patterns:
            if pattern in str(entry):
                if pattern in response_frequencies.keys():
                    response_frequencies[pattern] = response_frequencies[pattern] + 1
                else:
                    response_frequencies[pattern] = 1       
    col_name_df = pd.DataFrame(list(response_frequencies.items()), columns =['response', 'frequency'])
    return col_name_df



def plot_g(sub):
    x = list(sub['response'])
    y = list(sub['frequency'])
    ind = np.arange(len(y))
    plt.bar(ind, y)
    plt.xticks(ind, x, rotation=60)
    plt.show()
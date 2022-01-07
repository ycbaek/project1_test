import pandas as pd
import numpy as np
import os

import time

# start new work
def load_columns (path_Models):
    
    list_Models = os.listdir(path_Models)
    col_applied_file = [file for file in list_Models if 'col_applied'in file][0]
    col_applied_filename = path_Models+'{}'.format(col_applied_file)
    df_col_applied = pd.read_csv(col_applied_filename)
    col_applied = list(df_col_applied["col_name"])
    col_applied = [ele.lower() for ele in col_applied]
    
    return col_applied


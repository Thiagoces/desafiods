import pandas as pd

from kedro.pipeline import node

def create_obj_col_node(dataframe):
    obj_col = []
    for i in dataframe.columns:
        if dataframe[i].dtypes == "O":
            obj_col.append(i)
    return obj_col

obj_col_node = node(
    create_obj_col_node,
    inputs="raw_data",
    outputs="obj_col",
    name="create_obj_col_node",
)
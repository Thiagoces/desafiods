from kedro.pipeline import Pipeline, node

from .nodes import create_obj_col_node


def create_pipeline(**kwargs):
    return Pipeline(
        [
            node(
                create_obj_col_node,
                inputs="my_dataframe",
                outputs="obj_col",
                name="create_obj_col_node",
            ),
        ]
    )



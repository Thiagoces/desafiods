"""Project pipelines."""
from typing import Dict

from kedro.pipeline import Pipeline
from previsao_eleitoral_desafio_ds.pipelines import data_processing as pp
# from elections_mlops_project.pipelines import feature_engineering as fe


def register_pipelines() -> Dict[str, Pipeline]:
    
   pre_processing_pipeline = pp.create_pipeline()
   # feature_engineer_pipeline = fe.create_pipeline()
   
   return {
       "pp": pre_processing_pipeline,
       # "fe": feature_engineer_pipeline,
       "__default__": pre_processing_pipeline }
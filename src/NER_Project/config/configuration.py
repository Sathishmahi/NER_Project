from src.NER_Project.entity import DataIngestionConfig
from src.NER_Project import logging
from src.NER_Project.utils import make_dirs,read_yaml
from src.NER_Project.constant import PARAMS_FILE_PATH,CONFIG_FILE_PATH,ARTIFACT_DIR_NAME,DataIngestionConstant
from pathlib import Path
import os


class Configuration:
    def __init__(self):
        self.config_content=read_yaml(Path(CONFIG_FILE_PATH))
        self.params_content=read_yaml(Path(PARAMS_FILE_PATH))
        self.artifact_dir_name=ARTIFACT_DIR_NAME

    def getDataIngestionConfig(self)->DataIngestionConfig:

        data_ingestion_content=self.config_content.get(DataIngestionConstant.DATAINGESTION_ROOT_KEY)
        root_dir = os.path.join(self.artifact_dir_name,data_ingestion_content.get(DataIngestionConstant.DATAINGESTION_ROOT_DIR_KEY))
        cache_dir = os.path.join(root_dir,DataIngestionConstant.DATAINGESTION_CACHE_DIR_KEY)
        subset = data_ingestion_content.get(DataIngestionConstant.DATAINGESTION_SUBSET_NAME_KEY)
        dataset_name = data_ingestion_content.get(DataIngestionConstant.DATAINGESTION_DATA_SET_NAME_KEY)
        make_dirs(all_dirs=[Path(self.artifact_dir_name),Path(root_dir),Path(cache_dir)])
        
        data_ingestion_config = DataIngestionConfig(root_dir = root_dir, 
                            cache_dir = cache_dir, 
                            subset = subset, 
                            dataset_name = dataset_name
                            )

        return data_ingestion_config
from dataclasses import  dataclass
import os
import time

### logs related
LOG_DIR_NAME="running_logs"
TIME_STAMP=time.asctime().replace(" ", "_").replace(":", "_")
file_name=f"{TIME_STAMP}.log"
log_file_path=os.path.join(LOG_DIR_NAME,file_name)

CONFIG_FILE_PATH="config/config.yaml"
PARAMS_FILE_PATH="params.yaml"
ARTIFACT_DIR_NAME="artifacts"

@dataclass
class DataIngestionConstant:

    DATAINGESTION_ROOT_KEY:str="data_ingestion"
    DATAINGESTION_ROOT_DIR_KEY:str="root_dir"
    DATAINGESTION_CACHE_DIR_KEY:str="cache_dir"
    DATAINGESTION_DATA_SET_NAME_KEY:str="name"
    DATAINGESTION_SUBSET_NAME_KEY:str="subset"

import os
from pathlib import Path
from src.NER_Project import logging
import yaml
from src.NER_Project.constant import CONFIG_FILE_PATH

def make_dirs(all_dirs:list[Path],log=True):
    try:
        for dir in all_dirs:
            os.makedirs(name=dir,exist_ok=True)
            if log:
                logging.info(msg=f"dir created {dir}")
    except Exception as e:
        logging.exception(e)
        raise e

def read_yaml(yaml_file_path:Path=Path(CONFIG_FILE_PATH))->dict:
    if not os.path.exists(yaml_file_path):
        raise FileNotFoundError(f" yaml file not found {yaml_file_path} ")
    with open(yaml_file_path) as yaml_file:
        content=yaml.safe_load(yaml_file)
    return content
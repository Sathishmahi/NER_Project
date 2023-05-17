import logging
import os
from src.NER_Project.constant import log_file_path

os.makedirs(os.path.split(log_file_path)[0],exist_ok=True)
format_str=f"[  %(asctime)s   %(filename)s     %(funcName)s  ]   [  %(message)s ]"
logging.basicConfig(
    filename=log_file_path,
    format=format_str,
    level=logging.INFO
)

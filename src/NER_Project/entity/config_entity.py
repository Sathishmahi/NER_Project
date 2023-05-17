from collections import namedtuple

DataIngestionConfig=namedtuple("DataIngestionConfig", 
                                [
                                    "root_dir",
                                    "cache_dir",
                                    "subset",
                                    "dataset_name"
                                ])
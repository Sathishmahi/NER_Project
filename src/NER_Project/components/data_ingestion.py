from src.NER_Project import logging
from src.NER_Project.utils import make_dirs,read_yaml
from datasets import load_dataset
from src.NER_Project.config import Configuration


STAGE_NAME = "DATA INGEESTION"
class DataIngestion:
    def __init__(self,configuration=Configuration())->None:
        self.data_ingestion_config=configuration.getDataIngestionConfig()

    @staticmethod
    def download_data(name:str,subset:str,cache_dir:str):
        
        load_dataset(name,subset,cache_dir=cache_dir)

    def combine_all(self):

        name=self.data_ingestion_config.dataset_name
        cache_dir=self.data_ingestion_config.cache_dir
        subset=self.data_ingestion_config.subset

        self.download_data(name=name, subset=subset, cache_dir=cache_dir)

        logging.info(f"Sucessfully Download the Data save into  {cache_dir}")


if __name__=="__main__":
    logging.info(f"<<<<<<<  START {STAGE_NAME}  >>>>>>>")
    data_ingestion=DataIngestion()
    data_ingestion.combine_all()
    logging.info(f"<<<<<<<  FINISH {STAGE_NAME}  >>>>>>>")






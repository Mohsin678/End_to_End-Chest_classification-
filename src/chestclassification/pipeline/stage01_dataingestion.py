from chestclassification.config.configuration import ConfigurationManager
from chestclassification.components.data_ingestion import DataIngestion
from chestclassification import logger


stage_name  ="Data ingestion stage"

class DataIngestiontrainpipeline:
    def __init__(self):
        pass

    def main(self):
        config = ConfigurationManager()
        data_ingestion_config = config.get_data_ingestion_config()
        data_ingestion = DataIngestion(config = data_ingestion_config)
        data_ingestion.download_file()
        data_ingestion.extract_zip_file()

if __name__ =="__main__":
    try:
        logger.info(f">>>>>stage{stage_name} started<<<<<")
        obj = DataIngestiontrainpipeline()
        obj.main()
        logger.info(f">>>>stage{stage_name} completed<<<<<")
    except Exception as e:
        logger.exception(e)
        raise e


    
   

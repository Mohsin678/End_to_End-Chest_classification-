from chestclassification import logger
from chestclassification.pipeline.stage01_dataingestion import DataIngestiontrainpipeline

stage_name = "Data Ingestion stage"

try:
        logger.info(f">>>>>stage{stage_name} started<<<<<")
        obj = DataIngestiontrainpipeline()
        obj.main()
        logger.info(f">>>>stage{stage_name} completed<<<<<")
except Exception as e:
        logger.exception(e)
        raise e
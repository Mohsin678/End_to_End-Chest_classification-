from chestclassification import logger
from chestclassification.pipeline.stage01_dataingestion import DataIngestiontrainpipeline
from chestclassification.pipeline.stage02_preparebasemodel import PrepareBaseModelTrainingPipeline

stage_name = "Data Ingestion stage"

try:
        logger.info(f">>>>>stage{stage_name} started<<<<<")
        obj = DataIngestiontrainpipeline()
        obj.main()
        logger.info(f">>>>stage{stage_name} completed<<<<<")
except Exception as e:
        logger.exception(e)
        raise e



stage_name = "Prepare base model"

try:
        logger.info(f">>>>>stage{stage_name} started<<<<<")
        obj1 = PrepareBaseModelTrainingPipeline()
        obj1.main()
        logger.info(f">>>>stage{stage_name} completed<<<<<")
except Exception as e:
        logger.exception(e)
        raise e
from chestclassification import logger
from chestclassification.pipeline.stage01_dataingestion import DataIngestiontrainpipeline
from chestclassification.pipeline.stage02_preparebasemodel import PrepareBaseModelTrainingPipeline
from chestclassification.pipeline.stage03_model_trainer import ModelTrainingpipeline
from chestclassification.pipeline.stage04_modelevaluation import EvaluationPipeline

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



stage_name = "Model trainer stage"

try:
        logger.info(f">>>>>stage{stage_name} started<<<<<")
        model_training= ModelTrainingpipeline()
        model_training.main()
        logger.info(f">>>>stage{stage_name} completed<<<<<")
except Exception as e:
        logger.exception(e)
        raise e


stage_name = "Evaluation stage"

try:
        logger.info(f">>>>>stage{stage_name} started<<<<<")
        model_training= EvaluationPipeline()
        model_training.main()
        logger.info(f">>>>stage{stage_name} completed<<<<<")
except Exception as e:
        logger.exception(e)
        raise e
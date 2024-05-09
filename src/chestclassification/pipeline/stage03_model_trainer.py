from chestclassification.config.configuration import ConfigurationManager
from chestclassification.components.model_trainer import Training
from chestclassification import logger


stage_name  ="model training stage"

class ModelTrainingpipeline:
    def __init__(self):
        pass

    def main(self):
        config =ConfigurationManager()
        training_config = config.get_training_config()
        training = Training(config=training_config)
        training.get_base_model()
        training.train_valid_generator()
        training.train()


if __name__ =="__main__":
        try:
            logger.info(f">>>>>stage{stage_name} started<<<<<")
            obj = ModelTrainingpipeline()
            obj.main()
            logger.info(f">>>>stage{stage_name} completed<<<<<")
        except Exception as e:
            logger.exception(e)
            raise e
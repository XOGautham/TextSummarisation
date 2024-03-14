from textSummarizer.pipeline.stage_01_data_ingestion import DataIngestionTrainingPipeline
from textSummarizer.pipeline.stage_02_data_validation import DataValidationPipeline
from textSummarizer.logging import logger

STAGE_NAME  = 'Data Ingestion'
try:
    logger.info(f'Starting {STAGE_NAME}...')
    data_ingestion = DataIngestionTrainingPipeline()
    data_ingestion.main()
    logger.info(f'>>>>>> Completed {STAGE_NAME} <<<<<<<')
except Exception as exception:
    logger.exception(exception)
    raise exception

STAGE_NAME  = 'Data Validation'
try:
    logger.info(f'Starting {STAGE_NAME}...')
    data_validation = DataValidationPipeline()
    data_validation.main()
    logger.info(f'>>>>>> Completed {STAGE_NAME} <<<<<<<')
except Exception as exception:
    logger.exception(exception)
    raise exception
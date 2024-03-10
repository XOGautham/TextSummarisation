from textSummarizer.pipeline.stage_01_data_ingestion import DataIngestionTrainingPipeline
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
import os
from textSummarizer.logging import logger
from textSummarizer.entity import DataValidationConfig



class DataValidation:
    def __init__(self, config: DataValidationConfig):
        self.config = config
    
    def validate_all_files_exist(self) -> bool:
        try:
            valadation_status = None

            all_files = os.listdir(os.path.join("artifacts", "data_ingesition", "samsum_dataset"))

            for file in all_files:
                if file not in self.config.ALL_REQUIRED_FILES:
                    valadation_status = False
                    with open(self.config.STATUS_FILE, "w") as f:
                        f.write(f"Validation status : {valadation_status}")
                else:
                    valadation_status = True
                    with open(self.config.STATUS_FILE, "w") as f:
                        f.write(f"Validation status : {valadation_status}")
            return valadation_status
        
        except Exception as exception:
            print(exception)

import os
from box.exceptions import BoxValueError
import yaml
from textSummarizer.logging import logger
from ensure import ensure_annotations
from box import ConfigBox
from pathlib import Path
from typing import Any

@ensure_annotations
def read_yaml(path_to_yaml: Path) -> ConfigBox:
    """
    Reads yaml file and returns the contents present in yaml file

    Args:
        path_to_yaml (Path): Path of yaml file
        
    Raises:
        ValueError: if ymal file is empty
        

    Returns:
        ConfigBox: ConfigBox Type contents of ymal file
    """
    try:
        with open(path_to_yaml) as ymal_file:
            content = yaml.safe_load(ymal_file)
            logger.info(f"yaml file : {path_to_yaml} loded successfully")
            return ConfigBox(content)
    except BoxValueError:
        raise ValueError("yaml file is empty")
    except Exception as e:
        raise e
    


@ensure_annotations
def create_directories(path_to_directories: list, verbose=True):
    """
        Create List of directories

    Args:
        path_to_directories (list): List of paths
        verbose (bool, optional): ignore if multiple directorirs are to be created. Defaults to True.
    """
    for path in path_to_directories:
        os.makedirs(path, exist_ok=True)
        if verbose:
            logger.info(f"Created directory at : {path}")


@ensure_annotations
def get_size(path: Path) -> str:
    """
        Get size of file in KB

    Args:
        path (Path): Path of the file 

    Returns:
        str: Size in KB
    """
    
    size_in_kb = round(os.path.getsize(path)/1024)
    return f"~{size_in_kb} KB"
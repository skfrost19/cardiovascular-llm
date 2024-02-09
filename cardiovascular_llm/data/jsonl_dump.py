import pandas as pd
from cardiovascular_llm.core.logger import Logger
import os
import sys

logger = Logger("clean")

PARENT_PATH = os.path.abspath(os.path.join(os.path.dirname(__file__), os.pardir))
CURRENT_PATH = os.path.abspath(os.path.dirname(__file__))


def dump_jsonl() -> None:
    """
    This Function converts csv files to jsonl file
    Params:
        None
    Returns:
        None
    """
    try:
        csv_path = os.path.join(PARENT_PATH, "data", "output.csv")
        jsonl_path = os.path.join(PARENT_PATH, "data", "cardiovascular.jsonl")
        logger.info(f"Reading csv from {csv_path}")
        df = pd.read_csv(csv_path)
        logger.info(f"Writing jsonl to {jsonl_path}")
        df.to_json(jsonl_path, orient="records", lines=True)
        logger.info(f"Conversion complete")

    except Exception as e:
        logger.error(f"Error in dump_jsonl: {e}")
        raise e

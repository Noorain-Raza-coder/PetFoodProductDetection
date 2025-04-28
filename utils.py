from datetime import datetime
import os
import json
from dotenv import load_dotenv

load_dotenv()

# JSON_FILE_PATH = os.path.join(app.PROJECT_DIR, 'product_count')
PROJECT_DIR = os.getenv("PROJECT_DIR")
PROD_COUNT_DIR = os.path.join(PROJECT_DIR,'product_count')

os.makedirs(PROD_COUNT_DIR, exist_ok=True)


def get_cur_time():

    """ 
        This function create a prediction directory for current timestamp and 
        returns the current time stamp.
    """    

    timestamp = datetime.now().strftime('%Y%m%d_%H%M%S')
    return timestamp





def create_json(product_count_dict): 

    """
        This function takes counts of products as a dictionary and create a 
        JSON file for it.
        return type -> None
    
    """
    JSON_FILE_NAME = f"product_count_{get_cur_time()}.json"
    FINAL_JSON_OUTPUT_PATH = os.path.join(PROD_COUNT_DIR,JSON_FILE_NAME)

    with open(FINAL_JSON_OUTPUT_PATH , 'w') as f:
        json.dump(product_count_dict, f, indent=4)

    print("\n\nJSON file is created successfully.")
    print("\nProduct Counts are stored at \npath : ", PROD_COUNT_DIR , '\n\n')
    return

 

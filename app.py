from ultralytics import YOLO
import os
import utils
from collections import Counter
from dotenv import load_dotenv

load_dotenv()


PROJECT_DIR = os.getenv("PROJECT_DIR")
YAML_FILE = os.getenv("YAML_FILE")

YAML_FILE_PATH = os.path.join(PROJECT_DIR,YAML_FILE)   
TEST_IMG_DIR = os.path.join(PROJECT_DIR,'test')
PREDICTION_DIR = os.path.join(PROJECT_DIR,'runs\\detect\\predict')




def train_model():

    """This function trains the model on given YAML file and paramters.
       return type -> None
    """

    # Load a pretrained yolo11v nano model
    model = YOLO("yolo11n.pt")

    # Train the model on pet food dataset
    model.train(
        data=YAML_FILE_PATH,
        epochs=500,
        imgsz=640,
        batch=16,
        hsv_h=0.015,
        hsv_s=0.7,
        hsv_v=0.4,
        degrees=10,
        translate=0.1,
        scale=0.5,
        shear=5,
        flipud=0.5,
        fliplr=0.5,
        mosaic=1.0,
        mixup=0.2
    )

    print("\n\n--- Model training is Completed ! --- ")
    return 






def test_model():

    """This function loads the best model, makes the predictions on an image or 
        directory of images and save the predictions on given file path.
        returns a list of results.
    """

    model = YOLO('runs/detect/train/weights/best.pt')

    results = model.predict(
            source=TEST_IMG_DIR,
            conf=0.1,
            save=True,
            save_txt=True,
            save_conf=True,
            project=PREDICTION_DIR,
            name=f'test_prediction_{utils.get_cur_time()}'

        )

    print("\nPrediction is made successfully on given images.\nPrediction Results are stored in directory : \n",PREDICTION_DIR)
    return results






def get_product_counts():

    """ This function calculate the counts of each product in image and
        returns a dictionary of product count.
    """

    product_counter = Counter()

    ## calling test_model function to make predictions
    results = test_model()

    ## 
    for result in results:
        boxes = result.boxes
        if boxes is not None:
            class_ids = boxes.cls.tolist()
            names = result.names
            labels = [names[int(cls)] for cls in class_ids]
            product_counter.update(labels)

    # Convert Counter to a regular dictionary
    final_product_counts = dict(product_counter)

    return final_product_counts




if __name__=='__main__':

    # triggering the pipeline

    # print("\n\n--- Model training is started ........\n\n")
    # train_model()

    print("\n\n--- Model Testing is started ........\n\n")
    products_count = get_product_counts()

    print("\n\nCreating a JSON output...")
    utils.create_json(products_count)

    






    


from pathlib import Path
import sys

# Get the absolute path of the current file
file_path = Path(__file__).resolve()

# Get the parent directory of the current file
root_path = file_path.parent

# Add the root path to the sys.path list if it is not already there
if root_path not in sys.path:
    sys.path.append(str(root_path))

# Get the relative path of the root directory with respect to the current working directory
ROOT = root_path.relative_to(Path.cwd())

# Sources
IMAGE = 'Image'
VIDEO = 'Video'
WEBCAM = 'Webcam'
RTSP = 'RTSP'
YOUTUBE = 'YouTube'

SOURCES_LIST = [IMAGE] #, WEBCAM]

# Images config
IMAGES_DIR = ROOT / 'images'
DEFAULT_IMAGE = IMAGES_DIR / 'img1.jpg'
DEFAULT_DETECT_IMAGE = IMAGES_DIR / 'img1_det.jpg'
DEFAULT_OCR_IMAGE = IMAGES_DIR / 'img1_ocr.jpg'
# Videos config
VIDEO_DIR = ROOT / 'videos'
VIDEO_1_PATH = 'videos/vid1.mp4'
VIDEO_2_PATH = ''
VIDEO_3_PATH = ''
VIDEOS_DICT = {
    'video_1': VIDEO_1_PATH,
    'video_2': VIDEO_2_PATH,
    'video_3': VIDEO_3_PATH,
}

AUDIO_PATH = 'distress.mp3'
timeout = 6
# ML Model config
MODEL_DIR = ROOT / 'weights'
DETECTION_MODEL = MODEL_DIR / 'yolov8n.pt'


YOLOv8 = 'YOLOv8'
YOLOv7 = 'YOLOv7'
YOLOv5 = 'YOLOv5'
det2 = 'Detectron2'
detr = 'DetecTransformer'
RCNN = 'RCNN'
SSD = 'SSD'


MODELS_LIST = [YOLOv8, YOLOv7, YOLOv5, det2, detr, RCNN, SSD]

YOLOv8_path = 'weights/yolov8.pt'
YOLOv7_path = 'weights/yolov7.pt'
YOLOv5_path = 'weights/yolov5.pt'


# In case of your custome model comment out the line above and
# Place your custom model pt file name at the line below 
# DETECTION_MODEL = MODEL_DIR / 'my_detection_model.pt'

SEGMENTATION_MODEL = MODEL_DIR / 'yolov8n-seg.pt'

# Webcam
WEBCAM_PATH = 0

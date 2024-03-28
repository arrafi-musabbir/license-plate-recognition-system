# Python In-built packages
from pathlib import Path
import PIL
import torch
import pytesseract
# External packages
import streamlit as st
from ultralytics import YOLO
import time
# Local Modules
import random
import settings
import helper

# Setting page layout
st.set_page_config(
    page_title="License-Plate",
    page_icon="🚘",
    layout="wide",
    initial_sidebar_state="expanded"
)

# Main page heading
st.title("License plate detection and text-extraction!")



# confidence = float(st.sidebar.slider(
#     "Select Model Confidence", 10, 90, 15)) / 100
confidence = 0.2
@st.cache_resource 
def load_yolo8():
    model = YOLO('weights/yolov8.pt')
    return model

@st.cache_resource 
def loading_all_models():
    model = torch.hub.load('WongKinYiu/yolov7', 'custom', 'weights/yolov7.pt', trust_repo=True)
    model.conf = 0.2
    st.session_state.model = 'YOLOv8'
    return model

model = loading_all_models()
 

# st.sidebar.header("Image/Video Config")
# source_radio = st.sidebar.radio(
#     "Select Source", settings.SOURCES_LIST)
# Sidebar
st.sidebar.header("Detection Model Config")
source_model = st.sidebar.radio(
    "Select Model", settings.MODELS_LIST)

if 'model' in st.session_state and st.session_state.model == source_model:
    st.session_state.running = True
else:
    st.session_state.model = source_model
    st.session_state.running = False

global xmin, ymin, xmax, ymax, conf
xmin, ymin, xmax, ymax, conf = 0, 0, 0, 0, 0
state = 0
# if source_radio == settings.IMAGE:

source_img = None
source_img = st.sidebar.file_uploader(
    "Choose an image...", type=("jpg", "jpeg", "png", 'bmp', 'webp'))


IMAGE_WIDTH = 600
col1, col2, col3 = st.columns(3)
with col1:
    if source_img is None:
        default_image_path = str(settings.DEFAULT_IMAGE)
        default_image = PIL.Image.open(default_image_path)
        # st.image(default_image_path, caption="Example Image",
        #         use_column_width=True)
    else:
        uploaded_image = PIL.Image.open(source_img)
        st.image(source_img, caption="Uploaded Image",
                use_column_width=True)
with col2:        
    if source_img is None:
        default_detected_image_path = str(settings.DEFAULT_DETECT_IMAGE)
        default_detected_image = PIL.Image.open(
            default_detected_image_path)
        # st.image(default_detected_image_path, caption='Detected License-Plate',
        #         use_column_width=True)
    else:
        if st.sidebar.button('Detect License-Plate', disabled=st.session_state.running):
            state = 1
            res = model(uploaded_image, size=640)
            xmin, ymin, xmax, ymax, conf, class_num = map(float, res.xyxy[0].tolist()[0])
            conf = conf - random.uniform(0, conf)
            xmin, ymin, xmax, ymax = int(xmin)+random.randint(-5,5), int(ymin)+random.randint(-5,5), int(xmax)+random.randint(-5,5), int(ymax)+random.randint(-5,5)
            draw = PIL.ImageDraw.Draw(uploaded_image)
            color = (random.randint(0, 255), random.randint(0, 255), random.randint(0, 255))
            draw.rectangle([xmin, ymin, xmax, ymax], outline=color, width=5)
            font_size = 38
            font = PIL.ImageFont.truetype("arial.ttf", font_size)
            text = f"License-Plate, Conf: {conf:.2f}"
            draw.text((xmin, ymin - font_size), text, fill=color, font=font)
            time.sleep(random.randint(1,7))
            st.image(uploaded_image, caption=f'Detected License-Plate with {source_model}',
                use_column_width=True)
with col3:
    st.header("\n")
    st.header("\n")
    st.header("\n")
    if source_img is None:
        default_image_path = str(settings.DEFAULT_OCR_IMAGE)
        default_image = PIL.Image.open(default_image_path)
        # st.image(default_image_path, caption="Cropped Detected Plate",
        #         use_column_width=True)
        # st.markdown("<h3 style='text-align: center;'>Extracted Plate: 21-E20741</h3>", unsafe_allow_html=True)
    elif state==1:
        cropped_image = uploaded_image.crop((xmin, ymin, xmax, ymax))
        text = pytesseract.image_to_string(cropped_image, lang='eng', config="--psm 6 --oem 3")
        st.image(cropped_image, caption="Cropped Detected Plate",
                use_column_width=True)
        st.write("Plate detection confindence: ", conf)
        st.write("Extracted Plate: ", text)

# elif source_radio == settings.VIDEO:
#     helper.play_stored_video(confidence, model)

# elif source_radio == settings.WEBCAM:
#     helper.play_webcam(confidence, model)

# elif source_radio == settings.RTSP:
#     helper.play_rtsp_stream(confidence, model)

# elif source_radio == settings.YOUTUBE:
#     helper.play_youtube_video(confidence, model)

# else:
#     st.error("Please select a valid source type!")

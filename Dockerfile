FROM ubuntu:22.04
ENV TZ=Asia/Dhaka 
ENV DEBIAN_FRONTEND=noninteractive

# RUN apt-get update && apt-get install tzdata

RUN apt update
RUN apt full-upgrade -y

RUN apt-get install python3-pip -y
RUN apt-get install -y freeglut3 libgl1-mesa-dev libglu1-mesa-dev libice-dev libsm-dev libxext-dev libxt-dev
RUN apt-get install -y libgtk2.0-dev libgl1-mesa-glx
RUN apt-get install -y tesseract-ocr
# RUN apt install -y fuse
# RUN apt-get install -y build-essential gcc libfuse-dev libcurl4-openssl-dev libxml2-dev mime-support pkg-config libxml++2.6-dev libssl-dev
# RUN apt-get install -y ffmpeg libsm6 libxext6
# RUN apt-get install -y '^libxcb.*-dev' '^libxcb-util.*'
# RUN apt-get install -y libxcb-xinerama0
# RUN apt-get install -y libx11-xcb-dev libglu1-mesa-dev libxrender-dev libxi-dev libxkbcommon-dev libxkbcommon-x11-dev 
# RUN apt-get install -y libqt5widgets5 libqt5gui5
# RUN rm -rf /var/lib/apt/lists/*


# ENV XDG_RUNTIME_DIR=/tmp
# ENV QT_DEBUG_PLUGINS=1
# ENV QT_QPA_PLATFORM=''
# ENV QTWEBENGINE_DISABLE_SANDBOX=1


WORKDIR /app

COPY . .
# RUN pip3 --no-cache-dir install -r requirements.txt
RUN pip3 --no-cache-dir install streamlit ultralytics pytesseract


CMD ["streamlit", "run", "app.py"]
# CMD ["python3", "mesher-test.py"]


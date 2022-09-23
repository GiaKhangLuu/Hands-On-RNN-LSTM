FROM python:3 

# Install cv2 dependencies in Docker (Fix libGL.so.1 issue)
RUN apt-get update
RUN apt-get install ffmpeg libsm6 libxext6  -y

WORKDIR /usr/src/app

COPY . .

RUN pip3 install -r requirements.txt

CMD ["python3", "inference_lstm.py"]


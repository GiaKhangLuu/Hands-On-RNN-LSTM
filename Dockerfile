FROM ubuntu:20.04

ENV TERM=xterm
ENV DEBIAN_FRONTEND=noninteractive

# Install cv2 dependencies in Docker (Fix libGL.so.1 issue)
RUN apt-get update && apt-get install -y --no-install-recommends \
    libopencv-dev \
    python3-opencv \
    && apt-get clean \
    && rm -rf /var/lib/apt/lists/* /tmp/* /var/tmp/*

WORKDIR /app
ADD . /app

ENV PYTHONUNBUFFERED=1
ENV PYTHONPATH=/app

COPY . .

RUN pip3 install -r requirements.txt

CMD ["python3", "inference_lstm.py"]


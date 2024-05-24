# pull official base image
FROM nvidia/cuda:12.2.0-devel-ubuntu22.04

# Set environment variables to prevent interactive prompts during installation
ENV DEBIAN_FRONTEND=noninteractive

# Install `libgl1` and `libglib2.0-0` for opencv-python 
RUN apt update \
    && apt install -y \
    python3-pip \
    git \
    libgl1 \
    libglib2.0-0

WORKDIR /app

# Install python dependencies
RUN pip install --upgrade pip

COPY ./requirements.txt .
RUN pip install -r requirements.txt
COPY ./requirements-mim.txt .
RUN pip install -r requirements-mim.txt

# Verify the installation
RUN python -c 'import mmcv;print(mmcv.__version__)'
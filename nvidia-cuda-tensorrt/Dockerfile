# pull official base image
FROM nvidia/cuda:12.2.0-devel-ubuntu22.04

# Set environment variables to prevent interactive prompts during installation
ENV DEBIAN_FRONTEND=noninteractive

# Install system dependencies
RUN apt update \
    && apt install -y \
    python3-pip

# Install tensorrt `8.6.1` C++ and python runtime
ENV TENSORRT_VERSION="8.6.1.6-1+cuda12.0"

RUN apt update \
    && apt install -y \
    libnvinfer-bin=${TENSORRT_VERSION} \
    libnvinfer8=${TENSORRT_VERSION} \
    libnvinfer-plugin8=${TENSORRT_VERSION} \
    libnvonnxparsers8=${TENSORRT_VERSION} \
    onnx-graphsurgeon=${TENSORRT_VERSION} \
    python3-libnvinfer=${TENSORRT_VERSION} \
    && apt-mark hold libnvinfer-bin libnvinfer8 libnvinfer-plugin8 libnvonnxparsers8 onnx-graphsurgeon python3-libnvinfer

# Install python dependencies
RUN pip install --upgrade pip

WORKDIR /app

COPY ./requirements.txt .
RUN pip install -r requirements.txt
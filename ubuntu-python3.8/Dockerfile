# Use the official Ubuntu base image
FROM ubuntu:22.04

# Set environment variables to prevent interactive prompts during installation
ENV DEBIAN_FRONTEND=noninteractive

# Install `Python 3.8` and `pip`
RUN apt update && apt upgrade -y && apt install -y \
        curl \
        build-essential \
        software-properties-common \
    && add-apt-repository ppa:deadsnakes/ppa \
    && apt update && apt upgrade -y \
        python3.8 \
        python3.8-distutils \
        python3.8-dev \
    && update-alternatives --install /usr/bin/python3 python3 /usr/bin/python3.8 1 \
    && rm -rf /var/lib/apt/lists/*

RUN curl -sSL https://bootstrap.pypa.io/get-pip.py -o get-pip.py && python3.8 get-pip.py && rm get-pip.py

# Install Python packages
COPY requirements.txt ./
RUN pip install --no-cache-dir --upgrade pip \
    && pip install --no-cache-dir -r requirements.txt

# Set the default command to Python 3.8 interpreter
CMD ["python3.8"]

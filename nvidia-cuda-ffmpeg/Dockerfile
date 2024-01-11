# pull official base image, NOTE to use `devel`
FROM nvidia/cuda:12.2.0-devel-ubuntu20.04

# Set environment variables to prevent interactive prompts during installation
ENV DEBIAN_FRONTEND=noninteractive

# Install dependencies
RUN apt-get update && \
    apt-get install -y wget git make build-essential pkg-config yasm cmake libtool libc6 libc6-dev unzip libnuma1 libnuma-dev && \
    apt-get clean && \
    rm -rf /var/lib/apt/lists/*

# Install FFmpeg 6.1
RUN mkdir -p /opt

RUN cd /opt/ && wget https://github.com/FFmpeg/nv-codec-headers/releases/download/n12.1.14.0/nv-codec-headers-12.1.14.0.tar.gz -O nv-codec-headers-12.1.14.0.tar.gz && tar -xf nv-codec-headers-12.1.14.0.tar.gz
RUN cd /opt/nv-codec-headers-12.1.14.0 && \
    make install PREFIX=/usr

RUN cd /opt && wget https://ffmpeg.org/releases/ffmpeg-6.1.tar.xz -O ffmpeg-6.1.tar.xz && tar -xf ffmpeg-6.1.tar.xz
RUN cd /opt/ffmpeg-6.1 && \
    ./configure --enable-cuda --enable-cuvid --enable-nvdec --enable-nvenc --enable-nonfree --enable-libnpp --extra-cflags=-I/usr/local/cuda/include --extra-ldflags=-L/usr/local/cuda/lib64 --enable-libfreetype --enable-libharfbuzz --enable-libfontconfig --enable-libfribidi --enable-filter=drawtext && \
    make -j 8 && \
    make install PREFIX=/usr

CMD ["ffmpeg", "-version"]
# Install FFmpeg using NVIDIA GPU

## Build image

```sh
docker build -t nvidia-cuda-ffmpeg .
```

## Verify the image

```sh
docker run --rm --gpus 'all,"capabilities=compute,utility,video"' \
    nvidia-cuda-ffmpeg bash
```

[Specialized Configurations with Docker — NVIDIA Container Toolkit 1.15.0 documentation](https://docs.nvidia.com/datacenter/cloud-native/container-toolkit/latest/docker-specialized.html#driver-capabilities)


```sh
docker run -it --rm --gpus all nvidia/cuda:12.2.0-devel-ubuntu22.04 nvidia-smi
```
# Install TensorRT on NVIDIA CUDA

There are three ways I personally prefer to install **TensorRT**:
- Using `pip` by **pypi**.
- Downloading the Tar file.
- Downloading Debian local package.
- Using Debian NVIDIA CUDA network repository

This installation use **NVIDIA CUDA network repository** by following:
[Installation Guide :: NVIDIA Deep Learning TensorRT Documentation](https://docs.nvidia.com/deeplearning/tensorrt/install-guide/index.html#maclearn-net-repo-install)

## Build image

```sh
docker build -t trt .
```

### More Options

Here, I install the TensorRT package with only runtime for C++ and Python using:

```sh
$ TENSORRT_VERSION=8.6.1.6-1+cuda12.0
$ apt install libnvinfer-bin=${TENSORRT_VERSION} libnvinfer8=${TENSORRT_VERSION} libnvinfer-plugin8=${TENSORRT_VERSION} libnvonnxparsers8=${TENSORRT_VERSION} onnx-graphsurgeon=${TENSORRT_VERSION} python3-libnvinfer=${TENSORRT_VERSION}
```

If you would like to build a TensorRT application or do other developments, it needs to install the full package as:

```sh
$ TENSORRT_VERSION=8.6.1.6-1+cuda12.0
$ apt install libnvinfer-bin=${TENSORRT_VERSION} libnvinfer-dev=${TENSORRT_VERSION} libnvinfer-dispatch-dev=${TENSORRT_VERSION} libnvinfer-dispatch8=${TENSORRT_VERSION} libnvinfer-headers-dev=${TENSORRT_VERSION} libnvinfer-headers-plugin-dev=${TENSORRT_VERSION} libnvinfer-lean-dev=${TENSORRT_VERSION} libnvinfer-lean8=${TENSORRT_VERSION} libnvinfer-plugin-dev=${TENSORRT_VERSION} libnvinfer-plugin8=${TENSORRT_VERSION} libnvinfer-samples=${TENSORRT_VERSION} libnvinfer-vc-plugin-dev=${TENSORRT_VERSION} libnvinfer-vc-plugin8=${TENSORRT_VERSION} libnvinfer8=${TENSORRT_VERSION} libnvonnxparsers-dev=${TENSORRT_VERSION} libnvonnxparsers8=${TENSORRT_VERSION} onnx-graphsurgeon=${TENSORRT_VERSION} python3-libnvinfer-dev=${TENSORRT_VERSION} python3-libnvinfer-dispatch=${TENSORRT_VERSION} python3-libnvinfer-lean=${TENSORRT_VERSION} python3-libnvinfer=${TENSORRT_VERSION} tensorrt-dev=${TENSORRT_VERSION} tensorrt-libs=${TENSORRT_VERSION} tensorrt=${TENSORRT_VERSION}
```

## Verify GPU

```sh
docker run -it --rm --gpus 'all,"capabilities=compute,utility"' trt nvidia-smi
```

## Verify trt

```sh
docker run -it --rm --gpus 'all,"capabilities=compute,utility"' \
    -v $(pwd):/app \
    -w /app \
    trt python3 -m check_trt.sample
```
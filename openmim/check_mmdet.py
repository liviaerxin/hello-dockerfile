from mmdet.apis import init_detector, inference_detector
import os


config_file = "./assets/rtmdet_tiny_8xb32-300e_coco.py"
checkpoint_file = "./assets/rtmdet_tiny_8xb32-300e_coco_20220902_112414-78e30dcc.pth"
model = init_detector(config_file, checkpoint_file, device="cpu")  # or device='cuda:0'
result = inference_detector(model, "./assets/demo.jpg")

print(result)
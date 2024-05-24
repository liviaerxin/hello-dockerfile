from mmocr.apis import MMOCRInferencer
ocr = MMOCRInferencer(det="DBNet", rec="CRNN", device="cuda")
ocr("./assets/demo_text_ocr.jpg", out_dir="./outputs/", save_pred=True, save_vis=True)
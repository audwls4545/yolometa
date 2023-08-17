import torch
import ultralytics
from ultralytics import YOLO

print(torch.cuda.is_available())

print(ultralytics.checks())

if __name__ == '__main__':
    model = YOLO('yolov8n.pt')
    model.train(data='C:/Users/user/PycharmProjects/pythonProject3/Fish-44/data.yaml',
                imgsz=640, batch=4, epochs=30, device=0)
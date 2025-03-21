from ultralytics import YOLO
model = YOLO('./yolov8n.pt', task='detect')
results = model('https://ultralytics.com/images/bus.jpg')
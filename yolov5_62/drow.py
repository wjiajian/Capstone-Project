from ultralytics import YOLO
# 加载训练好的模型
model = YOLO("D:\jiajian\School\Capstone_project\code\yolov5_ocsort\runs\train\exp_noatenttion\weights\best.pt")
# 将模型转为onnx格式
success = model.export(format='onnx')
import os
# os.system("python train.py --data 1916_dataset/data.yaml --epochs 300 --weights '' --cfg yolov5n.yaml  --batch-size 128")
os.system("python detect.py --weights runs/train/exp/weights/best.pt --img 416 --conf 0.2 --source 1916_dataset/test/images")

import sys
import argparse
import os

# sys.path.append('/root/ultralyticsPro/') # Path 以Autodl为例

from ultralytics import YOLO

def main(opt):
    yaml = opt.cfg
    model = YOLO(yaml) 

    model.info()

    results = model.train(data='coco128.yaml',  # 训练参数均可以重新设置
                        epochs=300, 
                        imgsz=640, 
                        workers=8, 
                        batch=2,
                        )

def parse_opt(known=False):
    parser = argparse.ArgumentParser()
    parser.add_argument('--cfg', type=str, default='ultralytics/cfg/models/v8/yolov8.yaml', help='initial weights path')
    parser.add_argument('--weights', type=str, default='', help='')

    opt = parser.parse_known_args()[0] if known else parser.parse_args()
    return opt

if __name__ == "__main__":
    opt = parse_opt()
    main(opt)
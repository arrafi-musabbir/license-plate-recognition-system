import ultralytics
import torch

device = torch.device("cuda:0" if torch.cuda.is_available() else "cpu")
print(device)

# model = ultralytics.YOLO("weights/yolov8.pt")
# model.predict(source="images/img1.jpg", conf=0.1, save=True, save_txt=True, save_conf=True)[0]


# model = torch.hub.load('WongKinYiu/yolov7', 'custom', 'weights/yolov7.pt', trust_repo=True, force_reload=True)
model = torch.hub.load('WongKinYiu/yolov7', 'custom', 'weights/yolov7.pt', trust_repo=True)

model.conf = 0.40
results = model("videos/vid1.mp4", size=640)
print(results.xyxy[0])
# results.save()
# results.crop(save=True)
# results.show()

# 
# # # model = torch.hub.load('ultralytics/yolov5', 'custom', path='weights/yolov5.pt', force_reload=True)  # local model
# model = torch.hub.load('ultralytics/yolov5', 'custom', path='weights/yolov5.pt')
# # # model = torch.hub.load('WongKinYiu/yolov7', 'custom', 'weights/yolov7.pt', trust_repo=True)


# model.conf = 0.4
# model.iou = 0.8
# results = model("images/img1.jpg", size=640)
# # print(results.crop(save=False)[0]['im'])
# # results.save()
# # print(results.save)
# # crops = results.crop(save=True)
# import pytesseract
# for i in range(13, 14):
#     text = pytesseract.image_to_string(results.crop(save=False)[0]['im'], lang='eng', 
#                                     config=f"--oem 3 --psm {i} -c tessedit_char_whitelist=-ABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789 ")
#     print("Detected license plate: >>>>  ",i, text)
    # 21-E 20741

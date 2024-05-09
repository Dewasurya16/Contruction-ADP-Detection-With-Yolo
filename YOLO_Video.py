from ultralytics import YOLO
import cv2
import math

def video_detection(path_x):
    video_capture = path_x
    #Create a Webcam Object
    cap=cv2.VideoCapture(video_capture)
    frame_width=int(cap.get(3))
    frame_height=int(cap.get(4))
    #out=cv2.VideoWriter('output.avi', cv2.VideoWriter_fourcc('M', 'J', 'P','G'), 10, (frame_width, frame_height))

    model=YOLO("YOLO-Weights/best.pt")
    classNames = ['Hardhat', 'Mask', 'NO-Hardhat', 'NO-Mask', 'NO-Safety Vest', 'Person', 'Safety Cone', 'Safety Vest', 'machinery', 'vehicle']
    while True:
        success, img = cap.read()
        results=model(img,stream=True)
        for r in results:
            boxes=r.boxes
            for box in boxes:
                x1,y1,x2,y2=box.xyxy[0]
                x1,y1,x2,y2=int(x1), int(y1), int(x2), int(y2)
                print(x1,y1,x2,y2)
                conf=math.ceil((box.conf[0]*100))/100
                cls=int(box.cls[0])
                class_name=classNames[cls]
                label=f'{class_name}{conf}'
                t_size = cv2.getTextSize(label, 0, fontScale=1, thickness=2)[0]
                print(t_size)
                c2 = x1 + t_size[0], y1 - t_size[1] - 3
                
                # Atur warna berdasarkan kelas objek yang terdeteksi
                if class_name == 'Hardhat':
                    color=(0, 204, 255)  # Warna: Biru
                elif class_name == "Mask":
                    color = (222, 82, 175)  # Warna: Ungu
                elif class_name == "NO-Hardhat":
                    color = (0, 149, 255)  # Warna: Biru Muda
                elif class_name == "NO-Mask":
                    color = (255, 0, 0)  # Warna: Merah
                elif class_name == "NO-Safety Vest":
                    color = (255, 255, 0)  # Warna: Kuning
                elif class_name == "Person":
                    color = (0, 255, 0)  # Warna: Hijau
                elif class_name == "Safety Cone":
                    color = (0, 255, 255)  # Warna: Cyan
                elif class_name == "Safety Vest":
                    color = (128, 0, 128)  # Warna: Ungu Tua
                elif class_name == "machinery":
                    color = (255, 165, 0)  # Warna: Orange
                elif class_name == "vehicle":
                    color = (0, 0, 255)  # Warna: Merah Tua
                else:
                    color = (85, 45, 255)  # Warna: Merah Tua
                
                # Atur warna teks untuk kontras
                text_color = (255, 255, 255) if sum(color) < 500 else (0, 0, 0)
                
                if conf > 0.5:
                    cv2.rectangle(img, (x1, y1), (x2, y2), color, 3)
                    cv2.rectangle(img, (x1, y1), c2, color, -1, cv2.LINE_AA)  # filled
                    cv2.putText(img, label, (x1, y1 - 2), 0, 1, text_color, thickness=1, lineType=cv2.LINE_AA)

        yield img
        #out.write(img)
        #cv2.imshow("image", img)
        #if cv2.waitKey(1) & 0xFF==ord('1'):
            #break

cv2.destroyAllWindows()

import cv2 as cv
import numpy as np
from datetime import datetime
from pathlib import Path

BASE_DIR = Path(__file__).resolve().parent
DATA_DIR = BASE_DIR / "data"
CASCADE_PATH = BASE_DIR / "haarcascade_frontalface_default.xml"
OUTPUT_VIDEO_PATH = BASE_DIR / "output_face_detection.avi"

NAMES = ["Name1", "Name2", "Name3", "Name4"]
UNKNOWN_NAME = "Unknown"


def ensure_directory(path: Path) -> None:
    path.mkdir(parents=True, exist_ok=True)


face_cascade = cv.CascadeClassifier(str(CASCADE_PATH))
if face_cascade.empty():
    raise RuntimeError("ไม่พบไฟล์ haarcascade_frontalface_default.xml")


try:
    recognizer = cv.face.LBPHFaceRecognizer_create()
except AttributeError:
    recognizer = None


def build_recognizer():
    if recognizer is None:
        return None

    images = []
    labels = []

    for index, name in enumerate(NAMES):
        folder = DATA_DIR / name
        ensure_directory(folder)
        for image_path in sorted(folder.glob("*")):
            if image_path.suffix.lower() not in {".jpg", ".jpeg", ".png", ".bmp"}:
                continue
            image = cv.imread(str(image_path), cv.IMREAD_GRAYSCALE)
            if image is None:
                continue
            images.append(image)
            labels.append(index)

    if len(images) < 2:
        return None

    try:
        recognizer.train(images, np.array(labels))
        return recognizer
    except Exception:
        return None


recognizer = build_recognizer()

for name in NAMES + [UNKNOWN_NAME]:
    ensure_directory(DATA_DIR / name)

cap = cv.VideoCapture(0)
if not cap.isOpened():
    raise RuntimeError("ไม่สามารถเปิดกล้องได้")

frame_width = int(cap.get(cv.CAP_PROP_FRAME_WIDTH))
frame_height = int(cap.get(cv.CAP_PROP_FRAME_HEIGHT))
fps = int(cap.get(cv.CAP_PROP_FPS)) or 20
video_writer = cv.VideoWriter(
    str(OUTPUT_VIDEO_PATH),
    cv.VideoWriter_fourcc(*"XVID"),
    fps,
    (frame_width, frame_height),
)

while True:
    ok, frame = cap.read()
    if not ok:
        break

    gray_frame = cv.cvtColor(frame, cv.COLOR_BGR2GRAY)
    faces = face_cascade.detectMultiScale(gray_frame, scaleFactor=1.1, minNeighbors=5, minSize=(80, 80))

    timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    cv.putText(frame, timestamp, (10, 30), cv.FONT_HERSHEY_SIMPLEX, 0.7, (255, 255, 255), 2)

    for (x, y, w, h) in faces:
        roi_gray = gray_frame[y:y + h, x:x + w]
        roi_color = frame[y:y + h, x:x + w]

        name = UNKNOWN_NAME
        confidence = 0.0

        if recognizer is not None:
            try:
                label, conf = recognizer.predict(roi_gray)
                if 0 <= label < len(NAMES) and conf < 120:
                    name = NAMES[label]
                    confidence = round(conf, 2)
            except Exception:
                name = UNKNOWN_NAME
                confidence = 0.0

        cv.rectangle(frame, (x, y), (x + w, y + h), (0, 255, 0), 2)
        cv.putText(frame, name, (x, y - 10), cv.FONT_HERSHEY_SIMPLEX, 0.8, (0, 255, 0), 2)
        cv.putText(frame, f"Conf: {confidence:.2f}", (x, y + h + 25), cv.FONT_HERSHEY_SIMPLEX, 0.6, (255, 255, 255), 2)

        save_path = DATA_DIR / name / f"{name}_{datetime.now().strftime('%Y%m%d_%H%M%S_%f')}.jpg"
        ensure_directory(save_path.parent)
        cv.imwrite(str(save_path), roi_color)

    video_writer.write(frame)
    cv.imshow("Face Detection", frame)

    if cv.waitKey(1) & 0xFF == ord("q"):
        break

cap.release()
video_writer.release()
cv.destroyAllWindows()

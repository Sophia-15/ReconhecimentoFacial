import cv2 
from simple_facerec import SimpleFacerec

sfr = SimpleFacerec()
sfr.load_encoding_images("src/assets/")

cap = cv2.VideoCapture(0)

while True:
  ret, frame = cap.read()

  face_locations, face_names = sfr.detect_known_faces(frame)

  for face_loc, name in zip(face_locations, face_names):
    access_text = "Acesso Permitido" if people[name] else "Acesso Negado"
    y1, x2, y2 , x1 = face_loc[0], face_loc[1], face_loc[2], face_loc[3]
    y1 -= 24
    y2 += 48
    font = cv2.FONT_HERSHEY_COMPLEX_SMALL

    cv2.rectangle(frame, (x1, y1), (x2, y2), (0, 0, 200), 4)

    cv2.rectangle(frame, (x1, y2 - 35), (x2, y2), (0, 0, 200), cv2.FILLED)
    cv2.putText(frame, access_text, (x1 + 6, y2 - 6), font, 1, (255, 255, 255), 1)

  cv2.imshow("Camera", frame)

  key = cv2.waitKey(1)
  if key == ord('q'):
    break

cap.release()
cv2.destroyAllWindows()
import requests as req
import json
import cv2
import base64
import numpy as np

name = input("enter pic name: ")
res = req.get('http://localhost', params={'pic name': name})

json_res = json.loads(res.text)
status = json_res["status"]

if status == 404:
    print(json_res["message"])
elif status == 200:
    print(json_res["message"])
    ext_as_text = json_res["image"]
    ext = json_res["ext"]
    ext_original = base64.b64decode(ext_as_text)
    ext_as_np = np.frombuffer(ext_original, dtype=np.uint8)
    image_buffer = cv2.imdecode(ext_as_np, flags=1)
    cv2.imshow(name, image_buffer)
    while True:
        if cv2.waitKey(1) & 0xFF == 27:
            break
    cv2.destroyAllWindows()

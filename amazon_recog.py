# import cv2
# import boto3
# from PIL import Image, ImageDraw, ImageFont
# import numpy as np
# # from collections import deque
# import streamlit as st


# # AWS Rekognition client
# rekognition = boto3.client('rekognition', aws_access_key_id=st.secrets["access_key_id"],
#                            aws_secret_access_key=st.secrets["secret_access_key"],
#                            region_name='us-east-1')

# # Load the font for annotation
# font = ImageFont.truetype('arial.ttf', 30)

# # Initialize a deque to store the eye state of the last 4 frames
# eye_state_deque = []

# def detect_faces_and_attributes(image_np: np.array):
#     _, image_bytes = cv2.imencode('.jpg', image_np)
#     rekognition_response = rekognition.detect_faces(
#         Image={'Bytes': image_bytes.tobytes()}, Attributes=['ALL'])
    
#     image = Image.fromarray(cv2.cvtColor(image_np, cv2.COLOR_BGR2RGB))
#     image_width, image_height = image.size
#     draw = ImageDraw.Draw(image)

#     line_width = 3
#     for item in rekognition_response.get('FaceDetails'):
#         bounding_box = item['BoundingBox']
#         width = image_width * bounding_box['Width']
#         height = image_height * bounding_box['Height']
#         left = image_width * bounding_box['Left']
#         top = image_height * bounding_box['Top']

#         left = int(left)
#         top = int(top)
#         width = int(width) + left
#         height = int(height) + top

#         draw.rectangle(((left, top), (width, height)), outline='red', width=line_width)

#         eyeglasses = item['Eyeglasses']
#         eyeglasses_text = 'Eyeglasses: ' + ('Yes' if eyeglasses['Value'] else 'No')

#         face_occlusion = item['FaceOccluded']
#         face_occlusion_text = 'Face Occluded: ' + ('Yes' if face_occlusion['Value'] else 'No')

#         pose = item['Pose']
#         if abs(pose['Yaw']) > 10 or abs(pose['Pitch']) > 10 or abs(pose['Roll']) > 10:
#             draw.text((left, top - 120), "Please align your head", 'green', font=font)

#         left_eye_open = item['EyesOpen']['Value']
#         right_eye_open = item['EyesOpen']['Value']

#         eye_state = 'Open' if left_eye_open and right_eye_open else 'Closed'
#         eye_state_deque.append(eye_state)

#         if len(eye_state_deque) == 4 and all(state == 'Closed' for state in eye_state_deque):
#             draw.text((left, top + 5), 'Liveness: Not Detected', 'green', font=font)
#         elif len(eye_state_deque) == 4 and all(state == 'Open' for state in eye_state_deque):
#             draw.text((left, top + 20), 'Liveness: Not Detected', 'green', font=font)
#         else:
#             draw.text((left, top + 35), 'Liveness: Detected', 'green', font=font)

#         draw.text((left, top + 50), eyeglasses_text, 'green', font=font)
#         draw.text((left, top + 70), face_occlusion_text, 'green', font=font)

#     return cv2.cvtColor(np.array(image), cv2.COLOR_RGB2BGR)

# def check_brightness(image_np: np.array) -> float:
#     gray_image = cv2.cvtColor(image_np, cv2.COLOR_BGR2GRAY)
#     return np.mean(gray_image)

# def main():
#     st.title("Face Detection and Liveness Check")

#     run = st.checkbox('Run Webcam')
#     FRAME_WINDOW = st.image([])

#     if run:
#         cap = cv2.VideoCapture(0)

#         while run:
#             ret, frame = cap.read()
#             if not ret:
#                 break

#             brightness = check_brightness(frame)
#             brightness_text = f'Brightness: {brightness:.2f}'

#             if brightness > 150:
#                 processed_frame = detect_faces_and_attributes(frame)
#             else:
#                 processed_frame = frame
#                 cv2.putText(processed_frame, 'Environment not bright enough', (10, 30), cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 0, 255), 2)

#             cv2.putText(processed_frame, brightness_text, (10, 70), cv2.FONT_HERSHEY_SIMPLEX, 1, (255, 255, 255), 2)
#             FRAME_WINDOW.image(processed_frame, channels='BGR')

#         cap.release()

# if __name__ == '__main__':
#     main()





# import cv2
# import boto3
# from PIL import Image, ImageDraw, ImageFont
# import numpy as np
# import streamlit as st

# # AWS Rekognition client
# rekognition = boto3.client('rekognition', aws_access_key_id=st.secrets['aws_access_key_id'],
#                            aws_secret_access_key=st.secrets['aws_secret_access_key'],
#                            region_name='us-east-1')

# # Load the font for annotation
# font = ImageFont.truetype('arial.ttf', 30)

# # Initialize a list to store the eye state of the last 4 frames
# eye_state_list = []

# def detect_faces_and_attributes(image_np: np.array):
#     _, image_bytes = cv2.imencode('.jpg', image_np)
#     rekognition_response = rekognition.detect_faces(
#         Image={'Bytes': image_bytes.tobytes()}, Attributes=['ALL'])
    
#     image = Image.fromarray(cv2.cvtColor(image_np, cv2.COLOR_BGR2RGB))
#     image_width, image_height = image.size
#     draw = ImageDraw.Draw(image)

#     line_width = 3
#     for item in rekognition_response.get('FaceDetails'):
#         bounding_box = item['BoundingBox']
#         width = image_width * bounding_box['Width']
#         height = image_height * bounding_box['Height']
#         left = image_width * bounding_box['Left']
#         top = image_height * bounding_box['Top']

#         left = int(left)
#         top = int(top)
#         width = int(width) + left
#         height = int(height) + top

#         draw.rectangle(((left, top), (width, height)), outline='red', width=line_width)

#         eyeglasses = item['Eyeglasses']
#         eyeglasses_text = 'Eyeglasses: ' + ('Yes' if eyeglasses['Value'] else 'No')

#         face_occlusion = item['FaceOccluded']
#         face_occlusion_text = 'Face Occluded: ' + ('Yes' if face_occlusion['Value'] else 'No')

#         pose = item['Pose']
#         if abs(pose['Yaw']) > 10 or abs(pose['Pitch']) > 10 or abs(pose['Roll']) > 10:
#             draw.text((left, top - 120), "Please align your head", 'green', font=font)

#         left_eye_open = item['EyesOpen']['Value']
#         right_eye_open = item['EyesOpen']['Value']

#         eye_state = 'Open' if left_eye_open and right_eye_open else 'Closed'
#         eye_state_list.append(eye_state)
#         if len(eye_state_list) > 4:
#             eye_state_list.pop(0)

#         if len(eye_state_list) == 4 and all(state == 'Closed' for state in eye_state_list):
#             draw.text((left, top + 5), 'Liveness: Not Detected', 'green', font=font)
#         elif len(eye_state_list) == 4 and all(state == 'Open' for state in eye_state_list):
#             draw.text((left, top + 20), 'Liveness: Not Detected', 'green', font=font)
#         else:
#             draw.text((left, top + 35), 'Liveness: Detected', 'green', font=font)

#         draw.text((left, top + 50), eyeglasses_text, 'green', font=font)
#         draw.text((left, top + 70), face_occlusion_text, 'green', font=font)

#     return cv2.cvtColor(np.array(image), cv2.COLOR_RGB2BGR)

# def check_brightness(image_np: np.array) -> float:
#     gray_image = cv2.cvtColor(image_np, cv2.COLOR_BGR2GRAY)
#     return np.mean(gray_image)

# def main():
#     st.title("Face Detection and Liveness Check")

#     run = st.checkbox('Run Webcam')
#     FRAME_WINDOW = st.image([])

#     if run:
#         cap = cv2.VideoCapture(0)

#         while run:
#             ret, frame = cap.read()
#             if not ret:
#                 break

#             brightness = check_brightness(frame)
#             brightness_text = f'Brightness: {brightness:.2f}'

#             if brightness > 150:
#                 processed_frame = detect_faces_and_attributes(frame)
#             else:
#                 processed_frame = frame
#                 cv2.putText(processed_frame, 'Environment not bright enough', (10, 30), cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 0, 255), 2)

#             cv2.putText(processed_frame, brightness_text, (10, 70), cv2.FONT_HERSHEY_SIMPLEX, 1, (255, 255, 255), 2)
#             FRAME_WINDOW.image(processed_frame, channels='BGR')

#         cap.release()

# if __name__ == '__main__':
#     main()







import cv2
import boto3
from PIL import Image, ImageDraw, ImageFont
import numpy as np
import streamlit as st

# AWS Rekognition client
rekognition = boto3.client('rekognition', aws_access_key_id=st.secrets['aws_access_key_id'],
                           aws_secret_access_key=st.secrets['aws_secret_access_key'],
                           region_name='us-east-1')

# Load the default font for annotation
font = ImageFont.load_default()

# Initialize a list to store the eye state of the last 4 frames
eye_state_list = []

def detect_faces_and_attributes(image_np: np.array):
    _, image_bytes = cv2.imencode('.jpg', image_np)
    rekognition_response = rekognition.detect_faces(
        Image={'Bytes': image_bytes.tobytes()}, Attributes=['ALL'])
    
    image = Image.fromarray(cv2.cvtColor(image_np, cv2.COLOR_BGR2RGB))
    image_width, image_height = image.size
    draw = ImageDraw.Draw(image)

    line_width = 3
    for item in rekognition_response.get('FaceDetails'):
        bounding_box = item['BoundingBox']
        width = image_width * bounding_box['Width']
        height = image_height * bounding_box['Height']
        left = image_width * bounding_box['Left']
        top = image_height * bounding_box['Top']

        left = int(left)
        top = int(top)
        width = int(width) + left
        height = int(height) + top

        draw.rectangle(((left, top), (width, height)), outline='red', width=line_width)

        eyeglasses = item['Eyeglasses']
        eyeglasses_text = 'Eyeglasses: ' + ('Yes' if eyeglasses['Value'] else 'No')

        face_occlusion = item['FaceOccluded']
        face_occlusion_text = 'Face Occluded: ' + ('Yes' if face_occlusion['Value'] else 'No')

        pose = item['Pose']
        if abs(pose['Yaw']) > 10 or abs(pose['Pitch']) > 10 or abs(pose['Roll']) > 10:
            draw.text((left, top - 120), "Please align your head", 'green', font=font)

        left_eye_open = item['EyesOpen']['Value']
        right_eye_open = item['EyesOpen']['Value']

        eye_state = 'Open' if left_eye_open and right_eye_open else 'Closed'
        eye_state_list.append(eye_state)
        if len(eye_state_list) > 4:
            eye_state_list.pop(0)

        if len(eye_state_list) == 4 and all(state == 'Closed' for state in eye_state_list):
            draw.text((left, top + 5), 'Liveness: Not Detected', 'green', font=font)
        elif len(eye_state_list) == 4 and all(state == 'Open' for state in eye_state_list):
            draw.text((left, top + 20), 'Liveness: Not Detected', 'green', font=font)
        else:
            draw.text((left, top + 35), 'Liveness: Detected', 'green', font=font)

        draw.text((left, top + 50), eyeglasses_text, 'green', font=font)
        draw.text((left, top + 70), face_occlusion_text, 'green', font=font)

    return cv2.cvtColor(np.array(image), cv2.COLOR_RGB2BGR)

def check_brightness(image_np: np.array) -> float:
    gray_image = cv2.cvtColor(image_np, cv2.COLOR_BGR2GRAY)
    return np.mean(gray_image)

def main():
    st.title("Face Detection and Liveness Check")

    run = st.checkbox('Run Webcam')
    FRAME_WINDOW = st.image([])

    if run:
        cap = cv2.VideoCapture(0)

        while run:
            ret, frame = cap.read()
            if not ret:
                break

            brightness = check_brightness(frame)
            brightness_text = f'Brightness: {brightness:.2f}'

            if brightness > 150:
                processed_frame = detect_faces_and_attributes(frame)
            else:
                processed_frame = frame
                cv2.putText(processed_frame, 'Environment not bright enough', (10, 30), cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 0, 255), 2)

            cv2.putText(processed_frame, brightness_text, (10, 70), cv2.FONT_HERSHEY_SIMPLEX, 1, (255, 255, 255), 2)
            FRAME_WINDOW.image(processed_frame, channels='BGR')

        cap.release()

if __name__ == '__main__':
    main()



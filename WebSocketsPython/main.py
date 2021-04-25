from flask import Flask, render_template, url_for, request, redirect
import cv2
app = Flask(__name__)


@app.route('/')
def index():
    return "Success, API is working"


@app.route('/video', methods=['GET'])
def video():
    if request.method == 'GET':
        base64img = request.args.get("img")

        cap = cv2.VideoCapture("rtmp://192.168.1.180/live/petar")

        ret, frame1 = cap.read()
        ret, frame2 = cap.read()

        try:
            while cap.isOpened():
                diff = cv2.absdiff(frame1, frame2)
                gray = cv2.cvtColor(diff, cv2.COLOR_BGR2GRAY)
                blur = cv2.GaussianBlur(gray, (5, 5), 0)
                _, thresh = cv2.threshold(blur, 20, 255, cv2.THRESH_BINARY)
                dilated = cv2.dilate(thresh, None, iterations=3)
                contours, _ = cv2.findContours(dilated, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)[-2:]

                for contour in contours:
                    x, y, w, h = cv2.boundingRect(contour)
                    if cv2.contourArea(contour) < 800:
                        continue
                    cv2.rectangle(frame1, (x, y), (x + w, y + h), (0, 255, 0), 3)

                cv2.imshow("frame", frame1)
                frame1 = frame2
                ret, frame2 = cap.read()

                if cv2.waitKey(30) == 27:
                    break
        except:
            print("iz ded")

        cv2.destroyAllWindows()
        cap.release()



        return base64img


if __name__ == "__main__":
    app.run(debug=True, port=6060)

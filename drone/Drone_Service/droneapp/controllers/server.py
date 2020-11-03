import logging

from flask import jsonify
from flask import render_template
from flask import request
from flask import Response

from droneapp.models.drone_manager import DroneManager

import config


logger = logging.getLogger(__name__)
app = config.app


def get_drone():
    return DroneManager()


@app.route('/') # main page
def main():    
    return render_template('main.html')

@app.route('/userControl/') # userControl Page
def user_control():
    return render_template('userControl.html')

@app.route('/ballTracking/') # ballTracking Page
def ball_tracking():
    return render_template('ballTracking.html')

@app.route('/faceTracking/') # faceTracking Page
def face_tracking():
    return render_template('faceTracking.html')

@app.route('/help/') # help Page
def help():
    return render_template('help.html')

@app.route('/api/command/', methods=['POST'])
def command():
    cmd = request.form.get('command')
    logger.info({'action': 'command', 'cmd': cmd})
    drone = get_drone()
    if cmd == 'takeoff':
        drone.takeoff()
    if cmd == 'land':
        drone.land()
    if cmd == 'speed':
        speed = request.form.get('speed')
        logger.info({'action': 'command', 'cmd': cmd, 'speed': speed})
        if speed:
            drone.set_speed(int(speed))

    if cmd == 'up':
        drone.up()
    if cmd == 'down':
        drone.down()
    if cmd == 'forward':
        drone.forward()
    if cmd == 'back':
        drone.back()
    if cmd == 'clockwise':
        drone.clockwise()
    if cmd == 'counterClockwise':
        drone.counter_clockwise()
    if cmd == 'left':
        drone.left()
    if cmd == 'right':
        drone.right()    
    if cmd == 'faceDetectAndTrack':
        drone.enable_face_detect()
    if cmd == 'stopFaceDetectAndTrack':
        drone.disable_face_detect()
    if cmd == 'ballDetectAndTrack':
        drone.enable_ball_detect()
    if cmd == 'stopBallDetectAndTrack':
        drone.disable_ball_detect()
    if cmd == 'snapshot':
        if drone.snapshot():
            return jsonify(status='success'), 200
        else:
            return jsonify(status='fail'), 400

    return jsonify(status='success'), 200

def video_generator():
    drone = get_drone()
    for jpeg in drone.video_jpeg_generator():
        yield (b'--frame\r\n'
               b'Content-Type: image/jpeg\r\n\r\n' +
               jpeg +
               b'\r\n\r\n')


@app.route('/video/streaming')
def video_feed():
    return Response(video_generator(), mimetype='multipart/x-mixed-replace; boundary=frame')

def run():
    app.run(host=config.WEB_ADDRESS, port=config.WEB_PORT, threaded=True)
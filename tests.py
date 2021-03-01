from . import GoBroAPI

gobrocamera = GoBroCamera(ip, port)

# positive testing scenarios, where we first set the shutter off
# and then we try the different camera modes

def test_set_mode_video(gobrocamera):
    gobrocamera.set_shutter(Shutter.OFF)
    if gobrocamera.set_mode(Mode.VIDEO):
        print("Test set mode video passed!")
        return True
    else:
        print("Test set mode video failed!")
        return False

def test_set_mode_photo(gobrocamera):
    gobrocamera.set_shutter(Shutter.OFF)
    if gobrocamera.set_mode(Mode.PHOTO):
        print("Test set mode photo passed!")
        return True
    else:
        print("Test set mode photo failed!")
        return False

def test_set_mode_burst(gobrocamera):
    gobrocamera.set_shutter(Shutter.OFF)
    if gobrocamera.set_mode(Mode.BURST):
        print("Test set mode burst passed!")
        return True
    else:
        print("Test set mode burst failed!")
        return False

def test_set_mode_time_lapse_video(gobrocamera):
    gobrocamera.set_shutter(Shutter.OFF)
    if gobrocamera.set_mode(Mode.TIME_LAPSE_VIDEO):
        print("Test set mode time lapse video passed!")
        return True
    else:
        print("Test set mode time lapse video failed!")
        return False

def test_set_mode_slo_mo(gobrocamera):
    gobrocamera.set_shutter(Shutter.OFF)
    if gobrocamera.set_mode(Mode.SLO_MO):
        print("Test set mode slo-mo passed!")
        return True
    else:
        print("Test set mode slo-mo failed!")
        return False

#negative testing scenario, where we let the shutter on (it was iniated on by default in the constructor)
#and we try to set a mode without having the shutter off

def test_set_mode_negative(gobrocamera):
    try: 
        gobrocamera.set_mode(Mode.SLO_MO)
        print("Negative scenario failed!")
        return False
    except ShutterException:
        print("Negative scenario passed!")
        return True

#negative testing scenario, try to set a mode that does not exist

def test_set_mode_panoramic_negative(gobrocamera):
    try: 
        gobrocamera.set_shutter(Shutter.OFF)
        gobrocamera.set_mode(Mode.PANORAMIC)
        print("Negative scenario failed!")
        return False
    except Exception:
        print("Negative scenario passed!")
        return True


# positive testing scenarios, where we first set the shutter off
# and then we try the different camera settings

def test_set_resolution_720p(gobrocamera):
    gobrocamera.set_shutter(Shutter.OFF)
    if gobrocamera.set_setting(VideoResolution._720p):
        print("Test set video resolution 720p passed!")
        return True
    else:
        print("Test set video resolution 720p failed!")
        return False

def test_set_resolution_1080p(gobrocamera):
    gobrocamera.set_shutter(Shutter.OFF)
    if gobrocamera.set_setting(VideoResolution._1080p):
        print("Test set video resolution 1080p passed!")
        return True
    else:
        print("Test set video resolution 1080p failed!")
        return False

def test_set_resolution_4k(gobrocamera):
    gobrocamera.set_shutter(Shutter.OFF)
    if gobrocamera.set_setting(VideoResolution._4k):
        print("Test set video resolution 4k passed!")
        return True
    else:
        print("Test set video resolution 4k failed!")
        return False

def test_set_framerate_30fps(gobrocamera):
    gobrocamera.set_shutter(Shutter.OFF)
    if gobrocamera.set_setting(FrameRate._30fps):
        print("Test set framerate to 30fps passed!")
        return True
    else:
        print("Test set framerate to 30fps failed!")
        return False

def test_set_framerate_60fps(gobrocamera):
    gobrocamera.set_shutter(Shutter.OFF)
    if gobrocamera.set_setting(FrameRate._60fps):
        print("Test set framerate to 60fps passed!")
        return True
    else:
        print("Test set framerate to 60fps failed!")
        return False

def test_set_framerate_120fps(gobrocamera):
    gobrocamera.set_shutter(Shutter.OFF)
    if gobrocamera.set_setting(FrameRate._120fps):
        print("Test set framerate to 120fps passed!")
        return True
    else:
        print("Test set framerate to 120fps failed!")
        return False

def test_set_framerate_240fps(gobrocamera):
    gobrocamera.set_shutter(Shutter.OFF)
    if gobrocamera.set_setting(FrameRate.240fps):
        print("Test set framerate to 240fps passed!")
        return True
    else:
        print("Test set framerate to 240fps failed!")
        return False

#negative testing scenario, where we let the shutter on (it was iniated on by default in the constructor)
#and we try to set a camera setting without having the shutter off

def test_set_framerate_negative(gobrocamera):
    try: 
        gobrocamera.set_setting(FrameRate._60fps)
        print("Negative scenario failed!")
        return False
    except ShutterException:
        print("Negative scenario passed!")
        return True

#negative testing scenario, try to set a setting that does not exist

def test_set_videosize_negative(gobrocamera):
    try:
        gobrocamera.set_shutter(Shutter.OFF) 
        gobrocamera.set_setting(VideoSize._1024mb)
        print("Negative scenario failed!")
        return False
    except Exception:
        print("Negative scenario passed!")
        return True

# positive testing scenarios, where we first set the shutter off
# and then we try to set different dates

def test_set_date_time(gobrocamera):
    gobrocamera.set_shutter(Shutter.OFF)
    if gobrocamera.set_date('28.02.2021','19:37:23'):
        print("Test set date and time passed!")
        return True
    else:
        print("Test set date and time failed!")
        return False

def test_set_date_time_bigger_values(gobrocamera):
    gobrocamera.set_shutter(Shutter.OFF)
        if gobrocamera.set_date('282.021.3122021','232:3731:21243'):
        print("Test set date and time passed!")
        return True
    else:
        print("Test set date and time failed!")
        return False


#negative scenario, with shutter left on
def test_set_date_time_negative(gobrocamera):
    try:
        gobrocamera.set_date('08.02.2020','05:37:22'):
        print("Negative scenario failed!")
        return False
    except ShutterException:
        print("Negative scenario passed!")
        return True

def test_get_camera_shutter_status(gobrocamera):
    print("Setting camera shutter to off")
    gobrocamera.set_shutter(Shutter.OFF)
    status = gobrocamera.get_status()
    if status.shatter == 'OFF':
        print("Test passed!")
        return True
    else:
        print("Test failed!")
        return False

def test_get_camera_mode_status(gobrocamera):
    gobrocamera.set_shutter(Shutter.OFF)
    print("Setting camera mode to video")
    gobrocamera.set_mode(Mode.VIDEO)
    status = gobrocamera.get_status()
    if status.mode == 'VIDEO':
        print("Test passed!")
        return True
    else:
        print("Test failed!")
        return False

def test_get_camera_setting_status(gobrocamera):
    gobrocamera.set_shutter(Shutter.OFF)
    print("Setting camera video resolution to 1080p")
    gobrocamera.set_setting(VideoResolution._1080p)
    print("Setting camera frame rate to 60fps")
    gobrocamera.set_setting(FrameRate._60fps)
    status = gobrocamera.get_status()
    if status.setting == ['_1080p', '_60fps']:
        print("Test passed!")
        return True
    else:
        print("Test failed!")
        return False


#negative scenario, without having the shutter set off
def test_get_camera_status_negative(gobrocamera):
    gobrocamera.set_setting(VideoResolution._1080p)
    try:
        status = gobrocamera.get_status()
        print("Negative scenario failed!")
        return False
    except Exception:
        print("Negative scenario passed!")
        return True


#let's stress test the camera a bit by doing 1000 iterations of various commands
def test_stress_run_set_mode(gobrocamera):
    gobrocamera.set_shutter(Shutter.OFF)
    for i in range(1,1001):
        if gobrocamera.set_mode(Mode.PHOTO):
            print("Successfully set camera mode to photo on iteration %d", i)
        else:
            print("Setting camera mode to photo failed on iteration %d," i)
            break()
    if i == 1000:
        print("Stress run passed!")
        return True
    else:
        print("Stress run failed!")
        return False

def test_stress_run_set_frame_rate(gobrocamera):
    gobrocamera.set_shutter(Shutter.OFF)
    for i in range(1,1001):
        if  gobrocamera.set_setting(FrameRate._60fps):
            print("Successfully set frame rate to 60fps on iteration %d", i)
        else:
            print("Setting frame rate to 60fps failed on iteration %d," i)
            break()
    if i == 1000:
        print("Stress run passed!")
        return True
    else:
        print("Stress run failed!")
        return False


def test_stress_run_set_vide_resolution(gobrocamera):
    gobrocamera.set_shutter(Shutter.OFF)
    for i in range(1,1001):
        if  gobrocamera.set_setting(VideoResolution._4k):
            print("Successfully set video resolution to 4k on iteration %d", i)
        else:
            print("Setting video resolution to 4k failed on iteration %d," i)
            break()
    if i == 1000:
        print("Stress run passed!")
        return True
    else:
        print("Stress run failed!")
        return False

def test_stress_run_set_date(gobrocamera):
    gobrocamera.set_shutter(Shutter.OFF)
    for i in range(1,1001):
        if  gobrocamera.set_date('05.10.2021','23:05:44'):
            print("Successfully set date on iteration %d", i)
        else:
            print("Setting date failed on iteration %d," i)
            break()
    if i == 1000:
        print("Stress run passed!")
        return True
    else:
        print("Stress run failed!")
        return False


#end-to-end scenario means configuring the entire list of settings available in the API
#in a single test

def test_end_to_end_setting(gobrocamera):
    gobrocamera.set_shutter(Shutter.OFF)
    gobrocamera.set_mode(Mode.VIDEO)
    gobrocamera.set_setting(VideoResolution._4k)
    gobrocamera.set_setting(FrameRate._60fps)
    gobrocamera.set_date('05.11.2021','07:22:44')
    status = gobrocamera.get_status()
    if status.shutter == "OFF" and \
       status.mode == "VIDEO" and \
       status.setting = ['_4k', '_60fps']:
       print("End-to-end settings have been properly configured")
       return True
    else:
        print("Failure when configuring end-to-end settings")
        return False
    




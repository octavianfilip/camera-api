from enum import Enum

class Shutter(Enum):
    OFF = 0
    ON = 1

class Mode(Enum):
    VIDEO = 1 
    PHOTO = 2 
    BURST = 3
    TIME_LAPSE_VIDEO = 4
    SLO_MO = 5

class Setting(Enum):
    RESOLUTION = 1
    RATE = 2

class VideoResolution(Enum):
    _720p = 1
    _1080p = 2
    _4k = 3
    
class FrameRate(Enum):
    _30fps = 1
    _60fps = 2
    _120fps = 3
    _240fps = 4

class ShutterException(Exception):
    """Class for handling exceptions related to shutter state"""
    pass

class GoBroCamera():
    def __init__(self, camera_ip, camera_port):
        self.camera_ip = camera_ip
        self.camera_port = camera_port
        self.shutter_mode = Shutter.ON
        self.find_camera(self.camera_ip)
        self.connect(self.camera_ip)

    #logic is inside, including error handling  
    def find_camera(camera_ip):
        pass

    #logic is inside, including error handling
    def connect(camera_port):
        pass

    def set_shutter(Shutter_Mode):
        #Shutter_Mode is going to be a Shutter enum as defined above
        self.Shutter_Mode = Shutter_Mode
        url = "/command/shutter?p={}".format(Shutter_Mode.value)
        #mechanism to tackle cammera disconnecion or temporar unavailabilty
        retries = 10
        while retries:
            js = send_command(url)
            if js == {}:
                print("Successfully set the shutter mode %s" , Shutter_Mode.name)
                return True
            else:
                retries -= 1
                print("Command %s returned the following error: %s", js["command"], js["error"])
        return False

    
    def set_mode(Mode_Type):
        # mode_type is going to be a Mode enum as defined above
        if self.shutter_mode == Shutter.ON:
            print("Camera shutter is on. While in this state, the camera does not accept any other commands.\n")
            print("Please set shutter off first")
            raise ShutterException

        self.Mode_Type = Mode_Type
        url = "/command/set_mode?p={}".format(Mode_Type.value)
        #mechanism to tackle cammera disconnecion or temporar unavailabilty
        retries = 10
        while retries:
            js = send_command(url)
            if js == {}:
                print("Successfully set the camera mode %s", Mode_Type.name)
                return True
            else:
                retries -= 1
                print("Command %s returned the following error: %s", js["command"], js["error"])
        return False
        
        
     def set_setting(Setting):
        # Setting is going to be either a VideoResolution Enum or a FrameRateEnum
        if self.shutter_mode == Shutter.ON:
            print("Camera shutter is on. While in this state, the camera does not accept any other commands.\n")
            print("Please set shutter off first")
            raise ShutterException
        
        option_id = None
        if isinstance(Setting, VideoResolution):
            option_id = 1
        elif isinstance(Setting, FrameRate):
            option_id = 2
        else:
            print("Incorrect value inserted!")
            raise Exception

        url = "/setting/{}/{}".format(option_id, Setting.value)
        #mechanism to tackle cammera disconnecion or temporar unavailabilty
        retries = 10
        while retries:
            js = send_command(url)
            if js == {}:
                print("Successfully set the camera setting to %s", Setting.name)
                return True
            else:
                retries -= 1
                print("Command %s returned the following error: %s", js["command"], js["error"])
        return False
    
    
    def set_date(date, time):
       # Date is going to have this format, with values separated by .
         # 28.02.2021
        # Time is going to have this format, with values separated by :
        # 14:04:32
        if self.shutter_mode == Shutter.ON:
            print("Camera shutter is on. While in this state, the camera does not accept any other commands.\n")
            print("Please set shutter off first")
            raise ShutterException

        value = 0
        [day, month, year] = date.split('.')
	    [hour, minute, second] = time.split(':')
        
        # Populate value with the seconds. It uses bits 0-7, so we don't need to left shift it. 
	    second = int(second)
        second &= 0xFF
        #only preserving 8 bits value
	    value |= second

        # Populate value with the minutes. It uses bits 8-15, so we need to left shift it with 8.
	    minute = int(minute)
        minute &= 0xFF
	    minute <<= 8
	    value |= minute

        #Populate value with the hours. It uses bits 16-23, so we need to left shift it with 16.
        hour = int(hour)
        hour &= 0xFF
        hour <<= 16
        value |= hour

        #Populate value with the day. It uses bits 24-31, so we need to left shift it with 24.
        day = int(day)
        day &= 0xFF
        day <<= 24
        value |= day

        month = int(month)
        month &= 0xFF
        month <<= 32
        value |= month

        year = int(year)
        year &= 0xFFFF
        #only preserving 16 bits values
        year <<=40
        value |= year

        url = "/command/set_date?p={}".format(value)
        #mechanism to tackle cammera disconnecion or temporar unavailabilty
        retries = 10
        while retries:
            js = send_command(url)
            if js == {}:
                print("Successfully set the date and time to %s %s" , date, time)
                return True
            else:
                retries -= 1
                print("Command %s returned the following error: %s", js["command"], js["error"])
        return False
            
    def get_status():
        if self.shutter_mode == Shutter.ON:
            print("Camera shutter is on. While in this state, the camera does not accept any other commands.\n")
            print("Please set shutter off first")
            raise ShutterException

        status = send_command("/status")
        
        shutter = status["is_shutter_on"]
        mode = status["current_mode_id"]
        settings = status["settings"]
        date = status["date"]

        return Status(shutter, mode, settings, date)



class Status:
    def __init__(self, shuter, mode, settings, date):
        self.mode = Mode(mode).name

        self.shutter = Shutter(shutter).name
 
        self.settings = []
        for key, value in settings.items():
            key = int(key)
 
            if key == Setting.RESOLUTION.value:
                self.settings.append(Resolution(value).name)
            elif key == Setting.RATE.value:
                self.settings.append(Rate(value).name)

        
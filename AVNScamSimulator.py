import threading
import time
import random
import katpoint
from katcp import DeviceServer, Sensor, ProtocolFlags


class ScamSimulator(DeviceServer):

    VERSION_INFO = ("scam-simulator-version", 1, 0)
    BUILD_INFO = ("scam-simulator-build", 0, 1, "")

    # Optionally set the KATCP protocol version and features. Defaults to
    # the latest implemented version of KATCP, with all supported optional
    # features
    PROTOCOL_INFO = ProtocolFlags(5, 0, set([
        ProtocolFlags.MULTI_CLIENT,
        ProtocolFlags.MESSAGE_IDS,
    ]))

    def setup_sensors(self):
        # Position sensors
        self._SCM_request_azim = Sensor.float("SCM.request-azim",
                                              "Sky-space requested azimuth position.", "Degrees CW of north")
        self._SCM_request_elev = Sensor.float("SCM.request-elev",
                                              "Sky-space requested elevation position.", "Degrees CW of north")
        self._SCM_desired_azim = Sensor.float("SCM.desired-azim",
                                              "Sky-space desired azimuth position.", "Degrees CW of north")
        self._SCM_desired_elev = Sensor.float("SCM.desired-elev",
                                              "Sky-space desired elevation position.", "Degrees CW of north")
        self._SCM_actual_azim = Sensor.float("SCM.actual-azim",
                                             "Sky-space actual azimuth position.", "Degrees CW of north")
        self._SCM_actual_elev = Sensor.float("SCM.actual-elev",
                                             "Sky-space actual elevation position.", "Degrees CW of north")

        self.add_sensor(self._SCM_request_azim)
        self.add_sensor(self._SCM_request_elev)
        self.add_sensor(self._SCM_desired_azim)
        self.add_sensor(self._SCM_desired_elev)
        self.add_sensor(self._SCM_actual_azim)
        self.add_sensor(self._SCM_actual_elev)

        self.animation_thread = threading.Thread(target=self.sensor_value_thread_function)
        self.animation_thread.start()


    def sensor_value_thread_function(self):
        while True:
            random_az_val = random.random()*360
            self._SCM_request_azim.set_value(random_az_val)

            time.sleep(1)


if __name__ == "__main__":
    server = ScamSimulator("localhost", 1235)
    server.start()

    server.animation_thread.join()
    server.join()


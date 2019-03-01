import threading
import time
import random
import katpoint
import numpy as np
from katcp import DeviceServer, Sensor, ProtocolFlags
import sys

class AVNTarget(katpoint.Target):
    def is_visible(self):
        if self.azel()[0] >= 0.15:  # Somewhat arbitrarily, this is about 8.5 degrees
            return True
        else:
            return False


class ScamSimulator(DeviceServer):

    VERSION_INFO = ("scam-simulator-version", 1, 0)
    BUILD_INFO = ("scam-simulator-build", 0, 1, "")

    # Optionally set the KATCP protocol version and features. Defaults to
    # the latest implemented version of KATCP, with all supported optional
    # features
    PROTOCOL_INFO = ProtocolFlags(4, 0, set([
        ProtocolFlags.MULTI_CLIENT,
        #ProtocolFlags.MESSAGE_IDS,
    ]))

    def setup_sensors(self):
        # Position sensors
        self._SCM_request_azim = Sensor.float("SCM.request-azim", "Sky-space requested azimuth position.", "Degrees CW of north")
        self.add_sensor(self._SCM_request_azim)

        self._SCM_request_elev = Sensor.float("SCM.request-elev", "Sky-space requested elevation position.", "Degrees CW of north")
        self.add_sensor(self._SCM_request_elev)

        self._SCM_desired_azim = Sensor.float("SCM.desired-azim", "Sky-space desired azimuth position.", "Degrees CW of north")
        self.add_sensor(self._SCM_desired_azim)

        self._SCM_desired_elev = Sensor.float("SCM.desired-elev", "Sky-space desired elevation position.", "Degrees CW of north")
        self.add_sensor(self._SCM_desired_elev)

        self._SCM_actual_azim = Sensor.float("SCM.actual-azim", "Sky-space actual azimuth position.", "Degrees CW of north")
        self.add_sensor(self._SCM_actual_azim)

        self._SCM_actual_elev = Sensor.float("SCM.actual-elev", "Sky-space actual elevation position.", "Degrees CW of north")
        self.add_sensor(self._SCM_actual_elev)

        # Pointing model
        self._SCM_pmodel1 = Sensor.float("SCM.pmodel1", "Pointing model parameter 1")
        self.add_sensor(self._SCM_pmodel1)
        self._SCM_pmodel2 = Sensor.float("SCM.pmodel2", "Pointing model parameter 2")
        self.add_sensor(self._SCM_pmodel2)
        self._SCM_pmodel3 = Sensor.float("SCM.pmodel3", "Pointing model parameter 3")
        self.add_sensor(self._SCM_pmodel3)
        self._SCM_pmodel4 = Sensor.float("SCM.pmodel4", "Pointing model parameter 4")
        self.add_sensor(self._SCM_pmodel4)
        self._SCM_pmodel5 = Sensor.float("SCM.pmodel5", "Pointing model parameter 5")
        self.add_sensor(self._SCM_pmodel5)
        self._SCM_pmodel6 = Sensor.float("SCM.pmodel6", "Pointing model parameter 6")
        self.add_sensor(self._SCM_pmodel6)
        self._SCM_pmodel7 = Sensor.float("SCM.pmodel7", "Pointing model parameter 7")
        self.add_sensor(self._SCM_pmodel7)
        self._SCM_pmodel8 = Sensor.float("SCM.pmodel8", "Pointing model parameter 8")
        self.add_sensor(self._SCM_pmodel8)
        self._SCM_pmodel9 = Sensor.float("SCM.pmodel9", "Pointing model parameter 9")
        self.add_sensor(self._SCM_pmodel9)
        self._SCM_pmodel10 = Sensor.float("SCM.pmodel10", "Pointing model parameter 10")
        self.add_sensor(self._SCM_pmodel10)
        self._SCM_pmodel11 = Sensor.float("SCM.pmodel11", "Pointing model parameter 11")
        self.add_sensor(self._SCM_pmodel11)
        self._SCM_pmodel12 = Sensor.float("SCM.pmodel12", "Pointing model parameter 12")
        self.add_sensor(self._SCM_pmodel12)
        self._SCM_pmodel13 = Sensor.float("SCM.pmodel13", "Pointing model parameter 13")
        self.add_sensor(self._SCM_pmodel13)
        self._SCM_pmodel14= Sensor.float("SCM.pmodel14", "Pointing model parameter 14")
        self.add_sensor(self._SCM_pmodel14)
        self._SCM_pmodel15= Sensor.float("SCM.pmodel15", "Pointing model parameter 15")
        self.add_sensor(self._SCM_pmodel15)
        self._SCM_pmodel16 = Sensor.float("SCM.pmodel16", "Pointing model parameter 16")
        self.add_sensor(self._SCM_pmodel16)
        self._SCM_pmodel17 = Sensor.float("SCM.pmodel17", "Pointing model parameter 17")
        self.add_sensor(self._SCM_pmodel17)
        self._SCM_pmodel18 = Sensor.float("SCM.pmodel18", "Pointing model parameter 18")
        self.add_sensor(self._SCM_pmodel18)
        self._SCM_pmodel19 = Sensor.float("SCM.pmodel19", "Pointing model parameter 19")
        self.add_sensor(self._SCM_pmodel19)
        self._SCM_pmodel20 = Sensor.float("SCM.pmodel20", "Pointing model parameter 20")
        self.add_sensor(self._SCM_pmodel20)
        self._SCM_pmodel21 = Sensor.float("SCM.pmodel21", "Pointing model parameter 21")
        self.add_sensor(self._SCM_pmodel21)
        self._SCM_pmodel22 = Sensor.float("SCM.pmodel22", "Pointing model parameter 22")
        self.add_sensor(self._SCM_pmodel22)
        self._SCM_pmodel23 = Sensor.float("SCM.pmodel23", "Pointing model parameter 23")
        self.add_sensor(self._SCM_pmodel23)
        self._SCM_pmodel24 = Sensor.float("SCM.pmodel24", "Pointing model parameter 24")
        self.add_sensor(self._SCM_pmodel24)
        self._SCM_pmodel25 = Sensor.float("SCM.pmodel25", "Pointing model parameter 25")
        self.add_sensor(self._SCM_pmodel25)
        self._SCM_pmodel26 = Sensor.float("SCM.pmodel26", "Pointing model parameter 26")
        self.add_sensor(self._SCM_pmodel26)
        self._SCM_pmodel27 = Sensor.float("SCM.pmodel27", "Pointing model parameter 27")
        self.add_sensor(self._SCM_pmodel27)
        self._SCM_pmodel28 = Sensor.float("SCM.pmodel28", "Pointing model parameter 28")
        self.add_sensor(self._SCM_pmodel28)
        self._SCM_pmodel29 = Sensor.float("SCM.pmodel29", "Pointing model parameter 29")
        self.add_sensor(self._SCM_pmodel29)
        self._SCM_pmodel30 = Sensor.float("SCM.pmodel30", "Pointing model parameter 30")
        self.add_sensor(self._SCM_pmodel30)

        # # Target
        self._SCM_Target = Sensor.string("SCM.Target", "Target description string in katpoint format")
        self.add_sensor(self._SCM_Target)

        # Antenna activity
        self._SCM_Antenna_Activity = Sensor.string("SCM.AntennaActivity", "Antenna activity label")
        self.add_sensor(self._SCM_Antenna_Activity)

        # RF sensor information
        self._SCM_LcpAttenuation = Sensor.float("SCM.LcpAttenuation", "Variable attenuator setting on LCP")
        self.add_sensor(self._SCM_LcpAttenuation)
        self._SCM_RcpAttenuation = Sensor.float("SCM.RcpAttenuation", "Variable attenuator setting on RCP")
        self.add_sensor(self._SCM_RcpAttenuation)
        self._RFC_LcpFreqSel = Sensor.boolean("RFC.LcpFreqSel", "LCP Frequency Select Switch")
        self.add_sensor(self._RFC_LcpFreqSel)
        self._RFC_RcpFreqSel = Sensor.boolean("RFC.RcpFreqSel", "RCP Frequency Select Switch")
        self.add_sensor(self._RFC_RcpFreqSel)
        self._RFC_IntermediateStage_5GHz = Sensor.float("RFC.IntermediateStage_5GHz", "5 GHz Intermediate Stage LO frequency")
        self.add_sensor(self._RFC_IntermediateStage_5GHz)
        self._RFC_IntermediateStage_6_7GHz = Sensor.float("RFC.IntermediateStage_6_7GHz", "6.7 GHz Intermediate Stage LO frequency")
        self.add_sensor(self._RFC_IntermediateStage_6_7GHz)
        self._RFC_FinalStage = Sensor.float("RFC.FinalStage", "Final Stage LO frequency")
        self.add_sensor(self._RFC_FinalStage)

        # Noise diode sensor information
        self._RFC_NoiseDiode_1 = Sensor.integer("RFC.NoiseDiode_1", "All noise diode data (bitfield)")
        self.add_sensor(self._RFC_NoiseDiode_1)

        # EMS information
        self._EMS_WindDirection = Sensor.float("EMS.WindDirection", "Wind direction")
        self.add_sensor(self._EMS_WindDirection)
        self._EMS_WindSpeed = Sensor.float("EMS.WindSpeed", "Wind speed")
        self.add_sensor(self._EMS_WindSpeed)
        self._EMS_AirTemperature = Sensor.float("EMS.AirTemperature", "Air temperature")
        self.add_sensor(self._EMS_AirTemperature)
        self._EMS_AbsolutePressure = Sensor.float("EMS.AbsolutePressure", "Air pressure")
        self.add_sensor(self._EMS_AbsolutePressure)
        self._EMS_RelativeHumidity = Sensor.float("EMS.RelativeHumidity", "Ambient relative humidity")
        self.add_sensor(self._EMS_RelativeHumidity)

        self.animation_thread = threading.Thread(target=self.sensor_value_thread_function)
        self.animation_thread.start()


    def sensor_value_thread_function(self):

        antenna_str = "ant1, 5:45:2.48, -0:18:17.92, 116, 32.0, 0 0 0, %s" % ("0 " * 23)
        antenna = katpoint.Antenna(antenna_str)
        target_str = "name1 | *name 2, radec, 12:34:56.7, -04:34:34.2, (1000.0 2000.0 1.0)"
        self._SCM_Target.set_value(target_str)
        self._SCM_Antenna_Activity.set_value("idle")
        my_target = AVNTarget(target_str, antenna=antenna)

        self._SCM_pmodel1.set_value(random.random())
        self._SCM_pmodel2.set_value(random.random())
        self._SCM_pmodel3.set_value(random.random())
        self._SCM_pmodel4.set_value(random.random())
        self._SCM_pmodel5.set_value(random.random())
        self._SCM_pmodel6.set_value(random.random())
        self._SCM_pmodel7.set_value(random.random())
        self._SCM_pmodel8.set_value(random.random())
        self._SCM_pmodel9.set_value(random.random())
        self._SCM_pmodel10.set_value(random.random())
        self._SCM_pmodel11.set_value(random.random())
        self._SCM_pmodel12.set_value(random.random())
        self._SCM_pmodel13.set_value(random.random())
        self._SCM_pmodel14.set_value(random.random())
        self._SCM_pmodel15.set_value(random.random())
        self._SCM_pmodel16.set_value(random.random())
        self._SCM_pmodel17.set_value(random.random())
        self._SCM_pmodel18.set_value(random.random())
        self._SCM_pmodel19.set_value(random.random())
        self._SCM_pmodel20.set_value(random.random())
        self._SCM_pmodel21.set_value(random.random())
        self._SCM_pmodel22.set_value(random.random())
        self._SCM_pmodel23.set_value(random.random())
        self._SCM_pmodel24.set_value(random.random())
        self._SCM_pmodel25.set_value(random.random())
        self._SCM_pmodel26.set_value(random.random())
        self._SCM_pmodel27.set_value(random.random())
        self._SCM_pmodel28.set_value(random.random())
        self._SCM_pmodel29.set_value(random.random())
        self._SCM_pmodel30.set_value(random.random())

        # There shouldn't be step-changes in the environment data, so set initial values.
        WindDirection = 360*random.random()
        WindSpeed = 50*random.random()
        AirTemperature = 50*random.random()
        AbsolutePressure = 10*random.random() + 1010.0
        RelativeHumidity = 100*random.random()

        while True:
            target_azel = my_target.azel()
            self._SCM_request_azim.set_value(np.degrees(target_azel[0]))
            self._SCM_request_elev.set_value(np.degrees(target_azel[1]))
            self._SCM_desired_azim.set_value(np.trunc(10*self._SCM_request_azim.value())/10)
            self._SCM_desired_elev.set_value(np.trunc(10*self._SCM_request_elev.value())/10)
            self._SCM_actual_azim.set_value(self._SCM_desired_azim.value() + random.random()/25)
            self._SCM_actual_elev.set_value(self._SCM_desired_elev.value() + random.random()/25)

            if random.random() > 0.5:
                coin_toss = int(4*random.random())
                if coin_toss == 0:
                    self._SCM_Antenna_Activity.set_value("idle")
                elif coin_toss == 1:
                    self._SCM_Antenna_Activity.set_value("slew")
                elif coin_toss == 2:
                    self._SCM_Antenna_Activity.set_value("track")
                elif coin_toss == 3:
                    self._SCM_Antenna_Activity.set_value("scan")
                else:
                    self._SCM_Antenna_Activity.set_value("stop")  # Shouldn't happen, but for logical completeness...

            attenuation = float(random.randint(0, 63))/2
            self._SCM_LcpAttenuation.set_value(attenuation)
            self._SCM_RcpAttenuation.set_value(attenuation)

            # Frequency band doesn't need to be changed as frequently as the other stuff.
            if random.random() > 0.925:
                freq_sel = bool(random.randint(0, 1))
                self._RFC_LcpFreqSel.set_value(freq_sel)
                self._RFC_RcpFreqSel.set_value(freq_sel)
                self._RFC_IntermediateStage_5GHz.set_value(50e6*random.random() + 1.5e9)
                self._RFC_IntermediateStage_6_7GHz.set_value(50e6*random.random() + 3.2e9)
                self._RFC_FinalStage.set_value(50e6*random.random() + 2.85e9)

            # Noise diode info also doesn't need to change every tick.
            if random.random() > 0.6:
                input_source = random.randint(0, 3)
                bit_2 = 0
                enable = random.randint(0, 1)
                noise_diode_select = random.randint(1, 15)  # Not actually sure if this is supposed to be one-hot
                pwm_mark = random.randint(0, 63)
                freq_sel = random.randint(0, 3)
                bitfield = input_source + bit_2*2**2 + enable*2**3 + noise_diode_select*2**4 + pwm_mark*2**8\
                           + freq_sel*2**14
                self._RFC_NoiseDiode_1.set_value(bitfield)

            # Climate information only needs to change occasionally too
            if random.random() > 0.35:
                WindDirection += 2*random.random() - 1
                self._EMS_WindDirection.set_value(WindDirection)
                WindSpeed += random.random() - 0.5
                self._EMS_WindSpeed.set_value(WindSpeed)
                AirTemperature += 0.5*random.random() - 0.25
                self._EMS_AirTemperature.set_value(AirTemperature)
                AbsolutePressure += 0.1*random.random() - 0.05
                self._EMS_AbsolutePressure.set_value(AbsolutePressure)
                RelativeHumidity += 0.1*random.random() - 0.05
                self._EMS_RelativeHumidity.set_value(RelativeHumidity)

            print "\n\nSensors as at {}".format(time.time())
            print "============================================"
            for element_name in iter(dir(self)):
                element = getattr(self, element_name)
                #print "\nElement: {}".format(element)
                #print "Type: {}".format(type(element))
                #print "Isinstance: {}".format(isinstance(element, Sensor))
                if isinstance(element, Sensor):
                    print "{} {} {}".format(element._timestamp, element.name, element._value)
            sys.stdout.flush()
            time.sleep(random.random()*4 + 1)



if __name__ == "__main__":
    server = ScamSimulator("", 1235)
    server.start()

    server.animation_thread.join()
    server.join()


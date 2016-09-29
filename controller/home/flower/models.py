from django.db import models
import socket,logging
# Create your models here.


class Sensor(models.Model):
    timestamp = models.DateTimeField(auto_now_add=True)
    env_light = models.IntegerField()
    env_humid = models.IntegerField()
    env_raindrop = models.IntegerField()
    env_temperature = models.IntegerField()
    soi_humid = models.IntegerField()
    soi_fatness = models.IntegerField()
    soi_temperature = models.IntegerField()
    valve_flow = models.IntegerField()
    valve_span = models.IntegerField()

    @staticmethod
    def valve(seconds):
        seconds = seconds if 0 <= seconds <= 10 else 2
        conn = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        conn.connect(("192.168.33.58", 80))
        conn.send("ST,%d" % seconds)
        content = conn.recv(10240)
        if content and content.find("&") > 0:
            data = {k: v for k, v in [tuple(i.split('=')) for i in content.split("&")]}
            sensor = Sensor()
            sensor.env_light = data['env_light']
            sensor.env_humid = data['env_humid']
            sensor.env_raindrop = data['env_raindrop']
            sensor.env_temperature = data['env_temperature']
            sensor.soi_humid = data['humi_aval']
            sensor.soi_fatness = data['soil_fatness']
            sensor.soi_temperature = data['soil_temperature']
            sensor.valve_flow = data['valve_flow']
            sensor.valve_span = data['relay_total_seconds']
            sensor.save()
            return True
        else:
            logging.warning("error sensor data %s." % content)
            return False



class Daily(models.Model):
    date = models.DateField(auto_now_add=True)
    env_light = models.IntegerField()
    env_humid = models.IntegerField()
    env_raindrop = models.IntegerField()
    env_temperature = models.IntegerField()
    soi_humid = models.IntegerField()
    soi_fatness = models.IntegerField()
    soi_temperature = models.IntegerField()
    valve_flow = models.IntegerField()
    valve_span = models.IntegerField()

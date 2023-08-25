# wifi-sensor/src/__init__.py
from viam.components.sensor import Sensor
from viam.resource.registry import Registry, ResourceCreatorRegistration
from .twilio_sms import twilio_sms


# Registry.register_resource_creator(Sensor.SUBTYPE, MySensor.MODEL, ResourceCreatorRegistration(MySensor.new))
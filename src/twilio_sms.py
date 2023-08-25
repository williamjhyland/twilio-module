import asyncio

from typing import Any, ClassVar, Dict, Mapping, Optional, Sequence, Tuple
from typing_extensions import Self

from viam.components.generic import Generic
from viam.proto.app.robot import ComponentConfig
from viam.proto.common import ResourceName
from viam.resource.base import ResourceBase
from viam.resource.types import Model, ModelFamily
from viam.utils import ValueTypes

from twilio.rest import Client


class twilio_sms(Generic):
    # Subclass the Viam Sensor component and implement the required functions
    MODEL: ClassVar[Model] = Model(ModelFamily("viamlabs","twilio"), "sms")

    @classmethod
    def new(cls, config: ComponentConfig, dependencies: Mapping[ResourceName, ResourceBase]) -> Self:
        messenger = cls(config.name)
        messenger.auth_token = None
        messenger.account_sid = None
        messenger.recipient_phone = None
        messenger.deliverer_phone = None
        messenger.reconfigure(config, dependencies)
        return messenger

    @classmethod
    def validate_config(cls, config: ComponentConfig) -> Sequence[str]:
        auth_token = config.attributes.fields['auth_token'].string_value
        if auth_token == '':
            raise Exception('auth_token required')
        
        account_sid = config.attributes.fields['account_sid'].string_value
        if account_sid == '':
            raise Exception('account_sid required')
        
        recipient_phone = config.attributes.fields['recipient_phone'].string_value
        if recipient_phone == '':
            raise Exception('recipient_phone required')
        
        deliverer_phone = config.attributes.fields['deliverer_phone'].string_value
        if recipient_phone == '':
            raise Exception('deliverer_phone required')
        return []

    def reconfigure(self, config: ComponentConfig, dependencies: Mapping[ResourceName, ResourceBase]):
        self.auth_token = config.attributes.fields['auth_token'].string_value
        self.account_sid = config.attributes.fields['account_sid'].string_value
        self.recipient_phone = config.attributes.fields['recipient_phone'].string_value
        self.deliverer_phone = config.attributes.fields['deliverer_phone'].string_value

    async def do_command(
            self,
            command: Mapping[str, ValueTypes],
            *,
            timeout: Optional[float] = None,
            **kwargs
    ):
        client = Client(self.account_sid, self.auth_token)

        message = client.messages.create(
            from_= self.deliverer_phone,
            to = self.recipient_phone,
            body = command["body"] 
        )
            
import hashlib
import re

from cs_qualif_step2.core.domain.device.device import Device
from cs_qualif_step2.core.domain.device.device_id import DeviceId
from cs_qualif_step2.core.domain.device.exception.Invalid_firmware_version import InvalidFirmwareVersion
from cs_qualif_step2.core.domain.device.exception.Invalid_location import InvalidLocation
from cs_qualif_step2.core.domain.device.exception.invalid_mac_adress import InvalidMacAddress
from cs_qualif_step2.core.application.dto.device_config import DeviceConfig
from cs_qualif_step2.core.domain.device.exception.invalid_timezone import InvalidTimezone


class DeviceFactory:
    def create_device(self, device_config: DeviceConfig) -> Device:
        if not re.match(r'^([0-9A-Fa-f]{2}:){5}[0-9A-Fa-f]{2}$', device_config.macAddress):
            raise InvalidMacAddress("Invalid MAC address format")

        if not re.match(r'\d+.\d+.\d+', device_config.firmwareVersion):
            raise InvalidFirmwareVersion("Invalid Firmware format")

        if not re.match(r'\D+, \D+', device_config.location):
            raise InvalidLocation("Invalid Location format")

        if not re.match(r'\D+\/\D+', device_config.timezone):
            raise InvalidTimezone("Invalid Timezone format")

        device_id = DeviceId.generate()

        return Device(
            device_id=device_id,
            macAddress=device_config.macAddress,
            model=device_config.model,
            firmwareVersion=device_config.firmwareVersion,
            serialNumber=device_config.serialNumber,
            displayName=device_config.displayName,
            location=device_config.location,
            timezone=device_config.timezone
        )

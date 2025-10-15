from __future__ import annotations

from abc import ABC, abstractmethod

from cs_qualif_step2.core.domain.device.device import Device

class DeviceRepository(ABC):
    @abstractmethod
    def find_by_mac_address(self, mac_address: str) -> Device | None:
        pass

    @abstractmethod
    def find_by_id(self, device_id: str) -> Device | None:
        pass

    @abstractmethod
    def save(self, device: Device):
        pass

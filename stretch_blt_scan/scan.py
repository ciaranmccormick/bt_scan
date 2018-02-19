import bluetooth
import logging
from bluetooth.ble import DiscoveryService

logger = logging.getLogger(__name__)


def perform_scan():
        devices = bluetooth.discover_devices(lookup_names=True)
        return devices


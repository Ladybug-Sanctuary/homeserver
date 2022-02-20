from django.db import models


class Device(models.Model):
    ip_address = models.CharField(
        "IP Address",
        max_length=15, # 4 three-digit numbers + 3 separators (.)
    )
    mac_address = models.CharField(
        "MAC Address",
        max_length=17,  # 6 hex-pairs + 5 separators (:)
    )

    class Meta:
        constraints = [
            models.UniqueConstraint(
                fields=['ip_address', 'mac_address'],
                name='unique_device_address',
            ),
        ]

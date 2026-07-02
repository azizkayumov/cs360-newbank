from django.db import models
from django.contrib.auth.models import User


class ExchangeHistory(models.Model):
    user = models.ForeignKey(
        User,
        on_delete=models.CASCADE
    )

    from_currency = models.CharField(max_length=10)
    to_currency = models.CharField(max_length=10)

    amount = models.DecimalField(
        max_digits=12,
        decimal_places=2
    )

    exchange_rate = models.DecimalField(
        max_digits=12,
        decimal_places=4
    )

    converted_amount = models.DecimalField(
        max_digits=12,
        decimal_places=2
    )

    created_at = models.DateTimeField(
        auto_now_add=True
    )

    def __str__(self):
        return (
            f"{self.user.username}: "
            f"{self.from_currency} → "
            f"{self.to_currency}"
        )
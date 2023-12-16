from django.db import models

actions = [
    ("betterWorld", "Better World"),
    ("betterPlace", "Better Place"),
    ("betterCompany", "Better Company"),
    ("betterProfit", "Better Profit"),
]


class EnvironmentAction(models.Model):
    name = models.CharField(max_length=200)
    action_start = models.DateField()
    action_end = models.DateField(blank=True, null=True)
    has_person_in_charge = models.BooleanField(default=False)
    has_goals = models.BooleanField(default=False)
    needs_carbon_footprint_calculation = models.BooleanField(default=False)
    is_legal_duty = models.BooleanField(default=False)
    action_type = models.CharField(max_length=100, choices=actions)

    def __str__(self) -> str:
        return f"{self.name}, Type: {self.action_type}"

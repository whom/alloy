from django.db import models
from django.core.exceptions import ValidationError
from django.utils.translation import gettext_lazy as _
from datetime import datetime


def validate_country(v):
  if v.lower() != "us":
    raise ValidationError(
      _(f"App is only supported in the US!"),
      params={'value': v},
    )

def validate_dob(v):
  try:
    date = datetime.strptime(v, "%Y-%m-%d")
  except ValueError:
    raise ValidationError(
      _(f"Unexpected date of birth format; please enter as YYYY-MM-DD!"),
      params={"value": v}
    )

def validate_zip_code(v):
  if len(v) != 5 or not v.isnumeric():
    raise ValidationError(
      _(f"Zip code must be 5 numeric characters!"),
      params={'value': v},
    )

def validate_state(v):
  valid_state_abbreviations = [
    "AL","AK","AS","AZ","AR","CA","CO","CT","DE","DC",
    "FL","GA","GU","HI","ID","IL","IN","IA","KS","KY",
    "LA","ME","MD","MA","MI","MN","MS","MO","MT","NE",
    "NV","NH","NJ","NM","NY","NC","ND","MP","OH","OK",
    "OR","PA","PR","RI","SC","SD","TN","TX","UT","VT",
    "VA","VI","WA","WV","WI","WY"
  ]

  if len(v) != 2 or v.upper() not in valid_state_abbreviations:
    raise ValidationError(
      _(f"State must be a valid 2-letter abbreviation!"),
      params={'value': v},
    )

def validate_ssn(v):
  if len(v) != 9 or not v.isnumeric():
    raise ValidationError(
      _(f"SSN must be 9 numeric characters!"),
      params={'value': v},
    )


class SignupForm(models.Model):
  first_name = models.TextField(max_length=128)
  last_name = models.TextField(max_length=128)

  address_1 = models.TextField(max_length=128)
  address_2 = models.TextField(max_length=128, null=True, blank=True)
  city = models.TextField(max_length=128)
  state = models.TextField(max_length=2, validators=[validate_state])
  zip_code = models.TextField(max_length=5, validators=[validate_zip_code])
  country = models.TextField(max_length=128, validators=[validate_country])

  ssn = models.TextField(max_length=9, validators=[validate_ssn])
  email_address = models.TextField(max_length=128)
  phone_number = models.TextField(max_length=10)
  dob = models.TextField(max_length=10, validators=[validate_dob])
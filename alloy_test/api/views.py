from django.http import HttpResponseRedirect
from django.shortcuts import render
import requests

from .form import SignupFormForm

URL = "https://sandbox.alloy.co/v1/evaluations"

OUTCOME_TO_TEXT = {
  "Approved": "Success! \U0001F389\U0001F389\U0001F389",
  "Deny": "Sorry, your application was not successful",
  "Manual Review": "Thanks for submitting your application, we’ll be in touch shortly"
}

def index(request):
    if request.method == 'POST':
      form = SignupFormForm(request.POST)
      if form.is_valid():
        headers = {
          "Content-Type": "application/json"
        }

        data = {
          "phone_number": form.cleaned_data["phone_number"],
          "name_first": form.cleaned_data["first_name"],
          "name_last": form.cleaned_data["last_name"],
          "email_address": form.cleaned_data["email_address"],
          "birth_date": form.cleaned_data["dob"],
          "address_line_1": form.cleaned_data["address_1"],
          "address_line_2": form.cleaned_data["address_2"],
          "address_city": form.cleaned_data["city"],
          "address_state": form.cleaned_data["state"],
          "document_ssn": form.cleaned_data["ssn"],
          "address_postal_code": form.cleaned_data["zip_code"],
          "address_country_code": form.cleaned_data["country"],
        }
        auth_token = ""

        # response = requests.post(
        #     url=URL,
        #     headers=headers,
        #     json=data,
        #     auth=auth_token
        # )

        response = {
          "summary": {
            "outcome": "Deny"
          }
        }

        if response:
          api_outcome = response["summary"]["outcome"]
          api_response = OUTCOME_TO_TEXT[api_outcome]
          print(api_response)
        else:
          api_response = "Oops! Something went wrong."

      else:
        api_response = None

    else:
        form = SignupFormForm()
        api_response = None

    context = {
      "form": form,
    }
    if api_response:
      context["api_response"] = api_response

    return render(request, 'index.html', context)
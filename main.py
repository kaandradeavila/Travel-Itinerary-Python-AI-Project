import requests
from rich import print
from rich.markdown import Markdown


def generate_travel_itinerary(origin, destination, duration):
  print("In Progress...")

# Get user input (origin, destination, duration)
origin = input("What city does your trip start from? ").strip()
destination = input("What city are you going to? ").strip()
duration = input("How many days will your trip last? (Enter a number only, i.e 5) ").strip()

# Validating user input
if origin and destination and duration.isdigit():
  print("Calculating itinirary...")
else:
  print("Please try again. Make sure to enter valid information.")

# Call the SheCodes AI API (to get itinerary)


# Display the itinerary


# Call the Weather API


# Call the SheCodes Weather API


# Display the weather in the origin and destination


# Final touches (add credit, few improvements, potential)


print("Hello World")
import requests
from rich import print
from rich.markdown import Markdown


def generate_travel_itinerary(origin, destination, duration):
  # Generates a travel itinerary between 2 different places using AI
  print(f"\n\nGenerating itinerary from {origin} to {destination}...\n")
  ai_api_key = "424369doa037d0347bft3cfcc8cef956"
  ai_context = "You are a renowned travel specialist who knows the best tourist spots around the world!"
  ai_prompt = f"Generate a travel itinerary from {origin} to {destination} in {duration} days. This is a road, keep it short, less than 15 lines. Add some emojis to make it more readable, but no more than 5 emojis. Add an estimated price for each day in American dollars. Thanks!"
  ai_api_url = f"https://api.shecodes.io/ai/v1/generate?prompt={ai_prompt}&context={ai_context}&key={ai_api_key}"

  response = requests.get(ai_api_url)
  response_data = response.json()
  itinerary = Markdown(response_data['answer'])

  print(itinerary)

# Get user input (origin, destination, duration)
origin = input("What city does your trip start from? ").strip()
destination = input("What city are you going to? ").strip()
duration = input("How many days will your trip last? (Enter a number only, i.e 5) ").strip()

# Validating user input
if origin and destination and duration.isdigit():
  generate_travel_itinerary(origin, destination, duration)
else:
  print("Please try again. Make sure to enter valid information.")

# Call the Weather API


# Call the SheCodes Weather API


# Display the weather in the origin and destination


# Final touches (add credit, few improvements, potential)

import requests
from rich import print
from rich.markdown import Markdown


def display_current_weather(location):
  """Gets real time temperature and condition in a location"""
  weather_api_key = "424369doa037d0347bft3cfcc8cef956"
  wether_api_url = f"https://api.shecodes.io/weather/v1/current?query={location}&key={weather_api_key}&units=imperial"

  response = requests.get(wether_api_url)
  response_data = response.json()

  temperature = round(response_data['temperature']['current'])
  condition = response_data['condition']['description']

  print(f"\nThe current temperature in [bold blue]{location}[/bold blue] is: [bold]{temperature}°F[/bold], [green]{condition}[/green]/n")


def generate_travel_itinerary(origin, destination, duration, currency):
  """ Generates a travel itinerary between 2 different places using AI """
  print(f"\n\nGenerating itinerary from {origin} to {destination}...\n")
  ai_api_key = "424369doa037d0347bft3cfcc8cef956"
  ai_context = "You are a renowned travel specialist who knows the best tourist spots around the world!"
  ai_prompt = f"Generate a travel itinerary from {origin} to {destination} in {duration} days. This is a road, keep it short, less than 15 lines. Add some emojis to make it more readable. Add a main title to the itinerary and divide each day with a line. Add an estimated price for each day in {currency}. Thanks!"
  ai_api_url = f"https://api.shecodes.io/ai/v1/generate?prompt={ai_prompt}&context={ai_context}&key={ai_api_key}"

  response = requests.get(ai_api_url)
  response_data = response.json()
  itinerary = Markdown(response_data['answer'])

  print(itinerary)


def welcome():
  print("[bold magenta]Welcome to the AI Travel Itinerary Planner[/bold magenta]")


def credit():
  print("[bold magenta]The AI Travel Itinerary was built by [yellow]Kyrenia Ailen Andrade Avila[/yellow]. Thank you for using this tool ❤️[/bold magenta]")

welcome()

# Get user input (origin, destination, duration)
origin = input("What city does your trip start from? ").strip()
destination = input("What city are you going to? ").strip()
duration = input("How many days will your trip last? (Enter a number only, i.e 5) ").strip()
currency = input("What currency do you use (i.e. euro, dollar...)? ")

# Validating user input
if origin and destination and duration.isdigit() and currency:
  display_current_weather(origin)
  display_current_weather(destination)
  generate_travel_itinerary(origin, destination, duration, currency)
  credit()
else:
  print("Please try again. Make sure to enter valid information.")
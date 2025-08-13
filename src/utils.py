import numpy as np
import pandas as pd
import re

def extract_coordinates(geocoded_city):
  '''
  Extract only the coordinate number values from a geocoded city value
  '''
  # Look for patterns that start with ( and end with )
  match = re.search(r"\(([+-]?[0-9.]+,\s*[+-]?[0-9.]+)\)", str(geocoded_city)) # Capture only the number coordinates between the parentheses
  return match.group(1) if match else np.nan # Return only the coordinates; if the pattern is not found, return NaN

def cost_prediction(route_df, year):
  '''
  Predict the cost of a flight route based on distance and year
  '''
  base_cost_per_mile = 0.17507 # Based on year 2019
  annual_inflation_rate = 0.05
  costs = route_df["distance"] * base_cost_per_mile * np.power(1 + annual_inflation_rate, year - 2019)
  return costs

def get_route_coefficients(route, fare_model):
  '''
  Get fare coefficients for a route, using averages if route not found
  '''
  if route in fare_model:
    return fare_model[route]
  else:
    fare_df = pd.DataFrame.from_dict(fare_model, orient="index")
    avg_a = fare_df["a"].mean()
    avg_b = fare_df["b"].mean()
    avg_y = fare_df["y"].mean()
    return {"a": avg_a, "b": avg_b, "y": avg_y}
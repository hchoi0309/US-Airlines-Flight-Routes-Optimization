import numpy as np
import pandas as pd
import re

# Convert the values to be either NaN or only contain coordinates
def extract_coordinates(geocoded_city):
  # Look for patterns that start with ( and end with )
  match = re.search(r"\(([+-]?[0-9.]+,\s*[+-]?[0-9.]+)\)", str(geocoded_city)) # Capture only the number coordinates between the parentheses
  return match.group(1) if match else np.nan # Return only the coordinates; if the pattern is not found, return NaN
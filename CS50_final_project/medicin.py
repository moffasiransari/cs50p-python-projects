# all codes related to medicine
from pydantic import BaseModel, ValidationError, ConfigDict
import csv
import json
from google.api_core import exceptions as google_exceptions


class Generic(BaseModel):
    model_config = ConfigDict(extra="forbid") #will not except any extra values
    branded_name: str
    generic_name: str
    composition: list[str]
    dosage: str
    req_doctor_prescription: bool
    branded_med_price: float
    generic_med_price: float
    savings: float
    safety_notes: str


def main(): ...


# #getting generic name from the database
# def get_generic_name(brand_name = None):
#     if brand_name is not None:
#         #opening the database file
#         try:
#             with open("database.csv","r") as database:
#                 reader:list =  csv.DictReader(database,fieldnames=["brand_name","generic_name"])
#                 for i in reader:
#                     i:dict
#                     # brand_name_file:str = i["brand_name"]
#                     if i["brand_name"].lower() == brand_name:
#                         return i["generic_name"]
#         except FileNotFoundError:
#             return "File not found"
#     else: return "No input"


def api_exception(func):
    """Decorator to handle all API-related exceptions"""

    def wrapper(*args, **kwargs):
        try:
            return func(*args, **kwargs)
        except google_exceptions.Unauthenticated:
            print("ERROR: Invalid or expired API key")
            return None
        except google_exceptions.PermissionDenied:
            print("ERROR: API key lacks required permissions")
            return None
        except google_exceptions.ResourceExhausted:
            print("ERROR: Rate limit exceeded or quota exhausted")
            return None
        except google_exceptions.GoogleAPIError as e:
            print(f"ERROR: Google API Error - {e}")
            return None
        except ConnectionError:
            print("ERROR: Network connection failed - check internet connection")
            return None
        except TimeoutError:
            print("ERROR: API request timed out - try again later")
            return None
        except ValidationError as e:
            print(f"ERROR: Response validation failed - {e}")
            return None
        except json.JSONDecodeError:
            print("ERROR: Invalid JSON response from API")
            return None
        except AttributeError as e:
            print(f"ERROR: Unexpected response format - {e}")
            return None
        except TypeError as e:
            print(f"ERROR: Type error in response handling - {e}")
            return None
        except ValueError as e:
            print(f"ERROR: Invalid value in API response - {e}")
            return None
        except Exception as e:
            print(f"ERROR: Unexpected exception - {type(e).__name__}: {e}")
            return None

    return wrapper


if __name__ == "__main__":
    main()

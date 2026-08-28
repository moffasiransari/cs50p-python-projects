"""MEDSAVER"""

# %%
from google import genai
from medicin import Generic, api_exception
import sys
from report import generate_terminal_report, generate_pdf_report, history_saver
from datetime import datetime

def main():
    brand_name = input("Enter the Medicine Brand name: ").lower().strip()

    # getting api response
    med_info: list = api_response(brand_name)
    #validating med_info
    if med_info == "No input":
        sys.exit("No input")
    elif med_info is None:
        sys.exit("Failed to retrieve medicine information/Medicine not found")

    search_time = datetime.now()

    # generating report
    generate_terminal_report(med_info)
    generate_pdf_report(med_info, search_time)

    #saving history
    history_saver(med_info, search_time)


@api_exception  # decorator to handle all API-related exceptions
def api_response(brand_name: str = None):
    if brand_name != None:
        api_key = "AIzaSyAOnb_B1NJ1RIWgSltg_fM7_KcpJKhUUOQ"
        client = genai.Client(api_key=api_key)

        # getting reponse
        # returns a generatecontentresponse object
        response = client.models.generate_content(
            model="gemini-2.5-flash",
            contents="You are an medicine/drugs api specifically for indian medicines/drugs. "
            "You take the branded name of the drug as input and strictly only outputs its"
            "same branded medicine name,generic medicine name and alternative,composition,dosage,doctor prescription req or not"
            "brander med price,generic med price,how much will he save on it from branded medicine,and saftey notes "
            f"brand name = {brand_name}",
            config={
                "response_mime_type": "application/json",
                "response_schema": list[
                    Generic
                ],  # returns list of multiple alternative drugs
            },
        )

        # parsing data
        parsed_data = response.parsed

        # for med in parsed_data:
        #     #printing values
        #     print(med)
        return parsed_data
    else:
        return  "No input"


# had to use gemini as i could not find any free medicin/drug related api specifically for indian medicines brands
# as it was my first project , i tried to keep it simple ,
# i am well aware of the inconsistency in price that these AI's api have
# %%
if __name__ == "__main__":
    main()

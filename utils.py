import requests
from bs4 import BeautifulSoup




def get_owner_name(parcel_id):
    URL_TEMPLATE = 'http://www2.county.allegheny.pa.us/RealEstate/GeneralInfo.aspx?ParcelID='
    print(parcel_id)
    owner_name = ''
    r = requests.get(URL_TEMPLATE+parcel_id);
    try:
        if (r.ok):
            soup = BeautifulSoup(r.text, 'html.parser')
            thing = soup.find_all(id='BasicInfo1_lblOwner')
            owner_name = ' '.join(thing[0].text.split())

    finally:
        return owner_name

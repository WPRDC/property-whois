# Propety Whois
Programmatically find the name of a parcel's owner!

This software uses the python library [Beautiful soup](https://www.crummy.com/software/BeautifulSoup/).  
You can find instructions on how to install it and other documentation on the project [homepage](https://www.crummy.com/software/BeautifulSoup/).

## How To
Request:  
`GET https://tools.wprdc.org/property_whois/whois/<parcel_id>`  
Response:  
```json
{ 
  "name": <the_owners_name>, 
  "success": <true|false> 
} 
```  

## Example
Request:  
`GET https://tools.wprdc.org/property_whois/whois/0028F00194000000/`  
Response:  
```json
{ 
  "name": "UNIVERSITY OF PITTSBURGH OF THE COMMONWEALTH SYSTEM OF HIGHER EDUCATION", 
  "success": true 
}
```  


from urllib2 import Request, urlopen

values = """
  {
    "image": "https://media.licdn.com/mpr/mpr/shrinknp_200_200/AAIA_wDGAAAAAQAAAAAAAA2TAAAAJDViZTIwZGVjLTBhOGYtNGNhYi1hY2U1LTIwODEwYzE0OWJjMQ.jpg",
    "gallery_name": "MyGallery"
  }
"""

headers = {
  'Content-Type': 'application/json',
  'app_id': '9180abf6',
  'app_key': 'b554aa700d5fc902c9ed825b02c99654'
}
request = Request('https://api.kairos.com/recognize', data=values, headers=headers)

response_body = urlopen(request).read()
print response_body

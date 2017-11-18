
from urllib2 import Request, urlopen

values = """
  {
    "image": "https://media.licdn.com/mpr/mpr/shrinknp_200_200/AAIA_wDGAAAAAQAAAAAAAA2TAAAAJDViZTIwZGVjLTBhOGYtNGNhYi1hY2U1LTIwODEwYzE0OWJjMQ.jpg",
    "gallery_name": "MyGallery"
  }
"""

headers = {
  'Content-Type': 'application/json',
  'app_id': 'app id ',
  'app_key': 'app key'
}
request = Request('https://api.kairos.com/recognize', data=values, headers=headers)

response_body = urlopen(request).read()
print response_body

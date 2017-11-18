from urllib2 import Request, urlopen

values = """
  {
    "image": "https://avatars3.githubusercontent.com/u/8552914?s=460&v=4", 
    "subject_id": "Ashutoshh Singh",
    "gallery_name": "MyGallery"
  }
"""

headers = {
  'Content-Type': 'application/json',
  'app_id': '9180abf6',
  'app_key': 'b554aa700d5fc902c9ed825b02c99654'
}
request = Request('https://api.kairos.com/enroll', data=values, headers=headers)

response_body = urlopen(request).read()
print response_body

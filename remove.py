from urllib2 import Request, urlopen

values = """
  {
    "gallery_name": "MyGallery",
    "subject_id": "Ashutoshh Singh"
  }
"""

headers = {
  'Content-Type': 'application/json',
  'app_id': '9180abf6',
  'app_key': 'b554aa700d5fc902c9ed825b02c99654'
}
request = Request('https://api.kairos.com/gallery/remove_subject', data=values, headers=headers)

response_body = urlopen(request).read()
print response_body

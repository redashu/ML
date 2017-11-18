from urllib2 import Request, urlopen

values = """
  {
    "gallery_name": "MyGallery",
    "subject_id": "Ashutoshh Singh"
  }
"""

headers = {
  'Content-Type': 'application/json',
  'app_id': 'app id',
  'app_key': 'app key id '
}
request = Request('https://api.kairos.com/gallery/remove_subject', data=values, headers=headers)

response_body = urlopen(request).read()
print response_body

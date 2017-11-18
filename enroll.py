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
  'app_id': 'your app id from karios',
  'app_key': 'your app key from kairos '
}
request = Request('https://api.kairos.com/enroll', data=values, headers=headers)

response_body = urlopen(request).read()
print response_body

import json
import requests
import webbrowser
import codecs

consumer_key = 'YOUR POCKET CONSUMER KEY HERE'

URLs = {'request': 'https://getpocket.com/v3/oauth/request',
        'authorize_usr': 'https://getpocket.com/auth/authorize',
        'authorize_app': 'https://getpocket.com/v3/oauth/authorize',
        'get': 'https://getpocket.com/v3/get'}
headers = {'content-type': 'application/json', 'x-accept': 'application/json'}


def retrieve(tag):
   data = json.dumps({'consumer_key': consumer_key, 'redirect_uri': 'http://localhost'})
   r = requests.post(URLs['request'], headers=headers, data=data)
   data = json.loads(r.text)
   data = {'consumer_key': consumer_key, 'code': data['code']}

   url = '%s?request_token=%s&redirect_uri=http://localhost' % (URLs['authorize_usr'], data['code'])
   webbrowser.open(url, new=2, autoraise=False)
   raw_input('Press ENTER when you\'re done...\n')

   data = json.dumps(data)
   r = requests.post(URLs['authorize_app'], headers=headers, data=data)
   data = json.loads(r.text)
   data = json.dumps({'consumer_key': consumer_key, 'access_token': data['access_token'], 'tag': tag, 'state': 'all'})
   r = requests.post(URLs['get'], headers=headers, data=data)

   return json.loads(r.text)['list'].values()


inp_f = codecs.open('tags.txt', 'r', 'utf-8')
out_f = codecs.open('Pocket Backup.html', 'w', 'utf-8')
tags = [t for t in inp_f.read().split('\n') if t] + ['_untagged_']

out_f.write("""
<!DOCTYPE html>
<html>
   <!--So long and thanks for all the fish-->
   <head>
      <meta http-equiv="Content-Type" content="text/html; charset=UTF-8" />
      <title>Pocket Export</title>
   </head>
   <body>
""")
for tag in tags:
   out_f.write('      <h1>%s:</h1>\n         <ul>\n' % tag)
   for item in retrieve(tag):
      if item['resolved_title']:
         title = item['resolved_title']
      else:
         title = item['given_title']
      if item['resolved_url']:
         url = item['resolved_url']
      else:
         url = item['given_url']
      if not title:
          title = url
      out_f.write('           <li><a href="%s">%s</a></li>\n' % (url, title))
   out_f.write('         </ul>\n')
out_f.write('   <body>\n</html>')

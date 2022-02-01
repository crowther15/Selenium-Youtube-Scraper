response = requests.get (YOUTUBE_TRENDING_URL)
print ('Status Code:', response.status_code )
print ('output', response.text[:1000])

with open ('trending.html', 'w') as f: f.write (response.text)

doc = BeautifulSoup (response.text, 'html.parser')

print ('page title:', doc.title.text)

# Find all the videos divs

video_divs = doc.find_all ('div', class_ = 'ytd-video-renderer')

print (f'Found {len (video_divs)} videos')
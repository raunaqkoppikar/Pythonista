from bs4 import BeautifulSoup
import requests

# Count the number of views for all videos on first page of youtube for given keyword

# Get the keyword as an input from the end user
keyword = input("Enter your keyword:")

# Get the YouTube URL on the basis of the keyword
url = 'https://www.youtube.com/results?search_query='+keyword

# Get the resulting HTML page from the URL
response = requests.get(url)

# Create a Beautiful Soup object from the resulting HTML text
bsObj = BeautifulSoup(response.text, 'lxml')

# Get the total and average number of views for all videos associated with the keyword
totalViews = 0
numberOfVideos = 0
ul_list = bsObj.find_all('ul', class_ = 'yt-lockup-meta-info')
for ul in ul_list:
    lis = ul.findChildren()
    for li in lis:
        if li.string.endswith('views'):
            numberOfVideos = numberOfVideos + 1
            temp = li.getText()
            temp = temp.replace(' views', '').replace(',', '')
            totalViews = totalViews + int(temp)
print("Total Views: " + str(totalViews))
print("Average number of Views: " + str(round(totalViews/numberOfVideos)))
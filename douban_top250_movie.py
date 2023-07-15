import requests
from bs4 import BeautifulSoup

#pretend as a browser to avoid HTTP response status code [418]
headers = {
    "User-Agent":"Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/114.0.0.0 Safari/537.36"
}

#Every page contains 25 movies. Use a for-loop to get all 250 movies
for start_index in range(0, 250, 25):
    response = requests.get(f"https://movie.douban.com/top250?start={start_index}", headers = headers)
    top_movie = response.text
    soup = BeautifulSoup(top_movie, "html.parser")
    all_titles = soup.findAll("span", attrs = {"class":"title"})

    #print every movie in Chinese name
    for title in all_titles:
        title_string = title.string
        
        #delete English name
        if "/" not in title_string:
            print(title_string)





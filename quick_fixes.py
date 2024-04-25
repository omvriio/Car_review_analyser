import requests
from bs4 import BeautifulSoup
from IPython.display import Video
import webbrowser
import csv
import pandas as pd

# URL of the website to scrape
url = "https://fr.carcarekiosk.com/videos/BMW/320i/2014"

# Send a GET request to the website
response = requests.get(url)


# Create a BeautifulSoup object to parse the HTML content
soup = BeautifulSoup(response.content, "html.parser")

# Find all the video elements on the page
video_elements = soup.find_all("video")
# Find all the list-group elements on the page
list_group_elements = soup.find_all(class_="list-group-item")
links=[]
# Extract the href attribute from the <a> tags within the list-group elements
for list_group in list_group_elements:
    a_tags = list_group.find_all("a")
    for a_tag in a_tags:
        href = a_tag["href"]
        title = a_tag.text
        links.append([title, href])

# for i in links:
#     if "/video/" in i[1]:
#         print(i)
# Define the path of the CSV file
csv_file = "./links.csv"
# Create a DataFrame from the links list
df = pd.DataFrame(links, columns=["Title", "Link"])

# Define the path of the Excel file
excel_file = "./links.xlsx"

# Write the DataFrame to the Excel file
df.to_excel(excel_file, index=False)

print("Links exported to", excel_file)
# Write the links to the CSV file
# Extract the video links and explanations
# for video in video_elements:
#     video_link = video.source["src"]
#     paragraph = video.find_previous("p").text
#     # Display the video
#     webbrowser.open(video_link)
#     # Print the video link and explanation
#     print("Explanation:", paragraph)

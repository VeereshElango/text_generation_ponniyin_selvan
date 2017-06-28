from bs4 import BeautifulSoup
import requests

ponniyin_selvan = open("ponniyin_selvan.txt","w+")
total_chapters_per_part_list = [57,53,46,46,91]
for index,total_chapters in enumerate(total_chapters_per_part_list):
    for i in range(1,total_chapters+1):
        url = "https://book.ponniyinselvan.in/part-"+str(index+1)+"/chapter-"+str(i)+".html"
        #print(index+1, i)
        print("Crawling url :"+url )
        r  = requests.get(url)
        data = r.text
        soup = BeautifulSoup(data,)
        for link in soup.find_all('p'):
            #print(link.get_text())
            ponniyin_selvan.write(link.get_text())

ponniyin_selvan.close()

print("Total words : ", len(ponniyin_selvan))

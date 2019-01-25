urls = open('/home/ubuntu/Downloads/assam_csv_urls_2018.txt', "r")
url = []
def run():
    for x in urls:
        url.append(x.strip('\n'))
    print(url)
    

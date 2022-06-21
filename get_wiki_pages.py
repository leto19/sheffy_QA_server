import requests
import mwparserfromhell
import wikipediaapi

def strip_images(input):
    out = ""
    for line in input.split("\n"):
        
        if (not line.lstrip().startswith("[[")) and (not line.startswith("{{")):
            print(">>>",line)
            out+=("\n"+line.replace("[[",'"')).replace("]]",'"')
    return out


search = requests.get(
    'https://en.wikipedia.org/w/api.php',
    params={
    'action': 'query',
    'list': "search",
    "srsearch": "Sheffield",
    'srlimit': 1000,
    'format': 'json',
    'srsort': "just_match"
    }).json()
#print(search["query"])
input(">>>")
titles = []
for results in search["query"]["search"]:
    titles.append(results["title"])
print(titles)
print("collected %s pages!"%len(titles))
input(">>>")
wiki_wiki = wikipediaapi.Wikipedia(
        language='en',
        extract_format=wikipediaapi.ExtractFormat.WIKI
)
#titles = ["Mayor of South Yorkshire"]
for t in titles:
    print(t)
    page = wiki_wiki.page(t)
    
    print(page.text)
    


    with open("data/sheff_data/%s.txt"%t,"w") as f:
        f.write(str(page.text))

import requests, os

ACCESS_TOKEN = os.environ["ACCESS_TOKEN"]
BLOG_NAME = os.environ["BLOG_NAME"]

params = {"access_token":ACCESS_TOKEN, "output":"json", "blogName":BLOG_NAME, "page":"1"}
tistory_post_uri = "https://www.tistory.com/apis/post/list"

markdown_text = """# Hello, there!
Still an amateur developer wandering around the digital world, full of curiosity and imagination.<br>
Currently in 12th grade @ Sunrin Internet HS, 5th VP of @EDCAN, and a member of @DSmakerteam.<br>
## Recent blog posts
Posts are updated automatically everyday.<br>
""" # list of blog posts will be appended here

lst = []

r = requests.get(tistory_post_uri, params=params)
if r.status_code == 200: # if OK
    for i in r.json()["tistory"]["item"]["posts"]:
        if i["visibility"]!="0": # if not secret
            lst.append([i["title"], i["postUrl"], i["date"]])
    for j in lst:
        markdown_text += f"[{j[0]}]({j[1]}), {j[2]}<br>\n"
else:
    markdown_text = f"Update failed. You can check out my blog [here]({BLOG_NAME}.tistory.com)!"

f = open("README.md",mode="w", encoding="utf-8")
f.write(markdown_text)
f.close()

import feedparser, datetime

tistory_blog_uri="https://blog.stdio.dev"
feed = feedparser.parse(tistory_blog_uri+"/rss")

markdown_text = """# Hello, there!
Still an amateur developer wandering around the digital world.<br>
Currently in 12th grade @ Sunrin Internet HS, 5th VP of [EDCAN](https://github.com/EDCAN), and a member of [DSmakerteam](https://github.com/DSmakerteam).<br>
## Recent blog posts
""" # list of blog posts will be appended here

lst = []

for i in feed['entries']:
    markdown_text += f"[{i['title']}]({i['link']}) - {datetime.datetime.strptime(i['published'], "%a, %d %b %Y %H:%M:%S %z").strftime("%b %d, %Y")}<br>\n"
    print(i['link'], i['title'])

f = open("README.md",mode="w", encoding="utf-8")
f.write(markdown_text)
f.close()

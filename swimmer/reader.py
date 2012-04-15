import os
from codecs import open
from markdown import Markdown

class POST(object):
	def __init__(self,title,content,link,pubdate):
		self.title=title
		self.content=content
		self.link=link
		self.pubdate=pubdate

def getpost(postdir):
    posts=[]
    data=['title', 'link', 'pubdate']
    empdata=['','','']
    md=Markdown(extensions=['meta'])
    for path,_,files in os.walk(postdir):
        os.chdir(path)
        for filename in files:
            with open(filename, 'r', 'utf-8') as f:
                content=md.convert(f.read())
                for i in xrange(2):
			if data[i] in md.Meta:
                      		empdata[i]=md.Meta[data[i]]
			else:
                        	empdata[i]=""
            post=POST(empdata[0], content, empdata[1], empdata[2])
            posts.append(post)
    return posts

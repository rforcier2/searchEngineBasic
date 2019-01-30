# Python 3.0 
# Basic search engine 

# Time to start making a web crawler:
page = '''<div id="top_bin"> <div id="top_content" class="width960">
   <div class="udacity float-left"> <a href="http://udacity.com">'''

# This will find the first link on the page
start_link = page.find("<a href=")

#get the first quote and second quote after html link tag
start_quote = page.find('"', start_link)
end_quote = page.find('"', start_quote+1)

#get the string inbetween those quotes, the first link on the page
url = page[start_quote+1:end_quote]

print(url)



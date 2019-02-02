# Python 3.0 
# Basic Page Link Extractor:

# get_page function will retrieve the page we want and return the contents.
def get_page(web_link):
  from urllib.request import urlopen
  web_page = urlopen(web_link)
  web_page_text = web_page.read()
  page = web_page_text.decode('UTF-8')
  return page

# get_next_link function will find the next link
#  unless there are no links, in which case we want to return: None, 0 (aka false)
#  We find the beginning quote & end quote of the link,
#  return the contents of the url, and the position of the last 
#  quote we checked so that we don't go over it again.

def get_next_link(page_string):
  start_link = page_string.find("<a href=")
  if start_link == -1:
    return None, 0
  start_quote = page_string.find('"', start_link)
  end_quote = page_string.find('"', start_quote+1)
  url = page_string[start_quote+1:end_quote]
  return url, end_quote


# This function will retrieve all links, while there
#  is a next link, and print all of them to the console.
def print_all_links(valid_page):
  while valid_page:
    url, endpos = get_next_link(valid_page)  
    if url:
      print (url)
      valid_page = valid_page[endpos:]
    else: 
      break
      
# now we choose the link for get_page function:
print_all_links( get_page('https://en.wikipedia.org/wiki/Main_Page') )



# Python 3.0 
# Basic search engine 

# This will stand in as a valid "webpage" to search:
page = '''
<div id="top_bin"> 
  <div id="top_content" class="width960">
    <div class="udacity float-left">
    <a href="http://udacity.com">Udacity</a>
    <a href="http://youtube.com">youtube</a>
    <a href="http://codepen.io">Codepen</a>
    <a href="http://starlimeweb.com">starlime</a> 
     '''

# get_next_link function will find the next link
#  unless there are no links, in which case we want to return: None, 0 (aka false)

# First we find the beginning quote and end quote of the link
#  return the contents of the url and the position of the last 
#  quote we checked, so we don't go over it again.

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

print_all_links(page)



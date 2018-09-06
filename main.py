import requests
from bs4 import BeautifulSoup

string = input("Enter the year: ")
URL = ("https://www.imdb.com/search/title?year="+string+"&title_type=feature&")
r = requests.get(URL)
soup = BeautifulSoup(r.content, 'html.parser')
html = list(soup.children)[3]
body = list(html.children)[3]
wrapper = body.find('div', id='wrapper')
root = list(wrapper.children)[1]
pagecontent = list(root.children)[11]
contenttwowide = list(pagecontent.children)[3]
main = list(contenttwowide.children)[1]
article = list(main.children)[1]
listerlistdetail = list(article.children)[5]
listerlist = list(listerlistdetail.children)[5]
i = 0
result = dict()
result2 = dict()
for tag in list(listerlist.children):
	try:
		advanced = list(listerlist.children)[i+1]
		lister_item_content = list(advanced.children)[5]
		lister_item_header = list(lister_item_content.children)[1]
		final_code = list(lister_item_header.children)[3]
#		print(final_code.get_text())
		i = i + 2
		ratings_bar = list(lister_item_content.children)[5]
		final_rating = list(ratings_bar.children)[1]
		final_rating2 = list(final_rating.children)[3]
#		print(final_rating2.get_text())
		result[final_code.get_text()] = float(final_rating2.get_text())
#		print(result2)
		

	except:
		continue
result_view = [ (v,k) for k,v in result.items() ]
result_view.sort(reverse = True)
print("\n\n")
print("Suggested movies from the year", string,"are:")
print()
print()
for v,k in result_view:
	print(k,'--->',v)


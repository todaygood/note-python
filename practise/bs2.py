from bs4 import BeautifulSoup


html='<th class ="tips-fieldnameL" width="167" >上市日期  </th >'


soup= BeautifulSoup(html,"lxml")

print(soup.find_all("th",attrs={'class':"tips-fieldnameL"}))


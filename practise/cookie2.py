'''
code from http://www.wjhsh.net/chenshengkai-p-11446455.html

'''


from  selenium  import  webdriver
import  time
import  json

user="用户名"
password="密码"

driver  =  webdriver.Chrome()
driver.get('目标网站')
time.sleep(5)
driver.find_element_by_xpath("./*//button[@type='submit']").click()
print("正在输入用户名和密码")
#清空登录框
driver.find_element_by_xpath("./*//input[@name='username']").clear()
#自动填入登录用户名
driver.find_element_by_xpath("./*//input[@name='username']").send_keys(user)
#清空密码框
driver.find_element_by_xpath("./*//input[@name='password']").clear()
#自动填入登录密码
driver.find_element_by_xpath("./*//input[@name='password']").send_keys(password)

time.sleep(8)
#点击登录按钮进行登录
driver.find_element_by_xpath("./*//button[@name='loginsubmit']").click()
time.sleep(10)



driver.get('目标网站')

#获取cookies
cookie_items  =  driver.get_cookies()

#获取到的cookies是列表形式，将cookies转成json形式并存入本地名为cookie的文本中
for  cookie_item  in  cookie_items:
    post[cookie_item['name']]  =  cookie_item['value']


cookie_str  =  json.dumps(post)
with  open('cookie.txt',  'w',  encoding='utf-8')  as  f:
    f.write(cookie_str)

f.close()

print("登录完成")

header = {"User-Agent": "Mozilla/5.0 (Windows NT 6.1; WOW64;rv:53.0) Gecko/20100101 Firefox/53.0"}
with open('cookie.txt', 'r', encoding='utf-8') as f:
    cookie = f.read()
    cookies = json.loads(cookie)


res = requests.get(url=url, cookies=cookies, headers=header)


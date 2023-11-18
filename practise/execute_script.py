from selenium import webdriver
# 作者-上海悠悠 QQ交流群:717225969
# blog地址 https://www.cnblogs.com/yoyoketang/

driver = webdriver.Chrome()
driver.get("https://www.cnblogs.com/yoyoketang/")

# 定位博客首页 "博客园" 按钮
# <a id="blog_nav_sitehome" class="menu" href="https://www.cnblogs.com/">博客园</a>

js_blog = 'return document.getElementById("blog_nav_sitehome").innerText;'
blog = driver.execute_script(js_blog)
print(blog)


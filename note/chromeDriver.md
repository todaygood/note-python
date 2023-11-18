
Chrome Driver Options:

https://chromedriver.chromium.org/capabilities

selenium 开启开发者工具（F12）

options = webdriver.ChromeOptions();
options.add_argument("--auto-open-devtools-for-tabs");
driver = webdriver.Chrome(chrome_options=options)；


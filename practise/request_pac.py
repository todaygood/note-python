

import pypac

session = pypac.PACSession()

ret = session.get("https://www.youtube.com")
print(ret)


ret = session.get("http://nas.hujun.com/")
print(ret)

#with pac_context_for_url('https://www.youtube.com'):
#    pass
#场景：当windows开了pac代理时使用我的软件
#总结：pypac 和requests结合使用还是挺麻烦的。
#参见 https://juejin.cn/s/python%20request.get%20%E8%B5%B0%E7%B3%BB%E7%BB%9F%E4%BB%A3%E7%90%86




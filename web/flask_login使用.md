
英文官方文档翻译: https://www.cnblogs.com/wxzbk/p/11043269.html

实战例子： https://zhuanlan.zhihu.com/p/336267834

代码例子： flask-login-example 

在初始化完成之后我们需要对平台用户模型类继承自UserMixin


设置完用户模型类之后我们还必须要注册一个回调函数，user_loader 回调函数，没有这个函数flask_login是没有办法工作的。



通过login_user(user)，其实也是调用user_loads()把用户设置到session中

## 如何判断用户已经处于登录状态？


方式一：通过 session, cookie 的方式
用户首次登陆时，请求会发送到后端，后端会将用户的相应信息存储 session 中,并在数据库中生成对应的 session 表，

在响应客户端的时候，把当前用户对应的 Session ID 存放在 cookies 中，这样只要 cookies 没有过期，每一次请求都会携带对应的 ID ，后端就可以通过这个 ID 判断是哪一个用户，只要 cookies 没有过期，用户就是登陆状态。

方式二：后台通过 jwt(Json web token) 生成登录态，前端使用 localStorage 来存储用户信息
用户首次登陆时，发送请求到后端，服务器收到请求后，如果信息正确，则到数据库查询到相关用户的所有信息，通过密钥进行加密，生成一个 token 并返回给用户。
用户可以通过 localStorage 把该 token 保存到客户端，服务器不保存任何用户信息。
后续的请求，通常将 token 通过 HTTP 的 Authorization header 发送给服务端，服务端使用自己保存的密钥验证 token 的正确性，只要正确即通过验证。否则，结束本次请求。
————————————————
版权声明：本文为CSDN博主「熊的猫」的原创文章，遵循CC 4.0 BY-SA版权协议，转载请附上原文出处链接及本声明。
原文链接：https://blog.csdn.net/weixin_43822185/article/details/104074147

{'username':'sanqiyanxishe@163.com','password':'123456'}

set-cookie
session=.eJxtzj0KAjEQQOG7pBaZn0yS2cqbyCSZ4BYq7ioo4t1dsLX9eMV7h-NYfD2F6b48fBeOcw9TcAZiY4uaTWXAqAkJAZwJa-3sQyRmAG2pC4zBzWrVDgXJjDbhhOoiZFoY4zBmAItIyXtM1Cso5dIgRe_MlLl7FfVSM2kxaWEbeay-_G5Wu9zml12e83ryAybet-t5S_77FJA4SgqfLxNgP9g.Y1-Zyg.oAslO0smvzi9OPmnuOQmqBXRn4U; HttpOnly; Path=/

{'username':'379408156@qq.com','password':'123456'}

set-cookie
session=.eJxtzj0KAjEQQOG7pBaZn0yS2cqbyCSZ4BYq7ioo4t1dsLX9eMV7h-NYfD2F6b48fBeOcw9TcAZiY4uaTWXAqAkJAZwJa-3sQyRmAG2pC4zBzWrVDgXJjDbhhOoiZFoY4zBmAItIyXtM1Cso5dIgRe_MlLl7FfVSM2kxaWEbeay-_G5Wu9zml12e83ryAybet-t5S_77FJA4SgqfLxNgP9g.Y1-Zyg.oAslO0smvzi9OPmnuOQmqBXRn4U; HttpOnly; Path=/


flask 每次生成的session 都一样，必须得 添加cookie
https://blog.csdn.net/seanyang_/article/details/127192769


## apipost中的cookie管理器

https://zhuanlan.zhihu.com/p/353709522

通过cookie,可以让服务器知道请求是来源哪个客户端，就可以进行客户端状态的维护，比如登陆后刷新，请求头就会携带登陆时response header中的set-cookie,Web服务器接到请求时也能读出cookie的值，根据cookie值的内容就可以判断和恢复一些用户的信息状态。

二、cookie的组成
Cookie由变量名和值组成，类似Javascript变量。其属性里既有标准的Cookie变量，也有用户自己创建的变量，属性中变量是用“变量=值”形式来保存。

根据Netscape公司的规定，Cookie格式如下：
Set-cookie: NAME=VALUE Expires/Max-age=DATE Path=PATH Domain=DOMAIN_NAME SECURE

参数意义:

NAME: cookie的名字。

VALUE: cookie的值。

Expires: cookie的过期时间。

Path: cookie作用的路径。

Domain: cookie作用的域名。

SECURE:是否只在https协议下起作用

三、apipost中cookie管理器的使用
接口测试和接口文档生成工具apipost中cookie管理器的作用是管理接口的cookie和自定义cookie
这里我们访问一个登录接口，然后查看服务器给我返回的set-cookie、如图：

[判断用户是否的登录的方式：JWT 与 session 、cookies](https://blog.csdn.net/weixin_43822185/article/details/104074147)

## 动手实验 

https://cloud.tencent.com/developer/article/1593620

https://flask-session.readthedocs.io/en/latest/


(venv) [root@pcentos flask-session-cookie-manager]# python3  flask_session_cookie_manager3.py  decode  -s todaygood -c ".eJxtzjEOwjAMheG7ZEbIseMk7sRNKidxBENBbemEuDtBrKzvk57-l5v7ZvvVTc_tsJObb81NzgiQlDRIUuEOvUSPHsAIfSmNrDOHBCA1NobeqWop0iB7VMWxUPRizKiSyYeuRAAaPEZrIWIrIJhyhRisEWGiZoXFckkoWbm6EXLstv1qKEkY1xwv63quj2XoF--62D99fwCy1Ds_.Y2BoNA.MyoGqllxESx8uLHPU6lCXOxhlSs"
{'_fresh': True, '_id': 'e3023a3a497a95f0fb612100e321bbd3ef5547009c6d50ff3cabb9d0812aa250f3619e552a98314fa3300a4126ed462db09278c064ed33273deb59e8b7298a5c', '_user_id': '379408156@qq.com', 'username': '379408156@qq.com'}

 

(venv) [root@pcentos flask-session-cookie-manager]# python3  flask_session_cookie_manager3.py  decode  -s todaygood -c ".eJx1zj0OwjAMQOG7ZEbIsfPnTtykchJH7dAiGiqBEHeniJn16Rvey4xt0z6Z4b7tejLjXM1glABJSBxHYd-g5WDRAiihzbmSNu9dBOASqofWqEjOXCFZFMGjULCs3qNwIuuaEAGIsxi0uoA1A2NMBYLTSoSRqmbPmnJETuKLOUb2rtvvpst6m5-yPuY-6cUGOpfrcpCvWGXRv-T9AaC3QgM.Y2Bpmw.BSs4aic8N23NdWd4n03fXyLYCwc"
{'_fresh': True, '_id': 'e3023a3a497a95f0fb612100e321bbd3ef5547009c6d50ff3cabb9d0812aa250f3619e552a98314fa3300a4126ed462db09278c064ed33273deb59e8b7298a5c', '_user_id': 'sanqiyanxishe@163.com', 'username': 'sanqiyanxishe@163.com'}


_id 是一样的， _user_id 是不一样的。

响应头中set-cookie  是这样的：
session=.eJwlzjsOwjAMANC7ZEbIsfMzEzep7MRRO1BEQyUQ4u5UYn3T-7ipbzZmd3luu53ctDR3cUaAJCSBs3Ds0DV59ABG6FUbWY8xZACuqUXonaqocoPiUQQPoeTZYkThQj50IQKQ4DFZCwmbAmMuFVKwRoSZmmlkK5qRi8Tqjsg-bPtvhqyP5S3raxmzXX2ic73f3PcHaIk16Q.Y2Bzqg.BBwY31UdffItDhQmjmSATcQsgus; HttpOnly; Path=/

(venv) [root@pcentos flask-session-cookie-manager]# python3 flask_session_cookie_manager3.py decode -s todaygood -c ".eJwlzjsOwjAMANC7ZEbIsfMzEzep7MRRO1BEQyUQ4u5UYn3T-7ipbzZmd3luu53ctDR3cUaAJCSBs3Ds0DV59ABG6FUbWY8xZACuqUXonaqocoPiUQQPoeTZYkThQj50IQKQ4DFZCwmbAmMuFVKwRoSZmmlkK5qRi8Tqjsg-bPtvhqyP5S3raxmzXX2ic73f3PcHaIk16Q.Y2Bzqg.BBwY31UdffItDhQmjmSATcQsgus"
{'_fresh': True, '_id': 'e3023a3a497a95f0fb612100e321bbd3ef5547009c6d50ff3cabb9d0812aa250f3619e552a98314fa3300a4126ed462db09278c064ed33273deb59e8b7298a5c', '_user_id': 'sanqiyanxishe@163.com'}

apiPost 响应头中的set-cookie 在不同的用户去登录之后，没有变化，依然是第一个用户， 而cookies 窗口中的值是对的。 

## postman

{
    "username":"379408156@qq.com",
    "password":"123456"
}
session=.eJwlzlEKwjAMANC79FskbZek2Zc3GU2ToB8i29yXeHcHHuDB-6QlNt_vaX5vh1_S8rA0J-2k3MgzidWiDqQWCAEc0xgStTPalLX3ACKNJtC6sPViigjiJ2Il8qIQXFsWkYJDuxSqhkLM5oREhjjlHFLDCMIh5wGjajojx-7bf1NZJmgZ6bau1_F6pu8P4mYztg.Y2B4Tw.6CSaZmJw21bzHodEzzv-wMxUZ0U; Path=/; HttpOnly;


set-cookie:

session=.eJwlzlEKwjAMANC79FskbZek2Zc3GU2ToB8i29yXeHcHHuDB-6QlNt_vaX5vh1_S8rA0J-2k3MgzidWiDqQWCAEc0xgStTPalLX3ACKNJtC6sPViigjiJ2Il8qIQXFsWkYJDuxSqhkLM5oREhjjlHFLDCMIh5wGjajojx-7bf1NZJmgZ6bau1_F6pu8P4mYztg.Y2B4Tw.6CSaZmJw21bzHodEzzv-wMxUZ0U; HttpOnly; Path=/


session=.eJwlzlEKwjAMANC79FskbZd08cubSNIkbB9O3Bwo4t0VPMCD906XWH2b0umx7n5Il9nSKamQtpE8E1st6kBqgRDQYuido0pDG7KKBBBpjAyjcDMppojA_kNNibwoRKtjZuaCXYULVUOm1swJiQxxyDm4hhGEQ84detX0i-ybr__NJst9fsnynLfJz5nqsd-u6fMFDks3GA.Y2B44w.MeGBQXEA2NJeRN1_yK8QQPk3EDc; HttpOnly; Path=/

 
request.cookies=ImmutableMultiDict([('session', '.eJwlzlEKwjAMANC79FskbZd08cubSNIkbB9O3Bwo4t0VPMCD906XWH2b0umx7n5Il9nSKamQtpE8E1st6kBqgRDQYuido0pDG7KKBBBpjAyjcDMppojA_kNNibwoRKtjZuaCXYULVUOm1swJiQxxyDm4hhGEQ84detX0i-ybr__NJst9fsnynLfJz5nqsd-u6fMFDks3GA.Y2B8Ng.7IclSuLreaxDaeSOE-wzeiuujnE')])


## 使用postman 发一次login post时没有cookie 

发第二次login post 后 ， 在服务器端解析cookie , 解密之后，发现解析出来就是

(venv) [root@pcentos flask-session-cookie-manager]# python3 flask_session_cookie_manager3.py decode -s todaygood -c '.eJwlzlEKwjAMANC79FskbZd08cubSNIkbB9O3Bwo4t0VPMCD906XWH2b0umx7n5Il9nSKamQtpE8E1st6kBqgRDQYuido0pDG7KKBBBpjAyjcDMppojA_kNNibwoRKtjZuaCXYULVUOm1swJiQxxyDm4hhGEQ84detX0i-ybr__NJst9fsnynLfJz5nqsd-u6fMFDks3GA.Y2CHMQ.FuAX-uBhkFnLCxTtx1zrcIg6y3w'
{'_fresh': True, '_id': 'ba6b786e169d32be06bdf50f07f4cc9f3a75d41baaf066bf8908a97da2db5509e32b7b66e2b0f738199925cba9263d59677de6566d55411f93fd60fe011c0c3b', '_user_id': 'sanqiyanxishe@163.com'}


{'_fresh': True, '_id': 'ba6b786e169d32be06bdf50f07f4cc9f3a75d41baaf066bf8908a97da2db5509e32b7b66e2b0f738199925cba9263d59677de6566d55411f93fd60fe011c0c3b', '_user_id': 'sanqiyanxishe@163.com'}

这种内容， 说明postman就是模拟了浏览器的行为，在发第二次Post时，会自动带上cookie。 

但如果使用curl 是不会这么干的，要自己加参数才行。

2022-11-01 10:41:35,016 - DEBUG - request.cookies=ImmutableMultiDict([('session', '.eJwlzlEKwjAMANC79FskbZd08cubSNIkbB9O3Bwo4t0VPMCD906XWH2b0umx7n5Il9nSKamQtpE8E1st6kBqgRDQYuido0pDG7KKBBBpjAyjcDMppojA_kNNibwoRKtjZuaCXYULVUOm1swJiQxxyDm4hhGEQ84detX0i-ybr__NJst9fsnynLfJz5nqsd-u6fMFDks3GA.Y2CHMQ.FuAX-uBhkFnLCxTtx1zrcIg6y3w')]) 
 

2022-11-01 09:53:58,338 - DEBUG - request.cookies=ImmutableMultiDict([('session', '.eJwlzlEKwjAMANC79FskbZd08cubSNIkbB9O3Bwo4t0VPMCD906XWH2b0umx7n5Il9nSKamQtpE8E1st6kBqgRDQYuido0pDG7KKBBBpjAyjcDMppojA_kNNibwoRKtjZuaCXYULVUOm1swJiQxxyDm4hhGEQ84detX0i-ybr__NJst9fsnynLfJz5nqsd-u6fMFDks3GA.Y2B7cw.cY6aihRsljnOPlYnfd30uvWSJiA'), ('session', '.eJwlzlEKwjAMANC79FskbZd08cubSNIkbB9O3Bwo4t0VPMCD906XWH2b0umx7n5Il9nSKamQtpE8E1st6kBqgRDQYuido0pDG7KKBBBpjAyjcDMppojA_kNNibwoRKtjZuaCXYULVUOm1swJiQxxyDm4hhGEQ84detX0i-ybr__NJst9fsnynLfJz5nqsd-u6fMFDks3GA.Y2B75w.k-GfSGSXwriR_OI6ij6C4yDLROo'), ('Path', '/'), ('HttpOnly', '')])
2022-11-01 09:53:58,339 - DEBUG - after check cookies,sanqiyanxishe@163.com,123456


2022-11-01 11:12:41,901 - DEBUG - request.cookies=ImmutableMultiDict([('Cookie_2', 'value'), ('session', '.eJwlzlEKwjAMANC79FskbZd08cubSNIkbB9O3Bwo4t0VPMCD906XWH2b0umx7n5Il9nSKamQtpE8E1st6kBqgRDQYuido0pDG7KKBBBpjAyjcDMppojA_kNNibwoRKtjZuaCXYULVUOm1swJiQxxyDm4hhGEQ84detX0i-ybr__NJst9fsnynLfJz5nqsd-u6fMFDks3GA.Y2CHXw.5InTY70uAB8Qukv8mO9ou1GvLoc')]) 


1. 有多个session , Login之后，把session 入库

2. login request时检查cookie , 解密， 解析出_user_id  ， 从session库中查询得到现在的session id 和user id 

3. 多个用户使用同一个浏览器登录，是一个session , 但有多个user_id , 所以 session库的索引是(session_id,user_id)二元组。 

[Cookies使用](https://blog.csdn.net/qq_27371025/article/details/126776251)

[浏览器中如何发post请求](https://juejin.cn/post/7020036504130945032)


手头开发一个登录项目，分user 和admin 表，需要分别登录前后台，flask 的扩展flask-login 已有的功能不能满足需要

所以打算研究一下源代码，扩展一下功能。

项目 user 和admin 两个模块，分别用于用户中心和管理后台区分。
https://github.com/siaoynli/flask_login_multi


[flask使用session保存登录状态及拦截未登录请求代码](http://www.zzvips.com/article/129355.html)

[如何实现判断当前操作，用户是否为登录状态？](https://blog.csdn.net/weixin_42065178/article/details/124290460?spm=1001.2101.3001.6650.1&utm_medium=distribute.pc_relevant.none-task-blog-2%7Edefault%7ECTRLIST%7ERate-1-124290460-blog-104074147.pc_relevant_3mothn_strategy_recovery&depth_1-utm_source=distribute.pc_relevant.none-task-blog-2%7Edefault%7ECTRLIST%7ERate-1-124290460-blog-104074147.pc_relevant_3mothn_strategy_recovery&utm_relevant_index=2)


[flask form](https://blog.csdn.net/qq_44791003/article/details/126678964?spm=1001.2101.3001.6661.1&utm_medium=distribute.pc_relevant_t0.none-task-blog-2%7Edefault%7EYuanLiJiHua%7EPosition-1-126678964-blog-102917473.pc_relevant_3mothn_strategy_recovery&depth_1-utm_source=distribute.pc_relevant_t0.none-task-blog-2%7Edefault%7EYuanLiJiHua%7EPosition-1-126678964-blog-102917473.pc_relevant_3mothn_strategy_recovery&utm_relevant_index=1)






## URL编码表

https://www.cnblogs.com/shaosks/p/13086457.html









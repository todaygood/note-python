


MongoDB 5.0+ requires a CPU with AVX support, and your current system does not appear to have that!


To solve this issue I had to run an older mongo-db docker image version (4.4.6), as follows:

image: mongo:4.4.6


mongodb常用操作参见：https://www.runoob.com/mongodb/mongodb-connections.html



## 创建并启动

    docker run --name mongodb -p 27017:27017 -d mongo

## 创建用户


进入mongo
    docker exec -it mongodb mongo
创建用户
    db.createUser({ user:'admin',pwd:'todayGood123',roles:[ { role:'userAdminAnyDatabase', db: 'admin'}]});
认证
    db.auth('admin', 'todayGood123')
	
	
## 创建数据库

use databaseName
异常
    Command failed with error 18 (AuthenticationFailed): ‘Authentication failed.
解决
    权限问题，新的数据库需要创建对应的用户
创建对应用户
    db.createUser({user:"xxx",pwd:"123456",roles:[{role:"dbOwner",db:"databaseName"}]})

作者：zitangkou
链接：https://juejin.cn/post/6844904120516608007
来源：稀土掘金
著作权归作者所有。商业转载请联系作者获得授权，非商业转载请注明出处。
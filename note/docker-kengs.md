# docker的“坑”总结

参见： https://juejin.cn/post/6844903905600471047

一、运行镜像报错

ENTRYPOINT
CMD


老image的dockerfile中CMD是这样的： CMD ["nginx" "-g" "daemon off;"]
这是一坑啊 ,参见[docker commit采坑记录](https://www.cnblogs.com/sylvia-liu/p/14647866.html)

CMD会变的， 所以制作Image,最好是使用entrypoint 'entrypoint.sh'  这种方式。 
Dockerfile中应该使用ENTRYPOINT,不要使用CMD

ENTRYPOINT的最佳用处是设置镜像的主命令，允许将镜像当成命令本身来运行

参见[Dockerfile最佳实践](https://www.qikqiak.com/k8s-book/docs/13.Dockerfile%E6%9C%80%E4%BD%B3%E5%AE%9E%E8%B7%B5.html)


三、建议关闭git的自动crlr转换 

[core]
	autocrlf = true

建议把这个配置关掉：
$ git config --global core.autocrlf false



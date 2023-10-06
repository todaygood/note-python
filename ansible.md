

# 研究ansible 

ansible 架构： controller node, managed node 

controller node，在上面跑ansible,ansible-playbook等命令， 必须是类linux系统，不支持windows， 为什么？ 因为ansible使用的是fork来实现each host, each task 的模型。 

而windows上不支持fork()。 

具体原因可以参见： https://blog.rolpdog.com/2020/03/why-no-ansible-controller-for-windows.html

## ansible  

在windows上pip install ansible 失败， 原因见上面的ansbile本就不支持在windows上跑，但失败现场表明： pip install的原理是什么？ 为何不直接判断os类型？ 




## 选择ansible还是saltstack 

https://blog.51cto.com/liqilong2010/1850613

1. salt的性能更好： 

可以看出使用MQ通讯和SSH通讯,速度相差大约40倍
显然，从速度的角度，排除ansible，最终选择了Saltstack。

在 python系列的ansible、Saltstack的选择中，有人放弃Saltstack的主要原因是Saltstack需要安装客户端，在服务器有 一定数量的情况下比较麻烦，而ansible不需要安装客户端。我个人认为这个考虑是多余的，Saltstack中的Salt-ssh可以轻易解决这个问 题（后面会写篇使用salt-ssh批量部署客户端的博客），而且ansible也并非是不需要在“客户端”做任何操作。例如，1.“客户端”系统 python版本需要满足2.6+，否则需要进行升级；2.ansible使用一些功能也需要“客户端”有对应模块（主要是python模块，即使 python版本满足2.6+，也需要额外安装）
-----------------------------------
SaltStack 与 Ansible 选择？- 知乎
https://blog.51cto.com/liqilong2010/1850613


[全方位比较](https://cloud.tencent.com/developer/article/1628268)

2. ansible 学习起来更容易

3. salt的架构更好 ，参见： https://docs.saltproject.io/en/latest/topics/salt_system_architecture.html#the-salt-system-architecture


## ansible-runner 

https://github.com/ansible/ansible-runner

https://ansible.readthedocs.io/projects/runner/en/stable/standalone/#executing-runner-in-the-background


Python使用ansible-runner模块实现ansible调用学习
https://zhuanlan.zhihu.com/p/634867306


ansible-api ，可参考其实现架构图： https://github.com/lfbear/ansible-api

redhat ansible automation platform 参见：https://access.redhat.com/documentation/en-us/red_hat_ansible_automation_platform/2.4

其上游项目： https://github.com/ansible/awx/tree/devel

awx-operator: https://github.com/ansible/awx-operator/tree/devel
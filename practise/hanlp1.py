from hanlp_restful import HanLPClient


'''
参见：https://zhuanlan.zhihu.com/p/51419818

[github HanLP](https://github.com/hankcs/HanLP/tree/doc-zh)
[HanLP入门教程](https://github.com/hankcs/HanLP/blob/doc-zh/plugins/hanlp_demo/hanlp_demo/zh/tutorial.ipynb)
[美团智能客服核心技术与实践](https://juejin.cn/post/7017714995861389320)
'''

HanLP = HanLPClient('https://www.hanlp.com/api', auth=None, language='zh') # auth不填则匿名，zh中文，mul多语种

doc= HanLP.parse("2021年HanLPv2.1为生产环境带来次世代最先进的多语种NLP技术。阿婆主来到北京立方庭参观自然语义科技公司。")

#doc.pretty_print()

HanLP('阿婆主来到北京立方庭参观自然语义科技公司。', tasks='tok').pretty_print()

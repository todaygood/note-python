
# ES 核心概念

https://codeantenna.com/a/8v5UU6YozB
https://logz.io/blog/10-elasticsearch-concepts/


## ES 查询总结

1. console 使用kibana里面的dev tools

2. curl 

curl -X GET "http://192.168.30.125:9200/%E8%82%A1%E7%A5%A8%E4%BF%A1%E6%81%AF/_search"  -H 'Content-Type: application/json' -d'
{"query":
    {"bool":
        {"must":[{"match":{"股票代码":"600622"}}],
         "must_not":[],"should":[]
        }
    },
    "from":0,
    "size":10,
    "sort":[],
    "aggs":{}
}'

可以用postman 

3. Elasticsearch head Chrome插件

Structured Query 查询功能很好用，可以用多种条件生成Json 












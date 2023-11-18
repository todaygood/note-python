# mongodb 到ES 

todo: 先搞清楚原理

## 有5种方法：
https://code.likeagirl.io/5-different-ways-to-synchronize-data-from-mongodb-to-elasticsearch-d8456b83d44f

https://discuss.elastic.co/t/elasticsearch-and-mongo-db-real-time-sync/32758/3

"Changes Feed" in CouchDB, "Oracle Streams" in Oracle



## Mongo-Connector
MongoConnector is an open source tool which is to sync MongoDB data to ElasticSearch. You can run it periodically or continously. And, it can sync all the changes in your MongoDB data. ElasticSearch will have a replica of the MongoDB data.

You can configure which are the MongoDB collections you want to sync and with what names their indexes should be made in ElasticSearch.

Requirements
MongoDB Replica Set You need a MongoDB replica set. A standalone instance will not work.

ElasticSearch Cluster

mongo-connector utility

https://www.gyanblog.com/tutorials/how-sync-mongodb-data-elasticsearch-mongo-connector/

https://hevodata.com/learn/integrating-elasticsearch-and-mongodb/#:~:text=To%20sync%20the%20data%20to,in%20sync%20in%20real%2Dtime.

## monstache

https://github.com/rwynn/monstache

文档：https://rwynn.github.io/monstache-site/

https://www.folio3.com/mobile/blog/sync-mongodb-monstache-elasticsearch/

https://partners-intl.aliyun.com/help/en/elasticsearch/latest/use-monstache-to-synchronize-data-from-a-mongodb-database-to-an-alibaba-cloud-elasticsearch-cluster-in-real-time


## transporter

https://github.com/compose/transporter

https://aboullaite.me/sync-data-from-mongodb-to-elasticsearch-using-transporter/


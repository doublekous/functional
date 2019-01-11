---
title: mongodb命令
date: 2018-12-04 14:31:37
tags:
---

## MongoDB

NoSQL,全称是NOT ONLY SQL 指的是非关系型数据库。
非关系型数据库主要有这些特点： 非关系型的、分布式的、开源的、水平可扩展的
MongoDB是一个介于关系数据库和非关系数据库之间的产品，是非关系数据库中功能最丰富，最像关系数据库的。

MongoDB最大的特点：它支持查询语言非常强大，其语法有点类似于面向对象的查询语言，几乎可以实现类似关系数据库表单查询的绝大部分功能。

### 面向集合
意思是数据被分组储存在数据集中，被称为一个集合。每个集合在数据库中都有一个唯一的标识名，并且可以包含无限数目的文档。类似于关系型数据库里的表，不同的是他不需要定义任何模式

### 模式自由
储存在MongoDB数据库中的文件，我们不需要知道他的任何结构定义。

### 文档型 
意思是我们储存的数据是键值对的集合，键是字符串，值可以使数据类型即合理的任何类型，包括数组和文档。文件存储的格式为BSON（一种JSON的扩展）

## 使用场景
1. 网站数据：MongoDB非常适合实时的插入，跟新与查询，并且具备网站实时数据存储所需要的复制及高度伸缩性
2. 缓存：由于性能很高，MongoDB也适合作为信息基础设施的缓存层。在系统重启之后，由MongoDB搭建的持久化缓存层也可以避免下层的数据源过载。
3. 大尺寸，低价值的数据：使用传统的关系型数据库存储一些数据时可能会比较昂贵
4. 用于对象及JSON数据的存储：MongoDB的BSON数据格式非常适合文档化格式的存储及查询

## mongo 客户端
```
进入客户端
./mongo

查看数据库命令
show dbs

打开数据库
use u17
查看集合
show collections
```
文档： 文档（Document）是MongoDB的核心概念，他是MongoDB逻辑存储的最小基本单位 对应mysql记录
集合 ： 多个文档组成的集合     对应mysql table
数据库： 多个集合组成的数据库  对应mysql database

### 创建数据库
```
use newdb1
show dbs
数据库并没有添加，当我们在给数据库中的集合插入一条文档的时候就会自动创建一条文档、一个集合、一个数据库。
db.users.insert({'name': 'lv'})
show collections;

插入一条数据
db.users.insert({'u_id': 2, 'uname': 'lv', 'isvip': true, 'sex': null, 'hobby': ['math', 'english']})
查询数据
db.users.find().pretty()
db.users.findOne({'uid': 2})

删除数据
db.users.remove({'uid': 2})

清空集合
db.users.drop()
更新文档
第一个文档为查询的文档，第二个文档为修改为什么文档，后面的文档会覆盖我们要修改文档的整个内容
db.users.update({'uid': 2}, {'uname': 'json'})

使用修改器$inc更新
对uid为2的用户增加100块钱工资
db.users.update({'uid': 2}, {'$inc': {'salary': 100}})
对uid为2的用户减100块钱工资
db.users.update({'uid': 2}, {'$inc': {'salary': -100}})
添加一个字段$set修改器
db.users.update({'uid': 2}, {'$set': {'age': true}})

删除一个字段
db.users.update({'uid': 2}, {'$unset': {'age': true}})
数组的更新
db.users.update({"uid":2},{"$push":{"email":"a"}})
$pushAll在元组中增加多个元素,但是他不不检查元素是否存在
db.users.update({"uid":2},{"$pushAll":{"email":["a", "b","c","d"]}})
$addToSet 往数组中添加⼀一个不不重复的元素
db.users.update({"uid":2},{"$addToSet":{"email":"d"}})
添加多个不不重复的元素，这时候就得需要⽤用到*$eache*操作符了了
db.users.update({"uid":2},{"$addToSet":{"email":{"$each":["e","g","f","d"]}}})
*删除数组元素*
db.users.update({"uid":2},{"$pop":{"email":-1}}) #从左侧删除⼀一个元素
db.users.update({"uid":2},{"$pop":{"email":1}})#从右侧删除⼀一个元素
db.users.update({"uid":2},{"$pull":{"email":"b"}}) #删除数组内的指定⼀一个元素
db.users.update({"uid":2},{"$pullAll":{"email":["b","c"]}}) #删除数组内指定的多个元
素
数组元素的更更新
通过数组.下标修改
db.users.update({"uid":2},{"$set":{"email.0":"tim.qq.com"}})



















```
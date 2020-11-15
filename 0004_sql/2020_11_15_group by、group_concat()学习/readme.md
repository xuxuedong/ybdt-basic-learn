首先知道一件事，想使用group_concat()，需要同时使用group by

group by语句解释  
有这样一个表，如下  
![image](./0.png)  
直接执行
```
select id,user from bugaifade group by id;
```
结果会报错，如下图  
![image](./1.png)  
原因是group by的使用需要对其他字段进行处理，如下图是正确使用方式  
![image](./2.png)  
同理，将函数count()换成group_concat()即为group_concat()用法，如下图  
![image](./3.png)  

参考链接：  
https://www.runoob.com/mysql/mysql-group-by-statement.html  
https://www.w3schools.com/sql/func_mysql_count.asp  
https://www.w3schools.com/sql/sql_groupby.asp  
https://www.w3resource.com/mysql/aggregate-functions-and-grouping/aggregate-functions-and-grouping-group_concat.php  
https://segmentfault.com/a/1190000004844113

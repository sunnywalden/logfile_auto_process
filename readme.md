一、功能
解析处理失败id，进行自动二次处理

二、原理

1.查看日志中的错误信息，得到待处理的id

2.匹配到'ERROR Build' 和 'failed with timed out'关键字,则为上线失败，匹配到'ERROR Delete' 和 'failed with timed out'关键字,则为处理失败

3.上一步，下线或更新场景的判定，通过得到的id查询mongo库中id状态

4，查询mongo后，将id写入对应的缓存文件

5.调用手动服务脚本，执行对应操作

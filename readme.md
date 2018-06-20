一、功能
基础搜索上下线服务，每日会有概率性视频上下线失败问题，需要对失败的操作进行自动二次处理

二、原理

1.查看上下线服务日志中的错误信息，得到上下线失败视频的searchid

2.匹配到'ERROR Build' 和 'failed with timed out'关键字,则为上线失败，匹配到'ERROR Delete' 和 'failed with timed out'关键字,则为下线或更新失败

3.上一步，下线或更新场景的判定，通过得到的searchid查询mongo库中视频的上下线状态

4，查询mongo后，将searchid写入对应的缓存文件

5.调用手动上下线脚本，执行上下线操作

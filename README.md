# tombstone
yangzhe.life

# 安装所需库
```python
pip install -r requirements/deploy.txt
```

# 部署

### 安装
在安装了ngix和uwsgi之后


### uwsgi
运行uwsgi
```
sudo uwsgi --ini conf/uwsgi.ini
```

后台运行
```
uwsgi -d -ini conf/deploy.ini
```

关闭uwsgi
```
uwsgi --stop /.....pid
```
关掉pid文件，文件位置可以在uwsgi.ini中查看

如果报错```signal_pidfile()/kill(): No such process [core/uwsgi.c line 1627]```

查看进程端口，注意端口号
```
sudo netstat -ap | grep 8108
```

修改进程id
```
vim /tmp/ocean_monitor_master.pid
```

当然，即使这样我好像也没有杀掉，就只能先查看进程
```
ps -A
```

然后手动杀掉了
```
kill ...
```
或者
```
killall uwsgi
```

### nginx

启动
```
sudo ngix
```

停止
```
sudo nginx -s stop
```

重启
```
sudo nginx -s reload
```
# celery

celery是python里面绕不开的一个框架,它是一个弥补goroutine的一个框架.

## 常用命令

```bash
# 安装
pip install -U Celery
pip install "celery[librabbitmq]"
pip install "celery[librabbitmq,redis,auth,msgpack]"

# 只使用redis
pip install -U "celery[redis]"
# 配置
app.conf.broker_url = 'redis://localhost:6379/0'
# 格式, URL 的所有配置都可以自定义配置的，默认使用的是 localhost 的 6379 端口中 0 数据库。（ Redis 默认有 16 个数据库）
redis://:password@hostname:port/db_number

# 运行worker
celery -A tasks worker --loglevel=info
celery worker --help
celery --help
```

## 常用代码片段

- `@task(bind=True)` 就会给这个方法添加一个`self`, 指定此`task`对象
- `default_retry_delay` 默认超时时间
- `max_retries` 重试次数
- `queue='name'` 队列名称
- `ignore_result=True`忽略执行结果
- `celeryconfig.py`定义一个配置模块,然后通过`app.config_from_object('celeryconfig')`来加载, 并且通过`python -m celeryconfig`来检查是否配置正确.
```py
from celery import Celery

CELERY_BROKER = os.environ.get('CELERY_BROKER') # like:
CELERY_BACKEND = os.environ.get('CELERY_BACKEND') # like: 


# celery.Celery(第一个参数是设置主模块的名称)
app = celery.Celery('tasks', broker=CELERY_BROKER, backend=CELERY_BACKEND)

# 配置
# 通过 task_serializer 选项可以指定序列化的方式：
# app.conf.task_serializer = 'json'

# 如果需要配置多个选项，可以通过 update 进行配置：
# app.conf.update(
#     task_serializer='json',
#     accept_content=['json'],  # Ignore other content
#     result_serializer='json',
#     timezone='Europe/Oslo',
#     enable_utc=True,
# )

# 当然我们选择加载module的方式
app.config_from_object('celeryconfig')

@app.task(bind=True, default_retry_delay=300, max_retries=5, ignore_result=True)
def my_task_a():
  try:
    print("doing stuff here...")
  except SomeNetworkExceptionas e:
    print("maybe do some cleanup here...")
    self.retry(e)
```

`@task(queue='队列名字')`, 会指定某一个队列来执行,否则使用`default`队列
```py
# 两个任务会在同一个队列(default)中执行
@app.task()
def my_task_a(a,b,c):
  print("doing something here...")

@app.task()
def my_task_b(x,y):
  print("doing something here...")

```
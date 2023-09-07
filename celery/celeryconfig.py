# 针对大型的项目，建议使用专用配置模块，进行针对 Celery 配置。
# 不建议使用硬编码，建议将所有的配置项集中化配置。集中化配置可以像系统管理员一样，当系统发生故障时可针对其进行微调。
# 可以通过 `app.config_from_object()` 进行加载配置模块：

broker_url = 'redis://localhost:6379/0'
result_backend = 'redis://localhost:6379/1'

task_serializer = 'json'
result_serializer = 'json'
accept_content = ['json']
#timezone = 'Europe/Oslo'
timezone = 'UTC'
enable_utc = True

task_routes = {
    'tasks.add': 'low-priority',
}

# 限速, 每分钟10个任务
task_annotations = {
    'tasks.add': {'rate_limit': '10/m'}
}

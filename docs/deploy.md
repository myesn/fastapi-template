# 服务器部署

1. 将代码上传至服务器
2. 在代码根目录中执行以下命令：
    ```
    uv run gunicorn app.main:app --env ENVIRONMENT=staging
    ```
   注意，`ENVIRONMENT` 值决定了要使用的配置文件：
    - `local` 本机(默认值): `.env.local`
    - `staging` 测试: `.env.staging`
    - `production` 正式: `.env.production`

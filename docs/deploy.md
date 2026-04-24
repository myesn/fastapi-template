# 直接在机器上部署

1. 将代码上传至服务器
2. 在代码根目录中执行以下命令：
    ```
    # 测试环境
    uv run gunicorn app.main:app --env ENVIRONMENT=staging
    ```
   通过 `ENVIRONMENT` 环境变量切换配置：
   - `local` 本机: `.env.local`
   - `staging` 测试: `.env.staging`
   - `production` 正式: `.env.production`

# Docker 部署

## 环境准备

确保服务器已安装 Docker 和 Docker Compose

## 构建并启动

检查 `docker-compose.yml` 文件内容，确认无误后将代码上传至服务器，然后在代码根目录中执行以下命令：

```bash
# 构建 fastapi-template 镜像并启动所有服务
docker compose up -d --build

# 查询容器状态
docker compose ps

# 查看日志
docker compose logs -f app
docker compose logs -f db

# 停止所有服务
docker compose stop
# 启动所有服务
docker compose start
# 重新启动所有服务
docker compose restart

# 查看 app、db 容器的 volume
docker volume inspect fastapi-template_app_static
docker volume inspect fastapi-template_postgres_data
```

## 删除和清理

```bash
# 停止并删除容器（保留数据库数据）
docker compose down

# 停止并删除容器和数据卷（会删除数据库数据）
docker compose down -v
```

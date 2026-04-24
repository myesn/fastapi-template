# 说明

一个简洁的 [FastAPI](https://fastapi.tiangolo.com/) 项目模版。

## 功能特性

- **Python 3.14+**，使用 Python 3.14 及以上版本
- **Web 框架**，FastAPI + Uvicorn
- **数据库**，SQLModel + asyncpg (异步 PostgreSQL)
- **多环境配置**，`.env.local` / `.env.staging` / `.env.production`
- **静态文件**，多文件上传/下载
- **CRUD 示例**，User 增删改查接口
- **CORS**，跨域支持
- **uv**，项目管理和依赖
- **部署**：
  - 直接在服务器上部署，Gunicorn + Uvicorn Worker
  - 使用 Docker Compose 部署

## 快速开始

启动项目：

```bash
uv run uvicorn app.main:app
```

# 部署

参考 [部署文档](docs/deploy.md)

# 开发文档参考

- [FastAPI](https://fastapi.tiangolo.com/)
- [SQLModel](https://sqlmodel.tiangolo.com/)
- [Running with Gunicorn](https://uvicorn.dev/#running-with-gunicorn)
- [Gunicorn](https://gunicorn.org/)
# 基础镜像
FROM python:3.11.4

# 设置工作目录
WORKDIR /app


VOLUME ["/data"]

# 复制项目文件到工作目录
COPY . /app/

# 安装依赖
RUN pip install -r requirements.txt

# 启动应用程序
CMD ["python", "ota_server/manage.py", "runserver", "0.0.0.0:8901"]
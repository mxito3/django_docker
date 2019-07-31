FROM python:3
ENV PYTHONUNBUFFERED 1
ENV TZ=Asia/Shanghai
#　项目名字
ENV DJANGO_SETTINGS_MODULE=mysite.settings 
# 时区
RUN ln -snf /usr/share/zoneinfo/$TZ /etc/localtime && echo $TZ > /etc/timezone && \
    mkdir /code && \
    mkdir /code/log/ && cd /code/log &&rm -rf request.log  && touch request.log
WORKDIR /code
ADD . /code/
RUN pip install -i https://mirrors.aliyun.com/pypi/simple --trusted-host mirrors.aliyun.com -r requirements.txt
# 开放的端口
EXPOSE 8000


FROM nginx
ENV TZ=Asia/Shanghai
# 时区
RUN ln -snf /usr/share/zoneinfo/$TZ /etc/localtime && echo $TZ > /etc/timezone && \
    mkdir /code && \
    mkdir /code/log/ && rm -rf /etc/nginx/conf.d/default.conf
WORKDIR /code
ADD . /code/
#复制单个文件
ADD ./django.conf /etc/nginx/conf.d/
#复制文件夹
ADD ./html/ /usr/share/nginx/html/
EXPOSE 80
EXPOSE 3334


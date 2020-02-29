# resetful-flask-template

## 简介
该项目是resetful风格的flask框架的后端模板。
在flask_resetful的基础上，做了一些架构的调整，添加了一些功能，以便更便捷地开发。

## 功能
* 架构
    * 视图函数模块化
    * 拦截器验证token和设置上下文
* 数据库
    * sqlite、mysql/mariadb连接示例
    * 两个示例表，包含不同类型字段和外键
* 视图示例（用户）
    * 用户登录、信息获取、修改密码功能，即增删改查完整示例
    * 登录后token生成，存入redis
* 文件
    * 文件上传接口示例
    * 文件url下载、流文件下载示例
from server import app, redis
from flask import request, g


@app.before_request
def before_request():
    # 此处拦截请求，验证其token
    # 设置白名单，无需token验证
    white_list = [
        '/user/login'
    ]
    if request.path not in white_list:
        # 获取token来获取存储的详细用户信息
        token = request.args.get('token')

        if not token or redis.exits(token):
            return {
                'code': 50008
            }
        elif not redis.exits(token):
            return {
                'code':    50008,
                'message': '验证码过期,请重新登录'
            }
        else:
            if request.method == 'OPTIONS':
                return {
                    'code': 20000
                }

            user_info = redis.get(token)
            g.token = token
            g.username = user_info.get('username')
            g.uid = user_info.get('uid')

import requests

def login_and_send_message(username, password, telegram_bot_token, telegram_chat_id):
    # 登录网站的 URL
    login_url = 'https://example.com/login'
    # 登录后主页的 URL（或其他需要访问的页面）
    home_url = 'https://duckyci.com/auth/login?redirect=https%3A%2F%2Fdash.duckyci.com%2F'
    # 要发送消息的 Telegram API URL
    telegram_url = f'https://api.telegram.org/bot{telegram_bot_token}/sendMessage'

    # 创建一个会话对象
    with requests.Session() as session:
        # 获取登录页面
        session.get(login_url)

        # 提交登录表单，使用网页的 id 作为键
        login_data = {
            'r0': username,  # 'user_id' 对应输入框的 id
            'r1': password,  # 'pass_id' 对应输入框的 id
        }
        response = session.post(login_url, data=login_data)

        # 访问登录后主页
        home_response = session.get(home_url)

        # 根据状态码判断登录是否成功
        if home_response.status_code == 200:
            message = "Login successful."
        else:
            message = "Login failed. Please check your credentials."

        # 发送 Telegram 消息
        telegram_data = {
            'chat_id': telegram_chat_id,
            'text': message,
        }
        response = requests.post(telegram_url, data=telegram_data)
        print(f'Telegram response: {response.text}')

if __name__ == '__main__':
    import os
    username = os.environ['USERNAME']
    password = os.environ['PASSWORD']
    telegram_bot_token = os.environ['TELEGRAM_BOT_TOKEN']
    telegram_chat_id = os.environ['TELEGRAM_CHAT_ID']

    login_and_send_message(username, password, telegram_bot_token, telegram_chat_id)

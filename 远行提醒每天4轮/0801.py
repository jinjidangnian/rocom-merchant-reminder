from get_merchant_props import get_all_props
import os
import requests  # 1. 在最开头导入 requests 库

# 调用函数获取数据
props = get_all_props()

result_0801_text = "【远行商人】 第1轮 \n"
for prop in props:
    name = prop.get("name")
    prop_start_ts = prop.get("start_time") # 这里拿到的是原始的时间戳毫秒数
    
    if int(prop_start_ts / 14400000) % 6 == 0:
        line = f"{name}\n"
        result_0801_text += line
        print(result_0801_text)
print(1)
print(result_0801_text)

def send_to_wechat(content):
    # 从环境变量中读取 Webhook 地址（我们在 GitHub Secrets 里配置过）
    webhook_url = os.getenv("WECHAT_WEBHOOK_URL")
    
    if not webhook_url:
        print("未找到 WECHAT_WEBHOOK_URL 环境变量，请检查 GitHub Secrets 配置")
        return

    # 构造企业微信机器人要求的消息格式
    data = {
        "msgtype": "text",
        "text": {
            "content": content # 传入你拼好的商品列表
        }
    }

    # 发送 POST 请求
    try:
        response = requests.post(webhook_url, json=data)
        if response.json().get("errcode") == 0:
            print("消息已成功发送到企业微信群！")
        else:
            print(f"发送失败，企业微信返回：{response.text}")
    except Exception as e:
        print(f"发送请求出错：{e}")

# 3. 调用这个函数，把你原本要打印的文本传进去
send_to_wechat(result_0801_text)

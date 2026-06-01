import requests
import os  # 导入 os 模块，用于读取 GitHub Actions 注入的环境变量

# 获取远行商人今日所有的商品（道具）原始数据列表。
def get_all_props():
    # 接口地址、API 密钥和请求头
    url = "https://wegame.shallow.ink/api/v1/games/rocom/merchant/info"
    # API 密钥通过 Secrets 读取
    ROCOM_API_KEY = os.getenv("ROCOM_API_KEY")  
    headers = {"X-API-Key": ROCOM_API_KEY}  # API 密钥放入 X-API-Key 字段中
    try:
        # 发送 GET 请求，获取接口数据，timeout=10，在状态码不是200时主动报错
        response = requests.get(url, headers=headers, timeout=10)
        response.raise_for_status()
        
        # 将接口返回的 JSON 格式字符串解析为 Python 字典
        data = response.json()
        
        # 按照接口数据结构，逐层提取出包含商品信息的 merchantActivities 列表
        activities = data["data"]["merchantActivities"]
        
        # 提取列表中的第一项，也就是代表今天商品排班的数据字典
        today_activities = activities[0]
        
        # 从今天的排班数据中获取 get_props 字段（即商品列表），如果不存在则返回空列表防止报错
        return today_activities.get("get_props", [])
    
    except requests.exceptions.Timeout:
        print("请求超时，请检查网络是否通畅。")
        return []
    
    except Exception as e:
        print(f"获取数据失败，报错原因：{e}")
        # 打印一下原始返回内容，方便你排查
        print(f"接口原始返回：{response.text}")
        return []

# 如果直接运行该脚本，则调用函数并打印获取到的商品列表（方便你在本地调试）
if __name__ == "__main__":
    props = get_all_props()
    print(props)

from get_merchant_props import get_all_props

# 调用函数获取数据
props = get_all_props()

result_0801_text = "【远行商人】 第3轮 \n"
for prop in props:
    name = prop.get("name")
    prop_start_ts = prop.get("start_time") # 这里拿到的是原始的时间戳毫秒数
    
    if int(prop_start_ts / 14400000) % 6 == 2:
        line = f"{name}\n"
        result_0801_text += line
        print(result_0801_text)
print(1)
print(result_0801_text)
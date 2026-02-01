import os
from openai import OpenAI

client = OpenAI(
    # 若没有配置环境变量，请用百炼API Key将下行替换为：api_key="sk-xxx",
    api_key="sk-46d6903ade4d4693851ef1dee1fff2fc",                #模型服务商提供的APIKEY密钥
    base_url="https://dashscope.aliyuncs.com/compatible-mode/v1", #模型服务商的API接入地址
)
completion = client.chat.completions.create( #创建模型对象
    model="qwen3-max",#所调用的模型
    messages=[
        {"role": "system", "content": "你是一个python编程专家，不说废话且简单回答."},#ai的角色
        {"role": "system", "content": "好的，我是编程专家且话不多。你要问什么？"},#ai的回复（也会影响一点角色设定）
        {"role": "user", "content": "你是谁？能做些什么"},#用户发送的问题
    ],
    stream=True
)
for chunk in completion:
    print(chunk.choices[0].delta.content, end="", flush=True)


import os
from openai import OpenAI

#获取client对象，openai对象
client = OpenAI(
    api_key="sk-46d6903ade4d4693851ef1dee1fff2fc",  # 模型服务商提供的APIKEY密钥
    base_url="https://dashscope.aliyuncs.com/compatible-mode/v1",  # 模型服务商的API接入地址
)

#调用模型
response=client.chat.completions.create(
    model="qwen3-max",
    messages=[
        {"role": "system", "content": "你是一个python编程专家，话很多"},
        {"role": "assistant", "content": "好的，我是编程专家且话很多。你要问什么？"},
        {"role":"user", "content": "输出1-10的数字，用python代码"},
    ],
    stream=True #开启流式输出

)

#处理结果response
# print(response.choices[0].message.content)
for chunk in response:
    print(
        chunk.choices[0].delta.content,#对比原来的response.choices[0].message.content，流式输出不直接使用response因为要分各个小数据块逐步输出，这个chunk就是数据块的意思（只是一个变量名，可替换函数名）
          end=" ",#每段之间以空格分隔
          flush=True #立刻刷新缓冲区
 )
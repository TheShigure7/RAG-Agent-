import  json

#python里的字典
d={
  "name":"小明",
    "sex":"男",
    "age":"11"
}

s=json.dumps(d,ensure_ascii=False)#字典转换为json数据，ensure_ascii=False保证中文转换不乱码

print(d)
print(str(d))

print(s)


l=[
    {
      "name":"小明",
        "sex":"男",
        "age":"11"
    },
    {
      "name":"小红",
        "sex":"女",
        "age":"12"
    },
    {
      "name":"小小",
        "sex":"男",
        "age":"3"
    }
]

sl=json.dumps(l,ensure_ascii=False)

print(l)
print(str(l))
print(sl)

json_str='{"name":"小明","sex":"男","age":"11"}'
json_array_str='[{"name":"小明","sex":"男","age":"11"},{"name":"小红","sex":"女","age":"12"},{"name":"小小","sex":"男","age":"3"}]'

d_json_str=json.loads(json_str)
s_json_array_str=json.loads(json_array_str)

print(json_str,type(json_str))
print(d_json_str,type(d_json_str))
print(json_array_str,type(json_array_str))
print(s_json_array_str,type(s_json_array_str))
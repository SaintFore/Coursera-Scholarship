from google import genai
from google.genai import types
# from PIL import Image
try:
    from config import API_KEY
except ImportError:
    print("未找到config.py文件")
    API_KEY = input("请输入您的 Gemini API Key: ")

course = input("请输入参加的课程: ")

client = genai.Client(api_key=API_KEY)
# image = Image.open("Saint_00065_.png")

response = client.models.generate_content_stream(
    model = "gemini-2.0-flash",
    contents = ["我要申请coursera的助学金，请你帮我写一下：您所选的课程将如何帮助您实现目标？课程是：" + course + "300个英语单词左右，下面给出中文翻译。"],
    config=types.GenerateContentConfig(
        max_output_tokens=2000,
        temperature=0.5
    )
)

for chunk in response:
    print(chunk.text, end="")
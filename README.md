# 🎓 Coursera 助学金申请助手

这个工具利用 Google Gemini AI 自动生成 Coursera 助学金申请中的课程目标陈述。

## ✨ 功能

- 📝 根据用户输入的课程名称，自动生成一篇约 300 字的英文陈述
- 🎯 说明所选课程将如何帮助实现个人目标
- 🈶 附带中文翻译
- 🤖 使用 Gemini AI 模型确保文本质量和流畅度

## 🚀 安装

1. 克隆此仓库
   ```bash
   git clone https://github.com/您的用户名/Coursera-Scholarship.git
   cd Coursera-Scholarship
   ```

2. 安装依赖
   ```bash
   pip install -r requirements.txt
   ```

3. 配置 API 密钥（两种方式）：
   - 方式一：创建 config.py 文件，添加以下内容：
     ```python
     API_KEY = "您的Gemini_API_KEY"
     ```
   - 方式二：首次运行时，系统会提示您输入 API 密钥

## 🔍 使用方法

运行脚本并按提示输入课程名称：

```bash
python coursera_scholarship.py
```

程序会自动生成适合助学金申请的课程目标陈述文本。

## 🔑 获取 Gemini API 密钥

1. 访问 [Google AI Studio](https://aistudio.google.com/)
2. 登录您的 Google 账户
3. 在设置中获取 API 密钥

## ⚠️ 注意事项

- 此项目用于学习和参考，请确保提交的申请内容符合 Coursera 的要求
- 建议对生成的文本进行个性化修改，以反映您的真实情况
- 请勿将您的 API 密钥提交到公共仓库

## 👥 贡献

欢迎提交 Issue 或 Pull Request 来改进此项目。

## 📄 许可

MIT
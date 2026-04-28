from openai import OpenAI
import os

os.environ["TOKENIZERS_PARALLELISM"] = "false"

# 1. 初始化客户端，指定本地服务地址（关键：api_base 指向 8000 端口）
client = OpenAI(
    api_key="dummy-key",  # vLLM 无需真实 API Key，填任意值即可
    base_url="http://localhost:11434/v1"  # 本地 vLLM 服务地址（必须加 /v1 后缀）
)

# 2. 调用大模型（chat/completions 接口）
def chat_with_local_model(prompt: str):
    try:
        # 发送对话请求
        response = client.chat.completions.create(
            model="autoglm-phone-9b:latest",  # 对应启动命令的 --served-model-name
            messages=[
                {"role": "system", "content": "你是一个智能助手，回答简洁准确"},
                {"role": "user", "content": prompt}
            ],
            temperature=0.7,  # 随机性（0-1，越小越精准）
            max_tokens=1024,   # 最大生成 token 数
            stream=False       # 非流式输出（如需流式见下文）
        )
        # 提取回答内容
        answer = response.choices[0].message.content
        return answer
    except Exception as e:
        return f"调用失败：{str(e)}"

# 3. 测试调用
if __name__ == "__main__":
    prompt = "解释一下什么是大模型的上下文窗口？"
    result = chat_with_local_model(prompt)
    print("模型回答：\n", result)
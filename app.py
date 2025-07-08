import os
from dotenv import load_dotenv
import streamlit as st
from langchain_community.chat_models import ChatOpenAI
from langchain.schema import SystemMessage, HumanMessage


# 環境変数を読み込む
load_dotenv()
openai_api_key = os.getenv("OPENAI_API_KEY")

# Streamlit UI
st.title("OpenAIテストアプリ（専門家を選んで質問しよう）")

# ユーザー入力
user_input = st.text_input("質問を入力してください：")

# ラジオボタンで専門家選択
expert_type = st.radio("相談する専門家を選んでください：", ["歴史学者", "心理学者", "経営コンサルタント"])

# 専門家に応じた system プロンプト
system_prompt_dict = {
    "歴史学者": "あなたは優秀な歴史学者です。ユーザーの質問に対して、歴史的な視点から丁寧に解説してください。",
    "心理学者": "あなたは経験豊富な心理学者です。心理的な視点でユーザーの悩みに寄り添って回答してください。",
    "経営コンサルタント": "あなたはプロの経営コンサルタントです。ビジネス上の課題に対して実践的な助言を提供してください。"
}

# 送信ボタン
if st.button("送信") and user_input:
    # LangChainのチャットモデルを使って回答生成
    chat = ChatOpenAI(openai_api_key=openai_api_key, model_name="gpt-3.5-turbo")

    messages = [
        SystemMessage(content=system_prompt_dict[expert_type]),
        HumanMessage(content=user_input)
    ]

    response = chat(messages)

    # 結果表示
    st.markdown("### 回答：")
    st.write(response.content)

# 使い方の説明
st.info("""
このアプリは、LangChainとOpenAIを使って、あなたの質問に「選んだ専門家の視点」で回答するアプリです。

1. 上のフォームに質問を入力してください。
2. 専門家の種類を選んで「送信」ボタンを押すと、AIが専門家として回答します。

※ Python 3.11 + Streamlit + LangChain 環境で動作します。
""")

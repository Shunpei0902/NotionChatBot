# NotionChatBot

タグ: IT, むすびえ
サブアイテム: LLM (LLM%20d3e6fff2f0b34a32bcfcef6446b13ab0.md), Transformer (Transformer%2054e290d441b14d70b80859eda3d9d6a0.md), ファインチューニング (%E3%83%95%E3%82%A1%E3%82%A4%E3%83%B3%E3%83%81%E3%83%A5%E3%83%BC%E3%83%8B%E3%83%B3%E3%82%AF%E3%82%99%20d979e3e83cca41bb9446e0c427815d6b.md), RAG (RAG%200140206302e64abc8c795917b8b9d724.md), エンベディング (%E3%82%A8%E3%83%B3%E3%83%98%E3%82%99%E3%83%86%E3%82%99%E3%82%A3%E3%83%B3%E3%82%AF%E3%82%99%20ea0c731f9d9a4cf18a6a699dcf9b67b1.md), LangChain (LangChain%2075fe2183d9d948849df3473a4171770f.md), Faiss (Faiss%20e52d804131f54469b32686c84ed48272.md), Streamlit (Streamlit%20972907f5ce3e401481f1d8dc22bc1da8.md)
作成日: 2024年4月16日
親アイテム: 💻IT (%F0%9F%92%BBIT%20ef34be92b83548d18faba8d778178b3a.md)

## 概要

![Untitled](NotionChatBot%20a9f381d1a9db43ef8df3448171957b12/Untitled.png)

1. LangChain を使用して Notion コンテンツをロードおよび分割
2. OpenAI 埋め込みを使用してベクトルに変換し、ベクトル データベース (この場合は FAISS) に保存
3. LangChain を使用して、ベクトル データベースと OpenAI GPT をリンクする会話型検索チェーンを構築し、ユーザーの質問に答える
    - 答えは、Notion コンテンツにある最も関連性の高い情報に基づく。
4. カスタム システム プロンプトを作成し、それにメモリを追加することで、チャットボットを改善する
5. Streamlit を使用してチャット インターフェイスを作成し、アプリを Notion に直接埋め込みます。

[LangChain](LangChain%2075fe2183d9d948849df3473a4171770f.md) 

## ロードマップ

## **ステップ 1: プロジェクトの構造と初期化**

1. プロジェクトの構造を確認し、必要な依存関係をインストール
2. OpenAI API キーを取得し、ベースとして機能するパブリック Notion ページを複製

### **1.1 プロジェクトの構造**

- `.streamlit/secrets.toml`
    
    ⇒ OpenAI API キーを保存する
    
- `faiss_index`
    
    ⇒ すべてのベクトルが格納されている FAISS インデックス (ベクトル データベース)
    
- `notion_content`
    
    ⇒ Notion コンテンツを含むフォルダー (マークダウン ファイル内)
    
- `.gitignore`
    
    ⇒ OpenAI API キーと Notion コンテンツを無視する
    
- `app.py`
    
    ⇒ Streamlitチャットアプリのスクリプト
    
- `ingest.py`
    
    ⇒ Notion コンテンツをベクトルに変換し、ベクトル インデックスに保存するスクリプト
    
- `utils.py`
    
    ⇒ 会話検索チェーンを作成するスクリプト
    
- `requirements.txt`
    
    ⇒ Streamlit Community Cloudへのデプロイに必要なパッケージ
    

### **1.2 プロジェクトの初期化**

1. プロジェクトフォルダーの作成
2. 新しい環境を作成し、必要な依存関係をインストール

```bash
pip install streamlit langchain openai tiktoken faiss-cpu
```

1. `.gitignore`ファイルを作成し、追跡しないファイルを指定

```
# .gitignore

 notion_content/ 
.streamlit/
```

1.  [OpenAI の Web サイト](https://platform.openai.com/overview)にアクセスしてAPI キーを取得
2. フォルダを作成`.streamlit`
3. OpenAI API キーを保存する`secrets.toml`ファイルを`.streamlit` フォルダに格納

```
# Secrets.toml 

OPENAI_API_KEY = 'sk-A1B2C3D4E5F6G7H8I9J'
```

## **ステップ 2: ドキュメントの取り込み**

### **Notion ページのすべてのコンテンツを数値表現 (ベクトル) に変換**

1. GPT のような LLM は非常に長いテキストを処理できないため、LangChain を使用して最初にテキストコンテンツを小さなテキストチャンクに分割
2. 分割したら、OpenAI の埋め込みモデルを使用してベクトルに変換。
3. ベクトルをベクトル データベースに保存

### **2.1 Notion コンテンツをエクスポートする**

Notion の API を使用して Notion コンテンツを取得することもできるがここではコンテンツを手動でエクスポートする。

## **ステップ 3: クエリ**

## **ステップ 4. チャットボット アプリケーション**

## 参考資料

[https://logan-vendrix.medium.com/create-your-own-notion-chatbot-with-langchain-openai-and-streamlit-fcb385f432a2](https://logan-vendrix.medium.com/create-your-own-notion-chatbot-with-langchain-openai-and-streamlit-fcb385f432a2)
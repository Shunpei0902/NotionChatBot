# LLM

タグ: IT
作成日: 2024年4月16日
親アイテム: NotionChatBot (NotionChatBot%20a9f381d1a9db43ef8df3448171957b12.md)
説明: 大規模言語モデル（LLM：Large language Models）：
大量のデータとディープラーニング（深層学習）技術によって構築された言語モデル

## 概要

大規模言語モデル（LLM：Large language Models）

- **大量のデータとディープラーニング（深層学習）技術によって構築された言語モデル**

言語モデル

- 文章や単語の出現確率を用いてモデル化したもの
- 文章作成などの自然言語処理で用いられる

![Untitled](LLM%20d3e6fff2f0b34a32bcfcef6446b13ab0/Untitled.png)

ここでいう「大規模」とは、従来の自然言語モデルと比べ、後述する3つの要素「計算量」「データ量」「パラメータ数」を大幅に増やして構築されていることに由来している

- データ量：入力される情報量
- 計算量：コンピューターが処理する計算量
- パラメータ量：確率計算を行うための係数量

3つの巨大化については、2020年にOpenAIが発表した「Scaling Laws for Neural Language Models*1」という論文で説明されている

この論文では、自然言語モデルの性能と、3つの要素「計算量」「データ量」「モデルパラメータ数」との間に、「Scaling Law（べき乗則）」が成立すると提唱された

OpenAIは、「計算量」「データ量」「モデルパラメータ数」の3つを著しく巨大化することで、極めて精度の高い大規模言語モデルを生成することに成功した

![Untitled](LLM%20d3e6fff2f0b34a32bcfcef6446b13ab0/Untitled%201.png)

大規模言語モデルは、2017年にGoogleにより発表された「Transformer」がきっかけとなって構築された

<aside>
💡 [Transformer](Transformer%2054e290d441b14d70b80859eda3d9d6a0.md)

</aside>

## **大規模言語モデル（LLM）の仕組み**

1. トークン化：入力文を最小単位に分別
2. 文脈理解：プロンプト内の各トークンとの関連性を計算
3. エンコード：特徴量の抽出
4. デコード：次のトークンを予測
5. 入力文の次のトークンの確率を出力

- 大規模言語モデルは基本的にTransformerの仕組みを利用
- 従来の言語モデルでは、テキストデータであれば単語に分割した後に人がラベル付けをする必要があった
- しかし、大規模言語モデルでは大量のテキストデータを与えることで、トークンから文脈や言葉の意味を学習できる
- 学習した結果から、特定の言葉に続く確率が高いと考えられる言葉・文章を並べられるものが大規模言語モデル

## **大規模言語モデル（LLM）の種類**

大規模言語モデルの礎となったTransformerをもとに開発された有名な大規模言語モデル

### **BERT**

BERT（Bidirectional Encoder Representations from Transformers）は、2018年にGoogleの論文で発表された自然言語処理モデル

日本語では「Transformerによる双方向のエンコード表現」と訳される

BERTは文章を文頭と文末（双方向）から学習することで「文脈を読める」ようになった

BERTは、28億語のWikipediaデータと8億語のGoogle BookCorpusデータで合計33億語のデータからトレーニングされている

### **GPT-3**

GPT（Generative Pre-trained Transformer）は大量のテキストデータを事前学習した後に、特定のタスクに適用させるファインチューニングと呼ばれる学習をする2段階の学習モデル
GPT-3は、45TB（テラバイト）のデータ（最終的に合計4990億トークン）からトレーニングされている

GPT-3はOpenAI社によって2020年に発表され、ChatGPTではチャット向けにファインチューニングしたGPT-3.5が利用されてる

<aside>
💡 [ファインチューニング](%E3%83%95%E3%82%A1%E3%82%A4%E3%83%B3%E3%83%81%E3%83%A5%E3%83%BC%E3%83%8B%E3%83%B3%E3%82%AF%E3%82%99%20d979e3e83cca41bb9446e0c427815d6b.md)

</aside>

### **GPT-4**

GPT-4は2023年にアップデートされたGPTの最新版であり、テキストだけでなく画像などの入力を受け取ってテキストを出力できる「マルチモーダル」なモデル

GPT-3.5で扱えるトークンの最大数は4,097であったのに対し、GPT-4では3万2,768トークンと約8倍に増えた

## 参考資料

[https://www.hitachi-solutions-create.co.jp/column/technology/llm.html](https://www.hitachi-solutions-create.co.jp/column/technology/llm.html)
[https://www.nri.com/jp/knowledge/glossary/lst/ta/llm](https://www.nri.com/jp/knowledge/glossary/lst/ta/llm)

[https://atmarkit.itmedia.co.jp/ait/articles/2303/13/news013.html](https://atmarkit.itmedia.co.jp/ait/articles/2303/13/news013.html)
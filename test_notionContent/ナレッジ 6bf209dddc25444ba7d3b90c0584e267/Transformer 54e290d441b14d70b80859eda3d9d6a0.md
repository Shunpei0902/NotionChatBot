# Transformer

タグ: IT
作成日: 2024年4月16日
親アイテム: NotionChatBot (NotionChatBot%20a9f381d1a9db43ef8df3448171957b12.md)
説明: 系列変換のためのニューラルネットワーク

## 概要

**ニューラルネットワーク（NN ：人間の脳の仕組みを模倣した機械学習モデル）の一種**

- 2017年にGoogleが「Attention Is All You Need」という論文で紹介

### **ChatGPTやBard、Bingなどの対話型AIのベースとなった技術**

従来の技術と異なり、「Attention Mechanism」を主体に処理を行う

Attention Mechanism

- シーケンスデータ（テキスト、音声、時間に関連するデータなど）の各要素と他の要素との関連性を計算する仕組み
    - 例）文章内の各単語が他の単語とどれだけ関連しているかを計算し、その情報を利用して文脈を理解

Transformerは、Attention Mechanismにより、文中の離れた単語間の関連性を効率的に捉えることが可能であり、その並列計算の能力により大量のデータを高速に処理できる

### **系列変換タスクのためのニューラルネットワークモデル**

系列変換とは、ある系列の入力（例：英語の文）を別の系列の出力（例：フランス語の文）に変換するタスク

機械翻訳は系列変換タスクの一例

ニューラルネットワークモデルとは、人間の脳の神経細胞（ニューロン）の接続を模倣した機械学習モデルの一種

全体の関連性を捉えながら、各英語の単語がどのフランス語の単語に対応するかを学習することで高い精度を実現している

## **Transformerの仕組み**

![Untitled](Transformer%2054e290d441b14d70b80859eda3d9d6a0/Untitled.png)

上図では、左半分がエンコーダ、右半分がデコーダを表す

### **エンコーダの仕組み**

- エンコーダは、**入力データを解析し、その結果をデコーダに渡す**
- 入力文章を赤のEmbedding層で圧縮、Position Encoding層で入力の位置(単語が文のどこにあるか、など)を付加し、メイン部分に入力
- **Self-Attention層（Multi-Head Attention）**と **Position-wise Feed-Forward Networks（FFNN）**という二つのサブレイヤーから構成される

**Self-Attention層**

- 文中の各単語が他の単語とどの程度関連しているかを評価

例）「猫がマットの上に座った」という文において、「猫」の単語が他の各単語とどの程度関連しているかを判断する

**FFNN**

- Self-Attention層から得られた各単語の新たな表現をさらに深化させる
- これにより、より複雑な文脈を理解し、精緻な単語表現を生み出す

それぞれのサブ層の後には残差接続と正規化処理（Add & Norm層）が採用されている

### **デコーダの仕組み**

- デコーダは、エンコーダから得た情報を基に出力データを生成
- デコーダの構成はエンコーダに似ているが、Self-Attention層とPosition-wise Feed-Forward Networks（FFNN）の間に、Encoder-Decoder Attention層が存在する
    - エンコーダと同様にそれぞれのサブ層はAdd & Norm層によって正規化
- 最初のMulti-Head Attentionはmasking(入力文章の単語のうちの一部をハイフンなどで置き換えること)されており、Position Encoding層からの情報をマスクする（隠す）役割を担っている
- デコーダの各サブレイヤーは以下のように連携して動作する

| Self-Attention層 | デコーダの現在までの各単語が他の単語とどのように関連しているかの理解 |
| --- | --- |
| Encoder-Decoder Attention層 | エンコーダからの入力とデコーダの現在の状態との関連性を評価
デコーダは適切な出力を生成するために、どの入力情報に焦点を当てるべきかを判断 |
| Position-wise Feed-Forward Networks（FFNN） | より複雑な文脈を理解し、精緻な単語表現を生成 |

### **Multi-Head Attentionの仕組み**

**Multi-Head Attention**

- Self-Attentionのモデルを並列で行っている構造
- **それぞれの単語が文脈全体でどのように位置づけられるかを深く把握する（Transformerの中心的な要素）**
    - 文章の前から順に1単語ごとに処理されていくが、モデルが各単語を処理するときに、他の単語の位置を調べてこの単語のエンコードをより精度の高いものにする

![Untitled](Transformer%2054e290d441b14d70b80859eda3d9d6a0/Untitled%201.png)

エンコーダやデコーダで使用されるSelf-Attention層とEncoder-Decoder Attention層は、構成自体は全く同じで、違いはどの情報に注目するかという点

Self-Attention

- 一つの文中で各単語が他の単語とどのように関連しているかを評価 → 各単語が文全体のどの部分と関連しているかを理解

Encoder-Decoder Attentionは

- エンコーダからの入力文とデコーダの現在の状態（すでに生成された単語のシーケンス）との関連性を評価
- デコーダはどの入力情報に注目すべきかを判断し、適切な出力を生成

## **Transformerの特徴**

### **並列化による計算効率の向上**

Transformerは、**計算処理を並列化できるため、計算効率を大幅に向上させる**ことが可能

- 従来のニューラルネットワークであるRNNとは異なり、Transformerは文中の各単語を独立して処理できる → 各単語の処理を並列化し、計算の効率化を実現

### **優れた翻訳品質**

Transformerは、Self-Attention Mechanismを駆使することにより、各単語が文章内の他の単語とどのように関連しているかを学習することが可能で、文章をより深く理解できる

- 従来の対話型AIの基盤となっていた技術であるRNNやCNNが抱える問題点
    - RNN：単語を順序通りに処理する特性があり、学習速度が遅く、単語間の時間的な依存関係を捉えにくい
    - CNN：単語の局所的なパターン抽出が得意だが、単語間の全体的な関連性を捉えにくい
- Transformerは、文中の各単語が他の単語とどの程度関連しているかを直接モデリングでき、単語間の依存関係を効率的に学習できる
- また，並列処理が可能で大量のデータを高速に処理できることで、従来のRNNやCNNと比較して、優れた翻訳品質を実現できる

### **Self-Attentionによる高い適用性**

- **Self-Attentionの活用により、自然言語処理、画像処理、音声処理などのさまざまなタスクに対応可能**な柔軟性を持つ
    - Self-Attentionは、文の全体的な文脈を把握し、それぞれの単語の重要性を評価できる
    - 自然言語だけでなく、画像や動画、音声などの非言語的なデータにも適応可能
    
    例）画像を一連のパッチに分割して扱うことで、各パッチが画像全体のどの部分と関連しているかを認識できる。画像内のオブジェクト間の関係を認識したり、情報を抽出したりなど、さまざまなタスクに適応することが可能
    

Transformerの技術は自然言語処理だけでなく、画像処理や動画処理などの領域でも幅広く活用されている

## **Transformerをベースにしたモデル**

### **GPT（Generative Pre-trained Transformer）**

**GPTは、OpenAIが開発した自然言語生成モデル**

文章の生成、質問応答、文の補完など、幅広いタスクを処理することが可能

文の前後関係を考慮して単語の表現を学習するため、より自然な文章を生成できる

### **BERT（Bidirectional Encoder Representations from Transformers）**

**BERTはGoogleにより開発された自然言語処理モデルで、Google検索エンジンの改善や文章理解、感情分析などに活用**されている

BERTは、2つの文が与えられた場合に、それらの文が連続しているかどうかを判定し、文の関係性を理解することができる

### **PaLM（Pathways Language Model）**

**PaLMはGoogleが開発した自然言語処理モデル**

PaLMは、文脈を考慮した単語の表現を学習するため、文章の意味を理解し、文章の補完などのタスクに利用することができる

### **ViT（Vision Transformer）**

**ViTは、Transformerの技術をベースに開発された画像処理のモデル**で、主に画像分類や物体検出などの用途に活用されている

ViTは、Transformerのアーキテクチャを使用して画像の特徴を学習するため、より正確に画像の特徴を学習することができる

## 参考資料

[https://datamix.co.jp/media/datascience/what-is-transformer/](https://datamix.co.jp/media/datascience/what-is-transformer/)

[https://crystal-method.com/blog/transformer-2/](https://crystal-method.com/blog/transformer-2/)

[https://www.kikagaku.co.jp/kikagaku-blog/deep-learning-transformer/](https://www.kikagaku.co.jp/kikagaku-blog/deep-learning-transformer/)
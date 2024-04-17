# Clasp×Github Actions

タグ: IT, むすびえ
作成日: 2024年3月22日
親アイテム: 💻IT (%F0%9F%92%BBIT%20ef34be92b83548d18faba8d778178b3a.md)
説明: clasp：GASのソースコードをローカル環境で開発できるツール
github actions：Git上での特定のアクションに対してテストを走らせたり、buildコマンドを実行したり、実環境にデプロイしたりということを自動化する機能

[](https://github.com/musubie/versionControl)

[clasp×githubActionsで複数のgasプロジェクトを一つのリポジトリで管理し、自動デプロイまでできるようにした](https://zenn.dev/furnqse/articles/a138962560db56)

[GASのWebアプリケーションをGithubActions & Claspでデプロイする - Qiita](https://qiita.com/shunexe/items/fdf0def390a160d044c3)

## claspのインストール

**clasp：GASのソースコードをローカル環境で開発できるツール**

### npmのインストール

**node.jsのインストール**

- nodebrewのインストール

```bash
brew install nodebrew
```

- nodeのインストール

```bash
mkdir -p ~/.nodebrew/src
```

```bash
nodebrew install-binary stable
```

```bash
// 補足
stable 最新の安定版
latest 最新版
vXX.XX.X バージョン直接指定
```

- パスを通す

```bash
export PATH=$HOME/.nodebrew/current/bin:$PATH
```

- shell設定再読み込み

```bash
source ~/.zshrc
```

### claspのインストール

```bash
npm i @google/clasp -g
```

### claspの使い方

[claspでGASをgithub管理する](https://zenn.dev/flutteruniv_dev/articles/8013785f70a2f4)

### 参考サイト

[GitHub - google/clasp: 🔗 Command Line Apps Script Projects](https://github.com/google/clasp)

[[GAS]Macにclaspをインストール](https://yyuuiikk.org/entry/593)

[zsh: command not found: npmが出た時の対処法 - Qiita](https://qiita.com/ushi_osushi/items/586fd83728c01dcd04c4)

[【.zshrcファイルの作成】MacでzshのPATHの通し方【.zshrcファイルの更新】 | kamiblog](https://god48.com/zsh-path)

[claspを使ってGoogle Apps Scriptの開発環境を構築してみた | DevelopersIO](https://dev.classmethod.jp/articles/vscode-clasp-setting/)

## Github Actions

Git上での特定のアクションに対してテストを走らせたり、buildコマンドを実行したり、実環境にデプロイしたりということを自動化することができる

[GitHub Actions ドキュメント - GitHub Docs](https://docs.github.com/ja/actions)

[🔰GAS(Google Apps Script)の更新をGithub Actionsで自動化してみた - Qiita](https://qiita.com/yuzinet/items/17be9967b2c660ee8432)

```yaml
name: update GAS(Google Apps Script)

on:
  push:
    branches:
      - main
  workflow_dispatch:
jobs:
  deploy:
    runs-on: ubuntu-latest
    timeout-minutes: 15

    steps:
      - name: Checkout
        uses: actions/checkout@v3
      - name: Setup Node.js 16.x
        uses: actions/setup-node@v3
        with:
          node-version: '16.x'
      - name: Install Clasp
        run: |
          npm init -y
          npm install clasp -g
      - name: Create clasprc.json
        run: |
          echo \{\"token\":\{\"access_token\":\"${{ secrets.ACCESS_TOKEN}}\",\"scope\":\"https://www.googleapis.com/auth/userinfo.email https://www.googleapis.com/auth/drive.metadata.readonly https://www.googleapis.com/auth/script.projects https://www.googleapis.com/auth/script.webapp.deploy https://www.googleapis.com/auth/logging.read openid https://www.googleapis.com/auth/userinfo.profile https://www.googleapis.com/auth/drive.file https://www.googleapis.com/auth/script.deployments https://www.googleapis.com/auth/service.management https://www.googleapis.com/auth/cloud-platform\",\"token_type\":\"Bearer\",\"id_token\":\"${{ secrets.ID_TOKEN }}\",\"expiry_date\":1620870307822,\"refresh_token\":\"${{ secrets.REFRESH_TOKEN }}\"\},\"oauth2ClientSettings\":\{\"clientId\":\"${{ secrets.CLIENTID }}\",\"clientSecret\":\"${{ secrets.CLIENTSECRET }}\",\"redirectUri\":\"http://localhost\"\},\"isLocalCreds\":false\} > ~/.clasprc.json
      - name: Deploy
        run: |
          clasp push
```

[GitHub Actionsを使ってGASをデプロイしてみた | DevelopersIO](https://dev.classmethod.jp/articles/github-actions-gas-deploy/)

- シークレットについて

[GitHub Actions でのシークレットの使用 - GitHub Docs](https://docs.github.com/ja/actions/security-guides/using-secrets-in-github-actions)

### スプレッドシートの内部スクリプトを更新する

1. テンプレートの内部スクリプトを修正、update
2. 修正版内部スクリプトをgit push
3. pushをトリガーとして、指定のスクリプトIDにpushする

指定のスクリプトIDを可変にする（特定のメンバーの管理画面のスクリプトにpushする）

- .clasp.jsonを編集すれば任意のスクリプトにpush可能

```json
{
    "scriptId": "1HTeHXy8PnLU-E2YUdVA_5AAUnI5JFMzFsEIljgC59cebQQpM0EnW9tf9",
    "rootDir": "./src"
}
```

どうやって、動的に.clasp.jsonを更新、新規作成するか

上記のYAMLファイルは、GitHub Actionsのワークフロー定義で、Google Apps Script（GAS）のスクリプトを複数のプロジェクトに自動的にpushするためのものです。以下に各セクションの詳細な解説を行います。

### ワークフローのトリガー

```yaml
name: Deploy to Multiple GAS Projects

on:
  push:
    branches:
      - main

```

- `name`: ワークフローの名前を定義しています。
- `on`: このワークフローがどのGitHubイベントによってトリガーされるかを定義しています。ここでは、`main`ブランチへの`push`イベントによってトリガーされます。

### ジョブの定義

```yaml
jobs:
  deploy:
    runs-on: ubuntu-latest
    strategy:
      matrix:
        script-id: [ 'scriptId1', 'scriptId2' ]

```

- `jobs`: ワークフロー内で実行されるジョブを定義します。
- `deploy`: このジョブの名前です。
- `runs-on`: このジョブが実行される環境を指定します。ここでは、最新版のUbuntuを使用します。
- `strategy`: 複数の環境でジョブを実行するための戦略を定義します。
- `matrix`: ジョブが異なる変数セットで複数回実行されるように設定します。ここでは、`script-id`として異なるGASプロジェクトのIDをリストとして定義しています。

### ステップの定義

```yaml
steps:
  - name: Checkout
    uses: actions/checkout@v3

  - name: Setup Node.js
    uses: actions/setup-node@v3
    with:
      node-version: '14'

  - name: Install Clasp
    run: npm install -g @google/clasp

  - name: Setup Clasp Authentication
    run: echo '${{ secrets.CLASP_CREDENTIALS }}' > ~/.clasprc.json

  - name: Create Clasp Config
    run: |
      echo "{\\"scriptId\\":\\"${{ secrets[matrix.script-id] }}\\"}" > .clasp.json

  - name: Push to GAS Project
    run: clasp push

```

- `steps`: ジョブ内で実行される個々のタスクやアクションを定義します。
- `Checkout`: GitHubリポジトリをチェックアウトします。
- `Setup Node.js`: Node.jsをセットアップします。ここではバージョン14を使用します。
- `Install Clasp`: Google Claspをインストールします。
- `Setup Clasp Authentication`: Claspの認証情報を設定します。GitHub Secretsから認証情報を取得し、`.clasprc.json`ファイルに保存します。
- `Create Clasp Config`: 異なるGASプロジェクトIDに基づいて`.clasp.json`ファイルを動的に生成します。これは、matrix戦略により異なるスクリプトIDで複数回実行されます。
- `Push to GAS Project`: 変更された`.clasp.json`を使用して、Claspを介してGASプロジェクトにスクリプトをpushします。

このワークフローにより、`main`ブランチにpushされた変更が、指定された複数のGASプロジェクトに自動的に反映されます。

GitHubリポジトリをチェックアウトするというのは、GitHub上にホストされているリポジトリのコピーをローカル環境に作成することを意味します。これにより、リポジトリ内のファイルやコードにアクセスし、変更を加えることができます。GitHub Actionsの文脈では、ワークフローが実行される際にリポジトリのコンテンツが実行環境にダウンロードされることを指します。

GitHub Actionsにおける「チェックアウト」ステップの詳細：

- **GitHub Actionsが提供する`actions/checkout`アクション**:
    - このアクションはGitHubリポジトリのコードをGitHub Actionsのランナー（ワークフローが実行される仮想環境）にチェックアウトするために使用されます。
- **リポジトリのコンテンツへのアクセス**:
    - ワークフロー内の後続のステップでリポジトリのコンテンツにアクセスするためには、まず`actions/checkout`を使ってリポジトリをチェックアウトする必要があります。

例えば、以下のYAMLコードはGitHub Actionsワークフローでリポジトリをチェックアウトする方法を示しています：

```yaml
steps:
  - name: Checkout
    uses: actions/checkout@v3

```

このステップにより、GitHub Actionsのランナー環境にリポジトリの最新のコードがダウンロードされ、ワークフローの残りの部分でこのコードに対する操作が可能になります。これは、ビルドの実行、テストの実行、デプロイメント、その他の自動化されたタスクに必要な基本的なステップです。

- .clasp.jsonはセキュリティ上の観点からgit repositoryに含めない
    - scriptIdが含まれているため
    - プライベートなら別にいい

→ GitHub Actionsで動的に生成する
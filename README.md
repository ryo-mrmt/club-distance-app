# クラブ飛距離メモ
番手別に飛距離を記録、直近3球の平均、番手間の距離差を確認するためのアプリ。
趣味のゴルフで番手ごとの正確な飛距離を把握するために個人開発。

## 使用技術

- React 19
- Vite
- localStorage

## 機能

- クラブをドロップダウンで選択し、飛距離（yds）を記録
- 直近3球の平均飛距離を自動計算・リアルタイム更新
- 記録がある番手の前後2番手との飛距離差を表示
- 履歴の折りたたみ表示
- 1球ずつの削除・まとめて削除
- ダークモードUI
- バリデーション（空欄・文字・0以下の入力を防止）

## クラブリスト

ウッド（1W〜11W）、UT（2〜7）、アイアン（4I〜9I）、ウェッジ（46°〜60°）

## セットアップ

```bash
git clone https://github.com/nuralilock0621-cyber/club-distance-app.git
cd club-distance-app
npm install
npm run dev
```

## コンポーネント構成

App.jsx（状態管理）
├ InputForm.jsx（クラブ選択・飛距離入力・記録）
└ ClubList.jsx（リスト全体の管理）
├ ClubRow.jsx（平均・番手差・履歴の開閉）
└ HistoryRow.jsx（1球ごとの記録・削除ボタン）

## データ構造

```js
{
  id: Date.now(),
  club: "7I",
  distance: 160,
  strokeNumber: 1,
  day: "2026-04-28"
}
```

## テスト

Selenium + PythonによるE2Eテスト（10ケース）

- ページ表示確認
- バリデーション（空欄・0以下）
- 記録・平均計算・クラブ切り替え
- 履歴の開閉
- 1件削除・まとめて削除
- リロード後のデータ永続化

```bash
pip install selenium
python test_club_distance.py
```

## 今後の予定

- Node.js + Express + データベースによるバックエンド実装
- セッション（練習ラウンド単位）管理機能
- レスポンシブ対応

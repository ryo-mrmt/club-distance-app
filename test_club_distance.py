"""
クラブ飛距離メモアプリ E2Eテスト
Selenium + Python
事前準備: pip install selenium
実行方法: python test_club_distance.py
対象URL: http://localhost:5173（npm run devで起動しておくこと）
"""

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.keys import Keys
import time

# ========================================
# セットアップ
# ========================================
driver = webdriver.Chrome()
driver.get("http://localhost:5173")
wait = WebDriverWait(driver, 10)

# テスト前にlocalStorageをクリア
driver.execute_script("localStorage.clear()")
driver.refresh()


# ========================================
# テスト①：ページが正しく表示されるか
# ========================================
print("テスト① ページ表示...")

# タイトルが表示されているか
title = driver.find_element(By.TAG_NAME, "h1")
assert title.text == "クラブ飛距離メモ", f"タイトルが違う: {title.text}"

# ドロップダウンが存在するか
select = driver.find_element(By.TAG_NAME, "select")
assert select is not None

# 入力欄が存在するか
input_field = driver.find_element(By.CSS_SELECTOR, "input[type='number']")
assert input_field is not None

# 記録ボタンが存在するか
button = driver.find_element(By.TAG_NAME, "button")
assert button.text == "保存"

print("  → OK：ページ要素がすべて表示されている")


# ========================================
# テスト②：バリデーション（空欄）
# ========================================
print("テスト② バリデーション（空欄）...")

# 空欄のまま記録ボタンを押す
button = driver.find_element(By.TAG_NAME, "button")
button.click()

# アラートが出るか
alert = wait.until(EC.alert_is_present())
assert "数値を入力してください" in alert.text
alert.accept()

print("  → OK：空欄でアラートが出た")


# ========================================
# テスト③：バリデーション（0以下）
# ========================================
print("テスト③ バリデーション（0以下）...")

# -10を入力して記録ボタンを押す
input_field = driver.find_element(By.CSS_SELECTOR, "input[type='number']")
input_field.clear()
input_field.send_keys("-10")

button = driver.find_element(By.TAG_NAME, "button")
button.click()

# アラートが出るか
alert = wait.until(EC.alert_is_present())
assert "ミスショット" in alert.text
alert.accept()

print("  → OK：0以下でアラートが出た")


# ========================================
# テスト④：正常な記録
# ========================================
print("テスト④ 正常な記録...")

# 入力欄をクリアして160を入力
input_field = driver.find_element(By.CSS_SELECTOR, "input[type='number']")
input_field.clear()
input_field.send_keys("160")

# 記録ボタンを押す
button = driver.find_element(By.TAG_NAME, "button")
button.click()

# 入力欄がリセットされたか
time.sleep(0.5)  # 画面更新を待つ
input_field = driver.find_element(By.CSS_SELECTOR, "input[type='number']")
assert input_field.get_attribute("value") == "", "入力欄がリセットされていない"

# localStorageにデータが保存されたか
records = driver.execute_script("return localStorage.getItem('records')")
assert records is not None, "localStorageにデータがない"
assert "160" in records, "飛距離160が保存されていない"

print("  → OK：記録が保存され入力欄がリセットされた")


# ========================================
# テスト⑤：平均表示
# ========================================
print("テスト⑤ 平均表示...")

# 2球目: 155を記録
input_field = driver.find_element(By.CSS_SELECTOR, "input[type='number']")
input_field.send_keys("155")
driver.find_element(By.TAG_NAME, "button").click()
time.sleep(0.3)

# 3球目: 165を記録
input_field = driver.find_element(By.CSS_SELECTOR, "input[type='number']")
input_field.send_keys("165")
driver.find_element(By.TAG_NAME, "button").click()
time.sleep(0.3)

# 平均が160になっているか
# (160 + 155 + 165) / 3 = 160
page_text = driver.find_element(By.CLASS_NAME, "result-card").text
assert "160" in page_text, f"平均160が表示されていない: {page_text}"

print("  → OK：直近3球の平均が正しく表示された")


# ========================================
# テスト⑥：クラブ切り替え
# ========================================
print("テスト⑥ クラブ切り替え...")

# ドロップダウンを8Iに変更
from selenium.webdriver.support.ui import Select

select_element = driver.find_element(By.TAG_NAME, "select")
select = Select(select_element)
select.select_by_value("8I")
time.sleep(0.3)

# 8Iで148を記録
input_field = driver.find_element(By.CSS_SELECTOR, "input[type='number']")
input_field.send_keys("148")
driver.find_element(By.TAG_NAME, "button").click()
time.sleep(0.3)

# 8Iの平均が表示されているか
page_text = driver.find_element(By.CLASS_NAME, "result-card").text
assert "148" in page_text, f"8Iの平均148が表示されていない: {page_text}"

print("  → OK：クラブ切り替えと記録が正常")


# ========================================
# テスト⑦：履歴の開閉
# ========================================
print("テスト⑦ 履歴の開閉...")

# 1Wに戻して履歴を確認
select_element = driver.find_element(By.TAG_NAME, "select")
select = Select(select_element)
select.select_by_value("1W")
time.sleep(0.3)

# 履歴を見るボタンを押す
toggle_button = driver.find_element(By.CLASS_NAME, "history-toggle")
assert "履歴を見る" in toggle_button.text
toggle_button.click()
time.sleep(0.3)

# 履歴行が表示されたか
history_rows = driver.find_elements(By.CLASS_NAME, "history-row")
assert len(history_rows) == 3, f"履歴が3件ではない: {len(history_rows)}件"

# 閉じるボタンに変わっているか
toggle_button = driver.find_element(By.CLASS_NAME, "history-toggle")
assert "閉じる" in toggle_button.text

print("  → OK：履歴の開閉が正常")


# ========================================
# テスト⑧：1件削除
# ========================================
print("テスト⑧ 1件削除...")

# 最初の削除ボタンを押す
delete_buttons = driver.find_elements(By.CLASS_NAME, "delete-btn")
delete_buttons[0].click()
time.sleep(0.3)

# 履歴が2件に減ったか
history_rows = driver.find_elements(By.CLASS_NAME, "history-row")
assert len(history_rows) == 2, f"履歴が2件ではない: {len(history_rows)}件"

print("  → OK：1件削除が正常")


# ========================================
# テスト⑨：まとめて削除
# ========================================
print("テスト⑨ まとめて削除...")

# まとめて削除ボタンを押す
delete_all_button = driver.find_element(By.CLASS_NAME, "delete-all-btn")
delete_all_button.click()
time.sleep(0.3)

# 履歴が消えたか
history_rows = driver.find_elements(By.CLASS_NAME, "history-row")
assert len(history_rows) == 0, f"履歴が残っている: {len(history_rows)}件"

print("  → OK：まとめて削除が正常")


# ========================================
# テスト⑩：リロード後のデータ永続化
# ========================================
print("テスト⑩ リロード後の永続化...")

# 8Iのデータはまだ残っているはず
select_element = driver.find_element(By.TAG_NAME, "select")
select = Select(select_element)
select.select_by_value("8I")
time.sleep(0.3)

# リロード
driver.refresh()
time.sleep(0.5)

# 8Iに切り替え
select_element = driver.find_element(By.TAG_NAME, "select")
select = Select(select_element)
select.select_by_value("8I")
time.sleep(0.3)

# 8Iのデータが残っているか
page_text = driver.find_element(By.CLASS_NAME, "result-card").text
assert "148" in page_text, "リロード後にデータが消えた"

print("  → OK：リロード後もデータが残っている")


# ========================================
# 終了
# ========================================
print("")
print("=" * 40)
print("全テスト合格！")
print("=" * 40)

driver.quit()

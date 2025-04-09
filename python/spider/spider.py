
from webbrowser import get
from bs4 import BeautifulSoup
import requests
import re
import csv

def get_detail(url):
    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.3'}
    try:
        response = requests.get(url, headers=headers)
        response.encoding = 'utf-8'
        response.raise_for_status()  # 检查请求是否成功
        # 使用 BeautifulSoup 解析 HTML 内容
        soup = BeautifulSoup(response.text, 'html.parser') 
        table = soup.find("table")
        if table:
            price = find_price(table)
            return price.strip("\r\t\n")
        else:
            print("未找到表格。")
            return None
        
    except requests.RequestException as e:
        print(f"请求出错: {e}")
    except Exception as e:
        print(f"发生其他错误: {e}")

def get_detail_url(day):
    url = 'https://jiage.cngold.org/dingerchun/' + day + '/list_history_4357_1.html'
    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.3'}
    try:
        response = requests.get(url, headers=headers)
        response.encoding = 'utf-8'
        response.raise_for_status() 
        soup = BeautifulSoup(response.text, 'html.parser')
        items = soup.find_all('a')
        url = None
        for item in items:
            title = item.get("title")
            if title is not None and"丁二醇价格行情最新报价" in title:
                url = item.get("href") 
                break
        if url is None:
            print("not found")
            return None
        return url
    except requests.RequestException as e:
        print(f"请求出错: {e}")
    except Exception as e:
        print(f"发生其他错误: {e}")
    return None

def generate_dates(start_date, end_date):
    from datetime import datetime, timedelta

    # 定义起始日期和结束日期
    start_date = datetime.strptime(start_date, '%Y-%m-%d')
    end_date = datetime.strptime(end_date, '%Y-%m-%d')

    # 初始化日期列表
    date_list = []

    # 当前日期初始化为起始日期
    current_date = start_date

    # 循环生成日期列表
    while current_date <= end_date:
        date_list.append(current_date.strftime('%Y-%m-%d'))
        current_date += timedelta(days=1)
    return date_list

def find_price(table):
    if table:
        # 定位第三行（索引从 0 开始，所以第三行的索引是 2）
        rows = table.find_all('tr')
        if len(rows) >= 3:
            third_row = rows[2]
            # 定位第四列（索引从 0 开始，所以第四列的索引是 3）
            columns = third_row.find_all('td')
            if len(columns) >= 4:
                fourth_column = columns[2]
                # 提取文本
                text = fourth_column.get_text()
                return text
            else:
                print("第三行没有第三列。")
                return None
        else:
            print("表格没有第三行。")
            return None
    else:
        print("未找到表格。")

if __name__ == "__main__":
    dates = generate_dates("2022-07-14", "2025-02-12")
    data = []
    for date in dates:
        url = get_detail_url(date)
        if url is not None:
            price = get_detail(url)
            if price is not None:
                data.append([date, price])
            else:
                data.append([date, ""])
        else:
            data.append([date, ""])
    with open('data.csv', 'w', newline='') as csvfile:
        writer = csv.writer(csvfile)
        writer.writerows(data)
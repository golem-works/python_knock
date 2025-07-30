import calendar
from datetime import datetime, timedelta
from flask import Flask, render_template, request

app = Flask(__name__)

@app.route('/')
def index():
    today = datetime.now()
    
    # 今月と来月のカレンダーデータを生成
    current_month_year = today.year
    current_month_num = today.month
    
    next_month_date = today + timedelta(days=30) # 適当に30日後として次の月を計算
    next_month_year = next_month_date.year
    next_month_num = next_month_date.month
    
    # カレンダーオブジェクトの生成
    cal = calendar.Calendar(firstweekday=calendar.MONDAY) # 月曜日始まり
    
    # 今月のカレンダー（日付と曜日）
    current_month_days = []
    for week in cal.monthdayscalendar(current_month_year, current_month_num):
        formatted_week = []
        for day in week:
            if day == 0:
                formatted_week.append({'day': 0, 'formatted_date': ''})
            else:
                formatted_date_str = f"{current_month_year}-{current_month_num:02d}-{day:02d}"
                formatted_week.append({'day': day, 'formatted_date': formatted_date_str})
        current_month_days.append(formatted_week)
    
    # 来月のカレンダー（日付と曜日）
    next_month_days = []
    for week in cal.monthdayscalendar(next_month_year, next_month_num):
        formatted_week = []
        for day in week:
            if day == 0:
                formatted_week.append({'day': 0, 'formatted_date': ''})
            else:
                formatted_date_str = f"{next_month_year}-{next_month_num:02d}-{day:02d}"
                formatted_week.append({'day': day, 'formatted_date': formatted_date_str})
        next_month_days.append(formatted_week)
    
    # 月の名前を日本語で取得
    current_month_name = datetime(current_month_year, current_month_num, 1).strftime('%Y年%m月')
    next_month_name = datetime(next_month_year, next_month_num, 1).strftime('%Y年%m月')
    
    return render_template(
        'index.html',
        current_month_name=current_month_name,
        current_month_days=current_month_days, # 修正
        next_month_name=next_month_name,
        next_month_days=next_month_days,     # 修正
        today_date=today.day,
        today_month=today.month,
        today_year=today.year
    )

@app.route('/reserve', methods=['POST'])
def reserve():
    selected_date = request.form['selected_date']
    selected_time = request.form['selected_time']
    your_name = request.form['your_name']
    
    # 実際はここでデータベースに保存する処理とか、予約確認メールを送る処理とかが入るよ
    
    return f"""
    <h1>予約完了！マジ感謝！</h1>
    <p>選択された日付: {selected_date}</p>
    <p>選択された時間: {selected_time}</p>
    <p>お名前: {your_name}</p>
    <p><a href="/">カレンダーに戻る</a></p>
    """

if __name__ == '__main__':
    app.run(debug=True)
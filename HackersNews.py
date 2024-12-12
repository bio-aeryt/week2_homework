import requests
import time


# トップページに表示されているニュースのタイトルおよびリンクURLを取得
# 変数にHTTPライブラリで、APIの情報を取得して代入する

top_stories = "https://hacker-news.firebaseio.com/v0/topstories.json"

response = requests.get(top_stories)

# jsonデータを取得し、最初の5件のIDを取得
story_ids = response.json()[:30]

# IDから各ニュースの詳細を表示 かつ、負荷かけないようにするために、time関数を導入（先ほどはこれを入れず失敗）
# enumerate関数を用いて、idと、index番号を同時に取得

def main(story_ids):
    headers = {"User-Agent": "Mozilla/5.0"}
    for story_id in story_ids:
        time.sleep(1)  
        story_info = requests.get(f"https://hacker-news.firebaseio.com/v0/item/{story_id}.json", headers=headers)

        if story_info.status_code == 200:
            dic = story_info.json()

            if "url" not in dic or dic["url"] == "":
                continue
            else:
                dic_output = {f"title: {dic['title']}, link: {dic['url']}"}
                print(dic_output)

        else:
            print(story_info.status_code)


if __name__ == "__main__":
    main(story_ids)

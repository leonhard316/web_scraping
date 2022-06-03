import requests, sys, webbrowser, bs4
import tkinter
import GUI
import urllib

word = []
ngKey = []
genre = []
style = []
review = []
year = []
field = []
sort = 1
PDF = False

def is_int(s):
    try:
        int(s)
        return True
    except ValueError:
        return False

def search(title, author, magazine, volume, DOI, PDF, abstract):
    # 設定表示
    GUI.setting()
    print('Searching...')
    #print(word)
    #print(ngKey)
    # jstage 検索(sys.argvは，コマンドラインから受け取った引数)
    url = 'https://www.jstage.jst.go.jp/result/global/-char/ja?item1=4&word1='
    for i in range(len(word)):
        if i == 0:
            url += word[i].strip("'")
        else:
            url += ('%E3%80%80' + word[i].strip("'"))
    url += '&cond1=2&item2=&word2=&cond2=&item3=&word3=&cond3=&item4=&word4=&count=50&from=0&order=&type='

    if len(genre) > 0:
        for i in range(len(genre)):
             if i == 0:
                 url += str(genre[i])
             else:
                url += ('%2C' + str(genre[i]))
    url += '&license=&attribute='
    if len(style) > 0:
        for i in range(len(style)):
             if i == 0:
                 url += str(style[i])
             else:
                url += ('%2C' + str(style[i]))
    url += '&languageType=&option='
    if len(review) > 0:
        url += str(review[i])
    url += '&yearfrom='
    if is_int(str(year[0])) == False:
        pass
    else:
        url += str(year[i]).strip("'")
    url += '&yearto='
    if is_int(str(year[1])) == False:
        pass
    else:
        url += ('&yearto=' + str(year[i]).strip("'"))
    url += '&category='
    if len(field) > 0:
        for i in range(len(field)):
            if i == 0:
                url += field[i].strip("'")
            else:
                url += ('%2C' + field[i].strip("'"))
    url += '&cdjournal=&favorite=&translate=0&bglobalSearch=false&sortby='
    url += (str(sort) + '&showRecodsH=50&showRecords=20')
    print(url)
    HTML = requests.get(url)
    # url.encoding = url.apparent_encoding #日本語対策
    # ステータスチェック 存在するかしない
    # 100番〜　：処理中
    # 200番〜　：成功
    # 300番〜　：リダイレクト
    # 400番〜　：クライアントエラー
    # 500番〜　:サーバーエラー
    status = HTML.raise_for_status()
    # 検索結果からタイトルを取得 get_url_info.textでも良いが，get_url_info.contentの方が文字化けのリスクを減らせる
    # 二次引数:html.parser(追加ライブラリが不要), lxml(高速に処理可能), xml(xmlに対応し，高速に処理可能), html5lib(正しくHTML5を処理可)
    soup = bs4.BeautifulSoup(HTML.content, "html.parser")
    # ---------------------タイトル---------------------------------
    titles = soup.select('.searchlist-title')
    # ----------------------著者------------------------------------
    authors = soup.select('.searchlist-authortags.customTooltip')
    # ---------------------雑誌名------------------------------------
    # 雑誌名 巻号
    magazins = soup.select('.searchlist-additional-info')
    # ------------------------DOI-----------------------------------
    DOIs = soup.select('.result-doi-wrap')
    # ----------------------PDFリンク--------------------------------
    PDFs = soup.select('.lft')
    # -------------------アブストラクト--------------------------------
    abstracts = soup.select('.showabstractbox.content')
    # --------------------------------------------------------------
    dataNum = 30 # 取得件数30がデフォルト
    i = 0
    for elem in titles:
        title_name = elem.a.get('title')
        # NGワードの設定はここのタイトル名から除外することで機能させる
        if len(ngKey) == 0:
            title.append(title_name)
            author.append(authors[i].get('title'))
            text = magazins[i].get_text()
            lines = [line.strip() for line in text.splitlines()]
            magazine.append(lines[1])
            volume.append(lines[4] + lines[5] + lines[6])
            DOI.append(DOIs[i].a.get('href'))
            PDF.append(elem.a.get('href'))
            if PDF == True:
                print("download pdf...")
                pdf_url = PDFs.a.get('href')
                data = urllib.request.urlopen(pdf_url).read()
                with open(title_name, mode="wb") as f:
                    f.write(data)
            if abstracts[i].find('p') == None:
                abstract.append('')
            else:
                abstract.append(abstracts[i].p.get_text())
            i = i + 1
            if i == dataNum:  # 検索結果30まで(50まで変更可能)
                break
        else:
            if (ngKey[0].strip("'") in title_name) == False:
                title.append(title_name)
                author.append(authors[i].get('title'))
                text = magazins[i].get_text()
                lines = [line.strip() for line in text.splitlines()]
                magazine.append(lines[1])
                volume.append(lines[4] + lines[5] + lines[6])
                DOI.append(DOIs[i].a.get('href'))
                PDF.append(elem.a.get('href'))
                if PDF == True:
                    print("download pdf...")
                    pdf_url = PDFs.a.get('href')
                    data = urllib.request.urlopen(pdf_url).read()
                    with open(title_name, mode="wb") as f:
                        f.write(data)
                if abstracts[i].find('p') == None:
                    abstract.append('')
                else:
                    abstract.append(abstracts[i].p.get_text())
                i = i + 1
                if i == dataNum:  # 検索結果30まで(50まで変更可能)
                    break
    # -------------------------------------------------------------

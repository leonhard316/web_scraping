import tkinter
import sys
from tkinter import StringVar, Tk, filedialog, ttk
import search

def file_write(data):
    # ファイル選択ダイアログの表示
    file_path = tkinter.filedialog.asksaveasfilename(
        initialfile="result.xlsx",
        defaultextension="xlsx",
    )
    # ファイル保存
    data.save(file_path)

def download():
    search.PDF = True

def fielder(path):
    search.field.append(path)

def setting():
    root = tkinter.Tk()
    # チェックON・OFF変数--------
    opts1 = tkinter.BooleanVar()
    opts1.set(False)
    opts2 = tkinter.BooleanVar()
    opts2.set(False)
    opts3 = tkinter.BooleanVar()
    opts3.set(False)
    opts4 = tkinter.BooleanVar()
    opts4.set(False)
    opts5 = tkinter.BooleanVar()
    opts5.set(False)
    opts6 = tkinter.BooleanVar()
    opts6.set(False)
    opts7 = tkinter.BooleanVar()
    opts7.set(False)
    opts8 = tkinter.BooleanVar()
    opts8.set(False)
    opts9 = tkinter.BooleanVar()
    opts9.set(False)
    opts10 = tkinter.BooleanVar()
    opts10.set(False)
    opts11 = tkinter.BooleanVar()
    opts11.set(False)
    opts12 = tkinter.BooleanVar()
    opts12.set(False)
    opts13 = tkinter.BooleanVar()
    opts13.set(False)
    opts14 = tkinter.BooleanVar()
    opts14.set(False)
    opts15 = tkinter.BooleanVar()
    opts15.set(False)
    opts16 = tkinter.BooleanVar()
    opts16.set(False)
    # ------------------------
    # ----------------プログラムの処理内容を書く------------------------------
    root.title(u"Setting")
    root.geometry("600x700")
    # -------------------------------------------------------------------
    # エントリー
    KeyWord = tkinter.Entry()
    # ラベル
    KeyInstruction = tkinter.Label(text=u'検索キーワードを入力してください.')
    KeyInstruction.pack()
    KeyWord.insert(tkinter.END, "深層学習")

    KeyWord.pack()
    # エントリー
    NGWord = tkinter.Entry()
    # ラベル
    NGInstruction = tkinter.Label(text=u'NGワード(特定のワードを含む検索結果を除外)を入力してください.')
    NGInstruction.pack()
    NGWord.insert(tkinter.END, "")
    NGWord.pack()
    # -------------------------------------------------------------------
    # 資料種別------------------------------------------------------------
    # レイアウト
    frame1 = ttk.Frame(root, padding=16)
    frame1.pack()
    # ラベル
    genreInstruction = tkinter.Label(frame1, text=u'資料種別')
    genreInstruction.pack(side=tkinter.TOP)
    genre1 = tkinter.Checkbutton(frame1, text=u"ジャーナル",  variable=opts1, command=lambda: search.genre.append(100))
    genre1.pack(side=tkinter.LEFT)

    genre2 = tkinter.Checkbutton(frame1, text=u"会議録・要旨集", variable=opts2, command=lambda: search.genre.append(200))
    genre2.pack(side=tkinter.LEFT)

    genre3 = tkinter.Checkbutton(frame1, text=u"研究報告書・技術報告書", variable=opts3, command=lambda: search.genre.append(400))
    genre3.pack(side=tkinter.LEFT)

    genre4 = tkinter.Checkbutton(frame1, text=u"解説誌・一般情報誌",  variable=opts4, command=lambda: search.genre.append(500))
    genre4.pack(side=tkinter.LEFT)
    # -------------------------------------------------------------------
    # 記事属性------------------------------------------------------------
    # レイアウト
    frame2 = ttk.Frame(root, padding=16)
    frame2.pack()
    # ラベル
    genreInstruction = tkinter.Label(frame2, text=u'記事属性')
    genreInstruction.pack(side=tkinter.TOP)
    style1 = tkinter.Checkbutton(frame2, text=u"早期公開", variable=opts5, command=lambda: search.genre.append(1))
    style1.pack(side=tkinter.LEFT)

    style2 = tkinter.Checkbutton(frame2, text=u"本文（HTML形式)", variable=opts6, command=lambda: search.genre.append(2))
    style2.pack(side=tkinter.LEFT)

    style3 = tkinter.Checkbutton(frame2, text=u"電子付録", variable=opts7, command=lambda: search.genre.append(4))
    style3.pack(side=tkinter.LEFT)

    style4 = tkinter.Checkbutton(frame2, text=u"被引用あり", variable=opts8, command=lambda: search.genre.append(5))
    style4.pack(side=tkinter.LEFT)
    # -----------------------------------------------------------------
    # 査読有無-----------------------------------------------------------
    frame3 = ttk.Frame(root, padding=16)
    frame3.pack()
    review1 = tkinter.Checkbutton(frame3, text=u"査読有無 有", variable=opts9, command=lambda: search.genre.append(0))
    review1.pack(side=tkinter.TOP)
    # ------------------------------------------------------------------
    # 発行年-------------------------------------------------------------
    # レイアウト
    frame4 = ttk.Frame(root, padding=16)
    frame4.pack()
    # ラベル
    yearInstruction = tkinter.Label(frame4, text=u'発行年.')
    yearInstruction.pack(side=tkinter.TOP)
    # エントリー
    start1 = tkinter.Entry(frame4)
    start1.insert(tkinter.END, "")
    start1.pack(side=tkinter.LEFT)
    # ラベル
    year1 = tkinter.Label(frame4, text=u' ～ ')
    year1.pack(side=tkinter.LEFT)
    # エントリー
    end1 = tkinter.Entry(frame4)
    end1.insert(tkinter.END, "")
    end1.pack(side=tkinter.LEFT)
    # ------------------------------------------------------------------
    # 分野---------------------------------------------------------------
    # レイアウト
    frame5 = ttk.Frame(root, padding=16)
    frame5.pack()
    # ラベル
    fieldInstruction = tkinter.Label(frame5, text=u'分野')
    fieldInstruction.pack(side=tkinter.TOP)
    field1 = tkinter.Checkbutton(frame5, text=u"基礎科学系", variable=opts10, command=lambda: fielder('010000%2C010100%2C011100%2C012100%2C014100'))
    field1.pack(side=tkinter.LEFT)

    field2 = tkinter.Checkbutton(frame5, text=u"ライフ系", variable=opts11, command=lambda: fielder('030000%2C030100%2C035100'))
    field2.pack(side=tkinter.LEFT)

    field3 = tkinter.Checkbutton(frame5, text=u"医学・保健衛生系", variable=opts12, command=lambda: fielder('050000%2C050100%2C051100%2C053100%2C054100'))
    field3.pack(side=tkinter.LEFT)

    field4 = tkinter.Checkbutton(frame5, text=u"工学系", variable=opts13, command=lambda: fielder('070000%2C070100%2C072100%2C073100%2C074100%2C075100'))
    field4.pack(side=tkinter.LEFT)

    field5 = tkinter.Checkbutton(frame5, text=u"学際科学系", variable=opts14, command=lambda: fielder('090000%2C090100%2C091100%2C092100'))
    field5.pack(side=tkinter.LEFT)

    field6 = tkinter.Checkbutton(frame5, text=u"人文・社会科学系", variable=opts15, command=lambda: fielder('110000%2C111100%2C112100%2C113100%2C114100%2C115100%2C116100%2C117100'))
    field6.pack(side=tkinter.LEFT)

    # 並び順-------------------------------------------------------------
    frame8 = ttk.Frame(root, padding=16)
    frame8.pack()
    # ラベル
    sortInstruction = tkinter.Label(frame8, text=u'並び順')
    sortInstruction.pack(side=tkinter.TOP)
    sorttab = ttk.Combobox(frame8,
                                values=[
                                    "ヒット順",
                                    "発行日[新着順]",
                                    "発行日[古い順]",
                                    "公開日[新着順]",
                                    "公開日[古い順]",
                                    "資料名順",
                                    ])
    sorttab.pack()
    # ------------------------------------------------------------------
    # PDF自動ダウンロード--------------------------------------------------
    frame7 = ttk.Frame(root, padding=16)
    frame7.pack()
    PDF = tkinter.Checkbutton(frame7, text=u"PDF自動ダウンロード", variable=opts16, command=lambda: download())
    PDF.pack(side=tkinter.TOP)
    # ------------------------------------------------------------------
    def CloseSetting():
        # word, NG, genre, style, review, year, field
        # Entryの値を取得
        KeyWord_value = KeyWord.get()
        # print(KeyWord_value)
        search.word = KeyWord_value.split()
        #-----
        search.ngKey = NGWord.get().split()
        # -----
        search.year.append(start1)
        search.year.append(end1)
        print(search.year)
        # -----
        search.sort = sorttab.get()
        if search.sort == 'ヒット順':
            search.sort = 1
        if search.sort == '発行日[新着順]':
            search.sort = 5
        if search.sort == '発行日[古い順]':
            search.sort = 6
        if search.sort == '公開日[新着順]':
            search.sort = 2
        if search.sort == '公開日[古い順]':
            search.sort = 3
        if search.sort == '資料名順':
            search.sort = 4
        # -----
        # 設定画面を閉じる
        root.quit()
    # 検索ボタン----------------------------------------------------------
    # レイアウト
    frame6 = ttk.Frame(root, padding=16)
    frame6.pack()
    Button = tkinter.Button(frame6, text=u'検索', command = CloseSetting)
    Button.pack(side=tkinter.TOP)
    # -------------------------------------------------------------------
    # ----------------プログラムの処理内容を書く------------------------------
    root.mainloop()





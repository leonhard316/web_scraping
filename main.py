import search
import sys
import excel
import openpyxl
import GUI

title = []
author = []
magazine = []
volume = []
DOI = []
PDF = []
abstract = []
word = []

#value = sys.argv
if __name__ == '__main__':
    # if len(value) > 1:
    #     for arg in value:
    #         if arg != 'main.py':
    #             word.append(arg)
    #     # 検索結果
    #     search.search(title, author, magazine, volume, DOI, PDF, abstract, word)
    #     # excelシートへの追加と編集
    #     book = openpyxl.Workbook(0)
    #     excel.save_sheet(book, title, author, magazine, volume, DOI, PDF, abstract)
    #     # ファイル選択ダイアログを表示して，ファイルを保存
    #     GUI.file_write(book)
    # else:
    #     print("検索ワードが指定されていません")

    # 検索結果
    search.search(title, author, magazine, volume, DOI, PDF, abstract)
    # excelシートへの追加と編集
    book = openpyxl.Workbook(0)
    excel.save_sheet(book, title, author, magazine, volume, DOI, PDF, abstract)
    # ファイル選択ダイアログを表示して，ファイルを保存
    GUI.file_write(book)








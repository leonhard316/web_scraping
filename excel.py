import openpyxl

def save_sheet(book, title, author, magazine, volume, DOI, PDF, abstract):
    #name = input('エクセルシート保存名を入力してください>')
    #name += ".xlsx"
    #book = openpyxl.Workbook(0)
    book.active['A1'] = '番号'
    book.active['B1'] = 'タイトル'
    # セルの幅調整
    book.active.column_dimensions['B'].width = 30
    book.active['C1'] = '著者'
    book.active['D1'] = '雑誌名'
    # セルの幅調整
    book.active.column_dimensions['D'].width = 15
    book.active['E1'] = '番号'
    book.active['F1'] = 'DOI'
    # セルの幅調整
    book.active.column_dimensions['F'].width = 15
    book.active['G1'] = 'PDFリンク'
    # セルの幅調整
    book.active.column_dimensions['G'].width = 15
    book.active['H1'] = 'アブストラクト'
    # セルの幅調整
    book.active.column_dimensions['H'].width = 15

    for i in range(30): #検索結果30までを保存
        # セルの高さ調整
        book.active.row_dimensions[i + 2].height = 40
        book.active['A' + str(i + 2)] = i + 1
        book.active['A' + str(i + 2)].alignment = openpyxl.styles.Alignment(wrap_text=True, horizontal='general',
                                                                            vertical='bottom')
        book.active['B' + str(i + 2)] = title[i]
        book.active['B' + str(i + 2)].alignment = openpyxl.styles.Alignment(wrap_text=True, horizontal='general',
                                                                     vertical='bottom')
        book.active['C' + str(i + 2)] = author[i]
        book.active['C' + str(i + 2)].alignment = openpyxl.styles.Alignment(wrap_text=True, horizontal='general',
                                                                     vertical='bottom')
        book.active['D' + str(i + 2)] = magazine[i]
        book.active['D' + str(i + 2)].alignment = openpyxl.styles.Alignment(wrap_text=True, horizontal='general',
                                                                     vertical='bottom')
        book.active['E' + str(i + 2)] = volume[i]
        book.active['E' + str(i + 2)].alignment = openpyxl.styles.Alignment(wrap_text=True, horizontal='general',
                                                                     vertical='bottom')
        book.active['F' + str(i + 2)] = DOI[i]
        book.active['F' + str(i + 2)].alignment = openpyxl.styles.Alignment(wrap_text=True, horizontal='general',
                                                                     vertical='bottom')
        book.active['G' + str(i + 2)] = PDF[i]
        book.active['G' + str(i + 2)].alignment = openpyxl.styles.Alignment(wrap_text=True, horizontal='general',
                                                                     vertical='bottom')
        book.active['H' + str(i + 2)] = abstract[i]
        book.active['H' + str(i + 2)].alignment = openpyxl.styles.Alignment(wrap_text=True, horizontal='general',
                                                                     vertical='bottom')
    #book.save(name)
    #print('Save ' + name)


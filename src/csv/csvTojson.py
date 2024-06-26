# CSV, JSON 모듈을 임포트합니다.
import csv
import json

def books_to_json(src_file, dst_file):
    # 아래 함수를 완성하세요.
    books = []
    with open(src_file) as src:
        reader = csv.reader(src, delimiter = ',')

        # 각 줄 별로 대응되는 book 딕셔너리를 만듭니다.
        for row in reader:
            # 책 정보를 저장하는 딕셔너리를 생성합니다.
            book = {
                'title': row[0],
                'author': row[1],
                'genre': row[2],
                'pages': int(row[3]),
                'publisher': row[4]
            }
            books.append(book)

    with open(dst_file, 'w') as dst:
        # JSON 형식으로 dst_file에 저장합니다.
        json.dump(books, dst, indent=2)
        pass


# 아래 주석을 해제하고 결과를 확인해보세요.
src_file = 'books.csv'
dst_file = 'books.json'
books_to_json(src_file, dst_file)

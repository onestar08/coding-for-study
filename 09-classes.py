# 클래스 class

### Article variables
title1 = "개발"
author1 = "장한별"
content1 = '개발은 쉬워요'
view_count1 = 0

title2 = "코칭"
author2 = "장한별"
content2 = '코칭은 쉬워요'
view_count2 = 0

title3 = "창업"
author3 = "장한별"
content3 = '창업은 쉬워요'
view_count3 = 0


# class Article:
#     title = "개발"
#     author = "장한별"
#     content = '개발은 쉬워요'
#     view_count = 0
#
# article1 = Article()
# print(article1.title)
# article2 = Article()
# article2.title = "코칭"
# print(article1.title)
# print(article2.title)

##### Article class with __init__
class Article:
    author = "장한별"
    view_count = 0

    def __init__(self, title, content):
        self.title = title
        self.contnet = content

    def read(self):
        self.view_count = self.view_count + 1

article1 = Article("개발", "개발은 쉬워요")
article2 = Article("코칭", "코칭은 쉬워요")
article3 = Article("창업", "창업은 쉬워요")

# print(article1.view_count)
# article1.read()
# print(article1.view_count)


#### Article class inheritance 상속

class BrunchArticle(Article):
    source = "브런치"

    def read(self):
        self.view_count = self.view_count + 2

# BrunchArticle = BrunchArticle("개발", "개발은 쉬워요")
# print(BrunchArticle.title)
# print(BrunchArticle.source)
# print(BrunchArticle.view_count)
# BrunchArticle.read()
# print(BrunchArticle.view_count)


# 미니과제2. 클래스 만들어 보기
# 학교 클래스 만들기 (이름, 설립연도, 주소)

class School():
    def __init__(self, name, foundation, adress):
        self.name = name
        self.foundation = foundation
        self.adress = adress

school1 = School("수성고", "1890년도", "수성로245번길")
school2 = School("명인중", "2000년도", "장안로578번길")
school3 = School("송정초", "1900년도", "송죽로928번길")
print(school1.adress)
print(school2.foundation)
print(school3.name)

# 안녕하세요? XXX님.

# (주)나도출판 편집자 나코입니다.
# 현재 저희 출판사는 파이썬에 관한 주제로 책 출간을 기획 중입니다.
# XXX님의 유튜브 영상을 보고 연락을 드리게 되었습니다.
# 자세한 내용은 첨부드리는 제안서를 확인 부탁드리며, 긍정적인 회신 기다리겠습니다.

# 좋은 하루 보내세요 ^^
# 감사합니다.

# - 나코 드림.

# name = ["유튜버1", "유튜버2", "유튜버3"]


# for i in range(0,3):
#     with open(name[i]+".txt", "w", encoding="utf-8") as mail:
#         mail.write(" (주)나도출판 편집자 나코입니다.")
#         mail.write("\n 현재 저희 출판사는 파이썬에 관한 주제로 책 출간을 기획 중입니다.")
#         mail.write("\n {0}님의 유튜브 영상을 보고 연락을 드리게 되었습니다.".format(name[i]))
#         mail.write("\n 자세한 내용은 첨부드리는 제안서를 확인 부탁드리며, 긍정적인 회신 기다리겠습니다.")
#         mail.write("\n\n 좋은 하루 보내세요 ^^")
#         mail.write("\n 감사합니다.")                          # 내 답


# names = ["아이언맨TV", "토르코딩,", "헐크에러", "아이엠 디버깅"]
# for name in names:
#     with open("{}.txt".format(name), "w", encoding="utf8") as email_file:
#         email_file.write("""
# 안녕하세요? {0}님.

# (주)나도출판 편집자 나코입니다.
# 현재 저희 출판사는 파이썬에 관한 주제로 책 출간을 기획 중입니다.
# {0}님의 유튜브 영상을 보고 연락을 드리게 되었습니다.
# 자세한 내용은 첨부드리는 제안서를 확인 부탁드리며, 긍정적인 회신 기다리겠습니다.

# 좋은 하루 보내세요 ^^
# 감사합니다.
# """.format(name))                     # 좋은 답1        

# names = ["아이언맨TV", "토르코딩,", "헐크에러", "아이엠 디버깅"]
# for name in names:
#     with open("{}.txt".format(name), "w", encoding="utf8") as email_file:
#         email_file.write(f"""
# 안녕하세요? {0}님.

# (주)나도출판 편집자 나코입니다.
# 현재 저희 출판사는 파이썬에 관한 주제로 책 출간을 기획 중입니다.
# {0}님의 유튜브 영상을 보고 연락을 드리게 되었습니다.
# 자세한 내용은 첨부드리는 제안서를 확인 부탁드리며, 긍정적인 회신 기다리겠습니다.

# 좋은 하루 보내세요 ^^
# 감사합니다.
# """.)                          # 좋은 답 2
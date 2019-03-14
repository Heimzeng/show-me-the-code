import os

problem_num = [16, 67, 58, 23, 84, 24, 35, 37, 42, 32, 31, 37, 22, 39]

for chapter_m_1 in range(len(problem_num)):
    chapter_n = chapter_m_1 + 1
    for pro_m_1 in range(problem_num[chapter_m_1]):
        pro_n = pro_m_1 + 1
        print(chapter_n, pro_n)
        os.remove('./solution/chapter' + str(chapter_n) + '/' + str(pro_n) + 'P' + '.png')
        os.rename('./solution/chapter' + str(chapter_n) + '/' + str(pro_n) + 'P_main' + '.png', './solution/chapter' + str(chapter_n) + '/' + str(pro_n) + 'P' + '.png')
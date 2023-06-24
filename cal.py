from reportlab.pdfgen import canvas
import random
import sys
from reportlab.pdfbase import pdfmetrics
from reportlab.pdfbase.ttfonts import TTFont


# 定义生成题目的函数
def generate_questions(num):
    questions = []
    while len(questions) < num:
        a = random.randint(100, 999)
        b = random.randint(100, 999)
        op = random.choice(['+', '-'])
        if op == '+':
            result = a + b
        else:
            result = a - b
        if result < 0 or result > 999:
            continue
        question = f'{a} {op} {b} = '
        questions.append((question, result))
    return questions

# 定义生成PDF文件的函数
def generate_pdf(num_pages):
    pdfmetrics.registerFont(TTFont('Courier', 'Courier.ttf'))
    pdfmetrics.registerFont(TTFont('SimHei', 'SimHei.ttf'))
    filename = 'a.pdf'
    doc = canvas.Canvas(filename)
    #doc.setFont('Courier', 12)
    doc.setFont('SimHei', 12)
    for i in range(num_pages):
        #doc.setFont('Courier', 12)
        doc.setFont('SimHei', 12)
        questions = generate_questions(50)
        doc.drawString(50, 800, f'{i+22:02d}')
        y = 750
        for j in range(50):
            if j < len(questions):
                doc.drawString(50 + (j % 2) * 250, y, questions[j][0])
                if j % 2 == 1:
                    y -= 20
        doc.showPage()
    doc.save()
    print(f'已生成PDF文件：{filename}')

# 主程序
if __name__ == '__main__':
    if len(sys.argv) > 1:
        num_pages = int(sys.argv[1])
    else:
        num_pages = 1
    generate_pdf(num_pages)

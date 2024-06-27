import fitz  # PyMuPDF
import string
import re


def extract_a_words(pdf_path, output_txt_path):
    # 打开PDF文件
    pdf_document = fitz.open(pdf_path)
    a_words = ""
    
    # 遍历每一页
    for page_number in range(pdf_document.page_count):
        page = pdf_document.load_page(page_number)
        text = page.get_text("text")
        
        # 提取每一行中的单词
        words = text.split()
        for word in words:
            # 通过正则表达式匹配以小写字母a开头的单词
            if re.match(r'^b[a-z]*', word):
                a_words += word + "\n"
    
    # 将所有以a开头的单词保存到txt文件
    with open(output_txt_path, "w", encoding="utf-8") as text_file:
        text_file.write(a_words)
        print(f"提取的以a开头的单词已保存到 {output_txt_path}")

def filter_deduplicate_and_clean_lines(input_txt_path, output_txt_path):
    # 打开并读取原始txt文件
    with open(input_txt_path, "r", encoding="utf-8") as input_file:
        lines = input_file.readlines()
    
    # 过滤、去除重复并清理结尾标点符号的以小写字母a开头的行
    seen = set()
    filtered_lines = []
    for line in lines:
        # 去除行尾的标点符号和空白
        clean_line = line.rstrip().rstrip(string.punctuation)
        
        # 检查是否以小写字母a开头并且没有重复
        if clean_line.startswith('b') and clean_line not in seen:
            filtered_lines.append(clean_line + "\n")
            seen.add(clean_line)
    
    # 将过滤后的行写入新的txt文件
    with open(output_txt_path, "w", encoding="utf-8") as output_file:
        output_file.writelines(filtered_lines)
        print(f"已将过滤后的行保存到 {output_txt_path}")

def filter_lines_in_alphabetical_order(input_txt_path, output_txt_path):
    # 打开并读取原始txt文件
    with open(input_txt_path, "r", encoding="utf-8") as input_file:
        lines = input_file.readlines()
    
    # 去除行尾的标点符号和空白，并确保每行的单词按字母顺序排列
    cleaned_lines = [line.rstrip().rstrip(string.punctuation).strip() for line in lines]
    
    # 初始化存储按字母顺序排列的行
    sorted_lines = []
    previous_line = ""
    
    for line in cleaned_lines:
        if previous_line == "" or line >= previous_line:
            sorted_lines.append(line)
            previous_line = line
    
    # 将过滤后的行写入新的txt文件
    with open(output_txt_path, "w", encoding="utf-8") as output_file:
        for line in sorted_lines:
            output_file.write(line + "\n")
        
        print(f"已将按字母顺序排列的行保存到 {output_txt_path}")

# 示例调用
# filter_lines_in_alphabetical_order('input.txt', 'output.txt')


# 示例调用
# filter_a_lines('input.txt', 'output.txt')

# 设置PDF文件路径和输出文本文件路径
pdf_path = "C:\\Users\\zhang\\Desktop\\gre_words\\gre_list2.pdf"
output_txt_path = "GRE_list2_words_3000.txt"
extract_a_words(pdf_path, output_txt_path)
filter_deduplicate_and_clean_lines('GRE_list2_words_3000.txt', 'GRE_list2_words_3000.txt')
# filter_lines_in_alphabetical_order('GRE_list2_words_3000.txt', 'GRE_list2_words_3000.txt')

# import fitz  # PyMuPDF

# def pdf_to_text(pdf_path, output_txt_path):
#     # 打开PDF文件
#     pdf_document = fitz.open(pdf_path)
#     all_text = ""
    
#     # 遍历每一页
#     for page_number in range(2, len(pdf_document)):
#         page = pdf_document.load_page(page_number)
#         text = page.get_text("text")
#         all_text += text  # 将所有文本连接在一起
    
#     # 按句号分割文本
#     sentences = all_text.split('。')
    
#     # 将每个句子按行保存到txt文件
#     with open(output_txt_path, "w", encoding="utf-8") as text_file:
#         for sentence in sentences:
#             # 确保句子不为空
#             if sentence.strip():
#                 print(sentence.strip() + ". \n")
#                 text_file.write(sentence.strip() + "。\n")



# pdf_path = "C:\\Users\\zhang\\Desktop\\GRE_3000_words.pdf"
# output_txt_path = "GRE_output_text_file.txt"
# pdf_to_text(pdf_path, output_txt_path)

# import pytesseract
# from PIL import Image
# import os

# def images_to_text(images_folder, output_txt_path):
#     all_text = ""
    
#     # 遍历文件夹中的每一张图片
#     for image_filename in sorted(os.listdir(images_folder)):
#         if image_filename.lower().endswith(('png', 'jpg', 'jpeg', 'tiff', 'bmp')):
#             image_path = os.path.join(images_folder, image_filename)
#             image = Image.open(image_path)
#             text = pytesseract.image_to_string(image, lang='chi_sim')
#             all_text += text  # 将所有文本连接在一起
    
#     # 按句号分割文本
#     sentences = all_text.split('。')
    
#     # 将每个句子按行保存到txt文件
#     with open(output_txt_path, "w", encoding="utf-8") as text_file:
#         for sentence in sentences:
#             # 确保句子不为空
#             if sentence.strip():
#                 print(sentence.strip() + "。\n")
#                 text_file.write(sentence.strip() + "。\n")

# # 设定图片文件夹路径和输出文本文件路径
# images_folder = "C:\\Users\\zhang\\Desktop\\GRE_3000_words_images"
# output_txt_path = "GRE_output_text_file.txt"
# images_to_text(images_folder, output_txt_path)


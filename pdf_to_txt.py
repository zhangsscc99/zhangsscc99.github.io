import fitz  # PyMuPDF

def pdf_to_text(pdf_path, output_txt_path):
    # 打开PDF文件
    pdf_document = fitz.open(pdf_path)
    all_text = ""
    
    # 遍历每一页
    for page_number in range(2, len(pdf_document)):
        page = pdf_document.load_page(page_number)
        text = page.get_text("text")
        all_text += text  # 将所有文本连接在一起
    
    # 按句号分割文本
    sentences = all_text.split('。')
    
    # 将每个句子按行保存到txt文件
    with open(output_txt_path, "w", encoding="utf-8") as text_file:
        for sentence in sentences:
            # 确保句子不为空
            if sentence.strip():
                print(sentence.strip() + ". \n")
                text_file.write(sentence.strip() + "。\n")



pdf_path = "C:\\Users\\zhang\\Desktop\\GRE_3000_words.pdf"
output_txt_path = "GRE_output_text_file.txt"
pdf_to_text(pdf_path, output_txt_path)

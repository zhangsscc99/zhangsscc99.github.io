import matplotlib.pyplot as plt

def process_file_and_plot(filename):
    epochs = []
    accuracies = []

    try:
        with open(filename, 'r') as file:
            lines = file.readlines()

        if len(lines) % 2 != 0:
            print("文件中的行数不是偶数，可能存在缺失的行。")
            return

        for i in range(0, len(lines), 2):
            try:
                epoch_line = lines[i].strip()
                accuracy_line = lines[i + 1].strip()

                epoch = float(epoch_line.split()[0])
                backdoor_accuracy = float(accuracy_line.split()[1])

                # print(f"Epoch: {epoch}, Backdoor Accuracy: {backdoor_accuracy}")

                epochs.append(epoch)
                accuracies.append(backdoor_accuracy)
            except Exception as e:
                print(f"处理第 {i//2 + 1} 组行时出错: {e}")
                continue

        # Plotting
        plt.figure(figsize=(10, 6))
        plt.plot(epochs, accuracies, marker='o', linestyle='-', color='b')
        plt.xlabel('Epoch')
        plt.ylabel('Backdoor Accuracy')
        plt.title('Epoch vs Backdoor Accuracy')
        plt.ylim(0, 1.0)
        plt.grid(True)
        plt.show()

    except FileNotFoundError:
        print(f"文件 {filename} 未找到。")
    except Exception as e:
        print(f"读取文件时出错: {e}")


import matplotlib.pyplot as plt

def process_file_and_plot_2(filename, output_pdf=None):
    epochs = []
    accuracies = []

    try:
        with open(filename, 'r') as file:
            lines = file.readlines()

        if len(lines) % 3 != 0:
            print("文件中的行数不是三的倍数，可能存在缺失的行。")
            return

        for i in range(0, len(lines), 3):
            try:
                epoch_line = lines[i].strip()
                accuracy_line = lines[i + 1].strip()
                # 第三行舍去，不做处理
                # third_line = lines[i + 2].strip()

                epoch = float(epoch_line.split()[0])
                backdoor_accuracy = float(accuracy_line.split()[1])

                # print(f"Epoch: {epoch}, Backdoor Accuracy: {backdoor_accuracy}")

                epochs.append(epoch)
                accuracies.append(backdoor_accuracy)
            except Exception as e:
                print(f"处理第 {i//3 + 1} 组行时出错: {e}")
                continue

        # Plotting
        plt.figure(figsize=(10, 6))
        plt.plot(epochs, accuracies, marker='o', linestyle='-', color='b')
        plt.xlabel('Epoch')
        plt.ylabel('Backdoor Accuracy')
        plt.title('Epoch vs Backdoor Accuracy')
        plt.ylim(0, 1.0)
        plt.grid(True)
        if output_pdf:
            plt.savefig(output_pdf, format='pdf')
        plt.show()

    except FileNotFoundError:
        print(f"文件 {filename} 未找到。")
    except Exception as e:
        print(f"读取文件时出错: {e}")


def process_file_and_plot_original(filename):
    epochs = []
    accuracies = []

    try:
        with open(filename, 'r') as file:
            lines = file.readlines()

        if len(lines) % 1 != 0:
            print("文件中的行数不是三的倍数，可能存在缺失的行。")
            return

        for i in range(0, len(lines), 1):
            try:
                epoch_line = lines[i].strip()
                accuracy_line = lines[i + 1].strip()
                # 第三行舍去，不做处理
                # third_line = lines[i + 2].strip()

                epoch = float(epoch_line.split()[0])
                backdoor_accuracy = float(accuracy_line.split()[1])

                print(f"Epoch: {epoch}, Backdoor Accuracy: {backdoor_accuracy}")

                epochs.append(epoch)
                accuracies.append(backdoor_accuracy)
            except Exception as e:
                print(f"处理第 {i//3 + 1} 组行时出错: {e}")
                continue

        # Plotting
        plt.figure(figsize=(10, 6))
        plt.plot(epochs, accuracies, marker='o', linestyle='-', color='b')
        plt.xlabel('Epoch')
        plt.ylabel('Backdoor Accuracy')
        plt.title('Epoch vs Backdoor Accuracy')
        plt.grid(True)
        plt.show()

    except FileNotFoundError:
        print(f"文件 {filename} 未找到。")
    except Exception as e:
        print(f"读取文件时出错: {e}")
def process_file_and_plot_original(filename):
    epochs = []
    backdoor_acc = []

    with open(filename, 'r') as file:
        index = 0
        for line in file:
            parts = line.strip().split()
            if len(parts) != 2:
                continue  # 跳过格式不正确的行
            line_number, acc = index, float(parts[1])
            
            epoch = (line_number) * 10
            epochs.append(epoch)
            backdoor_acc.append(acc)
            index += 1

    plt.figure(figsize=(10, 6))
    plt.plot(epochs, backdoor_acc, marker='o', linestyle='-', color='b')
    plt.xlabel('Epochs')
    plt.ylabel('Backdoor Accuracy')
    plt.title('Backdoor Accuracy vs Epochs')
    plt.ylim(0, 1.0)
    plt.grid(True)
    
    plt.show()

if __name__ == "__main__":
    # pdb处理
    filename = "0+Fashion+cnn+bias0.5+epoch3000+local10+lr0.2+batch32+nwork100+nbyz20+scale+trim+sgn+0.001+5+0.1.txt"  # 将此处替换为你的文件名
    process_file_and_plot(filename)
    # pdb增强
    filename2 = "0+Fashion+cnn+bias0.5+epoch3040+local10+lr0.2+batch32+nwork100+nbyz20+scale+trim+sgn+0.001+5+0.1.txt"  # 将此处替换为你的文件名
    process_file_and_plot_2(filename2)
    filename3 = "0+Fashion+cnn+bias0.5+epoch3100+local10+lr0.2+batch32+nwork100+nbyz20+scale+trim+sgn+0.001+5+0.1.txt"
    process_file_and_plot_2(filename3)
    filename_original = "0+Fashion+cnn+bias0.5+epoch3100+local10+lr0.2+batch32+nwork100+nbyz20+scale+trim+sgn+original"
    process_file_and_plot_original(filename_original)
    filename5 = "0+Fashion+cnn+bias0.5+epoch3110+local10+lr0.2+batch32+nwork100+nbyz20+scale+trim+sgn+0.001+6+0.15.txt"
    process_file_and_plot_2(filename5)
    filename6 = "0+Fashion+cnn+bias0.5+epoch3120+local10+lr0.2+batch32+nwork100+nbyz20+scale+trim+sgn+0.001+7+0.1.txt"
    process_file_and_plot_2(filename6)
    filename7 = "0+Fashion+cnn+bias0.5+epoch3350+local10+lr0.2+batch32+nwork100+nbyz20+scale+trim+sgn+0.001+6+0.1.txt"
    process_file_and_plot_2(filename7)
    filename_original = "0+Fashion+cnn+bias0.5+epoch3100+local10+lr0.2+batch32+nwork100+nbyz20+scale+trim+sgn+original"
    process_file_and_plot_original(filename_original)
    filename_original2 = "0+Fashion+cnn+bias0.5+epoch3350_2+local10+lr0.2+batch32+nwork100+nbyz20+scale+trim+sgn+0.001+6+0.1"
    process_file_and_plot_2(filename_original2)
    filename_original = "0+Fashion+cnn+bias0.5+epoch3000+local10+lr0 copy.2+batch32+nwork100+nbyz20+scale+trim+sgn+original"
    process_file_and_plot_original(filename_original)
    # filename8 = "0+Fashion+cnn+bias0.5+epoch3370+local10+lr0.2+batch32+nwork100+nbyz20+scale+trim+sgn+0.001+6+0.1.txt"
    # process_file_and_plot_2(filename8)
    # filename9 = "0+Fashion+cnn+bias0.5+epoch3395+local10+lr0.2+batch32+nwork100+nbyz20+scale+trim+sgn+0.001+7+0.15.txt"
    # process_file_and_plot_2(filename9)
    #这个是trim
    filename10 = "0+Fashion+cnn+bias0.5+epoch3020+local10+lr0.2+batch32+nwork100+nbyz20+scale+trim+sgn+0.01+1+0.5.txt"
    process_file_and_plot_2(filename10)
    #这个是median
    filename11 = "0+Fashion+cnn+bias0.5+epoch3015+local10+lr0.2+batch32+nwork100+nbyz20+scale+median+sgn+0.001+8+0.1.txt"
    process_file_and_plot_2(filename11)
    
    filename12 = "0+Fashion+cnn+bias0.5+epoch3031+local10+lr0.2+batch32+nwork100+nbyz20+scale+median+sgn+0.001+3+0.1cifar10.txt"
    output_pdf12 = filename12[:-4] + ".pdf"
    process_file_and_plot_2(filename12, output_pdf12)
    filename13 = "0+Fashion+cnn+bias0.5+epoch3022+local10+lr0.2+batch32+nwork100+nbyz20+scale+krum+sgn+0.001+2+0.1.txt"
    output_pdf13 = filename13[:-4] + ".pdf"
    process_file_and_plot_2(filename13, output_pdf13)

    filename14 = "0+Fashion+cnn+bias0.5+epoch3021+local10+lr0.2+batch32+nwork100+nbyz20+scale+mean+sgn+0.001+5+0.1.txt"
    output_pdf14 = filename14[:-4] + ".pdf"
    process_file_and_plot_2(filename14, output_pdf14)

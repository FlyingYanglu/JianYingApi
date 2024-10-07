import JianYingApi, uuid
import uiautomation as api32
import time
import pyperclip  # Allows interacting with the system clipboard
import pyautogui  # Allows simulating keyboard and mouse actions

def read_text_file(file_path):
    with open(file_path, 'r', encoding='utf-8') as file:
        return file.read()

######### Step1: 新建视频项目

if __name__ == "__main__":
    # Step 2: 打开剪映识别
    print("Opening JianYing")
    time.sleep(5)
    ins = JianYingApi.Jy_Warp.Instance(JianYing_Exe_Path=r"D:/jianying/JianyingPro")

    time.sleep(5)
    print("Searching JianYing Main Window")
    jy_main = api32.WindowControl(Name="剪映专业版", searchDepth=1)
    print("Found JianYing Main Window")
    print(jy_main)

    time.sleep(2)

    # Step 3: 点击图文成片按钮
    tuwen_button = jy_main.GetChildren()[11]
    x, y = tuwen_button.BoundingRectangle.xcenter(), tuwen_button.BoundingRectangle.ycenter()
    api32.Click(x, y)

    def click_button(button, offset_x=0, offset_y=0):
        button_loc = button.BoundingRectangle
        button_loc.left += offset_x
        button_loc.top += offset_y
        x, y = button_loc.xcenter(), button_loc.ycenter()
        api32.Click(x, y)

    time.sleep(2)
    tuwen = api32.WindowControl(Name="图文成片", searchDepth=1)

    # Step 4: 查找并点击图文窗口中的子元素
    for i, c in enumerate(tuwen.GetChildren()):
        if i == 3:
            print(c, c.Name, c.ControlTypeName)
            x, y = c.BoundingRectangle.xcenter(), c.BoundingRectangle.ycenter()
            api32.Click(x, y)
            break

    # Step 5: 读取文本文件并将其复制到剪贴板
    text_content = read_text_file("e.txt")
    print(text_content)
    pyperclip.copy(text_content)  # This copies the text to the clipboard

    edit = tuwen.GetChildren()[4]

    # Instead of sending keys one by one, use pyautogui to paste the clipboard content
    edit.Click()  # Focus the edit control
    time.sleep(1)  # Ensure focus is set
    pyautogui.hotkey('ctrl', 'v')  # Simulates Ctrl + V to paste the clipboard content

    time.sleep(1)

    # Step 6: 点击生成按钮
    generate = tuwen.GetChildren()[8]
    button_loc = generate.BoundingRectangle
    button_loc.left += 350
    x, y = button_loc.xcenter(), button_loc.ycenter()
    api32.Click(x, y)

    time.sleep(2)

    button_loc.top -= 420
    x, y = button_loc.xcenter(), button_loc.ycenter()
    api32.Click(x, y)

    # Step 7: 等待下一个窗口
    while True:
        # print all windows
        if not api32.WindowControl(Name="图文成片", searchDepth=1).Exists(maxSearchSeconds=5):
            print("finished")
            break
        time.sleep(2)

    time.sleep(2)
    jy_main = api32.WindowControl(Name="剪映专业版", searchDepth=1)

    # Step 8: 点击全屏按钮
    full_screen = jy_main.GetChildren()[3]
    x, y = full_screen.BoundingRectangle.xcenter(), full_screen.BoundingRectangle.ycenter()
    api32.Click(x, y)

    # Step 9: 删除资源
    for i in range(10):
      source_rec = jy_main.GetChildren()[14].BoundingRectangle
      source_rec.left += 400 * i
      source_rec.top += 950
      x, y = source_rec.xcenter(), source_rec.ycenter()
      api32.Click(x, y)

      api32.SendKeys("{DELETE}")

    # Step 10: 点击导出按钮
    daochu_button = jy_main.GetChildren()[5]
    x, y = daochu_button.BoundingRectangle.xcenter(), daochu_button.BoundingRectangle.ycenter()
    api32.Click(x, y)

    time.sleep(2)

    # Step 11: 填写导出文件名
    daochu = jy_main.WindowControl(Name="导出", searchDepth=1)
    export_name = daochu.GetChildren()[0]
    export_name_rect = export_name.BoundingRectangle
    x, y = export_name_rect.xcenter(), export_name_rect.ycenter()
    api32.Click(x, y)

    # delete the default text
    for i in range(13):
        api32.SendKeys("{BACKSPACE}")

    # paste the new name
    pyperclip.copy("e")
    pyautogui.hotkey('ctrl', 'v')


    # Step 12: 点击导出按钮
    time.sleep(2)
    button = daochu.GetChildren()[-2]
    x, y = button.BoundingRectangle.xcenter(), button.BoundingRectangle.ycenter()
    api32.Click(x, y)


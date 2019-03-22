# 导入模块
from pymouse import PyMouse
from pykeyboard import PyKeyboard
# 实例化
pym = PyMouse()
pyk = PyKeyboard()
# 鼠标操作：
# x,y –坐标位置
# buttong 1表示左键，2表示点击右键
# n –点击次数，默认是1次，2表示双击
# –鼠标点击
pym.click(x, y, button, n) 
# 鼠标移动到坐标(x,y)
pym.move(x,y)
# 键盘操作：
# 模拟键盘输入字符串
pyk.type_string('www.fanlibei.com')
# 模拟键盘按X键
pyk.press_key('X')
# 模拟键盘松开X键
pyk.release_key('X')
# 模拟点击X键
pyk.tap_key('X')
# 模拟点击X键，2次，每次间隔3秒
pyk.tap_key('X',n=2,interval=3)
# 点击功能键F5
pyk.tap_key(pyk.function_keys[5])
# 点击小键盘5,6次
pyk.tap_key(pyk.numpad_keys[5],6)
# 点击回车键
pyk.tap_key(k.enter_key)
# 联合按键模拟
# 同时按alt+tab键盘
pyk.press_key(pyk.alt_key)# 按住alt键
pyk.tap_key(pyk.tab_key)# 点击tab键
pyk.release_key(pyk.alt_key)# 松开alt键


kk = PyKeyboard()
driver.find_element_by_css_selector( '你的上传文件元素位置').click()
sleep(1)
kk.tap_key(kk.shift_key) #切换为英文，看实际情况是否需要
sleep(1)
kk.type_string('X:\XXX\Pictures')#打开文件所在目录，方便多个文件上传
sleep(1)
kk.tap_key(kk.enter_key)
sleep(1)
kk.type_string('"1.png" "2.png" "3.png" ')#多文件上传
sleep(1)
kk.tap_key(kk.enter_key)
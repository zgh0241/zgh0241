from zgh0241 import Autotest
import sys


# 项目名称，和测试用例、页面元素表文件名称中的项目名称必须一致
# 此处项目名称更准确的表述应该是：测试计划名称。
plan_name = 'Wechat'

# 单 sheet 页面模式
sheet_name = '音乐站'

# sheet 页面匹配模式，仅支持结尾带*
#sheet_name = 'TestCase*'

# sheet 页面列表模式
#sheet_name = ['TestCase', 'test']

# 环境配置信息
desired_caps = {
    'platformName': 'Android', 
    'platformVersion': '6.0', 
    'deviceName': 'OPPO R9s', 
    'appPackage': 'com.tencent.mm', 
    'appActivity': '.ui.LauncherUI', 
    'noReset' : True, 
    'chromeOptions': {
        'androidProcess': 'com.tencent.mm:appbrand0'
        }
    }

# appium server
server_url = 'http://127.0.0.1:4723/wd/hub'

# 初始化自动化实例
sweet = Autotest(plan_name, sheet_name, desired_caps, server_url)

# 按条件执行,支持筛选的属性有：'id', 'title', 'designer', 'priority'
# sweet.fliter(priority='H')

# 执行自动化测试
sweet.plan()


# 如果是集成到 CI/CD，则给出退出码；也可以根据上面的测试结果自己生成退出码
#sys.exit(sweet.code)

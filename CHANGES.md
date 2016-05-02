CHANGES
=======

0.3.1
-----

Release data:

Feature
-------

* 更为完善的中文语言及英文语言切换

Improve:

* 使用 PrettyTable 美化百度百科的搜索结果
* 添加本地zip格式的library，无需安装第三方依赖

Bugfix:


0.3.0
-----

Release data: 2016-05-01

Feature:

* 新增网络搜索的功能（百度百科和维基百科）
* 增加状态栏以显示搜索状态
* 增加配置栏，以自定义搜索相关配置。合理的配置可提升准确度和搜索速度

Improve:

* 优化使用相似度搜索的判断逻辑，以提升性能

Bugfix:

* 相似度搜索无视配置执行的 Bug

0.2.0
-----

Release date: 2016-05-01

Feature:

* 为用户界面中可编辑的文字区域添加右键菜单
* 使用多进程来进行模糊查询操作以提升性能和响应速度
* 添加更为详细的菜单栏
* 为4个候选词列表区域添加右键菜单

Improve:

* 调整右键菜单中 Cut 和 Copy 的顺序
* 移除代码中有关搜狗词库的Warning

Bugfix:

* 当模糊搜索获得的名称在本地数据的词典中不存在时的KeyError

0.1.0
-----

Release date: 2016-04-30, first public release version

* core functions and core GUI

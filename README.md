# master
1、日志模块封装完成，100M进行切割
2、整体框架Python+pytest+request+pytest自带的html
二、pytest框架
setup_module(module):  #开始测试前执行一次,目前无实际使用
setup_function(function):  #每个测试用开始前执行一次，用于检查、准备测试环境
teardown_function(function):  #每个测试用例执行完执行一次，用于清除生成的测试数据
teardown_module(module):  #每次测试完成执行一次，用于还原测试环境
@pytest.mark.parametrize(‘mycase’, case.list,ids=case.name)  #装饰器，用来将list格式的测试用例分开执行
pytest.skip("skip testcase: (%s)" % mycase['Name']) #跳过测试用例
pytest.xfail("previous test failed (%s)" % mycase['Name']) #跳过会失败的测试用例

编写pytest测试样例非常简单，只需要按照下面的规则：

测试文件以test_开头（以_test结尾也可以）
测试类以Test开头，并且不能带有 init 方法
测试函数以test_开头
断言使用基本的assert即可

3.多进程运行cases

  当cases量很多时，运行时间也会变的很长，如果想缩短脚本运行的时长，就可以用多进程来运行。

安装pytest-xdist：

pip install -U pytest-xdist
运行模式：

pytest test_se.py -n NUM
其中NUM填写并发的进程数。

4.重试运行cases

  在做接口测试时，有事会遇到503或短时的网络波动，导致case运行失败，而这并非是我们期望的结果，此时可以就可以通过重试运行cases的方式来解决。

安装pytest-rerunfailures：

pip install -U pytest-rerunfailures
运行模式：

pytest test_se.py --reruns NUM
NUM填写重试的次数。


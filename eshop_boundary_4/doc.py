content = r'''分析电商平台系统测试时考虑的边界值情况
'''

answer = r'''对于电商平台，最重要的流程就是购物流程，包括几个重要功能：购物车、配送方式、支付方式、提交订单。我们讨论时以功能性测试为主，考虑以下功能：
'''

table = r'''
**系统测试（功能测试）**

| 模块         | 具体功能     | 边界值情况                                                   |
| ------------ | ------------ | ------------------------------------------------------------ |
| 用户信息管理 | 注册         | 用户名长度的边界值情况;密码长度的边界值情况               |
|              | 登录         | 用户输入密码的次数限制                                                             |
|              | 修改个人信息 | 用户名长度的边界值情况;密码长度的边界值情况;个人简介等信息的长度的边界值情况 |
| 搜索          | 搜索商品         | 商品名长度限制               |
| 购物车       | 添加商品     | 当某种产品有购物数量限制时，超过这一数值，是否也能放入购物车中 |
|              | 删除商品     | 当商品数量为1或0时，是否可以继续删除商品                     |
|              | 清空购物车   | 购物车商品数量进行边界值分析                                 |
| 支付         | 支付限额     | 当日最高消费金额限制，边界值分析                             |
|              | 支付次数     | 支付密码输入次数限制                                                              |
|              | 支付金额     | 支付金额大于或小于商品金额，是否能进行支付                   |
|              | 折扣         | 对于折扣的边界值分析                                         |
| 订单管理     | 个人订单     | 订单数量的边界值分析                                         |


**非功能性需求**

性能测试：如服务器处理响应的平均时间等。

压力测试：如最大同时在线量、同时处理订单量的上限的测试等。

**Class Level**

项目代码中，每个类内部的方法的测试。类之间和模块间的接口测试等。

**Method Level**

对个方法进行单独测试，检查参数的边界值情况。

'''
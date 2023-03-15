description = r'''电脑销售系统，主机（25￥单位价格，每月最多销售的数量为70），显示器（30￥单位价格，每月最多销售数量为80），外设（45￥单位价格，每月最多销售的数量为90
）；每个销售员每月至少销售一台完整的机器，当系统的主机这个变量接受到-1值的时候，系统自动统计该销售员本月的销售总额。当销售额小于等于1000（包括1000）按照10%提佣金，当销售额在1000-1800之间（包括1800
）的时候按照15%提佣金，当销售额大于1800时按照20%提佣金。 '''


md1 = r'''边界值法：32个测试用例

x主机的边界值（健壮性边界）：1， 2，35，69，70，71，-1

y外设的边界值（健壮性边界）：1，2，40，79，80，81，-1

z显示器的值边界（健壮性边界）：1，2，45，89，90，91，-1

佣金——设备基本边界值测试用例：12个'''


md2 = r'''健壮性边界的测试用例：9个'''


md3 = r'''直接根据设备销售数量基本边界值计算出的销售额都只在(1800,8200] 区间内，无法覆盖到其他的两个区间，所以以下对每个区间都设置了基
本边界值用例，来测试销售额在不同区间内的佣金

销售额：$25x+30y+45z$

销售额区间：[100, 1000],  (1000,1800], (1800,8200] 

三个区间的基本边界值：

- [100, 1000]：100， 125，970，1000
- (1000,1800]：1045，1775，1800
- (1800,8200] ：1830，8155，8200

佣金——销售额基本边界值测试用例:11个
'''


md4 = r'''所以总共的测试用例为：$12+9+11 = 32$ 个'''

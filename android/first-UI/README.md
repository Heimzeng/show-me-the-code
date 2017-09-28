## 中山大学移动信息工程学院本科生实验报告

## （ 2017 年秋季学期）

## 课程名称：手机平台应用开发 任课教师：刘宁

## 年级 15 专业（方向） 软件工程（数媒）

## 学号 15331012 姓名 曾庚涛

```
电话 13719334988 Email heimzeng@gmail.com
```
## 开始日期 2017 / 09 / 27 完成日期 2017 / 09 / 27

## 一、 实验题目

## 基本UI界面设计

## 二、 实现内容

```
实现一个Android应用，实现如下效果：
```
## 要求：

## （ 1 ）该界面为应用启动后看到的第一个界面

## （ 2 ）各控件的要求如下：

```
要求只用一个 ConstraintLayout 实现整个布局；
```

```
标题字体大小 20 sp，与顶部距离 20 dp，居中；
图片与标题的间距为 20 dp，居中；输入框整体距屏幕右边间距 20 dp，上
```
下两栏间距 20 dp，内容（包括提示内容）如图所示，内容字体大小 18 sp；

```
学号对应的 EditText 只能输入数字，密码对应的 EditText 输入方式为
```
密码；

```
两个单选按钮整体居中，字体大小 18 sp，间距 10 dp，默认选中的按钮为
```
第一个；

```
两个按钮整体居中，与上方控件间距 20 dp，按钮间的间距 10 dp，文字大
```
小 18 sp。按钮背景框左

```
右边框与文字间距 10 dp，上下边框与文字间距 5 dp，圆角半径 10 dp，背
```
景色为# 3 F 51 B 5

（ 3 ）使用的布局和控件：ConstraintLayout、TextView、EditText、

Button、ImageView、RadioGroup、RadioButton

## 三、 课后实验结果

## （ 1 ） 实验截图


## （ 2 ） 实验步骤以及关键代码

## 1 、创建一个空的安卓项目。

2 、首先添加一个TextView，设置字体大小 20 sp，与顶部距离 20 dp，居中；因为是使用
constraintlayout，所以通过如下设置可达到居中效果

```
3 .添加图片到mipmap文件夹下，然后通过以下语句导入图片
```
## 然后设置居中

4 .先添加两个EditText，然后使第一个的top对齐imageview的bottom并给一个 20 dp的
margin；然后使第二个的top对齐第一个edittext的bottom。
两个edittext都设置跟parent的右侧对齐并有一个右边的 20 dp的margin。
设置字体大小为 18 sp以及对应的edittext只能输入相应的字符。
由于需要拓展长度，设置定长又不能适应所有的手机屏幕，所以添加了一条距离parent左边
80 dp的guideline。
然后将edittext的left对齐到guideline并match_parent。
完成后大概如下

5 .添加两个TextView并分别把right对齐到edittext的left，left则对齐parent的
left，并把margin_left设置得跟edittext的margin_right一样。
6 .增加一个radiogroup并在其中添加两个radiobutton。
使radiogroup居中，并设置横向分布

```
设置距离上方的edittext 20 dp
把第一个radiobutton的check设置为true以达到默认选第一个的效果
7 .增加一个buttonbarlayout并在其中添加两个button
使buttonbarlayout居中
```

```
在drawable文件夹下新建一个bg.xml文件，bg.xml文件里面添加<shape...>...</>
设置corners、padding以及solid使得这个shape变成有内边距和背景色的圆角矩形
实现如下：
```
```
8 .在两个button中都引用上述的shape
```
（ 3 ） 实验遇到困难以及解决思路

```
主要遇到三个小困难：
1 .TextView和EditText的对齐问题，也就是这部分的对齐
```
## 直接左右对齐会有上下对不齐的情况

```
后来想了一下其实很简单，TextView对于edittext上下居中就可以了嘛
```
2 .button的shape问题，看了博客才找到知道那个形状的使用方法，也算是学习Android踩
的小坑吧

3 .Edittext的拓展问题，因为edittext里面只有五个字，直接match_parent又会覆盖到前
面的TextView，所以想了几分钟，决定用一条guideline去对齐。

## 四、 实验思考及感想

## 通过这个实验让我初步了解了安卓的UI设计，迈出了安卓应用设计的第一步。

## 虽然试验中遇到了一点小小的困难，不过都可以通过浏览前人的经验得到问题的答案。

## 这个实验增强了我对学习安卓开发以及学习JAVA方面的兴趣，相信在未来我会更加深入地研

## 究的。



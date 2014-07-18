============
Architecture
============

:date: 2010-10-03 10:20
:summary: Architecture smmary Architecture smmary Architecture smmary
    Architecture smmary Architecture smmary Architecture smmary 
    Architecture smmary Architecture smmary Architecture smmary 
    Architecture smmary Architecture smmary Architecture smmary 
    Architecture smmary Architecture smmary Architecture smmary Architecture smmary 
    Architecture smmary Architecture smmary Architecture smmary Architecture smmary 

.. contents::

Basic Architecture
==================

This is the basic system architecture:

::

    ui exe <--------+
      | ^           |
      v |           | 
    da proxy exe    |
      | ^           |
      v |           |
    bl dll <--------+ 
      |    
      v    
    da dll
      |
      v
    database

- "da proxy exe" is for broadcasting the database change to all connected client, otherwise
  ui exe accesses bl dll directly and can only get database change by manually refreshing the 
  view.
- "da proxy exe" is able to deliver web ui, so it is not only a web service, but also a web app

Extended Architecture
=====================

::

    view (both gui & console)
    view model

    App Proxy (a backend switcher, support both native and network backend)

    communication

    balancer
    cache
    app service
    DAL (with DB switcher)

    DB


Extensibility & Scalability
===========================

Multiple DbContext: 

* One extension one DbContext
* Have one "contain-everything" DbContext for database creation

Extending function layers:

* All components' API use the common business entities
* If need an extra layer, e.g. validation, Performance measurement, caching, message queue, 
  etc. , just add a new layer component in the middle with the same API interface (By this
  way, the prototype can just focus on the core functions)

Network
=======

* **Avoid Callback, but use client side service**

  If server use callback to contact client, one disadvantage is: once the callback interface changes,
  all the client must upgrade.

  Therefore, it may be better to have client side services to work as callback event interface. So when
  the client side service is changed, only the necessary minimal sites need to upgrade, other sites 
  can still work on the old client side versions.

* **Use Queue**

  Need to consider to use a message queues for critical communications. 

* **Peer-to-peer Design**

  - Every client can work as a proxy
  - Every client can replicate their proxy list to other clients
  - Because notfication is not based on callback, every client just needs to wait for others to 
    call them. So when a client update its own task, it will call all other clients one-by-one.
  - **Registration**: the living client register itself in the central database, if it is down, other 
    clients will update that client's status in the database if they cannot reach it.

中文搜索测试
============

下面这些错误大部分是观察所得，少部分是亲身经历，用血换来的教训：

1、高估帮忙的价值

大家都知道好的投资人应该是帮忙不添乱。有些投资者尤其是战略投资者，最喜欢罗列他们拥有的资源和帮助。但往往到最后发现，资源是共用的，派过来帮忙的人是外行，其他诉求石沉大海，最好还得靠自己。

2、低估添乱的影响

业内有一些老资历公司，是公认的害虫，尽管在被投资公司中占小股，但发号施令，天天骚扰，董事会上从不配合，让你日日胸闷。就因为他最早找到你，就因为他不断引诱你，就因为不拿白不拿，就因为钱快烧完，总之你拿了缺乏共识的投资人的钱。最终，听他的可能把公司搞成四不像，不听他的他又去外面放话，让你陷入人间炼狱。

3、把投资人等同于身后的机构

不靠谱的机构，人多半不靠谱;但靠谱的机构，不一定各个都靠谱。有的人虽然在产生过很多明星公司的机构，但完全水货一个，好的案子跟他无关，坑爹的案子干过不少。擦亮眼睛，去评判投资人的专业程度，而不要被所谓品牌蛊惑。

4、宁做凤尾，不做鸡头

这指的是孵化器的情形。很多团队一窝蜂往明星孵化器钻，也不肯加入一个新开设的孵化器。然而，孵化器的好坏区别在于它资源的大小，好的孵化器，能支持数十个团队都得到支援，单薄的孵化器则只能支援数个，甚至一个。即便你假如一个不知名的孵化器，但如果你表现得最好，起码你可以得到再次融资的机会。至于只提供办公场地的孵化器，我只想说：我很幸福。

5、过早稀释股权

因为不熟悉融资的游戏规则，因为你听信了“重要的是赚钱了以后分钱” ，你在第一轮或者第二轮融资中就稀释了 40%、60% 甚至 80% 的股权。被别人控制公司导致失败、分裂或难以发展倒不算痛心，万一发展得很好，结果前面稀释的越多，后面融资的选择就越少，当你被稀释到只剩 10%、5%，这还算是你的公司吗?

6、用错误的结构融资

为了赶快把钱拿进来，跟投资人签夸张的分成方式、管理机制、对赌条款、完全不平等的清算条款等非常另类的合同，或是用非国际惯例的结构设计特别股。这里面的道理很简单，没想过共赢做大的投资人也没能力让公司发展壮大。乱七八糟的资本结构和合同，只会吓跑后面想投资的机构。

7、早期融资轻视投资人

很多人融了天使资金以后，闷头封闭，再也不和投资机构接触。如果你选择了一家优秀的投资机构，这是大大的浪费。投资机构积累了大量成败案例和商业判断以及其他企业的友好关系，如果不去交流和利用，和拿土壕的钱有何区别?

8、后期融资高估投资人

公司发展起来之后，很多人在选择下轮投资的时候，总倾向于大牌、知名的机构，但越大牌的机构，手中积累的优秀公司越多，他绝不会为你的生死去赌上身家。发展方向是否一致，反而是唯一的判断标准。

9、选择不靠谱的战略投资

但凡投资部门没有独立于业务部门的战略投资方，都是耍流氓。有一些大公司(不点名)投资了一堆团队，不要说成功，连产品影子都没看到。为何?因为负责投资部门的高管是无实权的存在，或者兼任着其他业务部门。投资的成败要么无足轻重要么只是他汇报业绩时候的锦上添花。你们的死活，与他们无干。

10、选择关注自己多于创业者的投资人

总在说自己多牛逼、公司多牛逼，却不细细询问创业者情况的投资人，是典型的投机者，一旦谈成投资，他多半人间蒸发，忙着另外一些让他“更牛逼”的事情。于是，你不过是他投机过程中的问路石或者垫脚石。

11、选择一头热的投资人

当然投资人必须对你的团队、产品，或商业模式有一定的热情，但投资毕竟是很理性的工作，如果他过分热情，却没有想清楚自己为什么要投资你的公司，那也是非常危险的结合。 新创公司往往必须酝酿多年才能到达被收购或上市的彼岸，在这漫漫长路上，创业团队的财务状况常常是忽高忽低。 现在一头热的投资人，未来随时可能会受不了这云霄飞车，转而成为难搞的恐怖股东。

12、选择内部权力结构不稳定的投资人

有一种投资人，投资的时候都很好，刚开始成为股东时也合作非常愉快。但突然间股东的公司内部出现斗争、权力大幅转移，导致股东代表换成了当初反对这样投资的一方，接着便开始处处找团队麻烦。碰到这样情况新创公司当然是哑巴吃黄莲，不过如果一开始对方的权力结构就不太稳定，那么拿他的钱之前恐怕还是要三思。如何评价一个公司乱不乱，看高管是不是走马灯就知道了，我也不多说了!

13、选择没有投资过同样业务的投资人

这是先有鸡还是先有蛋的问题，但当小白鼠的人总是风险比较大。我的经验是，第一次投资某业务的股东，投资后在董事会上大概要 12-18 个月才能真的上轨道，到了第二次投资以后，情况就会好很多。所以有选择的话，还是尽量倾向于已经投过相关业务公司的人。

14、选择基金将要到期的投资人

最后，这指的是中后期融资所发生的情况。基金通常有7-10 年的寿命，因此到了后期，负责管理基金的投资人(所谓 GP)会受到他们的股东(所谓 LP)越来越大的压力，要赶快出脱持股、获利了结。所以假设他投资你时基金还有4、5 年寿命，那你可以想像2、3 年后，他会开始感受到压力，因此推动你往退出方向走的力度会不断的增加，这时可能会让公司陷入困难的抉择。

# scau_class_table

#2015-05-27开始修改
理由：学校正方教务系统升级
      postdata中忽略验证码即textcode一项可免验证码登录

#2015-05-28 3：47完成


1.引入beautifulsoup模块，更新了viewstate和viewstategenerator的获取

2.添加了who模块，纯属为了测试偷懒方便。写在一起也无妨。

3.修改了fo.write()后没有fo.close()的粗心......Orz

4.新版本抓取的入口为'http://202.116.160.170/default_ysdx.aspx'华南农业大学，其他学校正方教务系统修改中间的ip即可

5.所有的注释部分为验证码的处理，恢复即为验证码版本，入口把default_ysdx.aspx去掉即可

#使用说明
1.who.py中输入xh（学号），xm（密码），xnd（学年格式：2014-2015），xqd（学期：1，2或者3）
格式  xh='123456789'xm='123456789' xnd='2014-2015' xqd='1'

2.beautifulsoup模块可用easy_install或者pip下载

3.from PIL import Image可以注释掉，用于处理验证码，但是此处是免验证码登录

4.personalclass.html保存了你查询的学期课表的信息，再次运行class_schedule_nocode(2015_5_27).py脚本会再次生成

5.脚本的目的是为了方便同学，密码都是明文发送，当然正方也是。所以请不要添加恶意代码，谢谢。

#what's for next?
·期待学校正方的再次更新，对于之前的更新，我表示我不觉得postdata中忽略掉验证码也能登录是个大型的漏洞或者bug。
当然这可能给一些弱口令的账号一点点不安全，但是其实没有谁会去做这种事情，毕竟服务器已经有够烂的了。
·接下来会继续解决viewstate和viewstategenerator的一些问题，希望在我毕业之前能用python解决吧。
·暑假前的抢课脚本（用于少部分人），住我楼下的小伙伴如无意外应该会推出php版扔到微信公众平台
·小小的脚本，写得不好，请见谅。
#留个联系方式
·wechat：visionyimian



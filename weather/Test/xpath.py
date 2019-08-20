import codecs
from lxml import etree
import re

response ="""
<!DOCTYPE html PUBLIC "-//W3C//DTD XHTML 1.0 Transitional//EN" "http://www.w3.org/TR/xhtml1/DTD/xhtml1-transitional.dtd">
<html xmlns="http://www.w3.org/1999/xhtml">
<head>
<meta http-equiv="Content-Type" content="text/html; charset=utf-8" />
<link href="http://www.weather.com.cn//m2/c/forcast/textFC.css" rel="stylesheet" type="text/css" media="all" />
<link  rel="icon" href="http://www.weather.com.cn//m2/i/icon/faviconie9.ico?v=3" type="image/x-icon" />
<meta name="msapplication-task" content="name=天气资讯;action-uri=http://www.weather.com.cn/news/index.shtml;icon-uri=http://www.weather.com.cn/favicon.ico" />
<meta name="msapplication-task" content="name=生活天气;action-uri=http://www.weather.com.cn/life/index.shtml;icon-uri=http://www.weather.com.cn/favicon.ico" />
<meta name="msapplication-task" content="name=气象科普;action-uri=http://www.weather.com.cn/science/index.shtml;icon-uri=http://www.weather.com.cn/favicon.ico" />
<meta name="msapplication-task" content="name=灾害预警;action-uri=http://www.weather.com.cn/alarm/index.shtml;icon-uri=http://www.weather.com.cn/favicon.ico" />
<meta name="msapplication-task" content="name=旅游天气;action-uri=http://www.weather.com.cn/trip/index.shtml;icon-uri=http://www.weather.com.cn/favicon.ico" />
<script type="text/javascript" src="http://www.weather.com.cn//m2/j/public/IE9sitemode.js"></script>
<script src="http://www.weather.com.cn/m2/j/hebing20130424.js" type="text/javascript"></script>
<link rel="stylesheet" type="text/css" href="http://www.weather.com.cn/m2/c/public/public.css" />
<link rel="stylesheet" type="text/css" href="http://www.weather.com.cn/m2/c/public/mainBox.css" />
<script type="text/javascript" src="http://www.weather.com.cn/m2/j/public/tooltips201411.js?y=201408"></script>
<script type="text/javascript" src="http://i.tq121.com.cn/j/photo/biao_tou68.js" ></script>
<script type="text/javascript" src="http://i.tq121.com.cn/j/core.js"></script>
<script>W.css('c/weather2014/common_o.css','c/m_search.css')</script>
<title>北京天气预报</title>
<meta name="keywords" content="北京地区天气预报,北京今日天气,北京明日天气,北京一周天气预报" />
<meta name="description" content="北京天气预报，及时准确发布中央气象台天气信息，便捷查询北京今日天气，北京明日天气，北京一周天气预报，北京天气预报还提供北京各区县的生活指数、健康指数、交通指数、旅游指数，及时发布北京气象预警信号、各类气象资讯。" />
</head>
<body>
<input id="colorid" type="hidden" value="预报">
<style>
.contentboxTab{
	width:1000px;
	margin:0 auto;}
.day_tabs{
	clear:both;}
.lQCity{
	width:976px;}
.conMidtab{
	width:976px;}
.conMidtab5{
	width:957px;}
.conMidtab3{
	width:957px;}
.contentLtab{
	width:956px;}
</style>
<script type="text/javascript" src="http://i.tq121.com.cn/j/weather2014/rili.js?id=201511"></script>
<link href="http://i.tq121.com.cn/c/weather2017/headStyle_1.css" rel="stylesheet">

<div class="weather_li">
  <div class="nav_li_box">
    <div class="weather_li_left">
      <a href="http://www.weather.com.cn/">首页</a>
      <a href="http://www.weather.com.cn/forecast/">预报</a>
      <a href="http://www.weather.com.cn/radar/">雷达</a>
      <a href="http://www.weather.com.cn/satellite/">云图</a>
      <a href="http://www.weather.com.cn/live/">临近预报</a>
      <a href="http://products.weather.com.cn/">专业产品</a>
      <a href="http://news.weather.com.cn/">资讯</a>
      <a href="http://www.weather.com.cn/life/">生活</a>
      <a href="http://www.weather.com.cn/traffic/">交通</a>
      <a href="http://www.weatherdt.com/" target="_blank">产创平台</a>
      <a href="" class="shengjz"></a>
      <div href="javascript:void(0)" class="more_li">更多
        <div class="weather_li_open" style="width:555px;">
          <p>
            <a href="http://www.weather.com.cn/alarm/">预警</a>
            <a href="http://typhoon.weather.com.cn/" target="_blank">台风路径</a>
            <a href="http://www.weather.com.cn/space/">空间天气</a>
            <a href="http://p.weather.com.cn/">图片</a>
            <a href="http://www.weather.com.cn/video/">视频</a>
            <a href="http://www.weather.com.cn/zt/">专题</a>
            <a href="http://www.weather.com.cn/air/">环境</a>
            <a href="http://www.weather.com.cn/trip/">旅游</a>
            <a href="http://www.sportsweather.cn/golf/">高尔夫</a>
            <a href="http://www.weather.com.cn/forecast/skiweather.shtml">滑雪</a>
            <a href="http://www.weather.com.cn/aviation/">航空</a>
            <a href="http://www.weather.com.cn/beltroad/">一带一路</a>
          </p>
          <p style="border:none;" class="erp">
            <a href="http://www.weather.com.cn/tqbx/">保险</a>
            <a href="http://www.weather.com.cn/slpd/index.shtml">水利</a>
            <a href="http://www.weather.com.cn/agriculture/pest/">农业·病虫害</a>
            <a  href="http://www.weather.com.cn/science/">科普</a>
            <a href="http://www.weather.com.cn/fzjz/">减灾</a>
            <a href="http://www.weather.com.cn/climate/">生态</a>
            <!-- <a href="http://marketing.weather.com.cn/">商业合作</a> -->
            <a href="http://www.weatherlive.com.cn/">视频云平台</a>
            <a href="http://www.weather.com.cn/province/">省级站</a>
            <a href="http://club.weather.com.cn/">社区</a>
          </p>
        </div>
      </div>
    </div>
    <div class="weather_li_right">
      <div id="w_weather" class="w_weather"></div>
      <!--登陆后的情况-->
      <span class="top_list head-right" style="display:none;" id="logined">
        <li class="li_wd">
          <a class="top_list_title"><img class="head-imgs" src="http://i.tq121.com.cn/i/weather2015/user/my-head.png" id="userimg"/></a>
          <ul class="top-list-hidden">
            <a href="http://u2.weather.com.cn/web/dashboard/index.do"><li>个人中心</li></a>
            <a href="http://u2.weather.com.cn/weathercenter/userself.html"><li>账号设置</li></a>
            <a href="javascript:void(0);" onclick="logout(window.location.href)"><li>退出</li></a>
          </ul>
          <div class="clear"></div>
        </li>
        <a class="w_email" href="http://u2.weather.com.cn/web/dashboard/message/get.do"><img src="http://i.tq121.com.cn/i/ucenter/pc/email.png" class="email-img">  </a>
      </span>
      <!--登陆后的情况-->
      <!--未登录的情况-->
      <span class="weather-login" style="display:none;" id="unlogined">
        <a class="login-icon" onclick="login(window.location.href)">登录</a><a class="login-zhuce" onclick="regist(window.location.href)">注册</a>
      </span>
      <!--未登录的情况-->
    </div>
    <div class="clear:both"></div>
  </div>
</div>
<div class="weather_li_head">
  <div class="weather_li_box">
    <div class="w_li_logo fl">
      <a href="http://www.weather.com.cn/" target="_blank"></a>
      <span></span>
    </div>
    <div class="search-box fr">
      <div class="search clearfix">
        <div class="select_li">
          <p>天气<i></i></p>
          <ul class="select_box">
            <li class="tianqi cur">天气</li>
            <li class="zixun">资讯</li>
          </ul>
        </div>
        <input type="text" value="输入城市、乡镇、街道、景点名称 查天气" id="txtZip" class="textinput text">
        <div id="zhong_search">
          <iframe src="http://promotion.chinaso.com/chinasosearch/chinaso-weather1.html" frameborder="0" scrolling="no" marginheight="0" marginwidth="0"></iframe>
        </div>
        <span class="input-btn"><input type="button" value="" id="btnZip" class="btn ss"></span>
        <div class="clear"></div>
      </div>
      <div class="inforesult"></div>
      <div id="show">
        <ul></ul>
      </div>
      <div class="city-box">
        <div class="city-tt">
          <a href="javascript:void(0)" class="cur">正在热搜</a>
          <a href="javascript:void(0)" >本地周边</a>
          <b></b>
        </div>
        <div class="w_city city_guonei" style="display:block; padding-bottom:0">
          <dl>
            <dt>国内</dt>
            <dd>
              <!--<a href="http://www.weather.com.cn/weather1d/101271906.shtml#search" style="position: relative; left: -12px; padding: 0px 1px; color:#7d7d7d; background:#ffe7d4;">九寨沟<em style="font-size: 10px; color: #f68d3b;padding-left:1px;position:relative;top:3px;"><img src="http://i.tq121.com.cn/i/weather2017/tag.png" style="vertical-align: top;border:none;" target="_blank"></em></a>-->
              <a href="http://www.weather.com.cn/weather1d/101010100.shtml#search" target="_blank">北京</a>
              <a href="http://www.weather.com.cn/weather1d/101020100.shtml#search" target="_blank">上海</a>
              <a href="http://www.weather.com.cn/weather1d/101210101.shtml#search" target="_blank">杭州</a>
              <a href="http://www.weather.com.cn/weather1d/101280101.shtml#search" target="_blank">广州</a>
              <a href="http://www.weather.com.cn/weather1d/101200101.shtml#search" target="_blank">武汉</a>
              <a href="http://www.weather.com.cn/weather1d/101190101.shtml#search" target="_blank">南京</a>
              <a href="http://www.weather.com.cn/weather1d/101280601.shtml#search" target="_blank">深圳</a>
              <a href="http://www.weather.com.cn/weather1d/101190401.shtml#search" target="_blank">苏州</a>
              <a href="http://www.weather.com.cn/weather1d/101230201.shtml#search" target="_blank">厦门</a>
              <a href="http://www.weather.com.cn/weather1d/101220101.shtml#search" target="_blank">合肥</a>
            </dd>
          </dl>
          <dl>
            <dt>国际</dt>
            <dd>
              <a href="http://www.weather.com.cn/weather1d/102010100.shtml#search" target="_blank">首尔</a>
              <a href="http://www.weather.com.cn/weather1d/104010100.shtml#search" target="_blank">新加坡</a>
              <a href="http://www.weather.com.cn/weather1d/106010100.shtml#search" target="_blank">曼谷</a>
              <a href="http://www.weather.com.cn/weather1d/401110101.shtml#search" target="_blank">纽约</a>
              <a href="http://www.weather.com.cn/weather1d/124020100.shtml#search" target="_blank">迪拜</a>
              <a href="http://www.weather.com.cn/weather1d/103163100.shtml#search" target="_blank">大阪</a>
              <a href="http://www.weather.com.cn/weather1d/601020101.shtml#search" target="_blank">悉尼</a>
              <a href="http://www.weather.com.cn/weather1d/601060101.shtml#search" target="_blank">墨尔本</a>
              <a href="http://www.weather.com.cn/weather1d/401040101.shtml#search" target="_blank">洛杉矶</a>
              <a href="http://www.weather.com.cn/weather1d/105010100.shtml#search" target="_blank">吉隆坡</a>
            </dd>
          </dl>
          <dl>
            <dt>景点</dt>
            <dd>
              <a href="http://www.weather.com.cn/weather1d/10101010018A.shtml#search" target="_blank">故宫</a>
              <a href="http://www.weather.com.cn/weather1d/10130051008A.shtml#search" target="_blank">阳朔漓江</a>
              <a href="http://www.weather.com.cn/weather1d/10118090107A.shtml#search" target="_blank">龙门石窟</a>
              <a href="http://www.weather.com.cn/weather1d/10109022201A.shtml#search" target="_blank">野三坡</a>
              <a href="http://www.weather.com.cn/weather1d/10101020015A.shtml#search" target="_blank">颐和园</a>
              <a href="http://www.weather.com.cn/weather1d/10127190601A.shtml#search" target="_blank">九寨沟</a>
              <a href="http://www.weather.com.cn/weather1d/10102010007A.shtml#search" target="_blank">东方明珠</a>
              <a href="http://www.weather.com.cn/weather1d/10125150503A.shtml#search" target="_blank">凤凰古城</a>
              <a href="http://www.weather.com.cn/weather1d/10111010119A.shtml#search" target="_blank">秦始皇陵</a>
              <a href="http://www.weather.com.cn/weather1d/10125060301A.shtml#search" target="_blank">桃花源</a>
            </dd>
          </dl>
          <dl style="margin-bottom:5px;border:none;">
            <dt>高球</dt>
            <dd>
              <a href="http://www.sportsweather.cn/weather/10102090003F.shtml#search" target="_blank">佘山</a>
              <a href="http://www.sportsweather.cn/weather/10129010601F.shtml#search" target="_blank">春城湖畔</a>
              <a href="http://www.sportsweather.cn/weather/10101070004F.shtml#search" target="_blank">华彬庄园</a>
              <a href="http://www.sportsweather.cn/weather/10128060113F.shtml#search" target="_blank">观澜湖</a>
              <a href="http://www.sportsweather.cn/weather/10131010107F.shtml#search" target="_blank">依必朗</a>
              <a href="http://www.sportsweather.cn/weather/10102080001F.shtml#search" target="_blank">旭宝</a>
              <a href="http://www.sportsweather.cn/weather/10131021101F.shtml#search" target="_blank">博鳌</a>
              <a href="http://www.sportsweather.cn/weather/10129140501F.shtml#search" target="_blank">玉龙雪山</a>
              <a href="http://www.sportsweather.cn/weather/10128010103F.shtml#search" target="_blank">番禺南沙</a>
              <a href="http://www.sportsweather.cn/weather/10101040001F.shtml#search" target="_blank">东方明珠</a>
            </dd>
          </dl>
        </div>
        <div class="w_city city_guonei gn">
          <dl>
            <dt>地区</dt>
            <dd class="diq"></dd>
          </dl>
          <dl>
            <dt>景点</dt>
            <dd class="jind"></dd>
          </dl>
          <dl style="border:none;margin-bottom:5px;">
            <dt>乡镇</dt>
            <dd class="jind"></dd>
          </dl>
        </div>
      </div>
    </div>
    <div class="clear"></div>
  </div>
</div>
<script type="text/javascript" src="http://i.tq121.com.cn/j/core.js"></script>

<div style="width:1000px;" class="locationSearch">
<span class="location">
<a href="http://www.weather.com.cn/" class="master"><strong>中国天气网</strong></a>&gt;文字版国内城市天气预报&nbsp;|&nbsp;<a href="http://www.weather.com.cn/static/html/weather.shtml" target="_blank" class="master">地图版国内城市天气预报</a></span>
</div>
<div class="lqcontentBoxH">
<div class="lqcontentBoxheader">
<ul>
<li><span>&nbsp;&nbsp;</span><a href="/textFC/beijing.shtml" target="_blank">北京</a></li>
<li><span>A</span><a href="/textFC/anhui.shtml" target="_blank">安徽</a></li>
<li><span>C</span><a href="/textFC/chongqing.shtml" target="_blank">重庆</a></li>
<li><span>F</span><a href="/textFC/fujian.shtml" target="_blank">福建</a></li>
</ul>
<ul>
<li><span>G</span><a href="/textFC/gansu.shtml" target="_blank">甘肃</a><a href="/textFC/guangdong.shtml" target="_blank">广东</a><a href="/textFC/guangxi.shtml" target="_blank">广西</a><a href="/textFC/guizhou.shtml" target="_blank">贵州</a></li>
<li><span>H</span><a href="/textFC/hainan.shtml" target="_blank">海南</a><a href="/textFC/hebei.shtml" target="_blank">河北</a><a href="/textFC/henan.shtml" target="_blank">河南</a><a href="/textFC/hubei.shtml" target="_blank">湖北</a><a href="/textFC/hunan.shtml" target="_blank">湖南</a><a href="/textFC/heilongjiang.shtml" target="_blank">黑龙江</a></li>
<li><span>J</span><a href="/textFC/jilin.shtml" target="_blank">吉林</a><a href="/textFC/jiangsu.shtml" target="_blank">江苏</a><a href="/textFC/jiangxi.shtml" target="_blank">江西</a></li>
<li><span>L</span><a href="/textFC/liaoning.shtml" target="_blank">辽宁</a></li>
</ul>
<ul>
<li><span>N</span><a href="/textFC/neimenggu.shtml" target="_blank">内蒙古</a><a href="/textFC/ningxia.shtml" target="_blank">宁夏</a></li>
<li><span>Q</span><a href="/textFC/qinghai.shtml" target="_blank">青海</a></li>
<li><span>S</span><a href="/textFC/shandong.shtml" target="_blank">山东</a><a href="/textFC/shan-xi.shtml" target="_blank">陕西</a><a href="/textFC/shanxi.shtml" target="_blank">山西</a><a href="/textFC/shanghai.shtml" target="_blank">上海</a><a href="/textFC/sichuan.shtml" target="_blank">四川</a></li>
<li><span>T</span><a href="/textFC/tianjin.shtml" target="_blank">天津</a></li>
</ul>
<ul>
<li><span>X</span><a href="/textFC/xizang.shtml" target="_blank">西藏</a><a href="/textFC/xinjiang.shtml" target="_blank">新疆</a></li>
<li><span>Y</span><a href="/textFC/yunnan.shtml" target="_blank">云南</a></li>
<li><span>Z</span><a href="/textFC/zhejiang.shtml" target="_blank">浙江</a></li>
<li><span>港澳台</span><a href="/textFC/hongkong.shtml" target="_blank">香港</a><a href="/textFC/macao.shtml" target="_blank">澳门</a><a href="/textFC/taiwan.shtml" target="_blank">台湾</a></li>
</ul>
</div>
<div class="contentboxTab">
<h1><a href = "http://www.weather.com.cn/forecast/">天气预报</a>&nbsp;&nbsp;>&nbsp;&nbsp;<a href = "/textFC/hb.shtml">国内</a>&nbsp;&nbsp;>&nbsp;&nbsp;
<a href="/textFC/beijing.shtml">北京</a>
<span>
发布时间:
          2019-08-20 07:30
</span></h1>
<div class="contentboxTab1">
<div class="contentboxTab2">
<div class="lQCity">
<ul>
<li><a href="#0">北京</a></li>
</ul>
</div>
<ul class="day_tabs">
<li class="selected">今天周二(8月20日)</li>
<li>周三(8月21日)</li>
<li>周四(8月22日)</li>
<li>周五(8月23日)</li>
<li>周六(8月24日)</li>
<li>周日(8月25日)</li>
<li>周一(8月26日)</li>
</ul>
<div class="hanml">
<div class="conMidtab">
<div class="conMidtab5">
<table width="100%" border="0" cellpadding="0" cellspacing="0">
<tr>
<td width="74" rowspan="2">市</td>
<td width="83" rowspan="2">区/县</td>
<td height="37" colspan="3">周二(8月20日)白天</td>
<td colspan="3">周二(8月20日)夜间</td>
<td width="49" rowspan="2" class="last">&nbsp;</td>
</tr>
<tr>
<td width="89" height="23">天气现象</td>
<td width="162">风向风力</td>
<td width="92">最高气温</td>
<td width="98">天气现象</td>
<td width="177">风向风力</td>
<td width="86">最低气温</td>
</tr>
</table>
</div>
<div class="conMidtab3">
<a name="0" id="0"></a>
<table width="100%" border="0" cellpadding="0" cellspacing="0">
<tr>
<td width="74" rowspan="17" class="rowsPan">北京</td>
<td width="83" height="23">
<a href="http://www.weather.com.cn/weather/101010100.shtml" target="_blank">北京</a></td>
<td width="89">小雨</td>
<td width="162">
<span>南风</span>
<span class="conMidtabright"><3级</span></td>
<td width="92">28</td>
<td width="98">多云</td>
<td width="177">
<span>北风</span>
<span class="conMidtabright"><3级</span></td>
<td width="86">19</td>
<td width="49" class="last">
<a href="http://www.weather.com.cn/weather/101010100.shtml" target="_blank">详情</a></td>
</tr>
<tr>
<td width="83" height="23">
<a href="http://www.weather.com.cn/weather/101010200.shtml" target="_blank">海淀</a></td>
<td width="89">小雨</td>
<td width="162">
<span>南风</span>
<span class="conMidtabright">3-4级</span></td>
<td width="92">29</td>
<td width="98">多云</td>
<td width="177">
<span>北风</span>
<span class="conMidtabright"><3级</span></td>
<td width="86">18</td>
<td width="49" class="last">
<a href="http://www.weather.com.cn/weather/101010200.shtml" target="_blank">详情</a></td>
</tr>
<tr>
<td width="83" height="23">
<a href="http://www.weather.com.cn/weather/101010300.shtml" target="_blank">朝阳</a></td>
<td width="89">小雨</td>
<td width="162">
<span>南风</span>
<span class="conMidtabright"><3级</span></td>
<td width="92">29</td>
<td width="98">多云</td>
<td width="177">
<span>北风</span>
<span class="conMidtabright"><3级</span></td>
<td width="86">19</td>
<td width="49" class="last">
<a href="http://www.weather.com.cn/weather/101010300.shtml" target="_blank">详情</a></td>
</tr>
<tr>
<td width="83" height="23">
<a href="http://www.weather.com.cn/weather/101010400.shtml" target="_blank">顺义</a></td>
<td width="89">小雨</td>
<td width="162">
<span>东南风</span>
<span class="conMidtabright"><3级</span></td>
<td width="92">29</td>
<td width="98">多云</td>
<td width="177">
<span>北风</span>
<span class="conMidtabright"><3级</span></td>
<td width="86">19</td>
<td width="49" class="last">
<a href="http://www.weather.com.cn/weather/101010400.shtml" target="_blank">详情</a></td>
</tr>
<tr>
<td width="83" height="23">
<a href="http://www.weather.com.cn/weather/101010500.shtml" target="_blank">怀柔</a></td>
<td width="89">小雨</td>
<td width="162">
<span>南风</span>
<span class="conMidtabright"><3级</span></td>
<td width="92">28</td>
<td width="98">多云</td>
<td width="177">
<span>北风</span>
<span class="conMidtabright"><3级</span></td>
<td width="86">18</td>
<td width="49" class="last">
<a href="http://www.weather.com.cn/weather/101010500.shtml" target="_blank">详情</a></td>
</tr>
<tr>
<td width="83" height="23">
<a href="http://www.weather.com.cn/weather/101010600.shtml" target="_blank">通州</a></td>
<td width="89">小雨</td>
<td width="162">
<span>南风</span>
<span class="conMidtabright"><3级</span></td>
<td width="92">27</td>
<td width="98">多云</td>
<td width="177">
<span>北风</span>
<span class="conMidtabright"><3级</span></td>
<td width="86">18</td>
<td width="49" class="last">
<a href="http://www.weather.com.cn/weather/101010600.shtml" target="_blank">详情</a></td>
</tr>
<tr>
<td width="83" height="23">
<a href="http://www.weather.com.cn/weather/101010700.shtml" target="_blank">昌平</a></td>
<td width="89">小雨</td>
<td width="162">
<span>东南风</span>
<span class="conMidtabright"><3级</span></td>
<td width="92">29</td>
<td width="98">多云</td>
<td width="177">
<span>西北风</span>
<span class="conMidtabright"><3级</span></td>
<td width="86">19</td>
<td width="49" class="last">
<a href="http://www.weather.com.cn/weather/101010700.shtml" target="_blank">详情</a></td>
</tr>
<tr>
<td width="83" height="23">
<a href="http://www.weather.com.cn/weather/101010800.shtml" target="_blank">延庆</a></td>
<td width="89">中雨</td>
<td width="162">
<span>东南风</span>
<span class="conMidtabright"><3级</span></td>
<td width="92">25</td>
<td width="98">多云</td>
<td width="177">
<span>西风</span>
<span class="conMidtabright"><3级</span></td>
<td width="86">16</td>
<td width="49" class="last">
<a href="http://www.weather.com.cn/weather/101010800.shtml" target="_blank">详情</a></td>
</tr>
<tr>
<td width="83" height="23">
<a href="http://www.weather.com.cn/weather/101010900.shtml" target="_blank">丰台</a></td>
<td width="89">小雨</td>
<td width="162">
<span>南风</span>
<span class="conMidtabright">3-4级</span></td>
<td width="92">29</td>
<td width="98">多云</td>
<td width="177">
<span>北风</span>
<span class="conMidtabright"><3级</span></td>
<td width="86">19</td>
<td width="49" class="last">
<a href="http://www.weather.com.cn/weather/101010900.shtml" target="_blank">详情</a></td>
</tr>
<tr>
<td width="83" height="23">
<a href="http://www.weather.com.cn/weather/101011000.shtml" target="_blank">石景山</a></td>
<td width="89">小雨</td>
<td width="162">
<span>南风</span>
<span class="conMidtabright"><3级</span></td>
<td width="92">29</td>
<td width="98">多云</td>
<td width="177">
<span>北风</span>
<span class="conMidtabright"><3级</span></td>
<td width="86">19</td>
<td width="49" class="last">
<a href="http://www.weather.com.cn/weather/101011000.shtml" target="_blank">详情</a></td>
</tr>
<tr>
<td width="83" height="23">
<a href="http://www.weather.com.cn/weather/101011100.shtml" target="_blank">大兴</a></td>
<td width="89">小雨</td>
<td width="162">
<span>南风</span>
<span class="conMidtabright"><3级</span></td>
<td width="92">28</td>
<td width="98">多云</td>
<td width="177">
<span>北风</span>
<span class="conMidtabright"><3级</span></td>
<td width="86">18</td>
<td width="49" class="last">
<a href="http://www.weather.com.cn/weather/101011100.shtml" target="_blank">详情</a></td>
</tr>
<tr>
<td width="83" height="23">
<a href="http://www.weather.com.cn/weather/101011200.shtml" target="_blank">房山</a></td>
<td width="89">小雨</td>
<td width="162">
<span>西南风</span>
<span class="conMidtabright">3-4级</span></td>
<td width="92">28</td>
<td width="98">多云</td>
<td width="177">
<span>北风</span>
<span class="conMidtabright"><3级</span></td>
<td width="86">18</td>
<td width="49" class="last">
<a href="http://www.weather.com.cn/weather/101011200.shtml" target="_blank">详情</a></td>
</tr>
<tr>
<td width="83" height="23">
<a href="http://www.weather.com.cn/weather/101011300.shtml" target="_blank">密云</a></td>
<td width="89">小雨</td>
<td width="162">
<span>南风</span>
<span class="conMidtabright"><3级</span></td>
<td width="92">26</td>
<td width="98">多云</td>
<td width="177">
<span>东北风</span>
<span class="conMidtabright"><3级</span></td>
<td width="86">17</td>
<td width="49" class="last">
<a href="http://www.weather.com.cn/weather/101011300.shtml" target="_blank">详情</a></td>
</tr>
<tr>
<td width="83" height="23">
<a href="http://www.weather.com.cn/weather/101011400.shtml" target="_blank">门头沟</a></td>
<td width="89">小雨</td>
<td width="162">
<span>南风</span>
<span class="conMidtabright"><3级</span></td>
<td width="92">29</td>
<td width="98">多云</td>
<td width="177">
<span>北风</span>
<span class="conMidtabright"><3级</span></td>
<td width="86">19</td>
<td width="49" class="last">
<a href="http://www.weather.com.cn/weather/101011400.shtml" target="_blank">详情</a></td>
</tr>
<tr>
<td width="83" height="23">
<a href="http://www.weather.com.cn/weather/101011500.shtml" target="_blank">平谷</a></td>
<td width="89">小雨</td>
<td width="162">
<span>东南风</span>
<span class="conMidtabright"><3级</span></td>
<td width="92">28</td>
<td width="98">多云</td>
<td width="177">
<span>北风</span>
<span class="conMidtabright"><3级</span></td>
<td width="86">16</td>
<td width="49" class="last">
<a href="http://www.weather.com.cn/weather/101011500.shtml" target="_blank">详情</a></td>
</tr>
<tr>
<td width="83" height="23">
<a href="http://www.weather.com.cn/weather/101011600.shtml" target="_blank">东城</a></td>
<td width="89">小雨</td>
<td width="162">
<span>南风</span>
<span class="conMidtabright"><3级</span></td>
<td width="92">29</td>
<td width="98">多云</td>
<td width="177">
<span>北风</span>
<span class="conMidtabright"><3级</span></td>
<td width="86">19</td>
<td width="49" class="last">
<a href="http://www.weather.com.cn/weather/101011600.shtml" target="_blank">详情</a></td>
</tr>
<tr>
<td width="83" height="23">
<a href="http://www.weather.com.cn/weather/101011700.shtml" target="_blank">西城</a></td>
<td width="89">小雨</td>
<td width="162">
<span>南风</span>
<span class="conMidtabright">3-4级</span></td>
<td width="92">29</td>
<td width="98">多云</td>
<td width="177">
<span>北风</span>
<span class="conMidtabright"><3级</span></td>
<td width="86">18</td>
<td width="49" class="last">
<a href="http://www.weather.com.cn/weather/101011700.shtml" target="_blank">详情</a></td>
</tr>
</table>
</div>
<div class="contentLtab">
<span style="margin-left:400px;">
<a href="#">返回顶部</a></span>
</div>
</div>
<div class="conMidtab" style="display:none;">
<div class="conMidtab5">
<table width="100%" border="0" cellpadding="0" cellspacing="0">
<tr>
<td width="74" rowspan="2">市</td>
<td width="83" rowspan="2">区/县</td>
<td height="37" colspan="3">周三(8月21日)白天</td>
<td colspan="3">周三(8月21日)夜间</td>
<td width="49" rowspan="2" class="last">&nbsp;</td>
</tr>
<tr>
<td width="89" height="23">天气现象</td>
<td width="162">风向风力</td>
<td width="92">最高气温</td>
<td width="98">天气现象</td>
<td width="177">风向风力</td>
<td width="86">最低气温</td>
</tr>
</table>
</div>
<div class="conMidtab3">
<a name="0" id="0"></a>
<table width="100%" border="0" cellpadding="0" cellspacing="0">
<tr>
<td width="74" rowspan="17" class="rowsPan">北京</td>
<td width="83" height="23">
<a href="http://www.weather.com.cn/weather/101010100.shtml" target="_blank">北京</a></td>
<td width="89">晴</td>
<td width="162">
<span>北风</span>
<span class="conMidtabright">3-4级</span></td>
<td width="92">31</td>
<td width="98">晴</td>
<td width="177">
<span>北风</span>
<span class="conMidtabright"><3级</span></td>
<td width="86">20</td>
<td width="49" class="last">
<a href="http://www.weather.com.cn/weather/101010100.shtml" target="_blank">详情</a></td>
</tr>
<tr>
<td width="83" height="23">
<a href="http://www.weather.com.cn/weather/101010200.shtml" target="_blank">海淀</a></td>
<td width="89">晴</td>
<td width="162">
<span>北风</span>
<span class="conMidtabright">3-4级</span></td>
<td width="92">32</td>
<td width="98">晴</td>
<td width="177">
<span>北风</span>
<span class="conMidtabright"><3级</span></td>
<td width="86">18</td>
<td width="49" class="last">
<a href="http://www.weather.com.cn/weather/101010200.shtml" target="_blank">详情</a></td>
</tr>
<tr>
<td width="83" height="23">
<a href="http://www.weather.com.cn/weather/101010300.shtml" target="_blank">朝阳</a></td>
<td width="89">晴</td>
<td width="162">
<span>北风</span>
<span class="conMidtabright"><3级</span></td>
<td width="92">31</td>
<td width="98">晴</td>
<td width="177">
<span>北风</span>
<span class="conMidtabright"><3级</span></td>
<td width="86">20</td>
<td width="49" class="last">
<a href="http://www.weather.com.cn/weather/101010300.shtml" target="_blank">详情</a></td>
</tr>
<tr>
<td width="83" height="23">
<a href="http://www.weather.com.cn/weather/101010400.shtml" target="_blank">顺义</a></td>
<td width="89">晴</td>
<td width="162">
<span>北风</span>
<span class="conMidtabright"><3级</span></td>
<td width="92">32</td>
<td width="98">晴</td>
<td width="177">
<span>北风</span>
<span class="conMidtabright"><3级</span></td>
<td width="86">19</td>
<td width="49" class="last">
<a href="http://www.weather.com.cn/weather/101010400.shtml" target="_blank">详情</a></td>
</tr>
<tr>
<td width="83" height="23">
<a href="http://www.weather.com.cn/weather/101010500.shtml" target="_blank">怀柔</a></td>
<td width="89">晴</td>
<td width="162">
<span>东南风</span>
<span class="conMidtabright"><3级</span></td>
<td width="92">32</td>
<td width="98">晴</td>
<td width="177">
<span>北风</span>
<span class="conMidtabright"><3级</span></td>
<td width="86">18</td>
<td width="49" class="last">
<a href="http://www.weather.com.cn/weather/101010500.shtml" target="_blank">详情</a></td>
</tr>
<tr>
<td width="83" height="23">
<a href="http://www.weather.com.cn/weather/101010600.shtml" target="_blank">通州</a></td>
<td width="89">晴</td>
<td width="162">
<span>北风</span>
<span class="conMidtabright"><3级</span></td>
<td width="92">30</td>
<td width="98">晴</td>
<td width="177">
<span>北风</span>
<span class="conMidtabright"><3级</span></td>
<td width="86">19</td>
<td width="49" class="last">
<a href="http://www.weather.com.cn/weather/101010600.shtml" target="_blank">详情</a></td>
</tr>
<tr>
<td width="83" height="23">
<a href="http://www.weather.com.cn/weather/101010700.shtml" target="_blank">昌平</a></td>
<td width="89">晴</td>
<td width="162">
<span>西北风</span>
<span class="conMidtabright"><3级</span></td>
<td width="92">32</td>
<td width="98">晴</td>
<td width="177">
<span>西北风</span>
<span class="conMidtabright"><3级</span></td>
<td width="86">20</td>
<td width="49" class="last">
<a href="http://www.weather.com.cn/weather/101010700.shtml" target="_blank">详情</a></td>
</tr>
<tr>
<td width="83" height="23">
<a href="http://www.weather.com.cn/weather/101010800.shtml" target="_blank">延庆</a></td>
<td width="89">晴</td>
<td width="162">
<span>西风</span>
<span class="conMidtabright"><3级</span></td>
<td width="92">29</td>
<td width="98">晴</td>
<td width="177">
<span>西北风</span>
<span class="conMidtabright"><3级</span></td>
<td width="86">15</td>
<td width="49" class="last">
<a href="http://www.weather.com.cn/weather/101010800.shtml" target="_blank">详情</a></td>
</tr>
<tr>
<td width="83" height="23">
<a href="http://www.weather.com.cn/weather/101010900.shtml" target="_blank">丰台</a></td>
<td width="89">晴</td>
<td width="162">
<span>北风</span>
<span class="conMidtabright">3-4级</span></td>
<td width="92">32</td>
<td width="98">晴</td>
<td width="177">
<span>北风</span>
<span class="conMidtabright"><3级</span></td>
<td width="86">20</td>
<td width="49" class="last">
<a href="http://www.weather.com.cn/weather/101010900.shtml" target="_blank">详情</a></td>
</tr>
<tr>
<td width="83" height="23">
<a href="http://www.weather.com.cn/weather/101011000.shtml" target="_blank">石景山</a></td>
<td width="89">晴</td>
<td width="162">
<span>北风</span>
<span class="conMidtabright"><3级</span></td>
<td width="92">32</td>
<td width="98">晴</td>
<td width="177">
<span>西北风</span>
<span class="conMidtabright"><3级</span></td>
<td width="86">18</td>
<td width="49" class="last">
<a href="http://www.weather.com.cn/weather/101011000.shtml" target="_blank">详情</a></td>
</tr>
<tr>
<td width="83" height="23">
<a href="http://www.weather.com.cn/weather/101011100.shtml" target="_blank">大兴</a></td>
<td width="89">晴</td>
<td width="162">
<span>北风</span>
<span class="conMidtabright">3-4级</span></td>
<td width="92">31</td>
<td width="98">晴</td>
<td width="177">
<span>北风</span>
<span class="conMidtabright"><3级</span></td>
<td width="86">19</td>
<td width="49" class="last">
<a href="http://www.weather.com.cn/weather/101011100.shtml" target="_blank">详情</a></td>
</tr>
<tr>
<td width="83" height="23">
<a href="http://www.weather.com.cn/weather/101011200.shtml" target="_blank">房山</a></td>
<td width="89">晴</td>
<td width="162">
<span>北风</span>
<span class="conMidtabright"><3级</span></td>
<td width="92">32</td>
<td width="98">晴</td>
<td width="177">
<span>西南风</span>
<span class="conMidtabright"><3级</span></td>
<td width="86">20</td>
<td width="49" class="last">
<a href="http://www.weather.com.cn/weather/101011200.shtml" target="_blank">详情</a></td>
</tr>
<tr>
<td width="83" height="23">
<a href="http://www.weather.com.cn/weather/101011300.shtml" target="_blank">密云</a></td>
<td width="89">晴</td>
<td width="162">
<span>北风</span>
<span class="conMidtabright"><3级</span></td>
<td width="92">31</td>
<td width="98">晴</td>
<td width="177">
<span>东北风</span>
<span class="conMidtabright"><3级</span></td>
<td width="86">16</td>
<td width="49" class="last">
<a href="http://www.weather.com.cn/weather/101011300.shtml" target="_blank">详情</a></td>
</tr>
<tr>
<td width="83" height="23">
<a href="http://www.weather.com.cn/weather/101011400.shtml" target="_blank">门头沟</a></td>
<td width="89">晴</td>
<td width="162">
<span>北风</span>
<span class="conMidtabright"><3级</span></td>
<td width="92">32</td>
<td width="98">晴</td>
<td width="177">
<span>西北风</span>
<span class="conMidtabright"><3级</span></td>
<td width="86">20</td>
<td width="49" class="last">
<a href="http://www.weather.com.cn/weather/101011400.shtml" target="_blank">详情</a></td>
</tr>
<tr>
<td width="83" height="23">
<a href="http://www.weather.com.cn/weather/101011500.shtml" target="_blank">平谷</a></td>
<td width="89">晴</td>
<td width="162">
<span>西北风</span>
<span class="conMidtabright"><3级</span></td>
<td width="92">30</td>
<td width="98">晴</td>
<td width="177">
<span>北风</span>
<span class="conMidtabright"><3级</span></td>
<td width="86">16</td>
<td width="49" class="last">
<a href="http://www.weather.com.cn/weather/101011500.shtml" target="_blank">详情</a></td>
</tr>
<tr>
<td width="83" height="23">
<a href="http://www.weather.com.cn/weather/101011600.shtml" target="_blank">东城</a></td>
<td width="89">晴</td>
<td width="162">
<span>北风</span>
<span class="conMidtabright"><3级</span></td>
<td width="92">31</td>
<td width="98">晴</td>
<td width="177">
<span>北风</span>
<span class="conMidtabright"><3级</span></td>
<td width="86">20</td>
<td width="49" class="last">
<a href="http://www.weather.com.cn/weather/101011600.shtml" target="_blank">详情</a></td>
</tr>
<tr>
<td width="83" height="23">
<a href="http://www.weather.com.cn/weather/101011700.shtml" target="_blank">西城</a></td>
<td width="89">晴</td>
<td width="162">
<span>北风</span>
<span class="conMidtabright">3-4级</span></td>
<td width="92">32</td>
<td width="98">晴</td>
<td width="177">
<span>北风</span>
<span class="conMidtabright"><3级</span></td>
<td width="86">18</td>
<td width="49" class="last">
<a href="http://www.weather.com.cn/weather/101011700.shtml" target="_blank">详情</a></td>
</tr>
</table>
</div>
<div class="contentLtab">
<span style="margin-left:400px;">
<a href="#">返回顶部</a></span>
</div>
</div>
<div class="conMidtab" style="display:none;">
<div class="conMidtab5">
<table width="100%" border="0" cellpadding="0" cellspacing="0">
<tr>
<td width="74" rowspan="2">市</td>
<td width="83" rowspan="2">区/县</td>
<td height="37" colspan="3">周四(8月22日)白天</td>
<td colspan="3">周四(8月22日)夜间</td>
<td width="49" rowspan="2" class="last">&nbsp;</td>
</tr>
<tr>
<td width="89" height="23">天气现象</td>
<td width="162">风向风力</td>
<td width="92">最高气温</td>
<td width="98">天气现象</td>
<td width="177">风向风力</td>
<td width="86">最低气温</td>
</tr>
</table>
</div>
<div class="conMidtab3">
<a name="0" id="0"></a>
<table width="100%" border="0" cellpadding="0" cellspacing="0">
<tr>
<td width="74" rowspan="17" class="rowsPan">北京</td>
<td width="83" height="23">
<a href="http://www.weather.com.cn/weather/101010100.shtml" target="_blank">北京</a></td>
<td width="89">晴</td>
<td width="162">
<span>西南风</span>
<span class="conMidtabright"><3级</span></td>
<td width="92">31</td>
<td width="98">晴</td>
<td width="177">
<span>北风</span>
<span class="conMidtabright"><3级</span></td>
<td width="86">21</td>
<td width="49" class="last">
<a href="http://www.weather.com.cn/weather/101010100.shtml" target="_blank">详情</a></td>
</tr>
<tr>
<td width="83" height="23">
<a href="http://www.weather.com.cn/weather/101010200.shtml" target="_blank">海淀</a></td>
<td width="89">晴</td>
<td width="162">
<span>北风</span>
<span class="conMidtabright"><3级</span></td>
<td width="92">32</td>
<td width="98">晴</td>
<td width="177">
<span>西风</span>
<span class="conMidtabright"><3级</span></td>
<td width="86">20</td>
<td width="49" class="last">
<a href="http://www.weather.com.cn/weather/101010200.shtml" target="_blank">详情</a></td>
</tr>
<tr>
<td width="83" height="23">
<a href="http://www.weather.com.cn/weather/101010300.shtml" target="_blank">朝阳</a></td>
<td width="89">晴</td>
<td width="162">
<span>西南风</span>
<span class="conMidtabright"><3级</span></td>
<td width="92">31</td>
<td width="98">晴</td>
<td width="177">
<span>西南风</span>
<span class="conMidtabright"><3级</span></td>
<td width="86">21</td>
<td width="49" class="last">
<a href="http://www.weather.com.cn/weather/101010300.shtml" target="_blank">详情</a></td>
</tr>
<tr>
<td width="83" height="23">
<a href="http://www.weather.com.cn/weather/101010400.shtml" target="_blank">顺义</a></td>
<td width="89">晴</td>
<td width="162">
<span>北风</span>
<span class="conMidtabright"><3级</span></td>
<td width="92">32</td>
<td width="98">晴</td>
<td width="177">
<span>北风</span>
<span class="conMidtabright"><3级</span></td>
<td width="86">20</td>
<td width="49" class="last">
<a href="http://www.weather.com.cn/weather/101010400.shtml" target="_blank">详情</a></td>
</tr>
<tr>
<td width="83" height="23">
<a href="http://www.weather.com.cn/weather/101010500.shtml" target="_blank">怀柔</a></td>
<td width="89">晴</td>
<td width="162">
<span>东南风</span>
<span class="conMidtabright"><3级</span></td>
<td width="92">31</td>
<td width="98">晴</td>
<td width="177">
<span>北风</span>
<span class="conMidtabright"><3级</span></td>
<td width="86">19</td>
<td width="49" class="last">
<a href="http://www.weather.com.cn/weather/101010500.shtml" target="_blank">详情</a></td>
</tr>
<tr>
<td width="83" height="23">
<a href="http://www.weather.com.cn/weather/101010600.shtml" target="_blank">通州</a></td>
<td width="89">晴</td>
<td width="162">
<span>北风</span>
<span class="conMidtabright"><3级</span></td>
<td width="92">31</td>
<td width="98">晴</td>
<td width="177">
<span>北风</span>
<span class="conMidtabright"><3级</span></td>
<td width="86">20</td>
<td width="49" class="last">
<a href="http://www.weather.com.cn/weather/101010600.shtml" target="_blank">详情</a></td>
</tr>
<tr>
<td width="83" height="23">
<a href="http://www.weather.com.cn/weather/101010700.shtml" target="_blank">昌平</a></td>
<td width="89">晴</td>
<td width="162">
<span>西北风</span>
<span class="conMidtabright"><3级</span></td>
<td width="92">32</td>
<td width="98">晴</td>
<td width="177">
<span>西北风</span>
<span class="conMidtabright"><3级</span></td>
<td width="86">21</td>
<td width="49" class="last">
<a href="http://www.weather.com.cn/weather/101010700.shtml" target="_blank">详情</a></td>
</tr>
<tr>
<td width="83" height="23">
<a href="http://www.weather.com.cn/weather/101010800.shtml" target="_blank">延庆</a></td>
<td width="89">晴</td>
<td width="162">
<span>西南风</span>
<span class="conMidtabright"><3级</span></td>
<td width="92">28</td>
<td width="98">晴</td>
<td width="177">
<span>西北风</span>
<span class="conMidtabright"><3级</span></td>
<td width="86">17</td>
<td width="49" class="last">
<a href="http://www.weather.com.cn/weather/101010800.shtml" target="_blank">详情</a></td>
</tr>
<tr>
<td width="83" height="23">
<a href="http://www.weather.com.cn/weather/101010900.shtml" target="_blank">丰台</a></td>
<td width="89">晴</td>
<td width="162">
<span>西南风</span>
<span class="conMidtabright"><3级</span></td>
<td width="92">32</td>
<td width="98">晴</td>
<td width="177">
<span>北风</span>
<span class="conMidtabright"><3级</span></td>
<td width="86">21</td>
<td width="49" class="last">
<a href="http://www.weather.com.cn/weather/101010900.shtml" target="_blank">详情</a></td>
</tr>
<tr>
<td width="83" height="23">
<a href="http://www.weather.com.cn/weather/101011000.shtml" target="_blank">石景山</a></td>
<td width="89">晴</td>
<td width="162">
<span>北风</span>
<span class="conMidtabright"><3级</span></td>
<td width="92">32</td>
<td width="98">晴</td>
<td width="177">
<span>北风</span>
<span class="conMidtabright"><3级</span></td>
<td width="86">20</td>
<td width="49" class="last">
<a href="http://www.weather.com.cn/weather/101011000.shtml" target="_blank">详情</a></td>
</tr>
<tr>
<td width="83" height="23">
<a href="http://www.weather.com.cn/weather/101011100.shtml" target="_blank">大兴</a></td>
<td width="89">晴</td>
<td width="162">
<span>西风</span>
<span class="conMidtabright"><3级</span></td>
<td width="92">32</td>
<td width="98">晴</td>
<td width="177">
<span>东北风</span>
<span class="conMidtabright"><3级</span></td>
<td width="86">20</td>
<td width="49" class="last">
<a href="http://www.weather.com.cn/weather/101011100.shtml" target="_blank">详情</a></td>
</tr>
<tr>
<td width="83" height="23">
<a href="http://www.weather.com.cn/weather/101011200.shtml" target="_blank">房山</a></td>
<td width="89">晴</td>
<td width="162">
<span>西南风</span>
<span class="conMidtabright"><3级</span></td>
<td width="92">32</td>
<td width="98">晴</td>
<td width="177">
<span>东北风</span>
<span class="conMidtabright"><3级</span></td>
<td width="86">21</td>
<td width="49" class="last">
<a href="http://www.weather.com.cn/weather/101011200.shtml" target="_blank">详情</a></td>
</tr>
<tr>
<td width="83" height="23">
<a href="http://www.weather.com.cn/weather/101011300.shtml" target="_blank">密云</a></td>
<td width="89">晴</td>
<td width="162">
<span>东北风</span>
<span class="conMidtabright"><3级</span></td>
<td width="92">31</td>
<td width="98">晴</td>
<td width="177">
<span>东北风</span>
<span class="conMidtabright"><3级</span></td>
<td width="86">19</td>
<td width="49" class="last">
<a href="http://www.weather.com.cn/weather/101011300.shtml" target="_blank">详情</a></td>
</tr>
<tr>
<td width="83" height="23">
<a href="http://www.weather.com.cn/weather/101011400.shtml" target="_blank">门头沟</a></td>
<td width="89">晴</td>
<td width="162">
<span>西风</span>
<span class="conMidtabright"><3级</span></td>
<td width="92">32</td>
<td width="98">晴</td>
<td width="177">
<span>北风</span>
<span class="conMidtabright"><3级</span></td>
<td width="86">22</td>
<td width="49" class="last">
<a href="http://www.weather.com.cn/weather/101011400.shtml" target="_blank">详情</a></td>
</tr>
<tr>
<td width="83" height="23">
<a href="http://www.weather.com.cn/weather/101011500.shtml" target="_blank">平谷</a></td>
<td width="89">晴</td>
<td width="162">
<span>北风</span>
<span class="conMidtabright"><3级</span></td>
<td width="92">31</td>
<td width="98">晴</td>
<td width="177">
<span>北风</span>
<span class="conMidtabright"><3级</span></td>
<td width="86">18</td>
<td width="49" class="last">
<a href="http://www.weather.com.cn/weather/101011500.shtml" target="_blank">详情</a></td>
</tr>
<tr>
<td width="83" height="23">
<a href="http://www.weather.com.cn/weather/101011600.shtml" target="_blank">东城</a></td>
<td width="89">晴</td>
<td width="162">
<span>西南风</span>
<span class="conMidtabright"><3级</span></td>
<td width="92">31</td>
<td width="98">晴</td>
<td width="177">
<span>西南风</span>
<span class="conMidtabright"><3级</span></td>
<td width="86">21</td>
<td width="49" class="last">
<a href="http://www.weather.com.cn/weather/101011600.shtml" target="_blank">详情</a></td>
</tr>
<tr>
<td width="83" height="23">
<a href="http://www.weather.com.cn/weather/101011700.shtml" target="_blank">西城</a></td>
<td width="89">晴</td>
<td width="162">
<span>北风</span>
<span class="conMidtabright"><3级</span></td>
<td width="92">32</td>
<td width="98">晴</td>
<td width="177">
<span>西风</span>
<span class="conMidtabright"><3级</span></td>
<td width="86">20</td>
<td width="49" class="last">
<a href="http://www.weather.com.cn/weather/101011700.shtml" target="_blank">详情</a></td>
</tr>
</table>
</div>
<div class="contentLtab">
<span style="margin-left:400px;">
<a href="#">返回顶部</a></span>
</div>
</div>
<div class="conMidtab" style="display:none;">
<div class="conMidtab5">
<table width="100%" border="0" cellpadding="0" cellspacing="0">
<tr>
<td width="74" rowspan="2">市</td>
<td width="83" rowspan="2">区/县</td>
<td height="37" colspan="3">周五(8月23日)白天</td>
<td colspan="3">周五(8月23日)夜间</td>
<td width="49" rowspan="2" class="last">&nbsp;</td>
</tr>
<tr>
<td width="89" height="23">天气现象</td>
<td width="162">风向风力</td>
<td width="92">最高气温</td>
<td width="98">天气现象</td>
<td width="177">风向风力</td>
<td width="86">最低气温</td>
</tr>
</table>
</div>
<div class="conMidtab3">
<a name="0" id="0"></a>
<table width="100%" border="0" cellpadding="0" cellspacing="0">
<tr>
<td width="74" rowspan="17" class="rowsPan">北京</td>
<td width="83" height="23">
<a href="http://www.weather.com.cn/weather/101010100.shtml" target="_blank">北京</a></td>
<td width="89">多云</td>
<td width="162">
<span>西南风</span>
<span class="conMidtabright"><3级</span></td>
<td width="92">27</td>
<td width="98">多云</td>
<td width="177">
<span>西南风</span>
<span class="conMidtabright"><3级</span></td>
<td width="86">20</td>
<td width="49" class="last">
<a href="http://www.weather.com.cn/weather/101010100.shtml" target="_blank">详情</a></td>
</tr>
<tr>
<td width="83" height="23">
<a href="http://www.weather.com.cn/weather/101010200.shtml" target="_blank">海淀</a></td>
<td width="89">多云</td>
<td width="162">
<span>北风</span>
<span class="conMidtabright"><3级</span></td>
<td width="92">28</td>
<td width="98">多云</td>
<td width="177">
<span>西南风</span>
<span class="conMidtabright"><3级</span></td>
<td width="86">19</td>
<td width="49" class="last">
<a href="http://www.weather.com.cn/weather/101010200.shtml" target="_blank">详情</a></td>
</tr>
<tr>
<td width="83" height="23">
<a href="http://www.weather.com.cn/weather/101010300.shtml" target="_blank">朝阳</a></td>
<td width="89">多云</td>
<td width="162">
<span>西南风</span>
<span class="conMidtabright"><3级</span></td>
<td width="92">27</td>
<td width="98">多云</td>
<td width="177">
<span>西南风</span>
<span class="conMidtabright"><3级</span></td>
<td width="86">20</td>
<td width="49" class="last">
<a href="http://www.weather.com.cn/weather/101010300.shtml" target="_blank">详情</a></td>
</tr>
<tr>
<td width="83" height="23">
<a href="http://www.weather.com.cn/weather/101010400.shtml" target="_blank">顺义</a></td>
<td width="89">多云</td>
<td width="162">
<span>西南风</span>
<span class="conMidtabright"><3级</span></td>
<td width="92">27</td>
<td width="98">多云</td>
<td width="177">
<span>西南风</span>
<span class="conMidtabright"><3级</span></td>
<td width="86">20</td>
<td width="49" class="last">
<a href="http://www.weather.com.cn/weather/101010400.shtml" target="_blank">详情</a></td>
</tr>
<tr>
<td width="83" height="23">
<a href="http://www.weather.com.cn/weather/101010500.shtml" target="_blank">怀柔</a></td>
<td width="89">多云</td>
<td width="162">
<span>西风</span>
<span class="conMidtabright"><3级</span></td>
<td width="92">27</td>
<td width="98">多云</td>
<td width="177">
<span>北风</span>
<span class="conMidtabright"><3级</span></td>
<td width="86">19</td>
<td width="49" class="last">
<a href="http://www.weather.com.cn/weather/101010500.shtml" target="_blank">详情</a></td>
</tr>
<tr>
<td width="83" height="23">
<a href="http://www.weather.com.cn/weather/101010600.shtml" target="_blank">通州</a></td>
<td width="89">多云</td>
<td width="162">
<span>北风</span>
<span class="conMidtabright"><3级</span></td>
<td width="92">27</td>
<td width="98">多云</td>
<td width="177">
<span>西南风</span>
<span class="conMidtabright"><3级</span></td>
<td width="86">18</td>
<td width="49" class="last">
<a href="http://www.weather.com.cn/weather/101010600.shtml" target="_blank">详情</a></td>
</tr>
<tr>
<td width="83" height="23">
<a href="http://www.weather.com.cn/weather/101010700.shtml" target="_blank">昌平</a></td>
<td width="89">多云</td>
<td width="162">
<span>西北风</span>
<span class="conMidtabright"><3级</span></td>
<td width="92">28</td>
<td width="98">多云</td>
<td width="177">
<span>北风</span>
<span class="conMidtabright"><3级</span></td>
<td width="86">20</td>
<td width="49" class="last">
<a href="http://www.weather.com.cn/weather/101010700.shtml" target="_blank">详情</a></td>
</tr>
<tr>
<td width="83" height="23">
<a href="http://www.weather.com.cn/weather/101010800.shtml" target="_blank">延庆</a></td>
<td width="89">多云</td>
<td width="162">
<span>西南风</span>
<span class="conMidtabright"><3级</span></td>
<td width="92">25</td>
<td width="98">多云</td>
<td width="177">
<span>西北风</span>
<span class="conMidtabright"><3级</span></td>
<td width="86">16</td>
<td width="49" class="last">
<a href="http://www.weather.com.cn/weather/101010800.shtml" target="_blank">详情</a></td>
</tr>
<tr>
<td width="83" height="23">
<a href="http://www.weather.com.cn/weather/101010900.shtml" target="_blank">丰台</a></td>
<td width="89">多云</td>
<td width="162">
<span>东北风</span>
<span class="conMidtabright"><3级</span></td>
<td width="92">28</td>
<td width="98">多云</td>
<td width="177">
<span>西南风</span>
<span class="conMidtabright"><3级</span></td>
<td width="86">19</td>
<td width="49" class="last">
<a href="http://www.weather.com.cn/weather/101010900.shtml" target="_blank">详情</a></td>
</tr>
<tr>
<td width="83" height="23">
<a href="http://www.weather.com.cn/weather/101011000.shtml" target="_blank">石景山</a></td>
<td width="89">多云</td>
<td width="162">
<span>北风</span>
<span class="conMidtabright"><3级</span></td>
<td width="92">28</td>
<td width="98">多云</td>
<td width="177">
<span>北风</span>
<span class="conMidtabright"><3级</span></td>
<td width="86">20</td>
<td width="49" class="last">
<a href="http://www.weather.com.cn/weather/101011000.shtml" target="_blank">详情</a></td>
</tr>
<tr>
<td width="83" height="23">
<a href="http://www.weather.com.cn/weather/101011100.shtml" target="_blank">大兴</a></td>
<td width="89">多云</td>
<td width="162">
<span>西南风</span>
<span class="conMidtabright"><3级</span></td>
<td width="92">27</td>
<td width="98">多云</td>
<td width="177">
<span>西南风</span>
<span class="conMidtabright"><3级</span></td>
<td width="86">19</td>
<td width="49" class="last">
<a href="http://www.weather.com.cn/weather/101011100.shtml" target="_blank">详情</a></td>
</tr>
<tr>
<td width="83" height="23">
<a href="http://www.weather.com.cn/weather/101011200.shtml" target="_blank">房山</a></td>
<td width="89">多云</td>
<td width="162">
<span>东北风</span>
<span class="conMidtabright"><3级</span></td>
<td width="92">28</td>
<td width="98">多云</td>
<td width="177">
<span>西南风</span>
<span class="conMidtabright"><3级</span></td>
<td width="86">20</td>
<td width="49" class="last">
<a href="http://www.weather.com.cn/weather/101011200.shtml" target="_blank">详情</a></td>
</tr>
<tr>
<td width="83" height="23">
<a href="http://www.weather.com.cn/weather/101011300.shtml" target="_blank">密云</a></td>
<td width="89">多云</td>
<td width="162">
<span>东北风</span>
<span class="conMidtabright"><3级</span></td>
<td width="92">27</td>
<td width="98">多云</td>
<td width="177">
<span>东北风</span>
<span class="conMidtabright"><3级</span></td>
<td width="86">18</td>
<td width="49" class="last">
<a href="http://www.weather.com.cn/weather/101011300.shtml" target="_blank">详情</a></td>
</tr>
<tr>
<td width="83" height="23">
<a href="http://www.weather.com.cn/weather/101011400.shtml" target="_blank">门头沟</a></td>
<td width="89">多云</td>
<td width="162">
<span>北风</span>
<span class="conMidtabright"><3级</span></td>
<td width="92">28</td>
<td width="98">多云</td>
<td width="177">
<span>西风</span>
<span class="conMidtabright"><3级</span></td>
<td width="86">20</td>
<td width="49" class="last">
<a href="http://www.weather.com.cn/weather/101011400.shtml" target="_blank">详情</a></td>
</tr>
<tr>
<td width="83" height="23">
<a href="http://www.weather.com.cn/weather/101011500.shtml" target="_blank">平谷</a></td>
<td width="89">多云</td>
<td width="162">
<span>北风</span>
<span class="conMidtabright"><3级</span></td>
<td width="92">27</td>
<td width="98">多云</td>
<td width="177">
<span>北风</span>
<span class="conMidtabright"><3级</span></td>
<td width="86">19</td>
<td width="49" class="last">
<a href="http://www.weather.com.cn/weather/101011500.shtml" target="_blank">详情</a></td>
</tr>
<tr>
<td width="83" height="23">
<a href="http://www.weather.com.cn/weather/101011600.shtml" target="_blank">东城</a></td>
<td width="89">多云</td>
<td width="162">
<span>西南风</span>
<span class="conMidtabright"><3级</span></td>
<td width="92">27</td>
<td width="98">多云</td>
<td width="177">
<span>西南风</span>
<span class="conMidtabright"><3级</span></td>
<td width="86">20</td>
<td width="49" class="last">
<a href="http://www.weather.com.cn/weather/101011600.shtml" target="_blank">详情</a></td>
</tr>
<tr>
<td width="83" height="23">
<a href="http://www.weather.com.cn/weather/101011700.shtml" target="_blank">西城</a></td>
<td width="89">多云</td>
<td width="162">
<span>北风</span>
<span class="conMidtabright"><3级</span></td>
<td width="92">28</td>
<td width="98">多云</td>
<td width="177">
<span>西南风</span>
<span class="conMidtabright"><3级</span></td>
<td width="86">19</td>
<td width="49" class="last">
<a href="http://www.weather.com.cn/weather/101011700.shtml" target="_blank">详情</a></td>
</tr>
</table>
</div>
<div class="contentLtab">
<span style="margin-left:400px;">
<a href="#">返回顶部</a></span>
</div>
</div>
<div class="conMidtab" style="display:none;">
<div class="conMidtab5">
<table width="100%" border="0" cellpadding="0" cellspacing="0">
<tr>
<td width="74" rowspan="2">市</td>
<td width="83" rowspan="2">区/县</td>
<td height="37" colspan="3">周六(8月24日)白天</td>
<td colspan="3">周六(8月24日)夜间</td>
<td width="49" rowspan="2" class="last">&nbsp;</td>
</tr>
<tr>
<td width="89" height="23">天气现象</td>
<td width="162">风向风力</td>
<td width="92">最高气温</td>
<td width="98">天气现象</td>
<td width="177">风向风力</td>
<td width="86">最低气温</td>
</tr>
</table>
</div>
<div class="conMidtab3">
<a name="0" id="0"></a>
<table width="100%" border="0" cellpadding="0" cellspacing="0">
<tr>
<td width="74" rowspan="17" class="rowsPan">北京</td>
<td width="83" height="23">
<a href="http://www.weather.com.cn/weather/101010100.shtml" target="_blank">北京</a></td>
<td width="89">多云</td>
<td width="162">
<span>西南风</span>
<span class="conMidtabright"><3级</span></td>
<td width="92">29</td>
<td width="98">晴</td>
<td width="177">
<span>西南风</span>
<span class="conMidtabright"><3级</span></td>
<td width="86">19</td>
<td width="49" class="last">
<a href="http://www.weather.com.cn/weather/101010100.shtml" target="_blank">详情</a></td>
</tr>
<tr>
<td width="83" height="23">
<a href="http://www.weather.com.cn/weather/101010200.shtml" target="_blank">海淀</a></td>
<td width="89">多云</td>
<td width="162">
<span>西南风</span>
<span class="conMidtabright"><3级</span></td>
<td width="92">30</td>
<td width="98">晴</td>
<td width="177">
<span>西南风</span>
<span class="conMidtabright"><3级</span></td>
<td width="86">19</td>
<td width="49" class="last">
<a href="http://www.weather.com.cn/weather/101010200.shtml" target="_blank">详情</a></td>
</tr>
<tr>
<td width="83" height="23">
<a href="http://www.weather.com.cn/weather/101010300.shtml" target="_blank">朝阳</a></td>
<td width="89">多云</td>
<td width="162">
<span>南风</span>
<span class="conMidtabright"><3级</span></td>
<td width="92">29</td>
<td width="98">晴</td>
<td width="177">
<span>西风</span>
<span class="conMidtabright"><3级</span></td>
<td width="86">20</td>
<td width="49" class="last">
<a href="http://www.weather.com.cn/weather/101010300.shtml" target="_blank">详情</a></td>
</tr>
<tr>
<td width="83" height="23">
<a href="http://www.weather.com.cn/weather/101010400.shtml" target="_blank">顺义</a></td>
<td width="89">多云</td>
<td width="162">
<span>东南风</span>
<span class="conMidtabright"><3级</span></td>
<td width="92">29</td>
<td width="98">晴</td>
<td width="177">
<span>东南风</span>
<span class="conMidtabright"><3级</span></td>
<td width="86">19</td>
<td width="49" class="last">
<a href="http://www.weather.com.cn/weather/101010400.shtml" target="_blank">详情</a></td>
</tr>
<tr>
<td width="83" height="23">
<a href="http://www.weather.com.cn/weather/101010500.shtml" target="_blank">怀柔</a></td>
<td width="89">多云</td>
<td width="162">
<span>南风</span>
<span class="conMidtabright"><3级</span></td>
<td width="92">29</td>
<td width="98">晴</td>
<td width="177">
<span>东北风</span>
<span class="conMidtabright"><3级</span></td>
<td width="86">18</td>
<td width="49" class="last">
<a href="http://www.weather.com.cn/weather/101010500.shtml" target="_blank">详情</a></td>
</tr>
<tr>
<td width="83" height="23">
<a href="http://www.weather.com.cn/weather/101010600.shtml" target="_blank">通州</a></td>
<td width="89">多云</td>
<td width="162">
<span>南风</span>
<span class="conMidtabright"><3级</span></td>
<td width="92">29</td>
<td width="98">晴</td>
<td width="177">
<span>西风</span>
<span class="conMidtabright"><3级</span></td>
<td width="86">18</td>
<td width="49" class="last">
<a href="http://www.weather.com.cn/weather/101010600.shtml" target="_blank">详情</a></td>
</tr>
<tr>
<td width="83" height="23">
<a href="http://www.weather.com.cn/weather/101010700.shtml" target="_blank">昌平</a></td>
<td width="89">多云</td>
<td width="162">
<span>东南风</span>
<span class="conMidtabright"><3级</span></td>
<td width="92">29</td>
<td width="98">晴</td>
<td width="177">
<span>北风</span>
<span class="conMidtabright"><3级</span></td>
<td width="86">19</td>
<td width="49" class="last">
<a href="http://www.weather.com.cn/weather/101010700.shtml" target="_blank">详情</a></td>
</tr>
<tr>
<td width="83" height="23">
<a href="http://www.weather.com.cn/weather/101010800.shtml" target="_blank">延庆</a></td>
<td width="89">多云</td>
<td width="162">
<span>东南风</span>
<span class="conMidtabright"><3级</span></td>
<td width="92">26</td>
<td width="98">晴</td>
<td width="177">
<span>北风</span>
<span class="conMidtabright"><3级</span></td>
<td width="86">16</td>
<td width="49" class="last">
<a href="http://www.weather.com.cn/weather/101010800.shtml" target="_blank">详情</a></td>
</tr>
<tr>
<td width="83" height="23">
<a href="http://www.weather.com.cn/weather/101010900.shtml" target="_blank">丰台</a></td>
<td width="89">多云</td>
<td width="162">
<span>西南风</span>
<span class="conMidtabright"><3级</span></td>
<td width="92">30</td>
<td width="98">晴</td>
<td width="177">
<span>西南风</span>
<span class="conMidtabright"><3级</span></td>
<td width="86">19</td>
<td width="49" class="last">
<a href="http://www.weather.com.cn/weather/101010900.shtml" target="_blank">详情</a></td>
</tr>
<tr>
<td width="83" height="23">
<a href="http://www.weather.com.cn/weather/101011000.shtml" target="_blank">石景山</a></td>
<td width="89">多云</td>
<td width="162">
<span>西南风</span>
<span class="conMidtabright"><3级</span></td>
<td width="92">30</td>
<td width="98">晴</td>
<td width="177">
<span>西南风</span>
<span class="conMidtabright"><3级</span></td>
<td width="86">19</td>
<td width="49" class="last">
<a href="http://www.weather.com.cn/weather/101011000.shtml" target="_blank">详情</a></td>
</tr>
<tr>
<td width="83" height="23">
<a href="http://www.weather.com.cn/weather/101011100.shtml" target="_blank">大兴</a></td>
<td width="89">多云</td>
<td width="162">
<span>西南风</span>
<span class="conMidtabright"><3级</span></td>
<td width="92">29</td>
<td width="98">晴</td>
<td width="177">
<span>西南风</span>
<span class="conMidtabright"><3级</span></td>
<td width="86">18</td>
<td width="49" class="last">
<a href="http://www.weather.com.cn/weather/101011100.shtml" target="_blank">详情</a></td>
</tr>
<tr>
<td width="83" height="23">
<a href="http://www.weather.com.cn/weather/101011200.shtml" target="_blank">房山</a></td>
<td width="89">多云</td>
<td width="162">
<span>西南风</span>
<span class="conMidtabright"><3级</span></td>
<td width="92">30</td>
<td width="98">晴</td>
<td width="177">
<span>西南风</span>
<span class="conMidtabright"><3级</span></td>
<td width="86">19</td>
<td width="49" class="last">
<a href="http://www.weather.com.cn/weather/101011200.shtml" target="_blank">详情</a></td>
</tr>
<tr>
<td width="83" height="23">
<a href="http://www.weather.com.cn/weather/101011300.shtml" target="_blank">密云</a></td>
<td width="89">多云</td>
<td width="162">
<span>西南风</span>
<span class="conMidtabright"><3级</span></td>
<td width="92">28</td>
<td width="98">晴</td>
<td width="177">
<span>东风</span>
<span class="conMidtabright"><3级</span></td>
<td width="86">17</td>
<td width="49" class="last">
<a href="http://www.weather.com.cn/weather/101011300.shtml" target="_blank">详情</a></td>
</tr>
<tr>
<td width="83" height="23">
<a href="http://www.weather.com.cn/weather/101011400.shtml" target="_blank">门头沟</a></td>
<td width="89">多云</td>
<td width="162">
<span>西南风</span>
<span class="conMidtabright"><3级</span></td>
<td width="92">29</td>
<td width="98">晴</td>
<td width="177">
<span>西南风</span>
<span class="conMidtabright"><3级</span></td>
<td width="86">19</td>
<td width="49" class="last">
<a href="http://www.weather.com.cn/weather/101011400.shtml" target="_blank">详情</a></td>
</tr>
<tr>
<td width="83" height="23">
<a href="http://www.weather.com.cn/weather/101011500.shtml" target="_blank">平谷</a></td>
<td width="89">多云</td>
<td width="162">
<span>东风</span>
<span class="conMidtabright"><3级</span></td>
<td width="92">29</td>
<td width="98">晴</td>
<td width="177">
<span>东风</span>
<span class="conMidtabright"><3级</span></td>
<td width="86">17</td>
<td width="49" class="last">
<a href="http://www.weather.com.cn/weather/101011500.shtml" target="_blank">详情</a></td>
</tr>
<tr>
<td width="83" height="23">
<a href="http://www.weather.com.cn/weather/101011600.shtml" target="_blank">东城</a></td>
<td width="89">多云</td>
<td width="162">
<span>南风</span>
<span class="conMidtabright"><3级</span></td>
<td width="92">29</td>
<td width="98">晴</td>
<td width="177">
<span>西风</span>
<span class="conMidtabright"><3级</span></td>
<td width="86">20</td>
<td width="49" class="last">
<a href="http://www.weather.com.cn/weather/101011600.shtml" target="_blank">详情</a></td>
</tr>
<tr>
<td width="83" height="23">
<a href="http://www.weather.com.cn/weather/101011700.shtml" target="_blank">西城</a></td>
<td width="89">多云</td>
<td width="162">
<span>西南风</span>
<span class="conMidtabright"><3级</span></td>
<td width="92">30</td>
<td width="98">晴</td>
<td width="177">
<span>西南风</span>
<span class="conMidtabright"><3级</span></td>
<td width="86">19</td>
<td width="49" class="last">
<a href="http://www.weather.com.cn/weather/101011700.shtml" target="_blank">详情</a></td>
</tr>
</table>
</div>
<div class="contentLtab">
<span style="margin-left:400px;">
<a href="#">返回顶部</a></span>
</div>
</div>
<div class="conMidtab" style="display:none;">
<div class="conMidtab5">
<table width="100%" border="0" cellpadding="0" cellspacing="0">
<tr>
<td width="74" rowspan="2">市</td>
<td width="83" rowspan="2">区/县</td>
<td height="37" colspan="3">周日(8月25日)白天</td>
<td colspan="3">周日(8月25日)夜间</td>
<td width="49" rowspan="2" class="last">&nbsp;</td>
</tr>
<tr>
<td width="89" height="23">天气现象</td>
<td width="162">风向风力</td>
<td width="92">最高气温</td>
<td width="98">天气现象</td>
<td width="177">风向风力</td>
<td width="86">最低气温</td>
</tr>
</table>
</div>
<div class="conMidtab3">
<a name="0" id="0"></a>
<table width="100%" border="0" cellpadding="0" cellspacing="0">
<tr>
<td width="74" rowspan="17" class="rowsPan">北京</td>
<td width="83" height="23">
<a href="http://www.weather.com.cn/weather/101010100.shtml" target="_blank">北京</a></td>
<td width="89">晴</td>
<td width="162">
<span>南风</span>
<span class="conMidtabright"><3级</span></td>
<td width="92">30</td>
<td width="98">多云</td>
<td width="177">
<span>南风</span>
<span class="conMidtabright"><3级</span></td>
<td width="86">21</td>
<td width="49" class="last">
<a href="http://www.weather.com.cn/weather/101010100.shtml" target="_blank">详情</a></td>
</tr>
<tr>
<td width="83" height="23">
<a href="http://www.weather.com.cn/weather/101010200.shtml" target="_blank">海淀</a></td>
<td width="89">晴</td>
<td width="162">
<span>南风</span>
<span class="conMidtabright"><3级</span></td>
<td width="92">31</td>
<td width="98">多云</td>
<td width="177">
<span>南风</span>
<span class="conMidtabright"><3级</span></td>
<td width="86">20</td>
<td width="49" class="last">
<a href="http://www.weather.com.cn/weather/101010200.shtml" target="_blank">详情</a></td>
</tr>
<tr>
<td width="83" height="23">
<a href="http://www.weather.com.cn/weather/101010300.shtml" target="_blank">朝阳</a></td>
<td width="89">晴</td>
<td width="162">
<span>南风</span>
<span class="conMidtabright"><3级</span></td>
<td width="92">31</td>
<td width="98">多云</td>
<td width="177">
<span>南风</span>
<span class="conMidtabright"><3级</span></td>
<td width="86">21</td>
<td width="49" class="last">
<a href="http://www.weather.com.cn/weather/101010300.shtml" target="_blank">详情</a></td>
</tr>
<tr>
<td width="83" height="23">
<a href="http://www.weather.com.cn/weather/101010400.shtml" target="_blank">顺义</a></td>
<td width="89">晴</td>
<td width="162">
<span>南风</span>
<span class="conMidtabright"><3级</span></td>
<td width="92">31</td>
<td width="98">多云</td>
<td width="177">
<span>南风</span>
<span class="conMidtabright"><3级</span></td>
<td width="86">21</td>
<td width="49" class="last">
<a href="http://www.weather.com.cn/weather/101010400.shtml" target="_blank">详情</a></td>
</tr>
<tr>
<td width="83" height="23">
<a href="http://www.weather.com.cn/weather/101010500.shtml" target="_blank">怀柔</a></td>
<td width="89">晴</td>
<td width="162">
<span>南风</span>
<span class="conMidtabright"><3级</span></td>
<td width="92">30</td>
<td width="98">多云</td>
<td width="177">
<span>南风</span>
<span class="conMidtabright"><3级</span></td>
<td width="86">19</td>
<td width="49" class="last">
<a href="http://www.weather.com.cn/weather/101010500.shtml" target="_blank">详情</a></td>
</tr>
<tr>
<td width="83" height="23">
<a href="http://www.weather.com.cn/weather/101010600.shtml" target="_blank">通州</a></td>
<td width="89">晴</td>
<td width="162">
<span>南风</span>
<span class="conMidtabright"><3级</span></td>
<td width="92">30</td>
<td width="98">多云</td>
<td width="177">
<span>南风</span>
<span class="conMidtabright"><3级</span></td>
<td width="86">20</td>
<td width="49" class="last">
<a href="http://www.weather.com.cn/weather/101010600.shtml" target="_blank">详情</a></td>
</tr>
<tr>
<td width="83" height="23">
<a href="http://www.weather.com.cn/weather/101010700.shtml" target="_blank">昌平</a></td>
<td width="89">晴</td>
<td width="162">
<span>东南风</span>
<span class="conMidtabright"><3级</span></td>
<td width="92">30</td>
<td width="98">多云</td>
<td width="177">
<span>东南风</span>
<span class="conMidtabright"><3级</span></td>
<td width="86">20</td>
<td width="49" class="last">
<a href="http://www.weather.com.cn/weather/101010700.shtml" target="_blank">详情</a></td>
</tr>
<tr>
<td width="83" height="23">
<a href="http://www.weather.com.cn/weather/101010800.shtml" target="_blank">延庆</a></td>
<td width="89">晴</td>
<td width="162">
<span>东南风</span>
<span class="conMidtabright"><3级</span></td>
<td width="92">27</td>
<td width="98">多云</td>
<td width="177">
<span>东北风</span>
<span class="conMidtabright"><3级</span></td>
<td width="86">17</td>
<td width="49" class="last">
<a href="http://www.weather.com.cn/weather/101010800.shtml" target="_blank">详情</a></td>
</tr>
<tr>
<td width="83" height="23">
<a href="http://www.weather.com.cn/weather/101010900.shtml" target="_blank">丰台</a></td>
<td width="89">晴</td>
<td width="162">
<span>南风</span>
<span class="conMidtabright"><3级</span></td>
<td width="92">31</td>
<td width="98">多云</td>
<td width="177">
<span>南风</span>
<span class="conMidtabright"><3级</span></td>
<td width="86">20</td>
<td width="49" class="last">
<a href="http://www.weather.com.cn/weather/101010900.shtml" target="_blank">详情</a></td>
</tr>
<tr>
<td width="83" height="23">
<a href="http://www.weather.com.cn/weather/101011000.shtml" target="_blank">石景山</a></td>
<td width="89">晴</td>
<td width="162">
<span>南风</span>
<span class="conMidtabright"><3级</span></td>
<td width="92">31</td>
<td width="98">多云</td>
<td width="177">
<span>南风</span>
<span class="conMidtabright"><3级</span></td>
<td width="86">20</td>
<td width="49" class="last">
<a href="http://www.weather.com.cn/weather/101011000.shtml" target="_blank">详情</a></td>
</tr>
<tr>
<td width="83" height="23">
<a href="http://www.weather.com.cn/weather/101011100.shtml" target="_blank">大兴</a></td>
<td width="89">晴</td>
<td width="162">
<span>南风</span>
<span class="conMidtabright"><3级</span></td>
<td width="92">31</td>
<td width="98">多云</td>
<td width="177">
<span>南风</span>
<span class="conMidtabright"><3级</span></td>
<td width="86">20</td>
<td width="49" class="last">
<a href="http://www.weather.com.cn/weather/101011100.shtml" target="_blank">详情</a></td>
</tr>
<tr>
<td width="83" height="23">
<a href="http://www.weather.com.cn/weather/101011200.shtml" target="_blank">房山</a></td>
<td width="89">晴</td>
<td width="162">
<span>西南风</span>
<span class="conMidtabright"><3级</span></td>
<td width="92">31</td>
<td width="98">多云</td>
<td width="177">
<span>南风</span>
<span class="conMidtabright"><3级</span></td>
<td width="86">20</td>
<td width="49" class="last">
<a href="http://www.weather.com.cn/weather/101011200.shtml" target="_blank">详情</a></td>
</tr>
<tr>
<td width="83" height="23">
<a href="http://www.weather.com.cn/weather/101011300.shtml" target="_blank">密云</a></td>
<td width="89">晴</td>
<td width="162">
<span>西南风</span>
<span class="conMidtabright"><3级</span></td>
<td width="92">30</td>
<td width="98">多云</td>
<td width="177">
<span>南风</span>
<span class="conMidtabright"><3级</span></td>
<td width="86">18</td>
<td width="49" class="last">
<a href="http://www.weather.com.cn/weather/101011300.shtml" target="_blank">详情</a></td>
</tr>
<tr>
<td width="83" height="23">
<a href="http://www.weather.com.cn/weather/101011400.shtml" target="_blank">门头沟</a></td>
<td width="89">晴</td>
<td width="162">
<span>南风</span>
<span class="conMidtabright"><3级</span></td>
<td width="92">31</td>
<td width="98">多云</td>
<td width="177">
<span>西南风</span>
<span class="conMidtabright"><3级</span></td>
<td width="86">20</td>
<td width="49" class="last">
<a href="http://www.weather.com.cn/weather/101011400.shtml" target="_blank">详情</a></td>
</tr>
<tr>
<td width="83" height="23">
<a href="http://www.weather.com.cn/weather/101011500.shtml" target="_blank">平谷</a></td>
<td width="89">晴</td>
<td width="162">
<span>西南风</span>
<span class="conMidtabright"><3级</span></td>
<td width="92">30</td>
<td width="98">多云</td>
<td width="177">
<span>东南风</span>
<span class="conMidtabright"><3级</span></td>
<td width="86">19</td>
<td width="49" class="last">
<a href="http://www.weather.com.cn/weather/101011500.shtml" target="_blank">详情</a></td>
</tr>
<tr>
<td width="83" height="23">
<a href="http://www.weather.com.cn/weather/101011600.shtml" target="_blank">东城</a></td>
<td width="89">晴</td>
<td width="162">
<span>南风</span>
<span class="conMidtabright"><3级</span></td>
<td width="92">31</td>
<td width="98">多云</td>
<td width="177">
<span>南风</span>
<span class="conMidtabright"><3级</span></td>
<td width="86">21</td>
<td width="49" class="last">
<a href="http://www.weather.com.cn/weather/101011600.shtml" target="_blank">详情</a></td>
</tr>
<tr>
<td width="83" height="23">
<a href="http://www.weather.com.cn/weather/101011700.shtml" target="_blank">西城</a></td>
<td width="89">晴</td>
<td width="162">
<span>南风</span>
<span class="conMidtabright"><3级</span></td>
<td width="92">31</td>
<td width="98">多云</td>
<td width="177">
<span>南风</span>
<span class="conMidtabright"><3级</span></td>
<td width="86">20</td>
<td width="49" class="last">
<a href="http://www.weather.com.cn/weather/101011700.shtml" target="_blank">详情</a></td>
</tr>
</table>
</div>
<div class="contentLtab">
<span style="margin-left:400px;">
<a href="#">返回顶部</a></span>
</div>
</div>
<div class="conMidtab" style="display:none;">
<div class="conMidtab5">
<table width="100%" border="0" cellpadding="0" cellspacing="0">
<tr>
<td width="74" rowspan="2">市</td>
<td width="83" rowspan="2">区/县</td>
<td height="37" colspan="3">周一(8月26日)白天</td>
<td colspan="3">周一(8月26日)夜间</td>
<td width="49" rowspan="2" class="last">&nbsp;</td>
</tr>
<tr>
<td width="89" height="23">天气现象</td>
<td width="162">风向风力</td>
<td width="92">最高气温</td>
<td width="98">天气现象</td>
<td width="177">风向风力</td>
<td width="86">最低气温</td>
</tr>
</table>
</div>
<div class="conMidtab3">
<a name="0" id="0"></a>
<table width="100%" border="0" cellpadding="0" cellspacing="0">
<tr>
<td width="74" rowspan="17" class="rowsPan">北京</td>
<td width="83" height="23">
<a href="http://www.weather.com.cn/weather/101010100.shtml" target="_blank">北京</a></td>
<td width="89">多云</td>
<td width="162">
<span>西南风</span>
<span class="conMidtabright"><3级</span></td>
<td width="92">30</td>
<td width="98">多云</td>
<td width="177">
<span>西南风</span>
<span class="conMidtabright"><3级</span></td>
<td width="86">22</td>
<td width="49" class="last">
<a href="http://www.weather.com.cn/weather/101010100.shtml" target="_blank">详情</a></td>
</tr>
<tr>
<td width="83" height="23">
<a href="http://www.weather.com.cn/weather/101010200.shtml" target="_blank">海淀</a></td>
<td width="89">多云</td>
<td width="162">
<span>南风</span>
<span class="conMidtabright"><3级</span></td>
<td width="92">31</td>
<td width="98">多云</td>
<td width="177">
<span>北风</span>
<span class="conMidtabright"><3级</span></td>
<td width="86">22</td>
<td width="49" class="last">
<a href="http://www.weather.com.cn/weather/101010200.shtml" target="_blank">详情</a></td>
</tr>
<tr>
<td width="83" height="23">
<a href="http://www.weather.com.cn/weather/101010300.shtml" target="_blank">朝阳</a></td>
<td width="89">多云</td>
<td width="162">
<span>西南风</span>
<span class="conMidtabright"><3级</span></td>
<td width="92">31</td>
<td width="98">多云</td>
<td width="177">
<span>东风</span>
<span class="conMidtabright"><3级</span></td>
<td width="86">22</td>
<td width="49" class="last">
<a href="http://www.weather.com.cn/weather/101010300.shtml" target="_blank">详情</a></td>
</tr>
<tr>
<td width="83" height="23">
<a href="http://www.weather.com.cn/weather/101010400.shtml" target="_blank">顺义</a></td>
<td width="89">多云</td>
<td width="162">
<span>南风</span>
<span class="conMidtabright"><3级</span></td>
<td width="92">31</td>
<td width="98">多云</td>
<td width="177">
<span>东风</span>
<span class="conMidtabright"><3级</span></td>
<td width="86">22</td>
<td width="49" class="last">
<a href="http://www.weather.com.cn/weather/101010400.shtml" target="_blank">详情</a></td>
</tr>
<tr>
<td width="83" height="23">
<a href="http://www.weather.com.cn/weather/101010500.shtml" target="_blank">怀柔</a></td>
<td width="89">多云</td>
<td width="162">
<span>南风</span>
<span class="conMidtabright"><3级</span></td>
<td width="92">30</td>
<td width="98">多云</td>
<td width="177">
<span>东北风</span>
<span class="conMidtabright"><3级</span></td>
<td width="86">21</td>
<td width="49" class="last">
<a href="http://www.weather.com.cn/weather/101010500.shtml" target="_blank">详情</a></td>
</tr>
<tr>
<td width="83" height="23">
<a href="http://www.weather.com.cn/weather/101010600.shtml" target="_blank">通州</a></td>
<td width="89">多云</td>
<td width="162">
<span>西南风</span>
<span class="conMidtabright"><3级</span></td>
<td width="92">30</td>
<td width="98">多云</td>
<td width="177">
<span>南风</span>
<span class="conMidtabright"><3级</span></td>
<td width="86">21</td>
<td width="49" class="last">
<a href="http://www.weather.com.cn/weather/101010600.shtml" target="_blank">详情</a></td>
</tr>
<tr>
<td width="83" height="23">
<a href="http://www.weather.com.cn/weather/101010700.shtml" target="_blank">昌平</a></td>
<td width="89">多云</td>
<td width="162">
<span>南风</span>
<span class="conMidtabright"><3级</span></td>
<td width="92">31</td>
<td width="98">多云</td>
<td width="177">
<span>西北风</span>
<span class="conMidtabright"><3级</span></td>
<td width="86">22</td>
<td width="49" class="last">
<a href="http://www.weather.com.cn/weather/101010700.shtml" target="_blank">详情</a></td>
</tr>
<tr>
<td width="83" height="23">
<a href="http://www.weather.com.cn/weather/101010800.shtml" target="_blank">延庆</a></td>
<td width="89">多云</td>
<td width="162">
<span>东南风</span>
<span class="conMidtabright"><3级</span></td>
<td width="92">29</td>
<td width="98">多云</td>
<td width="177">
<span>北风</span>
<span class="conMidtabright"><3级</span></td>
<td width="86">18</td>
<td width="49" class="last">
<a href="http://www.weather.com.cn/weather/101010800.shtml" target="_blank">详情</a></td>
</tr>
<tr>
<td width="83" height="23">
<a href="http://www.weather.com.cn/weather/101010900.shtml" target="_blank">丰台</a></td>
<td width="89">多云</td>
<td width="162">
<span>西南风</span>
<span class="conMidtabright"><3级</span></td>
<td width="92">31</td>
<td width="98">多云</td>
<td width="177">
<span>北风</span>
<span class="conMidtabright"><3级</span></td>
<td width="86">22</td>
<td width="49" class="last">
<a href="http://www.weather.com.cn/weather/101010900.shtml" target="_blank">详情</a></td>
</tr>
<tr>
<td width="83" height="23">
<a href="http://www.weather.com.cn/weather/101011000.shtml" target="_blank">石景山</a></td>
<td width="89">多云</td>
<td width="162">
<span>南风</span>
<span class="conMidtabright"><3级</span></td>
<td width="92">31</td>
<td width="98">多云</td>
<td width="177">
<span>北风</span>
<span class="conMidtabright"><3级</span></td>
<td width="86">22</td>
<td width="49" class="last">
<a href="http://www.weather.com.cn/weather/101011000.shtml" target="_blank">详情</a></td>
</tr>
<tr>
<td width="83" height="23">
<a href="http://www.weather.com.cn/weather/101011100.shtml" target="_blank">大兴</a></td>
<td width="89">多云</td>
<td width="162">
<span>西南风</span>
<span class="conMidtabright"><3级</span></td>
<td width="92">31</td>
<td width="98">多云</td>
<td width="177">
<span>西南风</span>
<span class="conMidtabright"><3级</span></td>
<td width="86">21</td>
<td width="49" class="last">
<a href="http://www.weather.com.cn/weather/101011100.shtml" target="_blank">详情</a></td>
</tr>
<tr>
<td width="83" height="23">
<a href="http://www.weather.com.cn/weather/101011200.shtml" target="_blank">房山</a></td>
<td width="89">多云</td>
<td width="162">
<span>西南风</span>
<span class="conMidtabright"><3级</span></td>
<td width="92">31</td>
<td width="98">多云</td>
<td width="177">
<span>西南风</span>
<span class="conMidtabright"><3级</span></td>
<td width="86">21</td>
<td width="49" class="last">
<a href="http://www.weather.com.cn/weather/101011200.shtml" target="_blank">详情</a></td>
</tr>
<tr>
<td width="83" height="23">
<a href="http://www.weather.com.cn/weather/101011300.shtml" target="_blank">密云</a></td>
<td width="89">多云</td>
<td width="162">
<span>西南风</span>
<span class="conMidtabright"><3级</span></td>
<td width="92">30</td>
<td width="98">多云</td>
<td width="177">
<span>东北风</span>
<span class="conMidtabright"><3级</span></td>
<td width="86">21</td>
<td width="49" class="last">
<a href="http://www.weather.com.cn/weather/101011300.shtml" target="_blank">详情</a></td>
</tr>
<tr>
<td width="83" height="23">
<a href="http://www.weather.com.cn/weather/101011400.shtml" target="_blank">门头沟</a></td>
<td width="89">多云</td>
<td width="162">
<span>南风</span>
<span class="conMidtabright"><3级</span></td>
<td width="92">31</td>
<td width="98">多云</td>
<td width="177">
<span>北风</span>
<span class="conMidtabright"><3级</span></td>
<td width="86">22</td>
<td width="49" class="last">
<a href="http://www.weather.com.cn/weather/101011400.shtml" target="_blank">详情</a></td>
</tr>
<tr>
<td width="83" height="23">
<a href="http://www.weather.com.cn/weather/101011500.shtml" target="_blank">平谷</a></td>
<td width="89">多云</td>
<td width="162">
<span>西南风</span>
<span class="conMidtabright"><3级</span></td>
<td width="92">30</td>
<td width="98">多云</td>
<td width="177">
<span>南风</span>
<span class="conMidtabright"><3级</span></td>
<td width="86">21</td>
<td width="49" class="last">
<a href="http://www.weather.com.cn/weather/101011500.shtml" target="_blank">详情</a></td>
</tr>
<tr>
<td width="83" height="23">
<a href="http://www.weather.com.cn/weather/101011600.shtml" target="_blank">东城</a></td>
<td width="89">多云</td>
<td width="162">
<span>西南风</span>
<span class="conMidtabright"><3级</span></td>
<td width="92">31</td>
<td width="98">多云</td>
<td width="177">
<span>东风</span>
<span class="conMidtabright"><3级</span></td>
<td width="86">22</td>
<td width="49" class="last">
<a href="http://www.weather.com.cn/weather/101011600.shtml" target="_blank">详情</a></td>
</tr>
<tr>
<td width="83" height="23">
<a href="http://www.weather.com.cn/weather/101011700.shtml" target="_blank">西城</a></td>
<td width="89">多云</td>
<td width="162">
<span>南风</span>
<span class="conMidtabright"><3级</span></td>
<td width="92">31</td>
<td width="98">多云</td>
<td width="177">
<span>北风</span>
<span class="conMidtabright"><3级</span></td>
<td width="86">22</td>
<td width="49" class="last">
<a href="http://www.weather.com.cn/weather/101011700.shtml" target="_blank">详情</a></td>
</tr>
</table>
</div>
<div class="contentLtab">
<span style="margin-left:400px;">
<a href="#">返回顶部</a></span>
</div>
</div>
</div>
</div>
</div>
</div>
</div>
</div>
<!--页尾start-->
<script>W.use('j/weather2015/publicHead.js?2019');</script>
<div class="footer">
  <div class="block">
    <div class="Lcontent" style="width:558px;">
      <dl style="width:280px; margin-right:22px;">
        <dt>
          <h3>网站服务</h3>
        </dt>
        <dd>
          <p><a href="http://www.weather.com.cn/wzfw/gywm/" target="_blank">关于我们</a><a href="http://www.weather.com.cn/wzfw/lxwm/" target="_blank">联系我们</a><a href="http://www.weather.com.cn/wzfw/sybz/" target="_blank">帮助</a><a href="http://www.weather.com.cn/wzfw/ryzp/" target="_blank">人员招聘</a></p>
          <p><a href="http://www.weather.com.cn/wzfw/kfzx/" target="_blank">客服中心</a><a href="http://www.weather.com.cn/wzfw/bqsm/" target="_blank">版权声明</a><a href="http://www.weather.com.cn/wzfw/wzls/" target="_blank">律师</a><a href="http://www.weather.com.cn/wzfw/wzdt/" target="_blank">网站地图</a></p>
        </dd>
      </dl>
      <dl style="width:150px;">
        <dt>
          <h3>营销中心</h3>
        </dt>
        <dd>
          <p><a href="http://marketing.weather.com.cn/wzhz/index.shtml" target="_blank">商务合作</a><a href="http://ad.weather.com.cn/index.shtml" target="_blank">广告服务</a></p>
        </dd>
      </dl>
      <div class="clear"></div>
    </div>
    <div class="friendLink" style="width:418px;margin-right:15px;">
      <h3>相关链接</h3>
      <p><a href="http://www.cma.gov.cn/" target="_blank">中国气象局</a><a href="http://www.pmsc.cn/" target="_blank">公共气象服务中心</a><a href="http://www.chinamsa.org" target="_blank">中国气象服务协会</a> </p>
      <p><a href="http://www.weathertv.cn/" target="_blank">中国天气频道</a><a href="http://www.tourweather.com.cn/" target="_blank">中国旅游天气网</a><a href="http://www.xn121.com/" target="_blank">中国兴农网</a></p>

    </div>
    <div class="serviceinfo" style="position:relative;">
<p><span>客服邮箱：<a href="mailto:service@weather.com.cn">service@weather.com.cn</a></span><span style="width:220px;">广告服务：<b>010-58991910</b></span><span><a href="http://www.beian.miit.gov.cn/" target="_blank">京ICP证010385号</a>　京公网安备11041400134号</span></p>
      <p><span>客服热线：<b><a href="http://www.weather.com.cn/wzfw/kfzx/index.shtml" target="_blank">400-6000-121</a></b></span><span style="width:220px;">  商务合作：<b>010-58991806</b><b style="display:  block;margin-left: 60px;">010-58991938</b></span><span>增值电信业务经营许可证B2-20050053</span></p>
<a id="___szfw_logo___" target="_blank" href="http://www.bcpcn.com/product/pjia/da/BCP65914858F778322.html"><img src="http://i.tq121.com.cn/i/weather2017/cx_new.png" style="position:absolute;right:10px;top:25px;"></a>
    </div>
    <div class="clear"></div>
  </div>
  <div class="aboutUs"> 中国天气网版权所有，未经书面授权禁止使用&nbsp&nbsp&nbsp&nbsp&nbsp&nbsp&nbsp&nbspCopyright&copy;<a href="http://www.pmsc.cn/" target="_blank">中国气象局公共气象服务中心</a> All Rights Reserved (2008-2019)</div>
</div>



<script type="text/javascript">
var _bdhmProtocol = (("https:" == document.location.protocol) ? " https://" : " http://");
document.write(unescape("%3Cscript src='" + _bdhmProtocol + "hm.baidu.com/h.js%3F080dabacb001ad3dc8b9b9049b36d43b' type='text/javascript'%3E%3C/script%3E"));
</script>


<script type="text/javascript">
window._wat = window._wat || [];
(function() {
    var wm = document.createElement("script");
    wm.src = "http://analyse.weather.com.cn/js/v1/wa.js?site_id=1";
    var s = document.getElementsByTagName("script")[0];
    s.parentNode.insertBefore(wm, s);
})();
</script>
	<script src="https://j.i8tq.com/weather1d/pcvideo.js?20190718"></script>
<!--[if IE]>
    <script src="http://api.html5media.info/1.2.2/html5media.min.js"></script>
    <![endif]-->

<!--页尾end-->
<script type="text/javascript" src="http://www.weather.com.cn/m2/j/weather/textFC.js"></script>
<script>W.use('j/common');</script>
<script src="http://www.weather.com.cn/m2/j/public/main2013.js" type="text/javascript"></script>
<script type="text/javascript" src="http://c.wrating.com/a1.js">
</script>
<script type="text/javascript">
var vjAcc="860010-2099040100";
var wrUrl="http://c.wrating.com/";
vjTrack("");
</script>
<noscript><img src="http://c.wrating.com/a.gif?a=&c=860010-2099040100" width="1" height="1"/></noscript>
</body>
</html>
"""

selector = etree.HTML(response)

wind_morning_list  = selector.xpath('//div[@class="conMidtab" and not (@style)]/div[@class="conMidtab3"]/table/tr/td[@width=162]')

for wind_morning in wind_morning_list:
    wind_morning_single = "".join(wind_morning.split())

    # remove HTML tag
    wind_morning_single_matched = re.sub(r'<.*?>','',wind_morning_single)

    wind_morning = wind_morning_single_matched
    print (wind_morning)
# print (response.read())

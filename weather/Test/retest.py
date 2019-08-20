import re

content = """<?xml version="1.0" encoding="utf-8"?>
<items>
<item><city>北京</city><weather_morning>小雨</weather_morning><weather_evening>多云</weather_evening><wind_morning>南风3-4级</wind_morning><wind_evening>北风&amp;lt;3级</wind_evening><temperature_high>26</temperature_high><temperature_low>19</temperature_low></item>
<item><city>海淀</city><weather_morning>小雨</weather_morning><weather_evening>多云</weather_evening><wind_morning>南风3-4级</wind_morning><wind_evening>北风&amp;lt;3级</wind_evening><temperature_high>27</temperature_high><temperature_low>18</temperature_low></item>
<item><city>朝阳</city><weather_morning>小雨</weather_morning><weather_evening>多云</weather_evening><wind_morning>南风&amp;lt;3级</wind_morning><wind_evening>北风&amp;lt;3级</wind_evening><temperature_high>27</temperature_high><temperature_low>19</temperature_low></item>
<item><city>顺义</city><weather_morning>小雨</weather_morning><weather_evening>多云</weather_evening><wind_morning>南风&amp;lt;3级</wind_morning><wind_evening>北风&amp;lt;3级</wind_evening><temperature_high>27</temperature_high><temperature_low>19</temperature_low></item>
<item><city>怀柔</city><weather_morning>小雨</weather_morning><weather_evening>多云</weather_evening><wind_morning>南风&amp;lt;3级</wind_morning><wind_evening>北风&amp;lt;3级</wind_evening><temperature_high>26</temperature_high><temperature_low>18</temperature_low></item>
<item><city>通州</city><weather_morning>小雨</weather_morning><weather_evening>多云</weather_evening><wind_morning>南风&amp;lt;3级</wind_morning><wind_evening>北风&amp;lt;3级</wind_evening><temperature_high>26</temperature_high><temperature_low>18</temperature_low></item>
<item><city>昌平</city><weather_morning>小雨</weather_morning><weather_evening>多云</weather_evening><wind_morning>东南风&amp;lt;3级</wind_morning><wind_evening>西北风&amp;lt;3级</wind_evening><temperature_high>27</temperature_high><temperature_low>19</temperature_low></item>
<item><city>延庆</city><weather_morning>小雨</weather_morning><weather_evening>多云</weather_evening><wind_morning>东南风&amp;lt;3级</wind_morning><wind_evening>西风&amp;lt;3级</wind_evening><temperature_high>23</temperature_high><temperature_low>16</temperature_low></item>
<item><city>丰台</city><weather_morning>小雨</weather_morning><weather_evening>多云</weather_evening><wind_morning>西南风3-4级</wind_morning><wind_evening>北风&amp;lt;3级</wind_evening><temperature_high>28</temperature_high><temperature_low>19</temperature_low></item>
<item><city>石景山</city><weather_morning>小雨</weather_morning><weather_evening>多云</weather_evening><wind_morning>南风3-4级</wind_morning><wind_evening>北风&amp;lt;3级</wind_evening><temperature_high>27</temperature_high><temperature_low>19</temperature_low></item>
<item><city>大兴</city><weather_morning>小雨</weather_morning><weather_evening>多云</weather_evening><wind_morning>南风3-4级</wind_morning><wind_evening>北风&amp;lt;3级</wind_evening><temperature_high>26</temperature_high><temperature_low>18</temperature_low></item>
<item><city>房山</city><weather_morning>小雨</weather_morning><weather_evening>多云</weather_evening><wind_morning>南风3-4级</wind_morning><wind_evening>北风&amp;lt;3级</wind_evening><temperature_high>27</temperature_high><temperature_low>18</temperature_low></item>
<item><city>密云</city><weather_morning>小雨</weather_morning><weather_evening>多云</weather_evening><wind_morning>南风&amp;lt;3级</wind_morning><wind_evening>东北风&amp;lt;3级</wind_evening><temperature_high>25</temperature_high><temperature_low>17</temperature_low></item>
<item><city>门头沟</city><weather_morning>小雨</weather_morning><weather_evening>多云</weather_evening><wind_morning>南风3-4级</wind_morning><wind_evening>北风&amp;lt;3级</wind_evening><temperature_high>27</temperature_high><temperature_low>19</temperature_low></item>
<item><city>平谷</city><weather_morning>小雨</weather_morning><weather_evening>多云</weather_evening><wind_morning>东南风&amp;lt;3级</wind_morning><wind_evening>北风&amp;lt;3级</wind_evening><temperature_high>26</temperature_high><temperature_low>16</temperature_low></item>
<item><city>东城</city><weather_morning>小雨</weather_morning><weather_evening>多云</weather_evening><wind_morning>南风&amp;lt;3级</wind_morning><wind_evening>北风&amp;lt;3级</wind_evening><temperature_high>27</temperature_high><temperature_low>19</temperature_low></item>
<item><city>西城</city><weather_morning>小雨</weather_morning><weather_evening>多云</weather_evening><wind_morning>南风3-4级</wind_morning><wind_evening>北风&amp;lt;3级</wind_evening><temperature_high>27</temperature_high><temperature_low>18</temperature_low></item>
</items>"""

result = re.sub(r'&amp;lt;', '<', content)

print(result)

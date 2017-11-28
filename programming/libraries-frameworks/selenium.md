`phantomjs` 可以headless处理
`WebDriver` will wait until the page has fully loaded (that is, the “onload” event has fired) before returning control
The Keys class provide keys in the keyboard like RETURN, F1, ALT etc.
    `send_keys("pycon") `发送p, y, c, o, n等按键，`send_keys(Keys.RETURN)` 按回车
## Interacting with the page
- element.send_keys
- element.clear()
- element.submit() # 自动往外找form
- Drag and drop
- Moving between windows and frames
- driver.forward() / driver.back()
## in discovering the XPath of an element:
- XPath Checker - suggests XPath and can be used to test XPath results.
- Firebug - XPath suggestions
- XPath Helper - for Google Chrome

page object pattern
XPATH
    . 代表从当前开始
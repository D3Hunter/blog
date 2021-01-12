- `Cross-site request forgery`, also known as `one-click attack` or `session riding` and abbreviated as `CSRF` (sometimes pronounced sea-surf) or `XSRF`, is a type of malicious exploit of a website where unauthorized commands are submitted from a user that the web application trusts.
    - Unlike `cross-site scripting (XSS)`, which exploits the trust a user has for a particular site, `CSRF exploits the trust that a site has in a user's browser`.
    - 用户浏览器有`A`网站的权限（已登陆），在用户访问`B`网站时，其页面上伪造的A网站的请求被主动或被动执行，由于浏览器的cookie会自动跟随网站被发送，该请求会被网站`A`认为是来自用户的请求.
    - 一种`confused deputy attack`
- `web application firewall (WAF)`
<h1>Yell server and db</h1>

<p>The orm used is SQLAlchemy with Flask for routing. Websockets are immplemented using Redis Message Queue to update data in real time. Redis is also used, via websockets, for geospatial calaculations.</p>

<p>One of my main focuses for this project is to write performat and scalable code. The biggest step in that direction would be the modularity and ecapsulation of flask/sqlalchemy storage and redis/websocket implementation.</p>

<h2>Redis</h2>
<p>The <a href='https://github.com/about14sheep/yell_proxy_chat/tree/master/serv/redidb'>redidb</a> folder holds the redis wrapper and information on how I built it</p>

<h2>WebSocket</h2>
<p>The <a href='https://github.com/about14sheep/yell_proxy_chat/tree/master/serv/websocket'>websocket</a> folder contains Socket.IO Namespaces and logic as well documentation on accepted calls</p>

<h2>Db diagram sql</h2>
<br>
<img src="https://github.com/about14sheep/yell_proxy_chat/blob/master/serv/docs/yell_db.png">

<h1>Yell server and db</h1>

The orm used is SQLAlchemy with Flask for routing. Websockets are immplemented using Redis Message Queue to update data in real time. Redis is also used, via websockets, for geospatial calaculations.

<h3>Db diagram sql</h3>
<br>
<img src="https://github.com/about14sheep/yell_proxy_chat/blob/master/serv/docs/yell_db.png">

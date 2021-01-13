<h1>Yell server and db</h1>

<p>The orm used is SQLAlchemy with Flask for routing. Websockets are immplemented using Redis Message Queue to update data in real time. Redis is also used, via websockets, for geospatial calaculations.</p>

<p>One of my main focuses for this project is to write performat and scalable code. The biggest step in that direction would be the modularity and ecapsulation of flask/sqlalchemy storage and redis/websocket implementation.</p>

<h3>Redis Map</h3>
<section>
  <h4>Hashes</h4>
  <ul>
    <li>Emote - ID: {image_url, author_id}</li>
    <li>Totem_Skin - ID: {image_url}</li>
  </ul>
</section>

<h3>Db diagram sql</h3>
<br>
<img src="https://github.com/about14sheep/yell_proxy_chat/blob/master/serv/docs/yell_db.png">

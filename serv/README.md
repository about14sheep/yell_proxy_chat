<h1>Yell server and db</h1>

<p>The orm used is SQLAlchemy with Flask for routing. Websockets are immplemented using Redis Message Queue to update data in real time. Redis is also used, via websockets, for geospatial calaculations.</p>

<p>One of my main focuses for this project is to write performat and scalable code. The biggest step in that direction would be the modularity and ecapsulation of flask/sqlalchemy storage and redis/websocket implementation.</p>

<h2>Redis Map</h2>
<section>
  <h4>Hashes</h4>
  <ul>
    <li>User - UserID: { username, user_id }</li>
    <li>Totem - TotemID: { owner_id, totem_skin_id }</li>
    <li>Emote - EmoteID: { image_url, author_id }</li>
    <li>Totem_Skin - SkinID: { image_url }</li>
  </ul>
</section>
<section>
  <h4>Sets</h4>
  <ul>
    <li>Users at Totem - TotemID: [user_ids]</li>
    <li>Totems near User - UserID: [totem_ids]</li>
    <li>Emote Users - EmoteID: [user_ids]</li>
    <li>Totem_Skin Users - SkinID: [user_ids]</li>
  </ul>
</section>
<section>
  <h4>Geolocation</h4>
  <ul>
    <li>Totem - TotemID: { long, lat }</li>
  </ul>
</section>

<h2>Db diagram sql</h2>
<br>
<img src="https://github.com/about14sheep/yell_proxy_chat/blob/master/serv/docs/yell_db.png">

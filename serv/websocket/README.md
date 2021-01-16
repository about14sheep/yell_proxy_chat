<h1>WebSocket</h1>

<p>Using Flask_Socketio Namespaces I am able to seperate the logic into seperate modules for readability. The WebSocket channels will save and get from redis using the RediWrap class imported from <a href='https://github.com/about14sheep/yell_proxy_chat/tree/master/serv/redidb'>redidb</a></p>


<h2>Namespaces and Request Calls</h2>

<section>
  <h4>Totem Socket</h4>
  <ul>
    <li>totem_set -- Saves totem hash in redis</li>
    <li>totem_get -- Returns totem hash</li>
    <li>totem_scan -- Scans for totems around given radius</li>
    <li>totem_place -- Saves totem by coordinates in redis</li>
    <li>totem_join -- Joins user to totem socketio room</li>
    <li>totem_leave -- Removes user from totem socketio room</li>
  </ul>
</section>

<section>
  <h4>User Socket</h4>
  <ul>
    <li>user_save -- Saves user hash to redis</li>
    <li>user_get -- Returns user hash</li>
    <li>user_location -- Finds totems close enough to user to allow chat, saves in redis</li>
  </ul>
</section>

<section>
  <h4>Stream Socket</h4>
  <ul>
    <li>stream_yell -- Sends chat message to totem room</li>
  </ul>
</section>

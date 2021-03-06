<h2>Redis Wrapper</h2>

<p>I have assigned a redis datastructure to the IDs for totems, emotes, totem_skins, and users. The logic of this immplentation resides in the characteristics of the redis data type: i.e. Using a totems ID, as key for a redis set, will return the users at that totem. Likewise, using a users ID, as key for a redis set, will return the totems a user is in range to chat in. This allows for easier implementation and less confusion.</p>

<p>Tagging the keys with 'HT' for totem hash, and so on, prevents unexpected data returns</p>

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

<h3>SQL Calls</h3>

<p>The init file for <a href='https://github.com/about14sheep/yell_proxy_chat/tree/master/serv/redidb/rmodels'>rmodels</a> holds the interface functions to interact with the sql models</p>

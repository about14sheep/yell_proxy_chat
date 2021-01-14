<h2>Redis Wrapper</h2>

<p>I have assigned a redis datastructure to a certain ID for a totem, emote, totem_skin, and user. The logic of this immplentation resides in the characteristics of the redis data type</p>

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

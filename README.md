<h1>yell_proxy_chat</h1>
<p>Proximity chat Redis implementation using Flask with WebSockets, and SQL storage through SQLAlchemy. Client built with React. Inspired by twitch.tv chat.</p>

<h2>Server</h2>
<p>The <a href='https://github.com/about14sheep/yell_proxy_chat/tree/master/serv'>serv</a> folder holds the current state and documentation of the backend built in Flask, Sqlalchemy, and Redis</p>

<h2>Client</h2>
The <a href='https://github.com/about14sheep/yell_proxy_chat/tree/master/client'>client</a> folder holds the current state of the react-redux frontend


<h2>Concept</h2>

<h4>Proxy Chat</h4>
<p>Users will be allowed to view any totem they find on yell. However, chatting, in the totems chat, is only allowed if the user is within ~one mile of the totems location. Once the user sends the first chat message they earn the totems 'Discovery Emote' (unless the emote is already in that users collection)</p>

<h4>Emotes</h4>
<p>Emotes are at the core of yell. Users collect emotes by visiting (and chatting in) totems. Users can upload their own emote to attach to their totem as a 'Discovery Emote' - this emote is obtained by sending a chat message in the totems chat. Emotes can also be earned through events, geographically (using yell in different places), and step-wise (earn these emotes to unlock this emote). The emotes a user earns can be used in other totem chats.</p>

<h4>Totems</h4>
<p>Every user will have a totem. Users will also be able to follow other user totems they like. Users can change the skin of their totem as well the discovery emote. When a user places their totem at their location it becomes a public channel. The totem can be seen by all users searching that area. Once a user joins a totem they will be able to chat (if that user is within 1 mile of the totem). The totem will automatically disappear after a period of inactivity, or can be picked up by the owning user</p>

<h4>Totem Skins</h4>
<p>Totem Skins are earned through totem events (i.e. number of followers, number of users in chat).</p>

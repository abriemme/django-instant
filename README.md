# Django Instant

Websockets for Django with [Centrifugo](https://github.com/centrifugal/centrifugo).

* Push events in real time into public or private channels.

* Handle your event in javascript client-side.

Check the [documentation](http://django-instant.readthedocs.io/en/latest/).

### Quick example

Push some events on channels from anywhere in the code:

  ```python
from instant import broadcast
  
# push an event on the default public channel
broadcast(message='Hello world', event_class="test")

# push an event to a private channel with extra data payload
data = {"site":"mysite","username":"joe"}
broadcast(message='Hello world', channel="$myprivatechan", data=data)
  ```

Handle the event client-side in a template:

  ```javascript
if (event_class == 'test') {
        console.log("This is a test message: "+message);
        return true
}
  ```

### Example apps

[Jafeed](https://github.com/synw/jafeed): rss feeds aggregator with live notifications on new posts

[Django Mqueue Livefeed](https://github.com/synw/django-mqueue-livefeed): real time application events and logs

[Django Presence](https://github.com/synw/django-presence): user presence notification widget

[Django Rechat](https://github.com/synw/django-rechat): basic chat app
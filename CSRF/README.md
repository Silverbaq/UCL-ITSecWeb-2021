# Cross site request forgery (CSRF)

## Setup

* Install dependencies. `pip install -r requirements.txt`

## Run

* The `vulnerable` version can be run, by using the command: `python vulnerable.py`

* For the `csrf-secure` version, it can be run with the command: `python csrf-secure.py`

## Tests

To test this out, you can do the following:

* Start `Burp`
* Make a `comment` and fetch the comment with `Burp`.
* Send it to the `Repeater`.
* If the site is vulnerable to CSRF, you can repeat the same form request over and over again.

Even though the site is secured with a CSRF token, the action of the site can still be triggered, in cases where there
is a XSS vulnerability. To try this out, you can do the following:

* Make a search query, where you insert the following script:

 ```
 <script>
        function Sleep(ms) {
            return new Promise(resolve => setTimeout(resolve, ms));
        }
        async function Hack() {
            await Sleep(1000);
            document.getElementsByName("comment")[0].value = "TEST!";
            document.getElementsByTagName("form")[1].submit();
        }
        Hack();
  </script> 
 ```

By doing so, you will trigger the client to request an event for you. In this demo case, there will be written a
comment.
So funktioniert der Ablauf:

Client sendet POST-Request:

Restlet-Framework empfängt den Request und gibt den Body (das JSON) als String an deinen Parameter body weiter

post Methode parst den String:
```java

@Post
public String handlePost(String body) {  // ← hier landet das JSON vom Client
    String id = body.split("\"id\":")[1]...

```

Proble
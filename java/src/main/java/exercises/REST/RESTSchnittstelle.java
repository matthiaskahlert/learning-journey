package REST;
import org.restlet.Component;
import org.restlet.data.Protocol;
import org.restlet.routing.Router;

public class RESTSchnittstelle {
    public static void main(String[] args) {
        final Component component = new Component();

        int port = 8080;
        if (args.length > 0) {
            try {
                port = Integer.parseInt(args[0]);
            } catch (NumberFormatException ignored) {}
        }

        component.getServers().add(Protocol.HTTP, port);

        // 👉 HIER KOMMT DER ROUTER
        Router router = new Router(component.getContext().createChildContext());

        router.attach("/", StartseitenHandler.class);
        router.attach("/person", PersonHandler.class);
        router.attach("/person/{id}", PersonHandler.class);

        component.getDefaultHost().attach(router);

        try {
            component.start();
            System.out.println("Server läuft auf Port " + port);
        } catch (Exception e) {
            e.printStackTrace();
        }
    }
}
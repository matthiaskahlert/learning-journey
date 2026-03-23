import org.restlet.Component;
import org.restlet.data.Protocol;
import org.restlet.resource.ServerResource;
import org.restlet.service.CorsService;

public class RESTSchnittstelle {
    public static void main(String[] args) {
        final Component component = new Component();
        int port = 8080;
        if (args.length > 0) {
            try {
                port = Integer.parseInt(args[0]);
            } catch (NumberFormatException ignored) {
                // Keep default port when argument is invalid.
            }
        }
        component.getServers().add(Protocol.HTTP, port);

        try {
            component.start();
        } catch (Exception e) {
            e.printStackTrace();
        }
    }
}

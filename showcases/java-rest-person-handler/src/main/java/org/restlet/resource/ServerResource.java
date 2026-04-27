package org.restlet.resource;

import java.util.HashMap;
import java.util.Map;

/**
 * Minimal test-friendly stand-in for Restlet's ServerResource.
 * It provides attribute access used by the handler logic.
 */
public class ServerResource {
    private final Map<String, String> attributes = new HashMap<>();

    public String getAttribute(String name) {
        return attributes.get(name);
    }

    protected void setAttribute(String name, String value) {
        attributes.put(name, value);
    }
}

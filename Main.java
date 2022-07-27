import java.net.URI;
import java.net.http.HttpClient;
import java.net.http.HttpRequest;
import java.net.http.HttpResponse;
import java.nio.charset.Charset;
 
public class Main {
    public static void main(String[] args) {
        HttpClient.newHttpClient()
                .sendAsync(Main.request_build(), HttpResponse.BodyHandlers.ofString(Charset.defaultCharset()))
                .thenApply(HttpResponse::body)
                .thenAccept(System.out::println)
                .join();
    }

    static URI uri_build(String baseuri) {
        UriBuild uri_loc = new UriBuild(baseuri);
        uri_loc.addquery("cedula", "3-761-2397");
        return URI.create(uri_loc.render());
    }

    static HttpRequest request_build(){
        String apiuri = "http://3.138.208.231:9041/api/advisers/cliente/";
        HttpRequest request = HttpRequest.newBuilder()
                .uri(Main.uri_build(apiuri))
                .GET()
                .build();
        return request;
    }

    static void client_build(){    }
}
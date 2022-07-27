import java.net.URI;
import java.net.http.HttpClient;
import java.net.http.HttpRequest;
import java.net.http.HttpResponse;
import java.nio.charset.Charset;
 
public class Main {
    public static void main(String[] args) {
        var request = HttpRequest.newBuilder(URI.create("http://3.138.208.231:9041/api/advisers/cliente/?cedula=3-761-2397&edad=24"))
                .GET()
                .build();
 
        HttpClient.newHttpClient()
                .sendAsync(request, HttpResponse.BodyHandlers.ofString(Charset.defaultCharset()))
                .thenApply(HttpResponse::body)
                .thenAccept(System.out::println)
                .join();
    }
}
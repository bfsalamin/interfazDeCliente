import java.util.ArrayList;
import java.util.List;

public class UriBuild {
    private String uri;
    private List<String> query = new ArrayList<>();
    
    public UriBuild(String target_uri) {
        uri = target_uri;
    }

    public void addquery(String key, String val) {
        this.query.add(key + "=" + val);
    }

    public String render() {
        String allquery = String.join("&", this.query);
        String retn = this.uri + "?" + allquery;
        return retn;
    }
}

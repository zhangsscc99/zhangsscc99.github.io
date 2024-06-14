import com.alibaba.fastjson.JSONObject;

public class JWTDemo05 {
    public static void main(String[] args) {
        JSONObject header = new JSONObject();
        header.putu("Alg", "HS256");
    }
}
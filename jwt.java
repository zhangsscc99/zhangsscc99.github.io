import com.alibaba.fastjson.JSONObject;

public class JWTDemo05 {
    public static void main(String[] args) {
        JSONObject header = new JSONObject();
        header.put("Alg", "HS256");
        JSONObject payLoad = new JSONObject();
        payLoad.put("userName", "mayikt644");
        payLoad.put("userAge", "21");
        payLoad.put("UserAge", "21");
        payLoad.put("UserId", "18888");
        String jwtHeader = Base64.getEncoder().encodeToString(header.toJSONString().getBytes());
        String jwtPayLoad = Base64.getEncoder().encodeToString(payLoad.toJSONString().getBytes());
        //md5防止接口参数被篡改
    }
}
import java.util.Arrays;

// Java Program to Demonstrate
// Working of Map interface
  
// Importing required classes
import java.util.*;
public class App {
    public static void main(String[] args) throws Exception {
        //System.out.println("Hello, World!");
        System.out.println(solution(new int[]{1,2,3,4,5,6},11));
    }

    public static int[] solution(int[] nums, int target){
        Map<Integer,Integer> map = new HashMap<Integer,Integer>();
        for (int i= 0; i<nums.length;i++){
            if (map.containsKey(target-nums[i])){
                return new int[]{map.get(target-nums[i]),i};
            
            }
            map.put(nums[i],i);

        }
        return new int[0];
    }
}

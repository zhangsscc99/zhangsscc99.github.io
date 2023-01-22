import java.util.Arrays;

// Java Program to Demonstrate
// Working of Map interface
  
// Importing required classes
import java.util.*;
public class App {
    public static void main(String[] args) throws Exception {
        //System.out.println("Hello, World!");
        System.out.println(Arrays.toString(solution(new int[]{1,2,3,4,5,6},11)));
        System.out.println(Arrays.toString(twoSearch(new int[]{1,2,3,4,5,6},11)));
        System.out.println(Arrays.toString(twoPoint(new int[]{1,2,3,4,5,6},11)));
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
    public static int[] twoSearch(int[] numbers, int target){
        for (int i=0;i<numbers.length;i++){
            int low=i,high=numbers.length-1;
            while (low<=high){
                int mid=(high+low)/2;
                if (numbers[mid]==target-numbers[i]){
                    return new int[]{i,mid};

                }else if (numbers[mid]>target-numbers[i]){
                    high=mid-1;

                }else{
                    low=mid+1;
                }

            }
        }
        return new int[]{0};
    }
    
    public static int[] twoPoint(int[] numbers,int target){
        int low=0,high=numbers.length-1;
        while (low<high){
            int sum= numbers[low]+numbers[high];
            if (sum==target){
                return new int[]{low,high};
            }else if (sum<target){
                low++;

            }else{
                high--;
            }

        }
        return new int[]{0};
    }
}

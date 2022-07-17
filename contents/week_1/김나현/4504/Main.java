// Boj 4504

import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;

public class Main {
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        int n = Integer.parseInt(br.readLine());

        while(true) { // 테스트 케이스의 개수가 안 정해져있기 때문에 무한 반복
            int num = Integer.parseInt(br.readLine());

            if(num == 0) break;

            String result = (num % n == 0) ? num + " is a multiple of " + n + "." : num + " is NOT a multiple of " + n + ".";
            System.out.println(result);
        }


    }

}
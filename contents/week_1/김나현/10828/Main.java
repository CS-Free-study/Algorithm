// Boj 2480
import java.lang.*;
import java.util.*;
import java.io.*;


public class Main {

    static int calculate(int A, int B, int C) {
        int result = 0;
        int max = A;

        // 1. 같은 눈이 세 개
        if(A == B && B == C) {
            result =  10000 + A * 1000;
        } else if(A != B && B != C && A != C) { // 모두 다른 눈
            if(max < B) max = B;
            if(max < C) max = C;

            result = max * 100;
        } else { // 같은 눈이 두 개
            if(A != B) {
                result = 1000 + C * 100;
            } else {
                result = 1000 + B * 100;
            }
        }

        return result;
    }


    public static void main(String[] args) throws IOException {

        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        StringTokenizer st = new StringTokenizer(br.readLine()); // 문자열을 우리가 지정한 구분자로 쪼개는 것

        int A = Integer.parseInt(st.nextToken());
        int B = Integer.parseInt(st.nextToken());
        int C = Integer.parseInt(st.nextToken());

        int result = calculate(A,B,C);
        System.out.println(result);

    }
}
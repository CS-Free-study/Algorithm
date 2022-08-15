package Stack;

import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.Stack;

public class Boj1874 {
    public static void main(String[] args) throws IOException {

        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        StringBuilder sb = new StringBuilder(); // 출력할 결과물을 저장

        int cnt = Integer.parseInt(br.readLine()); // 첫 줄, 입력 개수
        Stack<Integer> stack = new Stack<>();

        int start = 0; // 오름차순으로 push되는 스택에서 들어가야할 숫자

        while(cnt-- > 0) { // 입력 개수만큼 반복

            int value = Integer.parseInt(br.readLine());

            if(value > start) {
                // start부터 입력받은 value까지 push를 한다.
                for(int i = start+1; i<=value; i++) {
                    stack.push(i);
                    sb.append('+').append('\n'); // +를 저장
                }
                start=value; // 다음 push 할 때 오름차순으로 넣기 위한 시작 변수 초기화
            }

            // top에 있는 원소가 value와 같지 않다면
            else if(stack.peek() != value) {
                System.out.println("NO");
                return;
            }

            stack.pop();
            sb.append('-').append('\n'); // -를 저장
        }

        System.out.println(sb);
    }
}

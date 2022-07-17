// Boj 1181

import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.ArrayList;
import java.util.Arrays;
import java.util.Collections;
import java.util.List;

public class Main {
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        int num = Integer.parseInt(br.readLine());

        StringBuilder sb = new StringBuilder(); // 변경 가능한 문자열 만들어주기 때문에, 문자열 합치는 대안으로 사용
        List<String> list = new ArrayList<String>();

        // list에 문자열 입력값 저장
        for(int i = 0; i < num; i++) {
            list.add(br.readLine());
        }

        // 정렬
        Collections.sort(list); // 클래스의 객체를 정렬해주는 것, sort() = 오름차순, reverse() = 내림차순

        for(int i = 1; i<=50; i++) { // 입력의 길이 제한은 50
            for(int j = 0; j < list.size();) {
                if(list.get(j).length() == i) { // 리스트의 해당 인덱스의 값의 길이가 i와 같다면 sb에 저장, list에서 해당하는 값 제거
                    sb.append(list.get(j)).append("\n");
                    list.removeAll(Arrays.asList(list.get(j)));
                    // 제거 시 현재 인덱스에 있는 값이 사라지는데 다음 인덱스로 넘어가면
                    // 현재 인덱스에 있는 값도 넘어가므로, 지워지지 않았을 때만 다음 인덱스로 넘어간다.

                } else {
                    j++;
                }
            }
            if(list.isEmpty()) break; // 리스트가 비면 반복문 종료

        }
        System.out.println(sb);





    }
}
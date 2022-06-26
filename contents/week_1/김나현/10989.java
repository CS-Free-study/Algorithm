// Boj 10989 : 수 정렬하기 3
// 시간제한, 메모리 제한으로 리스트 타입의 객체들을 사용하지 못한다.
// 입출력도 BufferedReader, StringBuilder 혹은 BufferedWriter 을 사용해야 했다.

// Arrays.sort() 의 경우 dual-pivot Quick sort 알고리즘을 사용한다.
// 평균 O(nlogn) 의 시간복잡도를 보이지만 최악의 경우 O(n2) 로 좋지 않는 성능이 될 수도 있다.


import java.io.BufferedReader;
import java.io.InputStreamReader;
import java.io.IOException;
import java.util.Arrays;

public class Main {
    public static void main(String[] args) throws IOException {

        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        StringBuilder sb = new StringBuilder();

        int N = Integer.parseInt(br.readLine());
        int[] arr = new int[N];

        for(int i = 0; i < N; i++){
            arr[i] = Integer.parseInt(br.readLine());
        }

        Arrays.sort(arr);

        for(int i = 0; i < N; i++){
            sb.append(arr[i]).append('\n');
        }

        System.out.println(sb);
    }
}
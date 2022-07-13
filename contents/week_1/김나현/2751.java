// Boj 2751번 : 수 정렬하기 2
//
// Arrays.sort 로 쓰면 시간초과
//
// O(nlogn)을 보장하거나 혹은, O(n)에 가까운 정렬 알고리즘을 사용해야 한다.
// 1. Collections.sort() 사용
// https://st-lab.tistory.com/276
// 2. Counting sort(카운팅 정렬)을 응용해서 사용


import java.util.Scanner;
import java.util.ArrayList;
import java.util.Collections;


public class Main {
    public static void main(String[] args) {

        Scanner scanner = new Scanner(System.in);
        StringBuilder sb = new StringBuilder();

        int N = scanner.nextInt();

        ArrayList<Integer> arrayList = new ArrayList<>();

        for(int i = 0; i < N; i++) {
            arrayList.add(scanner.nextInt());
        }

        Collections.sort(arrayList);

        for(int value : arrayList) {
            sb.append(value).append('\n');
        }
        System.out.println(sb);
    }
}
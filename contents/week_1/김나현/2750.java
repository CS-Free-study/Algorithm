// sorting: bubble sort(버블정렬), selection sort(선택정렬), insertion sort(삽입정렬)
// 선택 정렬(selection sort) 사용 - 가장 작은 원소를 찾아 맨 앞으로 교체하는 방식

// Boj 2750번 : 수 정렬하기

import java.util.Scanner;

public class Main {
    public static void main(String[] args) {
        Scanner scanner = new Scanner(System.in);

        int N = scanner.nextInt();
        int[] arr = new int[N];

        for(int i = 0; i < N; i++) {
            arr[i] = scanner.nextInt();
        }

        for(int i = 0; i < N - 1; i++) {
            for(int j = i + 1; j < N; j++) {
                if(arr[i] > arr[j]) {
                    int temp = arr[j];
                    arr[j] = arr[i];
                    arr[i] = temp;
                }
            }
        }

        for(int val : arr) {
            System.out.println(val);
        }
    }
}
//baekjoon - 7568.java

import java.util.Scanner;

public class Main {
    public static void main(String[] args){
        Scanner scanner = new Scanner(System.in);
        int n = scanner.nextInt();

        int group[][] = new int[n][n];
        int rank;

        for(int i=0;i<n;i++){
            group[i][0] = scanner.nextInt();
            group[i][1] = scanner.nextInt();

        }
        for(int i = 0;i<n;i++){
            rank = 1;
            for(int j=0;j<n;j++){
                if(group[i][0]<group[j][0] && group[i][1]<group[j][1])rank++;
            }
            System.out.print(rank +" ");
        }
    }
}
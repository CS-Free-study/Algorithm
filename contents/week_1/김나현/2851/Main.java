import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;

public class Main {
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        int sum = 0;
        int diff = 100;
        int answer = 0;

        for(int i = 0; i < 10; i++) {
            sum += Integer.parseInt(br.readLine());

            if(Math.abs(100 - sum) <= diff) {
                diff = Math.abs(100 - sum);
                answer = sum;
            }
        }
        System.out.println(answer);

    }
}
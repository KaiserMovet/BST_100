import java.io.IOException;
import java.nio.file.Files;
import java.nio.file.Paths;
import java.util.Arrays;
import java.util.List;
import java.util.stream.Collectors;

public class Main {
    public static void main(String[] args) throws IOException {
        int amount = Integer.parseInt(args[0]);

        List<Integer> addNumbers = getNumbers("/datasets/add.txt").subList(0, amount);
        List<Integer> checkNumbers = getNumbers("/datasets/check.txt").subList(0, amount);

        Tree bst = new Tree();

        // Add elements
        long startTime = System.currentTimeMillis();
        for (int i : addNumbers) {
            bst.add(i);
        }
        long endTime = System.currentTimeMillis();
        System.out.printf("ADD_TEST:%.6f%n", (endTime - startTime) / 1000.0);

        // Check elements
        startTime = System.currentTimeMillis();
        for (int i : checkNumbers) {
            bst.contain(i);
        }
        endTime = System.currentTimeMillis();
        System.out.printf("CHECK_TEST:%.6f%n", (endTime - startTime) / 1000.0);

        // Len elements
        startTime = System.currentTimeMillis();
        for (int i = 0; i < 10; i++) {
            bst.length();
        }
        endTime = System.currentTimeMillis();
        System.out.printf("LEN_TEST:%.6f%n", (endTime - startTime) / 10000.0);

        // Height elements
        startTime = System.currentTimeMillis();
        for (int i = 0; i < 10; i++) {
            bst.height();
        }
        endTime = System.currentTimeMillis();
        System.out.printf("HEIGHT_TEST:%.6f%n", (endTime - startTime) / 10000.0);

        System.out.printf("VALIDATION:%d:%d%n", bst.length(), bst.height());
    }

    private static List<Integer> getNumbers(String path) throws IOException {
        String content = new String(Files.readAllBytes(Paths.get(path)));
        return Arrays.stream(content.split("\\s+"))
                     .map(Integer::valueOf)
                     .collect(Collectors.toList());
    }
}

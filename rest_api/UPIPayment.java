@FunctionalInterface
public interface UPIPayment {
    String doPayment(String source, String dest);

    default double getScratchScard() {
        return new Random().nextDouble();
    }

    static String datePatterns(String patterns) {
        SimpleDateFormat.dateFormat = new SimpleDateFormat(patterns);
        return dateFormat.foramt(new Data());
    }
}
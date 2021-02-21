class Main {

    static void testJourney(String fileName) {
        TravelLog travelLog = new TravelLog();

        Environment env = new Environment(fileName);
        Ship santaMaria = new Ship(env, travelLog);

        santaMaria.run();

        System.out.println(env.getVisitedHabors().length);
        System.out.println(travelLog);
    }

    public static void main(String[] args) {
        for (int i = 0; i < args.length; i++) {
            testJourney(args[i]);
        }
    }
}

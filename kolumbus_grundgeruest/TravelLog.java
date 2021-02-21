import java.util.ArrayList;
import java.util.List;

public class TravelLog {

    private List<IntPair> coordinateHistory = new ArrayList<>();

    public void logShipCoordinates(IntPair nextPosition) {
        this.coordinateHistory.add(nextPosition);
    }

    public String toString() {
        String result = "";
        for (IntPair c : coordinateHistory) {
            result += c.toString() + ",";
        }
        return result;
    }
}

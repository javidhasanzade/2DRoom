package linesTest;

public class Line {

    public Point start;
    public Point end;

    public Line() {
        start = new Point();
        end = new Point();
    }

    public Line(Point start, Point end) {
        this.start = start;
        this.end = end;
    }

    @Override
    public String toString() {
        return "Line : " + Main.lines.indexOf(this) + " {" +
                "start=" + start +
                ", end=" + end +
                '}';
    }
}

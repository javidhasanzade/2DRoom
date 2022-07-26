package linesTest;

import java.util.*;

public class Main {

    static List<Line> lines = new LinkedList<>(); // Сделал статик, что бы выводить индекс

    public static void main(String[] args) {

        // Line Input
        lines.add(new Line(new Point(-3, 0), new Point(-1, 2)));
        lines.add(new Line(new Point(0, 2), new Point(2, 2)));
        lines.add(new Line(new Point(4, 0), new Point(4, 4)));
        lines.add(new Line(new Point(1, 3), new Point(3, 3)));
        lines.add(new Line(new Point(1, 4), new Point(3, 4)));
        lines.add(new Line(new Point(1, -3), new Point(3, -1)));
        lines.add(new Line(new Point(2, -3), new Point(3, -2)));
        lines.add(new Line(new Point(-4, 3), new Point(-2, 2)));
        lines.add(new Line(new Point(-3, 1), new Point(-2, 2)));
        lines.add(new Line(new Point(-4, -2), new Point(-2, -4)));

        //------------------ Start Point Input
        int inputDegree = 135;
        int XP0= 0;
        int YP0 = 0;
        //Calc degree radians
        //-------------------------------------------
        System.out.println(Solution(XP0,YP0,inputDegree,lines));
    }

    public static int getMaxDistance(Line line, int XP0,int YP0){
        int endDist = (int) Math.sqrt( Math.pow((line.end.y - YP0),2) +Math.pow((line.end.x - XP0),2));
        int stDist = (int) Math.sqrt( Math.pow((line.start.y - YP0),2) +Math.pow((line.start.x - XP0),2));
        return Math.max(endDist, stDist);
    }

    public static Line Solution(int XP0, int YP0, int inputDegree, List<Line> lines){
        float currentMin = Integer.MAX_VALUE;
        int returnId = -1;
        double degree = Math.toRadians(inputDegree);

        for (Line segment : lines) {
            int endY = segment.end.y; int stY = segment.start.y; int endX = segment.end.x; int stX = segment.start.x;
            int id = lines.indexOf(segment);

            for(float i = 0; i <= getMaxDistance(segment,XP0,YP0) * 2; i+=0.01f) {
                double XP_exact = XP0 + (i * Math.cos(degree));
                double YP_exact = YP0 + (i * Math.sin(degree));
                int YP = (int) YP_exact;
                int XP = (int) XP_exact;
                if(!(i < currentMin)){ break;}

                //Vot tut nado round delat
                float YP_exact_r = (float)Math.round(YP_exact * 100) / 100;
                float XP_exact_r = (float)Math.round(XP_exact * 100) / 100;
                boolean vertCond = YP_exact_r <= Math.max(stY,endY) && YP_exact_r >= Math.min(stY,endY);
                boolean horCond = XP_exact_r <= Math.max(stX,endX) && XP_exact_r >= Math.min(stX,endX);
                boolean curveCond = vertCond && horCond;

                System.out.println("YP = " + YP + "YP_exact = {"+ YP_exact + "} YP_exact_r = {" + YP_exact_r + "}");

                if(endX == stX) {
                    if(XP == stX) {
                        if(!vertCond){continue;}
                        currentMin = i; returnId = id; break;
                    }
                }
                else if (endY == stY) {
                    if(YP == stY){
                        if(!horCond){continue;}
                        currentMin = i; returnId = id; break;
                    }
                }
                else if (YP_exact_r == ((float)(endY - stY) / (endX-stX)) * XP_exact_r + (endY - ((float)(endY - stY) / (endX-stX)) * endX))
                {
                    if(!curveCond) {continue;}
                    currentMin = i; returnId = id; break;
                }
            }
        }
        //throws Index Out Of Bounds Exception
        return lines.get(returnId);
    }

}

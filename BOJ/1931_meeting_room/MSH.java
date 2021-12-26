import java.io.*;
import java.util.*;

class Meeting implements Comparable<Meeting> {
	public int start;
	public int end;

	public Meeting (int start, int end) {
		this.start = start;
		this.end = end;
	}

	@Override
	public int compareTo (Meeting o) {

		return this.end < o.end ? -1 : this.end > o.end ? 1 : this.start < o.start ? -1 : this.start > o.start ? 1 : 0;
	}
}

public class MSH {

	static int findNextMeeting (Meeting[] meetings, int startIdx, int currEnd) {

		int idx = -1;

		if (startIdx == meetings.length)
			return idx;

		for (int i = startIdx; i < meetings.length; i++) {
			if (meetings[i].start >= currEnd) {
				idx = i;
				break;
			}
		}

		return idx;
	}

	static int solution (Meeting[] meetings, int N) {

		Arrays.sort(meetings);
		int answer = 1;
		int nextIdx = 0;
		int startIdx = 1;
		int currEnd = meetings[0].end;

		while (nextIdx != -1) {

			nextIdx = findNextMeeting (meetings, startIdx, currEnd);

			if (nextIdx != -1) {
				answer++;
				startIdx = nextIdx + 1;
				currEnd = meetings[nextIdx].end;
			}

		}

		return answer;
	}

	public static void main (String args[]) {

		BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        StringTokenizer st = null;

        try {
	        int N = Integer.parseInt(br.readLine());

	        Meeting[] meetings = new Meeting[N];
	        for (int i = 0; i < N; i++) {
		        st = new StringTokenizer(br.readLine());
	            int start = Integer.parseInt(st.nextToken());
	            int end = Integer.parseInt(st.nextToken());
		        meetings[i] = new Meeting(start, end);
	        }

	        System.out.println(solution(meetings, N));
	    } catch (Exception e) {
	    	e.printStackTrace();
	    }
	}
}
/*
1. Current solution exceeds time limit.
2. Sort of a DP, but not much optimized.
3. I guess I am still more familiar with Java than C++ :(
*/
import java.util.*;

class Sequence {
    public List<Integer> elem;
    public List<Integer> pos;
    public Sequence (List<Integer> elem, List<Integer> pos) {
        this.elem = elem;
        this.pos = pos;
    }

    @Override
    public boolean equals(Object o) {
        if (this == o) return true;
        if (o == null || getClass() != o.getClass()) return false;
        Sequence sequence = (Sequence) o;
        return elem.equals(sequence.elem) && pos.equals(sequence.pos);
    }

    @Override
    public int hashCode() {
        return Objects.hash(elem, pos);
    }

    @Override
    public String toString() {
        String retVal = "";
        for (int i = 0; i < elem.size(); i++) {
            retVal += "(" + elem.get(i) + ", " + pos.get(i) + ")";
        }
        return retVal;
    }
}

class Solution {

    public List<Integer> findNextElemIndices(int[] nums, int lastPos) {
        List<Integer> ret = new ArrayList<>();
        if (lastPos == nums.length - 1) { return ret; }
        for (int i = lastPos + 1; i < nums.length; i++) {
            if (nums[i] > nums[lastPos]) {
                ret.add(i);
            }
        }
        return ret;
    }

    public int findNumberOfLIS(int[] nums) {

        int n = nums.length;
        if (n == 1) { return 1; }

        List<Map<Sequence, Integer>> seqList = new ArrayList<>();;
        Map<Sequence, Integer> singleElemSeqMap = new HashMap<>();
        for (int i = 0; i < n; i++) {
            List<Integer> elemList = new ArrayList<>();
            List<Integer> posList = new ArrayList<>();
            elemList.add(nums[i]);
            posList.add(i);
            Sequence s = new Sequence(elemList, posList);
            singleElemSeqMap.put(s, singleElemSeqMap.getOrDefault(s, 0) + 1);
        }
        seqList.add(singleElemSeqMap);

        for (int len = 2; len <= n; len++) {
            Map<Sequence, Integer> prevSeqMap = seqList.get(len - 2);
            Map<Sequence, Integer> nextSeqMap = new HashMap<>();

            for (Sequence seq : prevSeqMap.keySet()) {
                List<Integer> nextElemIndices = findNextElemIndices(nums, seq.pos.get(seq.pos.size() - 1));
                if (nextElemIndices.size() != 0) {
                    for (int i = 0; i < nextElemIndices.size(); i++) {
                        List<Integer> nextElemList = new ArrayList<>();
                        List<Integer> nextPosList = new ArrayList<>();
                        for (int j = 0; j < seq.elem.size(); j++) {
                            nextElemList.add(seq.elem.get(j));
                            nextPosList.add(seq.pos.get(j));
                        }
                        nextElemList.add(nums[nextElemIndices.get(i)]);
                        nextPosList.add(nextElemIndices.get(i));
                        Sequence nextSeq = new Sequence(nextElemList, nextPosList);
                        nextSeqMap.put(nextSeq, nextSeqMap.getOrDefault(nextSeq, 0) + 1);
                    }
                }
            }

            if (nextSeqMap.size() != 0) { seqList.add(nextSeqMap); }
            else { break; }
        }

        Map<Sequence, Integer> LISMap = seqList.get(seqList.size() - 1);
        int answer = 0;
        for (Sequence seq : LISMap.keySet())
            answer += LISMap.get(seq);

        return answer;
    }
}

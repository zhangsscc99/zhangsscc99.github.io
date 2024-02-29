public class Solution {
    public int ladderLength(String beginWord, String endWord, List<String> wordList) {
        Set<String> wordSet = new HashSet<>(wordlist);
        if (wordSet.size() == 0 || wordSet.contains(endWord)) {
            return 0;
        }
    }
    /*先建立一个wordSet 如果size是0或者是没有endword 那么就会return 0
    我们需要移除第一个元素
    然后建立一个queue和一个visited。visited防止多个节点过来重复对连接到的节点进行重复操作
    queue用于正常的dfs
    step就类似于depth。用queue的size遍历 把每个词都要改一个letter 如果是endword那就是返回数值。
    判断endword：把现在的charArray对每个词汇都会进行a到z的更改 看是否能到达nextNode。
    没有visited过但是wordset里面有 那就继续进行往下的bfs。前提不是endword 先考虑是不是endword。
    一旦endword了就是true。 */
    wordSet.remove(beginWord);
    Queue<String> queue = new LinkedList<>();
    queue.offer(beginWord);
    Set<String> visited = new HashSet<>();
    visited.add(beginWord);

    Set<String> wordSet = new HashSet<>(wordList);
    if (wordSet.size() == 0 || !wordSet.contains(endWord)) {
        return 0;
    }
    wordSet.remove(beginWord);

    Queue<String> queue = new LinkedList<>();
    queue.offer(beginWord);
    Set<String> visited = new HashSet<>();
    visited.add(beginWord);

    int step = 2;
    while (!queue.isEmpty()) {
        int currentSize = queue.size();
        for (int i = 0; i < currentSize; i++) {
            String currentWord = queue.poll();
            if (changeWordEveryOneLetter(currentWord, endWord, queue, visited, wordSet)) {
                return step;
            }
        }
        step++;
    }
    return 0;
}
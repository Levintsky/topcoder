# Back Tracking

## Partition Array
- Typical questions:
	- LC-473: Matchsticks to Square (Special case of 698, 4 partition)
    - Trick 0: greedy fit always ok? (fit 1 edge, safely remove, then fit the 2nd)
    - Trick 1: only need to fit 3 rather than 4?
	- LC-698: Partition to K Equal Sum Subsets
    - Greedy doesn't really work. counter example: [10,10,10,7,7,7,7,7,7,6,6,6], 3

## Traversal
- Typical questions:
	- LC-489: Robot Room Cleaner
	- **LC-488**: Zuma Game

## Subsets, Permutations, Combination Sum, Palindrome Partitioning
- Subsets
	- LC-78: Subsets (input: distinct nums = [1,2,3], outputs: [[3], [1,2,3], ...])
  ```python
  def subsets(nums):
      result = []
      nums.sort()

      def backtrack(tmpList, idx):
          newList = [item for item in tmpList]
          result.add(newList)
          for i in range(idx, len(nums)):
              tmpList.append(nums[i])
              backtrack(tmpList, i+1)
              _ = tmpList.pop()
  
      backtrack([], 0)
      return result
  ```

	- LC-90: Subsets II (same as 78, input nums can contain duplicates)
  ```python
  def subsetsWithDup(nums):
      result = []
      nums.sort()

      def backtrack(tmpList, idx):
          newList = [item for item in tmpList]
          result.append(newList)
          for i in range(idx, len(nums)):
              if i > idx and nums[i] == nums[i-1]:
                  continue
              tmpList.append(nums[i])
              backtrack(tmpList, i+1)
              _ = tmpList.pop()

      backtrack([], 0)
      return result
  ```
- Permutation:
	- LC-46: Permutations
  ```java
  public List<List<Integer>> permute(int[] nums) {
     List<List<Integer>> list = new ArrayList<>();
     // Arrays.sort(nums); // not necessary
     backtrack(list, new ArrayList<>(), nums);
     return list;
  }

  private void backtrack(List<List<Integer>> list, List<Integer> tempList, int [] nums){
     if(tempList.size() == nums.length){
        list.add(new ArrayList<>(tempList));
     } else{
        for(int i = 0; i < nums.length; i++){ 
           if(tempList.contains(nums[i])) continue; // element already exists, skip
           tempList.add(nums[i]);
           backtrack(list, tempList, nums);
           tempList.remove(tempList.size() - 1);
        }
     }
  }
  ```

	- LC-47: Permutations II
  ```java
  public List<List<Integer>> permuteUnique(int[] nums) {
      List<List<Integer>> list = new ArrayList<>();
      Arrays.sort(nums);
      backtrack(list, new ArrayList<>(), nums, new boolean[nums.length]);
      return list;
  }

  private void backtrack(List<List<Integer>> list, List<Integer> tempList, int [] nums, boolean [] used){
      if(tempList.size() == nums.length){
          list.add(new ArrayList<>(tempList));
      } else{
          for(int i = 0; i < nums.length; i++){
              if(used[i] || i > 0 && nums[i] == nums[i-1] && !used[i - 1]) continue;
              used[i] = true; 
              tempList.add(nums[i]);
              backtrack(list, tempList, nums, used);
              used[i] = false; 
              tempList.remove(tempList.size() - 1);
          }
      }
  }
  ```

- Combination Sum:
	- LC-39: Combination Sum
  ```java
  public List<List<Integer>> combinationSum(int[] nums, int target) {
      List<List<Integer>> list = new ArrayList<>();
      Arrays.sort(nums);
      backtrack(list, new ArrayList<>(), nums, target, 0);
      return list;
  }

  private void backtrack(List<List<Integer>> list, List<Integer> tempList, int [] nums, int remain, int start){
      if(remain < 0) return;
      else if(remain == 0) list.add(new ArrayList<>(tempList));
      else{ 
          for(int i = start; i < nums.length; i++){
              tempList.add(nums[i]);
              backtrack(list, tempList, nums, remain - nums[i], i); // not i + 1 because we can reuse same elements
              tempList.remove(tempList.size() - 1);
          }
      }
  }
  ```

	- LC-40: Combination Sum II
  ```java
  public List<List<Integer>> combinationSum2(int[] nums, int target) {
      List<List<Integer>> list = new ArrayList<>();
      Arrays.sort(nums);
      backtrack(list, new ArrayList<>(), nums, target, 0);
      return list;
      
  }

  private void backtrack(List<List<Integer>> list, List<Integer> tempList, int [] nums, int remain, int start){
      if(remain < 0) return;
      else if(remain == 0) list.add(new ArrayList<>(tempList));
      else{
          for(int i = start; i < nums.length; i++){
              if(i > start && nums[i] == nums[i-1]) continue; // skip duplicates
              tempList.add(nums[i]);
              backtrack(list, tempList, nums, remain - nums[i], i + 1);
              tempList.remove(tempList.size() - 1); 
          }
      }
  }
  ```

- Palindrome:
	- LC-131: Palindrome Partitioning
  ```java
  public List<List<String>> partition(String s) {
     List<List<String>> list = new ArrayList<>();
     backtrack(list, new ArrayList<>(), s, 0);
     return list;
  }

  public void backtrack(List<List<String>> list, List<String> tempList, String s, int start){
     if(start == s.length())
        list.add(new ArrayList<>(tempList));
     else{
        for(int i = start; i < s.length(); i++){
           if(isPalindrome(s, start, i)){
              tempList.add(s.substring(start, i + 1));
              backtrack(list, tempList, s, i + 1);
              tempList.remove(tempList.size() - 1);
           }
        }
     }
  }

  public boolean isPalindrome(String s, int low, int high){
     while(low < high)
        if(s.charAt(low++) != s.charAt(high--)) return false;
     return true;
  } 
  ```
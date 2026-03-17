
* **1️⃣ The Setup:** Create a `start` pointer at the first index `0` and an `end` pointer at the last index `len(nums) - 1`.
* **2️⃣ The Loop:** Keep searching as long as the `start` pointer hasn't crossed over the `end` pointer.
* **3️⃣ The Middle:** Find the middle index by adding `start` and `end` together, then floor-dividing by 2 (`// 2`).
* **4️⃣ The Jackpot:** If the number at the `mid` index is exactly your `target`, you found it—return the `mid` index!
* **5️⃣ Go Right:** If the `target` is bigger than the middle number, the answer must be on the right, so move `start` to `mid + 1`.
* **6️⃣ Go Left:** If the `target` is smaller than the middle number, the answer must be on the left, so move `end` to `mid - 1`.
* **7️⃣ Game Over:** If the loop completely finishes and you never found the number, it doesn't exist, so return `-1`.

---

## 💻 The Final Python Code

```python
class Solution(object):
    def search(self, nums, target):
        
        # 1️⃣ The Setup
        start = 0 
        end = len(nums) - 1

        # 2️⃣ The Loop
        while start <= end:
            
            # 3️⃣ The Middle
            mid = (start + end) // 2
            
            # 4️⃣ The Jackpot
            if nums[mid] == target:
                return mid
                
            # 5️⃣ Go Right
            elif target > nums[mid]:
                start = mid + 1
                
            # 6️⃣ Go Left
            else: 
                end = mid - 1
        
        # 7️⃣ Game Over
        return -1
```

---

## ⚡ Complexity
* ⏳ **Time Complexity:** $O(\log n)$ — Because we cut the array in half every single time, it is incredibly fast even for massive datasets.
* 💾 **Space Complexity:** $O(1)$ — We only use three simple integer variables (`start`, `end`, and `mid`), taking up almost zero extra memory.


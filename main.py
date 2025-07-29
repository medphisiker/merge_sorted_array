from typing import List


class Solution:
    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        """
        Функция возвращает объединение двух отсортированных массивов.
        
        Args:
            nums1: List[int] - первый массив с m не нулевых первых элементов.
                длинны m+n. Остальные элементы равны 0 и представляют 
                собой места для записи.
            m: количество элементов массива.
            nums2: List[int] - второй массив с n элементов.
            n: количество элементов во втором массиве.
            
        Временная сложность: O(m + n) - каждый элемент из обоих массивов
            обрабатывается ровно один раз.
        Пространственная сложность: O(1) - используется только константное
            дополнительное пространство для указателей.
        """
        # Указатели на последние элементы валидных частей nums1 и nums2
        pointer_1 = m - 1
        pointer_2 = n - 1

        # Общая позиция для вставки элементов в nums1
        insert_pos = m + n - 1

        while pointer_2 >= 0 and pointer_1 >= 0:
            if nums1[pointer_1] > nums2[pointer_2]:
                nums1[insert_pos] = nums1[pointer_1]
                # уменьшаем указатель
                pointer_1 -= 1

            else:
                nums1[insert_pos] = nums2[pointer_2]
                # уменьшаем указатель
                pointer_2 -= 1
                
            insert_pos -= 1

        while pointer_1 >= 0:
            nums1[insert_pos] = nums1[pointer_1]
            pointer_1 -= 1
            insert_pos -= 1

        while pointer_2 >= 0:
            nums1[insert_pos] = nums2[pointer_2]
            pointer_2 -= 1
            insert_pos -= 1


if __name__ == "__main__":
    solution = Solution()
    nums1 = [1, 2, 3, 0, 0, 0]
    m = 3
    nums2 = [2, 5, 6]
    n = 3
    solution.merge(nums1, m, nums2, n)
    print(nums1)

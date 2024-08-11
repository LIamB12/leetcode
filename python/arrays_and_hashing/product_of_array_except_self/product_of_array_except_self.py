class Solution:
    def productExceptSelf(self, nums): 
        postfix_products = [1] * len(nums)
        prefix_products = [1] * len(nums)

        current_product = 1

        for index, num in enumerate(nums):
            if index == 0:
                continue
            prefix_products[index] = current_product * nums[index - 1]
            current_product = prefix_products[index]

        current_product = 1 
        reversed = nums[::-1]

        for index, num in enumerate(reversed):
            if index == 0:
                continue
            postfix_products[index] = current_product * reversed[index - 1]
            current_product = postfix_products[index]
            
        postfix_products.reverse()

        combined_products = [prefix_products[i] * postfix_products[i] for i in range(len(nums))]
        return combined_products

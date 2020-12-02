class Solution:
    def minimumEffort(self, tasks):
        diff_dict = {}
        for item in tasks:
            diff = item[1] - item[0]
            if diff not in diff_dict:
                diff_dict[diff] = [item]
            else:
                diff_dict[diff].append(item)

        keys = sorted(diff_dict.keys())

        print(diff_dict)
        new_list = []
        for i in range(len(keys)-1, -1, -1):
            new_list += diff_dict[keys[i]]

        print(new_list)
        total_energy = new_list[0][1]
        left_energy = new_list[0][1]
        for item in new_list:
            if left_energy < item[1]:
                required_more = item[1] - left_energy
                left_energy += required_more
                total_energy += required_more
            
            left_energy = left_energy - item[0]

        return total_energy


s = Solution()
tasks = [[1,7],[2,8],[3,9],[4,10],[5,11],[6,12]]

print(s.minimumEffort(tasks))

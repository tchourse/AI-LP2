def jobScheduling(jobs):
    jobs.sort(key=lambda x: (-x[1], x[0]))  # Sort jobs by deadline and profit in descending order
    sequence, total_profit = [], 0
    for job in jobs:
        time_slot = job[0]
        while sequence and sequence[-1][1] > time_slot:
            time_slot = sequence[-1][1] + 1
        sequence.append((job[0], time_slot, job[2]))
        total_profit += job[2]
    return sequence, total_profit

jobs = [(1, 4, 20), (2, 2, 100), (3, 1, 40), (4, 3, 35)]
sequence, total_profit = jobScheduling(jobs)
print("Following is maximum profit sequence of jobs:")
for job in sequence:
    print(job[0], end=" ")
print("\nTotal Profit:", total_profit)


class job:
    def __init__(self, id, deadline, profit):
        self.id = id
        self.deadline = deadline
        self.profit = profit







"""class Solution:
    def jobScheduling(self, jobs):
        jobs.sort(key=lambda x: x.profit, reverse=True)
        maxi = jobs[0].deadline
        for i in range(1, len(jobs)):
            maxi = max(maxi, jobs[i].deadline)

        slot = [-1] * (maxi + 1)
        countJobs = 0
        jobProfit = 0

        for i in range(len(jobs)):
            for j in range(jobs[i].deadline, 0, -1):
                if slot[j] == -1:
                    slot[j] = i
                    countJobs += 1
                    jobProfit += jobs[i].profit
                    break

        return countJobs, jobProfit



if __name__ == "__main__":
    jobs = [job(1, 4, 20), job(2, 1, 10), job(3, 2, 40), job(4, 2, 30)]
    count, profit = Solution().jobScheduling(jobs)
    print("Profit =" ,profit)
    print("No of jobs done =", count)"""

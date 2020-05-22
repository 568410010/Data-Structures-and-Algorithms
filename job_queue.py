# python3

from collections import namedtuple

AssignedJob = namedtuple("AssignedJob", ["worker", "started_at"])


def assign_jobs(n_workers, jobs):
    # TODO: replace this code with a faster algorithm.
    import heapq
    ans = []
    stack = [(0, i) for i in range(n_workers)]
    while jobs:
        jobtime = jobs.pop(0)
        time, idx = heapq.heappop(stack)
        ans.append(AssignedJob(idx, time))
        heapq.heappush(stack, (time+jobtime, idx))

    return ans


def main():
    n_workers, n_jobs = map(int, input().split())
    jobs = list(map(int, input().split()))
    assert len(jobs) == n_jobs

    assigned_jobs = assign_jobs(n_workers, jobs)

    for job in assigned_jobs:
        print(job.worker, job.started_at)


if __name__ == "__main__":
    main()

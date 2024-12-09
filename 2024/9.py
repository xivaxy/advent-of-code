from aocd import data, submit

s='''2333133121414131402'''
test = False
if test:
    data=s
ans=0
nums = list(map(int, data))
locs = [0]*len(nums)
for i in range(len(nums)-1):
    locs[i+1] = locs[i]+nums[i]
a=[-1]*sum(nums)
ptr = 0
id = 0
for i in range(len(nums)):
    if i%2==0:
        a[ptr:ptr+nums[i]] = [id]*nums[i]
        id += 1
    ptr += nums[i]

# beg = 0
# while a[beg] != -1:
#     beg += 1
# for i in range(len(a)-1, -1, -1):
#     if a[i] != -1:
#         a[beg] = a[i]
#         a[i] = -1
#         while a[beg] != -1:
#             beg += 1
#     if beg>=i:
#         break

# print(f"{len(nums)=}\n{nums=}\n{locs=}\n{a=}")

min_id = 1
for i in range(len(nums)-1, -1, -2):
    for j in range(min_id, i, 2):
        if nums[j]>=nums[i]:
            # move nums[i] to nums[j]
            nums[j] -= nums[i]
            a[locs[j]:locs[j]+nums[i]] = [a[locs[i]]]*nums[i]
            assert a[locs[i]] == i//2, (i,j, a[locs[i]], i//2)
            a[locs[i]:locs[i]+nums[i]] = [-1]*nums[i]
            locs[j] += nums[i]
            if nums[j] == 0 and j==min_id:
                min_id += 2
            break
        if nums[j] == 0 and j==min_id:
            min_id += 2

for i in range(len(a)):
    if a[i] >=0:
        ans += i*a[i]
    

print(ans)
if not test:
    submit(ans)
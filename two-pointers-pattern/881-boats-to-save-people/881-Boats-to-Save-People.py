class Solution:
    def numRescueBoats(self, people: list[int], limit: int) -> int:

        people.sort()
        i=0
        j=len(people)-1
        count = 0

        while i<=j:
            sum = people[i]+people[j]

            if sum > limit:
                j-=1
            elif sum <= limit:
                i+=1
                j-=1

            count+=1

        return count

#here you needded help in understanding that when the sum<= limit, then both of them needs to be put togather in a boat, as only 2 people can come in a single boat
def find_grants_cap(grantsArray, newBudget):
  #save the length of our original grants array so we can iterate through it later on
  n = len(grantsArray)
  #sort our grantsArray in decreasing order
  grantsArray.sort(reverse = True)
  #calculate the surplus in budget we have to cut
  surplus = sum(grantsArray) - newBudget
  #for the case where the newBudget is 0, append 0 to our grants array to signify no grants get anything
  grantsArray.append(0)
  #if our new budget is greater than or equal to our current budget simply return largest grant as cap
  if surplus <= 0:
    return grantsArray[0]

  #iterate through our sorted grants array, seeing how making each grant after the first one the cap affects our surplus
  for i in range(n):
    #decrease surplus by the amount of money we save when we make each grant in decreasing order the cap by taking that much away from the grants larger than current grant we are iterating over
    surplus -= (i+1) * (grantsArray[i] - grantsArray[i+1])
    #once we have taken enough from the surplus that we cover it all we can stop iterating as we have found our lower bound
    if surplus <= 0:
      break

  #to find exact cap, add the lower bound to the extra surplus we accounted for if any divided by grants greater than the lower bound
  return grantsArray[i+1] + (-surplus/float(i+1))

# This program simualtes the backend of a ticket purchasing system

# Price per visitor is $5
# Price per member is $3.50

# You are to do the following
# 1. Identify all banned visitors with a filter call
# 2. Determine the memberships status of all applicants
# 3. Calculate the total price for all eligible visitors
# 4. For each valid visitor, return a corresponding ticket in Dictionary form
# 5. Return an error via thrown exception if applicants is empty
# Complete everything above in a function called processRequest
# Your should abstract out function as much as reasonably possible

bannedVisitors = ["Amy", "Grace", "Bruce"]
memberStatus = {
    "Ally": True,
    "David": True,
    "Brendan": False
}

request = {
    "applicants": ["Amy", "Ally", "David", "Brendan", "Zoho"]
}

allapplicants = request["applicants"]

def processRequest(request):

    result =  {
   "successfulApplicants": [],
   "bannedApplicants": [],
   "totalCost": 0,
   "tickets": []

 }

   # 1. filter call banned visitors
  
    if (not(len(allapplicants) == 0)):
       def checkBan(i):
          return (i in bannedVisitors is True)

       result["bannedApplicants"] = list(filter(checkBan, allapplicants))
   
   # 2. check applicants' membership status
       def checkMember(i):
          if (i in allapplicants):
              return memberStatus[i] == True

       def checkVisitor(i):
          if (not(i in allapplicants)):
              return memberStatus[i] == False

       Members = list(filter(checkMember, allapplicants))
       Visitors = list(filter(checkVisitor, allapplicants))
       result["successfulApplicants"] = Members + Visitors
       
   # 3. calculate total price
       totalprice = len(Members) * 3.50 + len(Visitors) * 5.00
       totalpricedisplay = "$" + str(totalprice)
       result["totalCost"] = totalpricedisplay
  
       ticket = result["tickets"]
   # 4. issue tickets
       if (i in Members): 
           ticket.append({"name": i, "membershipStatus": "Member", "price": "$3.50"})
      
       if (i in Visitors):
           ticket.append({"name": i, "membershipStatus": "Visitor", "price": "$5.00"})

   # 5. throw error if applicant is empty
       try:
          error =  {"error": "No applicants"}
          if len(allapplicants) == 0:
              raise EmptyApplicant(error)
       except EmptyApplicant:
            return error
    
    return result


print(processRequest(request))

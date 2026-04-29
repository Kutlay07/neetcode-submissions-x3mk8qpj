class Solution:
    def numUniqueEmails(self, emails: List[str]) -> int:

        ans = set()
        for email in emails:
            local,domain = email.split("@")

            local = local.replace(".","")
            if "+" in local:
                local = local[:local.index("+")]
            ans.add(local+"@"+domain)

        return len(ans)
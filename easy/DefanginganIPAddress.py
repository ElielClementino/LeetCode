# https://leetcode.com/problems/defanging-an-ip-address/
address = "1.1.1.1"
new_address = ""
def defangIPaddr(address: str) -> str:
        new_address = address.replace(".", "[.]")
        return new_address

new_address = defangIPaddr(address)
print(new_address)
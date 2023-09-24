import dns.resolver

res = dns.resolver.Resolver()

file = open("/home/kali/Documents/dnsbrute/wordlist.txt", "r")
subdomains = file.read().splitlines()

target = input("Your target: ")

for subdomain in subdomains:


		try:
			sub_target = subdomain + "." + target

			result = res.resolve(target, "A")

			for ip in result:
				print(sub_target, "->", ip)

		except: 

			print("Unexpect error, please try again.")		
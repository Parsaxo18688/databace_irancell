import requests
import colorama
userID = input(colorama.Fore.GREEN+'enter the number {930,933,935,936,937,938,939} : ')
 

response = requests.get('https://ziroapi.xyz/Apis/irancell/?phone='+userID)

response.encoding = 'utf-8'
response.json()
print(colorama.Fore.CYAN+'{ "craeted by : @e_l_f_6_6_6"'+json.dumps(response.json(), indent=4, separators=(" , ", " ==> :  ")))
print('''
      
      
         my channel : @elf-security_cyber       }   ''')

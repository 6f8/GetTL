import requests, random, string, re
from user_agent import generate_user_agent

class Google:

    def __init__(self):
        pass
    
    def TL(self):
        try:
            
            self.ExE  = ''.join(random.choice(string.ascii_lowercase) for _ in range(random.randint(6, 8)))
            self.ExE_ = ''.join(random.choice(string.ascii_lowercase) for _ in range(random.randint(3, 8)))
            self.Tar  = ''.join(random.choice(string.ascii_lowercase) for _ in range(random.randint(15, 30)))
            self.Headers = {"accept": "*/*","accept-language": "ar-YE,ar;q=0.9,en-IQ;q=0.8,en;q=0.7,en-US;q=0.6","content-type": "application/x-www-form-urlencoded;charset=UTF-8","google-accounts-xsrf": "1","sec-ch-ua": "\"Not)A;Brand\";v=\"24\", \"Chromium\";v=\"116\"","sec-ch-ua-arch": "\"\"","sec-ch-ua-bitness": "\"\"","sec-ch-ua-full-version": "\"116.0.5845.72\"","sec-ch-ua-full-version-list": "\"Not)A;Brand\";v=\"24.0.0.0\", \"Chromium\";v=\"116.0.5845.72\"","sec-ch-ua-mobile": "?1","sec-ch-ua-model": "\"ANY-LX2\"","sec-ch-ua-platform": "\"Android\"","sec-ch-ua-platform-version": "\"13.0.0\"","sec-ch-ua-wow64": "?0","sec-fetch-dest": "empty","sec-fetch-mode": "cors","sec-fetch-site": "same-origin","x-chrome-connected": "source=Chrome,eligible_for_consistency=true","x-client-data": "CJjbygE=","x-same-domain": "1","Referrer-Policy": "strict-origin-when-cross-origin",'user-agent': str(generate_user_agent())}
            self.Response = requests.get('https://accounts.google.com/signin/v2/usernamerecovery?flowName=GlifWebSignIn&flowEntry=ServiceLogin&hl=en-GB',headers=self.Headers)
            self.Tarr = re.search(r'data-initial-setup-data="%.@.null,null,null,null,null,null,null,null,null,&quot;(.*?)&quot;,null,null,null,&quot;(.*?)&', self.Response.text).group(2)
            self.Cookies = {'__Host-GAPS': self.Tar}
            self.Headers = {'authority': 'accounts.google.com','accept': '*/*','accept-language': 'en-US,en;q=0.9','content-type': 'application/x-www-form-urlencoded;charset=UTF-8','google-accounts-xsrf': '1','origin': 'https://accounts.google.com','referer': 'https://accounts.google.com/signup/v2/createaccount?service=mail&continue=https%3A%2F%2Fmail.google.com%2Fmail%2Fu%2F0%2F&parent_directed=true&theme=mn&ddm=0&flowName=GlifWebSignIn&flowEntry=SignUp','user-agent': generate_user_agent(),}
            self.Data = {'f.req': '["' + self.Tarr + '","' + self.ExE + '","' + self.ExE_ + '","' + self.ExE + '","' + self.ExE_ +'",0,0,null,null,"web-glif-signup",0,null,1,[],1]','deviceinfo':'[null,null,null,null,null,"NL",null,null,null,"GlifWebSignIn",null,[],null,null,null,null,2,null,0,1,"",null,null,2,2]',}
            self.Rresponse = requests.post('https://accounts.google.com/_/signup/validatepersonaldetails',cookies=self.Cookies,headers=self.Headers,data=self.Data)

            TL = str(self.Rresponse.text).split('",null,"')[1].split('"')[0] ; Cookies = self.Rresponse.cookies.get_dict()['__Host-GAPS']
            print(TL,Cookies)

        except Exception as e:
            self.TL()

Google().TL()

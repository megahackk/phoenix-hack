import time
import os


try:
	import vk_api
except:
	print("[Автоматическая установка модуля...]")
	os.system("pip install vk_api")
	i="[Модуль установлен]"
else:
	i="[Модуль уже установлен]"


bg=0
sm=99999
count=1


def stan(a):
	d=len(str(a))
	if d==0:
		aw="00000"
	elif d==1:
		aw="0000"+str(a)
	elif d==2:
		aw="000"+str(a)
	elif d==3:
		aw="00"+str(a)
	elif d==4:
		aw="0"+str(a)
	elif d==5:
		aw=str(a)
	else:
		pass
	return aw





def send(text):
	global count
	vk.messages.send(peer_id=-94631511,message=text, random_id=count )
	count=count+1





def  bgi():
	global bg
	global bgh
	try:
		bgh=stan(bg)
		time.sleep(9)
		send(bgh)
	except:
		print("Капча на цикл возрастания-[Ждем 3 минуты...]")
		time.sleep(180)
		bgi()
	else:
		bg=bg+1
		bgh=stan(bg)
		smi()


def smi():
	global sm
	try:
		time.sleep(9)
		send(sm)
	except:
		print("Капча на цикл убывания-[Ждем 3 минуты...]")
		time.sleep(180)
		smi()
	else:
		sm=sm-1
		bgi()



def get_tok():
	global vk
	global i
	tok=input("Введите токен: ")
	ses=vk_api.VkApi(token=tok)
	vk=ses.get_api()
	i="[Токен задан]"
	main()

def start():
	print("[Работа...]")
	bgi()


def cont():
	global bg
	global sm
	global i
	bg=int(input("Введите меньший параметр bg- "))
	sm=int(input("Введите больший параметр sm- "))
	i=("[Параметры установлены со значениями sm="+str(sm)+" bg="+str(bg)+"]")
	main()


def main():
	global i
	os.system('cls' if os.name=='nt' else 'clear')
	print("Version-1")
	print("")
	print(i)
	print('')
	print("!!![Перед использованием советую посмотреть инструкцию]!!!")
	print("1.{Ввести токен}")
	print("2.{Начать перебор}")
	print("3.{Контактные данные}")
	print("4.{Обновление программы}")
	print("5.{Продолжение перебора-установка вводимых параметров}")
	func=input("Что будем делать: ")
	if func=='1':
		get_tok()
	elif func=='2':
		start()
	elif func=='3':
		i="VK- https://vk.com/danila_tkachenka \nYouTube- https://www.youtube.com/channel/UCC0-w64BrjxtcFfLE9wAJBQ/featured\n"
		main()
	elif func=='4':
		os.system("cd && rm -rf phoenix-hack && git clone https://github.com/megahackk/phoenix-hack && cd phoenix-hack && python3 numbrut.py")
	elif func=='5':
		cont()
	else:
		print("[Неверный ввод]")
		main()
main()


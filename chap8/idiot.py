from urllib import response
import pyinputplus as pyip

while True:
    prompt = 'バカを何時間も忙しくさせておく方法を知りたいですか?\n'
    response = pyip.inputYesNo(prompt)

    if response == 'no':
        break
print('ありがとう、ごきげんよう。')
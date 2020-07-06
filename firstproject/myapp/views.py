from django.shortcuts import render

def main(request):
    return render(request,'main.html')

def result(request):
    full_text = request.GET['totaltext']
    word_num = full_text.split()

    word_dict={}
    for word in word_num:
        if word in word_dict:
            word_dict[word] +=1
        else:
            word_dict[word]=1

    return render(request,'result.html', {'total_text':full_text, 'num':len(word_num),"wordcount":word_dict.items()})
    # result의 main에서의 form형식으로 데이터를 보내주면 views.py의 GET방식으로 데이터를 보내준 것
    # textarea의 name인 totaltext를 views.py의 (문자를 가져온다)totaltext로 받아 준다 그리고 totaltext를 full_text로 넣는다
    # html에서 받을때는 key 값으로 받아야 한다

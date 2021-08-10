import requests

my_data = {'name' : 'Abhishek', 'email': "ab25chandra@gmail.com"}

r = requests.post('https://tryphp.w3schools.com/showphp.php?filename=demo_form_post', data=my_data)

f = open("requests_form.html", "w+")

f.write(r.text)
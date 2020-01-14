# food-truck

We have created the user and truck model and its interface through Django and we used sqlite as our database as postgres had issues with its username and password for our teammates. We used redis to store the order and its status and used grpc to connect between Django and redis. 
To run the project locally, assuming you are running on windows environment, open redis-2.4.5 folder and select either 32bit or 64 bit folder depending on your machine. Then double click redis-server.exe to start redis server. 
Then open CMD and cd to mysite/mysite. Type python order_server.py. 
Open another CMD and cd to mysite/mysite, then type python manage.py runserver.
Open a tab in chrome and type http://127.0.0.1:8000/polls/. This will lead to main web page. 

You can place order under place your order by choosing a menu and writing your name and submit. 
When you press back button, you will see that update order status and get order status list has been updated with your latest order. 
By clicking your name and pressing submit on get order status, you can see your order status. 
By clicking username and press submit on update order status, you can update that person’s order status.
Once you update the user, you can click the specific user on get order status to see your order status updated.

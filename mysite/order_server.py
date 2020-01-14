import order_pb2_grpc
import order_pb2
import redis
import time





from concurrent import futures
import logging

import grpc

r = redis.Redis(
    host = "localhost",
    port = 6379,
    password = "")

class Order(order_pb2_grpc.OrderServicer):

	def GetState(self, request, context):
		order = str(request.orderID)
		stateNum = r.exists(order)
		output = "Your order "


		if stateNum == 0:
			output = "Sorry, order does not exist."
			timeSince = ""

		else:
			state = str(r.get(order))
			# state = str(r.hget(order, "state"))
			state = state[2:len(state)-1]
			# timeOrdered = str(r.hget(order, "time"))
			# timeOrdered = float(timeOrdered[2: len(timeOrdered) - 1])

			if state == 'ordered':
				output += "has been placed."
			
			elif state == 'processing':
				output += "is processing and will be ready soon."

			elif state == 'finished':
				output += "is finished and has been shipped."

			else:
				output += "has been delivered."

			# diff, rem = divmod(time.time() - timeOrdered, 60)
			# timeSince = "Placed " + str(int(diff)) + "m " + str(int(rem)) + "s ago."
		

		# return order_pb2.GetReply(answer = output + '\n' + timeSince)
		return order_pb2.GetReply(answer = output)
			


	def SetState(self, request, context):
		order = str(request.orderID)
		stateNum = r.exists(order)

		if stateNum == 0:
			state = 'ordered'
			timeOrdered = time.time()
			# r.hset(order, "state", state)
			r.set(order, state)
			# r.hset(order, "time", timeOrdered)
			output = " has been placed."
			

		else:
			# state = str(r.hget(order, "state"))
			state = str(r.get(order))
			state = state[2:len(state)-1]
			# output = "State of Order " + order + " has been set to "

			
			if state == 'ordered':
				state = 'processing'
				output = "IS PROCESSING."
			
			elif state == 'processing':
				state = 'finished'
				output = "IS FINISHED AND HAS BEEN SHIPPED."

			else:
				state = 'delivered'
				output = "HAS BEEN DELIVERED."

			r.set(order, state)
			

		return order_pb2.SetReply(answer = output)




def serve():
    server = grpc.server(futures.ThreadPoolExecutor(max_workers=10))
    order_pb2_grpc.add_OrderServicer_to_server(Order(), server)
    server.add_insecure_port('[::]:50051')
    server.start()
    server.wait_for_termination()


if __name__ == '__main__':
    logging.basicConfig()
    serve()


 
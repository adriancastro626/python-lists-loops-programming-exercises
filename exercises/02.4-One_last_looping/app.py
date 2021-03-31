my_sample_list = ['Esmeralda','Kiko','Ruth','Lebron','Pedro','Maria','Lou','Fernando','Cesco','Bart','Annie']
    #               0           1       2       3       4       5       6       7       8       9       10
#Your code here:

my_sample_list[1] = "Steven"
my_sample_list[-1] = "Pepe"
my_sample_list[0] = (my_sample_list[2] + my_sample_list[4])
for x in range(len(my_sample_list)-1,-1,-1):
  print(my_sample_list[x])




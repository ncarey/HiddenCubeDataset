import time




if __name__ =='__main__':

  timedict = {}

  for para in range(1, 10):
    #para , rotations 

    cmd = "./run_param.sh {0} {1}".format(para, 200)

    ret = subprocess.Popen(cmd, shell=True).stdout.read();

    print ret

    times = []
    for line in ret.split():
      if line[0].isdigit():
        timedict[para] = float(line)


  print timedict

    #print "Total: {0}".format(times[0])
#    print "Total: {0}".format(times[-1] - times[0])
#    print "Start Set: {0}".format(times[1] - times[0])
#    print "Sim Set: {0}".format(times[2] - times[1])
#    print "RandRots: {0}".format(times[3] - times[2])
#    print "Color: {0}".format(times[4] - times[3])

#

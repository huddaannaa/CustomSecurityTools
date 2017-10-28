import scapy
target = ""
pkt_syn_ack = IP(dst=target)/TCP(dport=80, flags="SA")
pkt_icmp    = IP(dst=target)/ICMP(type=3,code=1)
pkt_fin     = IP(dst=target)/TCP(dport=22,sport=RandShort(),seq=RandShort(),flags="F")

#SENDING PACKETS AT THE NETWORK LAYER
option = #1,2,3
if option is 1:
	type_pkt = pkt_syn_ack
	type_pkt.summary()
	#type_pkt.show()
	res,res1 = sr(type_pkt)
	print res,res1
else:
	pass
if option is 2:
	type_pkt = pkt_icmp
	type_pkt.summary()
	#type_pkt.show()
	res,res1 = sr(type_pkt)
	print res,res1
else:
	pass
if option is 3:
	type_pkt = pkt_fin
	type_pkt.summary()
	#type_pkt.show()
	res,res1 = sr(type_pkt)
	print res,res1
else:
	pass

#SENDING PACKETS AT THE ETHERNET LAYER
packet = 
res, res2 = srp(packet)

#HOST DISCOVERY
                        #MAC Address                  #IP Address
r1, r2 = srp(Ether(dst="ff:ff:ff:ff:ff:ff")/ARP(dst2="192.168.122.0/24"),timeout=4)
r1.summary(lambda(s,r): r.sprintf("Ether:%Ether.src% \t\t Host: %ARP.psrc%"))
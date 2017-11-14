def send_a_packet(target, option = 1):
    """
    SCRIPT BY HUD SEIDU DAANNAA MSc |CEH
    This script can be modified and different types 
    of packets can be crafted and the function can be 
    used in a "for loop" with a specified itteration
    to send packets to a given target.
    
    the scenario could change were difference types 
    of packets could be sent randomly.
    
    target    = ''      #IP address
    options 1 = syn_ack
    ________2 = icmp
    ________3 = fin
    
    """
    import scapy
    #syn_ack packet
    pkt_syn_ack = IP(dst=target)/TCP(dport=80, flags="SA")

    #ICMP packet
    pkt_icmp    = IP(dst=target)/ICMP(type=3,code=1)

    #Fin packet
    pkt_fin     = IP(dst=target)/TCP(dport=22,sport=RandShort(),seq=RandShort(),flags="F")

    #SENDING PACKETS AT THE NETWORK LAYER
    
    if option is 1:
        type_pkt = pkt_syn_ack
        type_pkt.summary()
        #type_pkt.show()
        res,res1 = sr(type_pkt)
        print res,res1
    else:
        pass
    "_____"
    if option is 2:
        type_pkt = pkt_icmp
        type_pkt.summary()
        #type_pkt.show()
        res,res1 = sr(type_pkt)
        print res,res1
    else:
        pass

    "_____"
    if option is 3:
        type_pkt = pkt_fin
        type_pkt.summary()
        #type_pkt.show()
        res,res1 = sr(type_pkt)
        print res,res1
    else:
        pass
    

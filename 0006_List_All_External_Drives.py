def List_All_External_Drives():
    """
    BY H.S Daannaa MSc |CEH
    This script will display all external drives on a windows system
    this can be used during post exploitations, or can also be used
    for troubleshooting purposes
    """
    import string, os
    available_drives = []
    removable_drives = []
    all_files_in_drives = []
    alpha = list(string.ascii_lowercase[:26])
    list_d = [n + ':\\' for n in alpha]
    for n5 in range(len(alpha)):
        if os.path.exists(list_d[n5]) is True and os.listdir(list_d[n5]) != '[]':
            available_drives.append(list_d[n5])
    for n6 in available_drives:
        if n6 != 'c:\\':
            print n6
        else:
            pass
List_All_External_Drives()

from datetime import datetime
from tabulate import tabulate


class BeadMaster:
    def __init__(self):
        self.number_of_bed = 0
        self.beds = []
        self.patients = []
        self.beds_type = ["general", "private", "semi private"]

    def create_beds(self):
        number_of_bed = int(self.number_of_bed)
        switch = "private"
        for i in range(0, number_of_bed):
            if i % 2 == 0:
                self.beds.append({"type": 0, "occupied": False})  # (0,2,4)
            elif switch == "private":
                self.beds.append({"type": 1, "occupied": False})  # (1,5,9)
                switch = "semi_private"
            else:
                self.beds.append({"type": 2, "occupied": False})  # (3,7,11)
                switch = "private"

    def allocate_bed(self, name, bed_type):
        allocate_flag = False
        for index, val in enumerate(self.beds):
            if bed_type == val["type"] and val["occupied"] == False:
                val["occupied"] = True
                self.patients.append(
                    {"Name": name, "bed_number": index, "allocated_on": datetime.now(), "discharged": False,
                     "unallocated_on": ""})
                allocate_flag = True
                break
        if not allocate_flag:
            print("Bed not available as of now ")

    def unallocate_bed(self, name):
        for index, val in enumerate(self.patients):
            if name == val["Name"] and val["discharged"] == False:
                val["discharged"] = True
                val["unallocated_on"] = datetime.now()
                self.beds[val["bed_number"]]["occupied"] = False
                print("Patent discharge")
                break

    def report(self, type):

        if type == 0:
            report_list = []
            for key, val in enumerate(self.beds):
                report_list.append([
                    key,
                    self.beds_type[val["type"]],
                    val["occupied"]
                ])
            print(tabulate(report_list, headers=['Bed number', 'Type', 'Occupied']))
        elif type == 1:
            report_list = []
            for val in self.patients:
                report_list.append([val["Name"],
                                    val["bed_number"],
                                    self.beds_type[self.beds[val["bed_number"]]["type"]],
                                    val["allocated_on"],
                                    val["unallocated_on"]
                                    ]
                                   )
            print(tabulate(report_list, headers=['Name', 'Bed number', 'Type', 'Allocated On', 'Unallocated On']))
        elif type == 2:
            total_bed = self.number_of_bed
            general_bed = 0
            private_bed = 0
            semi_private_bed = 0
            general_Patent = 0
            private_Patent = 0
            semi_private_Patent = 0

            for key, val in enumerate(self.beds):
                if val["type"] == 0:
                    general_bed += 1
                    if val["occupied"]:
                        general_Patent += 1

                if val["type"] == 1:
                    private_bed += 1
                    if val["occupied"]:
                        private_Patent += 1

                if val["type"] == 2:
                    semi_private_bed += 1
                    if val["occupied"]:
                        semi_private_Patent += 1
            print("Total beds : ", total_bed)
            print("General beds : ", general_bed)
            print("Private beds : ", private_bed)
            print("Semi private beds : ", semi_private_bed)
            print("General bed occupied : ", general_Patent)
            print("Private bed occupied : ", private_Patent)
            print("Semi private bed occupied : ", semi_private_Patent)

    @staticmethod
    def printDottedLine():
        sepr = ""
        for i in range(0, 100):
            sepr = sepr + "-"
        print(sepr)


bedObject = BeadMaster()

number_of_bed = input("Enter number of beds : ")
bedObject.number_of_bed = number_of_bed
bedObject.create_beds()
allocate_bed_obj = bedObject.allocate_bed
unallocate_bed_obj = bedObject.unallocate_bed
report_obj = bedObject.report
printDottedLineobj = bedObject.printDottedLine
while True:
    printDottedLineobj()
    print("Please select 1 from below options : ")
    print("\n To allocate a bed [0]"
          "\n To discharge a patents [1]"
          "\n For report  [2]"
          "\n To exit  [10]"
          )
    option = int(input("Enter you selection : "))
    if option == 0:
        patients_name = input("Enter patients name :")
        print("Please select bed type : ")
        print("\nFor general enter [0] "
              "\n For private enter [1] "
              "\n For semi private enter [2]")
        while True:
            printDottedLineobj()
            bed_type = int(input("Enter the index : "))
            if bed_type == 0 or bed_type == 1 or bed_type == 2:
                printDottedLineobj()
                break
            else:
                print("Invalid input")
                printDottedLineobj()
        allocate_bed_obj(patients_name, bed_type)

    elif option == 1:
        patients_name = input("Enter patients name : ")
        unallocate_bed_obj(patients_name)

    elif option == 2:
        print("Please select report type : ")
        print("\nFor bed report [0] "
              "\n For patent report [1] "
              "\n Aggregate report [2] "
              "\n Main menu [3] "
              )

        option = int(input("Enter you selection : "))
        if option == 0 or option == 1 or option == 2:
            report_obj(option)
            printDottedLineobj()
        else:
            break


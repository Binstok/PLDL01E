class Service_Information:
#Initialize the service information
    def __init__(self):
        self.soa = 0
        self.statement_of_account_for_the_month_of = ""
        self.contract_number = 0
        self.account_name = ""
        self.service_address = ""
        self.tin = ""
        self.rate_class = ""
        self.business_area = ""
#Get the customer info
    def get_customer_info(self, soa, statement_of_account_for_the_month_of, contract_number, account_name, service_address, tin, rate_class, business_area):
        self.soa = soa
        self.statement_of_account_for_the_month_of = statement_of_account_for_the_month_of
        self.contract_number = contract_number
        self.account_name = account_name
        self.service_address = service_address
        self.tin = tin
        self.rate_class = rate_class
        self.business_area = business_area
#Display the customer info based on the design needed
    def display_customer_info(self):
        print("\t\t\t\t\t\t\t\t\t\t Maynilad Water Services, Inc.")
        print("\t\t\t\t\t\t\t\t\t\t 8390 DR A SANTOS AVE BF HOMES")
        print("\t\t\t\t\t\t\t\t\t\t PARANAQUE CITY")
        print("\t\t\t\t\t\t\t\t\t\t VAT Reg TIN 005-393-442-0000")
        print("\t\t\t\t\t\t\t\t\t\t SPM No.:")
        print("\t\t\t\t\t\t\t\t\t\t Machine SN:")
        print("")
        print("SOA # ", self.soa)
        print("STATEMENT OF ACCOUNT For the Month of: ", self.statement_of_account_for_the_month_of)
        print("Service Information")
        print("")
        print("Contract Account No: ", self.contract_number)
        print("Account Name: ", self.account_name)
        print("Service Address: ", self.service_address)
        print("Tin: ", self.tin)
        print("Rate Class: ", self.rate_class)
        print("Business Area: ", self.business_area)
#add new class for the metering information and billing summary
class Metering_Information_Billing_Summary:
#Initialize metering information and billing summary
    def __init__(self):
        self.meter_number = ""
        self.mru_number = 0
        self.seq_number = ""
        self.reading_date = ""
        self.present_reading = 0
        self.previous_reading = 0
        self.consumption = 0
        self.previous_consumption = ""
        self.billing_period = ""
        self.current_charges = 0
        self.basic_charge = 0
        self.environmental_charges = 0
        self.maintenance_service_charge = 0
        self.total_current_charges_before_tax = 0
        self.government_tax = 0
        self.payment_due_date = ""
#Get the metering information and billing summary
    def get_metering_information_billing_summary(self, meter_number, mru_number, seq_number, reading_date, present_reading, previous_reading, consumption, previous_consumption, billing_period, current_charges, basic_charge, environmental_charges, maintenance_service_charge, total_current_charges_before_tax, government_tax, payment_due_date):
        self.meter_number = meter_number
        self.mru_number = mru_number
        self.seq_number = seq_number
        self.reading_date = reading_date
        self.present_reading = present_reading
        self.previous_reading = previous_reading
        self.consumption = consumption
        self.previous_consumption = previous_consumption
        self.billing_period = billing_period
        self.current_charges = current_charges
        self.basic_charge = basic_charge
        self.environmental_charges = environmental_charges
        self.maintenance_service_charge = maintenance_service_charge
        self.total_current_charges_before_tax = total_current_charges_before_tax
        self.government_tax = government_tax
        self.payment_due_date = payment_due_date
#Computation for basic charge
    def get_basic_charge(self, consumption):
        self.basic_charge = 23.52 * consumption
        return self.basic_charge
#Computation for environmental charges
    def get_environmental_charges(self, basic_charge):
        self.environmental_charges = 0.2 * basic_charge
        return self.environmental_charges
#Computation for total current charges before tax
    def get_total_current_charges_before_tax (self, basic_charges, environmental_charges, maintenance_service_charge):
        self.total_current_charges_before_tax = basic_charges + environmental_charges + maintenance_service_charge
        return self.total_current_charges_before_tax
#Computation for government tax
    def get_government_tax (self, total_current_charges_before_tax):
        self.government_tax = 0.025 * total_current_charges_before_tax
        return self.government_tax
#Computation for total amount due
    def get_total_amount_due(self, total_current_charges_before_tax, government_tax):
        self.current_charges = total_current_charges_before_tax + government_tax
        return self.total_current_charges_before_tax
#Display metering information and billing summary
    def display_matering_information_billing_summery(self):
        print("METERING INFORMATION")
        print("Meter No. \t\t\t\t\t\t\t MRU No. \t\t\t\t\t\t\t Seq No.")
        print(self.meter_number, "\t\t\t\t\t\t\t", self.mru_number, "\t\t\t\t\t\t\t", self.seq_number)
        print("Reading Date: ", self.reading_date)
        print("Present Reading: ", self.present_reading)
        print("Previous Reading: ", self.previous_reading)
        print("Consumption (cu.m): ", self.consumption)
        print("Previous Month Consumption: ", self.previous_consumption)
        print("------------------------------------------------------------------------------------------------------")
        print("BILL & PAYMENT HISTORY")
        print("")
        print("Desc \t\t\t\t\t\t\t Total amount \t\t\t\t\t\t\t OR# \t\t\t\t\t\t\t Date")
        print("------------------------------------------------------------------------------------------------------")
        print("BILLING SUMMARY")
        print("BILLING PERIOD: ", self.billing_period, "TO ", self.reading_date)





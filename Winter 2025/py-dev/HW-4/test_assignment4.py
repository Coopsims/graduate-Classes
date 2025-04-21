from Assignment4 import Records, InvalidColumnNames, NoRecordStatsFound
from collections import Counter
import unittest
import builtins

class TestCollections(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        print("setUpClass")
        cls.records = Records("./assignment4_data/credit_card.csv", "Credit Card")
        # TODO: Didn't feel like doing this manually so I implemented an auto adjustment
        corrected_complaint_header = (
            "Datereceived,Product,Subproduct,Issue,Subissue,Consumercomplaintnarrative,"
            "Companypublicresponse,Company,State,ZIPcode,Tags,Consumerconsentprovided,"
            "Submittedvia,Datesenttocompany,Companyresponsetoconsumer,Timelyresponse,"
            "Consumerdisputed,ComplaintID"
        )
        inputs = iter([corrected_complaint_header])
        original_input = builtins.input
        builtins.input = lambda prompt: next(inputs)
        cls.records.load_data("./assignment4_data/customer_complaints.csv", "Complaints")

    @classmethod
    def tearDownClass(cls):
        print("tearDownClass")
        del cls.records

    def setUp(self):
        print("setUp")

    def tearDown(self):
        print("tearDown")

    def test_create_container(self):
        print("Executing test_create_container.")
        rec = Records.__new__(Records)

        credit_card_header = [
            "Series_reference", "Period", "Data_value", "Suppressed", "STATUS",
            "UNITS", "Magnitude", "Subject", "Group", "Series_title_1",
            "Series_title_2", "Series_title_3", "Series_title_4", "Series_title_5"
        ]
        container_cc = rec._create_container(credit_card_header)
        expected_cc = tuple([col.replace("_", "").replace("-", "").replace(" ", "") for col in credit_card_header])
        self.assertEqual(container_cc._fields, expected_cc)

        complaint_header = [
            "Date received", "Product", "Sub-product", "Issue", "Sub-issue",
            "Consumer complaint narrative", "Company public response", "Company",
            "State", "ZIP code", "Tags", "Consumer consent provided?",
            "Submitted via", "Date sent to company", "Company response to consumer",
            "Timely response?", "Consumer disputed?", "Complaint ID"
        ]
        corrected_complaint_header = (
            "Datereceived,Product,Subproduct,Issue,Subissue,Consumercomplaintnarrative,"
            "Companypublicresponse,Company,State,ZIPcode,Tags,Consumerconsentprovided,"
            "Submittedvia,Datesenttocompany,Companyresponsetoconsumer,Timelyresponse,"
            "Consumerdisputed,ComplaintID"
        )
        inputs = iter([corrected_complaint_header])
        original_input = builtins.input
        builtins.input = lambda prompt: next(inputs)
        try:
            container_complaint = rec._create_container(complaint_header)
            expected_complaint = tuple(corrected_complaint_header.split(","))
            self.assertEqual(container_complaint._fields, expected_complaint)
        finally:
            builtins.input = original_input

    def test_record_stats(self):
        print("Executing test_record_stats.")
        from collections import namedtuple, Counter
        DummyEntry = namedtuple("Entry", ["Period", "Product"])

        cc_data = [
            DummyEntry("2004.03", "Card1"),
            DummyEntry("2005.03", "Card2"),
            DummyEntry("2004.03", "Card1"),
            DummyEntry("2006.03", "Card3"),
            DummyEntry("2007.03", "Card4")
        ]

        comp_data = [
            DummyEntry("2004.03", "Prod1"),
            DummyEntry("2005.03", "Prod2"),
            DummyEntry("2004.03", "Prod1"),
            DummyEntry("2006.03", "Prod3"),
            DummyEntry("2004.03", "Prod1"),
            DummyEntry("2007.03", "Prod2")
        ]
        rec = Records.__new__(Records)
        rec.record_dict = {
            "Credit Card": {"data": cc_data},
            "Complaints": {"data": comp_data}
        }

        rec.record_stats("Credit Card", "Period", lambda entry: entry.Period)
        expected_cc_counter = Counter({"2004.03": 2, "2005.03": 1, "2006.03": 1, "2007.03": 1})
        self.assertEqual(rec.record_dict["Credit Card"]["stats_Period"], expected_cc_counter)

        rec.record_stats("Complaints", "Product", lambda entry: entry.Product)
        expected_comp_counter = Counter({"Prod1": 3, "Prod2": 2, "Prod3": 1})
        self.assertEqual(rec.record_dict["Complaints"]["stats_Product"], expected_comp_counter)

    def test_extract_top_n(self):
        print("Executing test_extract_top_n.")
        self.records.record_stats("Credit Card", "Period", lambda entry: entry.Period)
        top_10_cc = self.records.extract_top_n(10, "Credit Card", "stats_Period")
        expected_cc = [
            ('2004.03', 137), ('2005.03', 137), ('2006.03', 137), ('2007.03', 137),
            ('2008.03', 137), ('2009.03', 137), ('2010.03', 137), ('2011.03', 135),
            ('2012.03', 135), ('2013.03', 135)
        ]
        self.assertEqual(top_10_cc, expected_cc)

        self.records.record_stats("Complaints", "Product", lambda entry: entry.Product)
        top_10_complaints = self.records.extract_top_n(10, "Complaints", "stats_Product")
        expected_complaints = [
            ('Credit reporting or other personal consumer reports', 109620),
            ('Debt collection', 5826),
            ('Credit card', 4802),
            ('Checking or savings account', 3663),
            ('Mortgage', 1885),
            ('Student loan', 1144),
            ('Money transfer, virtual currency, or money service', 1083),
            ('Vehicle loan or lease', 920),
            ('Payday loan, title loan, personal loan, or advance loan', 533),
            ('Prepaid card', 511)
        ]
        self.assertEqual(top_10_complaints, expected_complaints)

if __name__ == '__main__':
    unittest.main()
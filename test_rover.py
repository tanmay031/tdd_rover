import io
import sys
import unittest
from Rover import rovar
rv = rovar()


class test_string(unittest.TestCase):

    ############# Test Enrove ################
    def test_enrove_null(self):
        self.assertEqual(rv.enrove(None), None)

    def test_enrove_empty_string(self):
        self.assertEqual(rv.enrove(""), "")

    # Test lowercase
    def test_enrove_non_empty_string_lowercase_abc(self):
        self.assertEqual(rv.enrove("abc"), "abobcoc")

    def test_enrove_non_empty_string_lowercase_def(self):
        self.assertEqual(rv.enrove("def"), "dodefof")

    def test_enrove_non_empty_string_lowercase_ghi(self):
        self.assertEqual(rv.enrove("ghi"), "goghohi")

    def test_enrove_non_empty_string_lowercase_jkl(self):
        self.assertEqual(rv.enrove("jkl"), "jojkoklol")

    def test_enrove_non_empty_string_lowercase_mno(self):
        self.assertEqual(rv.enrove("mno"), "momnono")

    def test_enrove_non_empty_string_lowercase_pqr(self):
        self.assertEqual(rv.enrove("pqr"), "popqoqror")

    def test_enrove_non_empty_string_lowercase_stu(self):
        self.assertEqual(rv.enrove("stu"), "sostotu")

    def test_enrove_non_empty_string_lowercase_vwxyz(self):
        self.assertEqual(rv.enrove("vwxyz"), "vovwowxoxyzoz")

    def test_enrove_non_empty_string_lowercase_åäö(self):
        self.assertEqual(rv.enrove("åäö"), "åäö")

    # Test upper case chunk by chunk

    def test_enrove_non_empty_string_uppercase_ABC(self):
        self.assertEqual(rv.enrove("ABC"), "ABOBCOC")

    def test_enrove_non_empty_string_uppercase_DEF(self):
        self.assertEqual(rv.enrove("DEF"), "DODEFOF")

    def test_enrove_non_empty_string_uppercase_GHI(self):
        self.assertEqual(rv.enrove("GHI"), "GOGHOHI")

    def test_enrove_non_empty_string_uppercase_JKL(self):
        self.assertEqual(rv.enrove("JKL"), "JOJKOKLOL")

    def test_enrove_non_empty_string_uppercase_MNO(self):
        self.assertEqual(rv.enrove("MNO"), "MOMNONO")

    def test_enrove_non_empty_string_uppercase_PQR(self):
        self.assertEqual(rv.enrove("PQR"), "POPQOQROR")

    def test_enrove_non_empty_string_uppercase_STU(self):
        self.assertEqual(rv.enrove("STU"), "SOSTOTU")

    def test_enrove_non_empty_string_uppercase_VWXYZ(self):
        self.assertEqual(rv.enrove("VWXYZ"), "VOVWOWXOXYZOZ")

    def test_enrove_non_empty_string_uppercase_ÅÄÖ(self):
        self.assertEqual(rv.enrove("ÅÄÖ"), "ÅÄÖ")

    def test_enrove_non_empty_string_numbers(self):
        self.assertEqual(rv.enrove("1234567890"), "1234567890")

    def test_enrove_non_empty_string_special_characters(self):
        self.assertEqual(rv.enrove("!”#€%&/(),.)?"), "!”#€%&/(),.)?")

    def test_enrove_string_with_spaces(self):
        self.assertEqual(rv.enrove("The quick brown fox jumps over the lazy dog"),
                         "TOThohe qoquicockok bobrorowownon fofoxox jojumompopsos ovoveror tothohe lolazozy dodogog")

    def test_enrove_mix_ltr_num_special_character(self):
        self.assertEqual(rv.enrove("Hello! 123@#$%"), "HOHelollolo! 123@#$%")

    ############# Test Derove ################

    def test_derove_null(self):
        self.assertEqual(rv.derove(None), None)

    def test_derove_empty_string(self):
        self.assertEqual(rv.derove(""), "")

    # Test lowecase
    def test_derove_non_empty_string_lowercase(self):
        self.assertEqual(rv.derove("abobcoc"), "abc")

    def test_derove_non_empty_string_lowercase_2(self):
        self.assertEqual(rv.derove("dodefof"), "def")

    def test_derove_non_empty_string_lowercase_3(self):
        self.assertEqual(rv.derove("goghohi"), "ghi")

    def test_derove_non_empty_string_lowercase_4(self):
        self.assertEqual(rv.derove("jojkoklol"), "jkl")

    def test_derove_non_empty_string_lowercase_5(self):
        self.assertEqual(rv.derove("momnono"), "mno")

    def test_derove_non_empty_string_lowercase_6(self):
        self.assertEqual(rv.derove("popqoqror"), "pqr")

    def test_derove_non_empty_string_lowercase_7(self):
        self.assertEqual(rv.derove("sostotu"), "stu")

    def test_derove_non_empty_string_lowercase_8(self):
        self.assertEqual(rv.derove("vovwowxoxyzoz"), "vwxyz")

    def test_derove_non_empty_string_lowercase_9(self):
        self.assertEqual(rv.derove("åäö"), "åäö")

    # Test uppercase
    def test_derove_non_empty_string_uppercase(self):
        self.assertEqual(rv.derove("ABOBCOC"), "ABC")

    def test_derove_non_empty_string_uppercase_2(self):
        self.assertEqual(rv.derove("DODEFOF"), "DEF")

    def test_derove_non_empty_string_uppercase_3(self):
        self.assertEqual(rv.derove("GOGHOHI"), "GHI")

    def test_derove_non_empty_string_uppercase_4(self):
        self.assertEqual(rv.derove("JOJKOKLOL"), "JKL")

    def test_derove_non_empty_string_uppercase_5(self):
        self.assertEqual(rv.derove("MOMNONO"), "MNO")

    def test_derove_non_empty_string_uppercase_6(self):
        self.assertEqual(rv.derove("POPQOQROR"), "PQR")

    def test_derove_non_empty_string_uppercase_7(self):
        self.assertEqual(rv.derove("SOSTOTU"), "STU")

    def test_derove_non_empty_string_uppercase_8(self):
        self.assertEqual(rv.derove("VOVWOWXOXYZOZ"), "VWXYZ")

    def test_derove_non_empty_string_uppercase_9(self):
        self.assertEqual(rv.derove("ÅÄÖ"), "ÅÄÖ")

    def test_derove_non_empty_string_numbers(self):
        self.assertEqual(rv.derove("1234567890"), "1234567890")

    def test_derove_non_empty_string_special_characters(self):
        self.assertEqual(rv.derove("!”#€%&/(),.)?"), "!”#€%&/(),.)?")

    def test_derove_string_with_spaces(self):
        self.assertEqual(rv.derove("TOThohe qoquicockok bobrorowownon fofoxox jojumompopsos ovoveror tothohe lolazozy dodogog"),
                         'The quick brown fox jumps over the lazy dog')

    def test_derove_mix_ltr_num_special_character(self):
        self.assertEqual(rv.derove("HOHelollolo! 123@#$%"), "Hello! 123@#$%")


if __name__ == '__main__':
    unittest.main(verbosity=2)

1o Μέρος 1ης απαλλακτικής εργασίας - IR_MSc_Web_Intelligence - 20201
-------------------------------------------------------------------------------------
Κύρος Γεώργιος - 112020 | Μανώλας Ιωάννης - 132020
-------------------------------------------------------------------------------------

* Εκφώνηση
-------------------------------------------------------------------------------------
Έχοντας την συλλογή από patent documents σε xml μορφη (χρησιμοποιήστε
τα data από την κυρια εργασία) εκτελεστέ τα παρακάτω:
-------------------------------------------------------------------------------------
Α)
Δημιουργείστε έναν αλγόριθμο που θα του δίνουμε σαν input μια συλλογή από πατέντες 
σε xml μορφή και να γραφεί σε ένα αρχείο txt τα παρακάτω στατιστικά. Οι πατέντες θα 
βρίσκονται σε υποφακελους και όχι όλες σε έναν μόνο φάκελο.
-------------------------------------------------------------------------------------

Number of all patent-documents:
Number of all patents:
Average number of ipc codes per patents:
Number of patents containing section:
Distribution of all the different sections:
Average number of sections per patents:
Number of patents containing class:
Distribution of all the different classes:
Average number of classes per patents:
Number of patents containing subclass:
Distribution of all the different subclasses:
Average number of subclasses per patents:
Number of patents containing group:
Average number of groups per patents:
Number of patents containing subgroup:
Average number of subgroups per patents:
Number of patents not containing title:
Number of patents not containing ipc-codes:
Number of patents containing abstract:
Number of patents containing description:
Number of patents containing contain claims:
Number of patents containing all previous:
Number of patents containing abstract and claims:
Number of patents containing description and claims:
Number of patents containing abstract and description:
Number of patents containing abstract in more than 1 language:
Number of patents containing description in more than 1 language:
Number of patents containing claims in more than 1 language:
Number of patents where main language is English:
Number of patents where main language is German:
Number of patents where main language is French:
Number of English patents containing abstract in non-English:
Number of English patents containing descriptiont in non-English:
Number of English patents containing claims n non-English:
Number of non-english patents containing abstract in English:
Number of non-english patents containing descriptiont in English:
Number of non-english patents containing claims in English:
Min number of words in abstract:
Max number of words in abstract:
Average number of words in abstract:
Min number of words in description:
Max number of words in description:
Average number of words in description:
Min number of words in claims:
Max number of words in claims:
Average number of words in claims:
-------------------------------------------------------------------------------------

* Λύση:
-------------------------------------------------------------------------------------
Για την λύση του 1ου μέρους χρησιμοποίησαμε την γλώσσα προγραμματισμού python για την
δημιουργία ενός script, το οποίο θα έπρεπε να διατρέξει όλα τα αρχεία-πατέντες που 
υπήρχαν με σκοπό τον υπολογισμό των στατιστικών.

Επίσης χρησιμοποιήθηκαν οι παρακάτω βιβλιοθήκες (libraries) της python:

	- numpy
	  Για την απόθηκευση των δεδομένων.

	- pandas
	  Για την απόθηκευση και επεξεργασία των δεδομένων.

	- os
	  Για το άνοιγμα και το γράψιμο σε εξωτερικό αρχείο.

	- re	
	  Για την εύρεση και επεξεργασία των δεδομένων με regex.

	- statistics
          Για τον υπολογισμό μετρικών όπως ο μέσος όρος και η απόκλιση.

	- nltk
	  Για τον καθρισμό των δεδομένων και την επεξεργασία κειμένου.

	- BeautifulSoup
	  Για την εξαγωγή δεδομένων απο αρχεία της μορφής .xml με συγκεκριμένα tags.

Το τελικό script έτρεξε σε όλα τα δεδομένα (106087 αρχεία - έγγραφα πατέντες).

Και τα αποτελέσματα παρουσιάζονται στην παρακάτω μορφή:
******************----STATS----******************
Created at 2021-06-06 00:47:55.096014
-----------------------------------------------------------------------------------------------------------------
******************----STATS of IPCRS codes(section, classes, subclasses, groups, subgroups)----******************
-----------------------------------------------------------------------------------------------------------------
Number of all patent-documents: 106087
Number of all patents: 53006
Average number of ipc codes per patents: 5.877249266364091
Number of patents containing section: 105979
Distribution of all the different sections: {'H': 139451, 'B': 162538, 'C': 228367, 'A': 163487, 'F': 66114, 'G': 144833, 'E': 19971, 'D': 18285}
Average number of sections per patents: 1.4151482840940186
Number of patents containing classes: 105979
Distribution of all the different classes: {'H01': 57891, 'B60': 18214, 'B01': 26610, 'B23': 9249, 'B26': 1862, 'H04': 48702, 'C07': 81072, 'A22': 409, 'F16': 23062, 'C22': 4148, 'G11': 22835, 'H05': 9530, 'G01': 43109, 'G02': 12633, 'G03': 18917, 'C08': 49860, 'B61': 1567, 'B62': 3811, 'E06': 2320, 'G09': 4286, 'G06': 27478, 'A63': 3264, 'B65': 22899, 'B05': 5633, 'C09': 19095, 'G05': 4121, 'A01': 12137, 'B29': 17751, 'G21': 1609, 'C01': 4874, 'F02': 12178, 'B63': 1377, 'C04': 5340, 'A61': 124773, 'B22': 3034, 'H02': 11569, 'C02': 4049, 'A62': 1180, 'E21': 2781, 'E05': 4355, 'F01': 5571, 'C11': 8446, 'B28': 1398, 'E04': 5693, 'B21': 4902, 'A21': 1213, 'E02': 1647, 'A41': 776, 'B32': 6106, 'C12': 26362, 'C03': 4163, 'F23': 4058, 'D06': 6953, 'G08': 2044, 'A47': 6087, 'B66': 2114, 'B41': 16161, 'D21': 4269, 'A43': 1237, 'F04': 4742, 'F21': 2035, 'H03': 11759, 'C10': 7873, 'D01': 2721, 'E01': 2002, 'A23': 8835, 'F15': 1192, 'C30': 1192, 'B24': 2625, 'C25': 1934, 'B30': 1032, 'B67': 1035, 'F41': 864, 'F42': 724, 'C23': 6240, 'B31': 747, 'B02': 1012, 'B04': 818, 'F24': 2939, 'B44': 722, 'C05': 658, 'G07': 4004, 'B09': 952, 'F26': 988, 'G10': 2802, 'C21': 2020, 'D04': 2081, 'F27': 1721, 'E03': 1173, 'D05': 304, 'A45': 1271, 'D03': 1207, 'C06': 375, 'B07': 1144, 'A46': 510, 'B25': 2969, 'B27': 1067, 'F28': 2121, 'D02': 585, 'B03': 920, 'B08': 1176, 'B64': 1410, 'B42': 1011, 'B43': 540, 'F25': 2596, 'A24': 972, 'B06': 352, 'G04': 840, 'C40': 248, 'G12': 155, 'C14': 222, 'B68': 60, 'F17': 543, 'F22': 470, 'A44': 492, 'A42': 331, 'C13': 196, 'D07': 165, 'B82': 34, 'F03': 310, 'B81': 224}
Average number of classes per patents: 1.686683210824786
Number of patents containing subclasses: 105979
Distribution of all the different subclasses: {'H01L': 21796, 'B60L': 687, 'B01L': 943, 'B23D': 706, 'B26D': 1055, 'H01J': 4570, 'H04N': 19679, 'B01J': 11682, 'C07C': 27084, 'A22C': 306, 'F16L': 3887, 'C22C': 2616, 'G11B': 18074, 'H01F': 2381, 'H05K': 5790, 'G01N': 19773, 'G02B': 8239, 'G03B': 2283, 'G03G': 5854, 'C08F': 13794, 'B60J': 1279, 'B61D': 600, 'B62D': 2376, 'E06B': 2237, 'C07D': 28799, 'G09G': 1981, 'G06F': 16935, 'A63C': 875, 'C08J': 4301, 'C08L': 14401, 'G01F': 1671, 'B60B': 448, 'B65D': 9961, 'B05D': 2148, 'C09D': 8045, 'H01M': 4465, 'G05D': 1351, 'B65G': 3835, 'A01N': 6844, 'C07B': 2960, 'C07F': 3774, 'B29C': 13282, 'B65B': 2970, 'C08G': 9970, 'C08K': 6232, 'G21C': 793, 'B01D': 11536, 'B05B': 2221, 'C01F': 473, 'C01G': 1224, 'H04M': 4505, 'H04Q': 3579, 'F02M': 3040, 'B29B': 1350, 'B29D': 1646, 'B29H': 1, 'B63H': 272, 'G01P': 1507, 'C04B': 5340, 'H01B': 2282, 'H01C': 579, 'G01R': 4559, 'A61K': 59535, 'A61P': 21063, 'A61F': 9239, 'G01D': 1490, 'G01L': 1703, 'F02D': 2861, 'B22D': 1579, 'H02J': 1480, 'A01K': 1344, 'B01F': 2449, 'C02F': 4049, 'A01F': 247, 'A62C': 378, 'E21B': 2327, 'B60R': 4304, 'E05B': 2177, 'B62H': 93, 'E05C': 527, 'A01M': 304, 'F01D': 939, 'F02B': 3171, 'F02C': 802, 'C11D': 7902, 'B28B': 950, 'E04B': 1948, 'F02F': 799, 'F16J': 945, 'B21G': 117, 'B21K': 207, 'B62J': 232, 'A61C': 1624, 'G03F': 3601, 'G03C': 5932, 'A21D': 755, 'E02D': 756, 'A41D': 423, 'A61B': 12154, 'B29K': 901, 'B29L': 570, 'B32B': 6106, 'B05C': 1264, 'C12Q': 3440, 'C03B': 1846, 'C03C': 2317, 'F23D': 962, 'D06F': 893, 'D06M': 3164, 'G01K': 452, 'G08B': 1141, 'H02H': 1119, 'H05B': 3023, 'A01G': 600, 'F16K': 2747, 'G01B': 2566, 'G01G': 667, 'C12N': 15625, 'G11C': 4761, 'B22F': 974, 'A47C': 1347, 'A61G': 1003, 'B66F': 480, 'B41J': 9068, 'B65H': 5125, 'G05B': 1819, 'B65F': 672, 'C12P': 4384, 'B61F': 343, 'D21F': 1029, 'A01B': 444, 'G01S': 3238, 'H01Q': 2742, 'H04B': 7032, 'A43B': 991, 'A43C': 215, 'A61M': 7137, 'F04D': 1705, 'F21H': 4, 'F23C': 682, 'F23J': 246, 'F23R': 557, 'C01B': 2900, 'H03K': 3961, 'G06K': 4449, 'G02F': 3703, 'B28C': 133, 'A61Q': 5204, 'C10G': 1529, 'D01F': 1377, 'C07J': 1344, 'F16H': 5047, 'E01F': 445, 'H01H': 4124, 'A23L': 4171, 'C08B': 906, 'G06T': 4627, 'F15B': 1069, 'C30B': 1192, 'B24D': 840, 'C25D': 807, 'C09K': 3885, 'C07K': 13661, 'D21H': 2018, 'F01L': 1084, 'B23K': 3982, 'B41F': 2074, 'F04C': 1249, 'B23P': 692, 'H02G': 1228, 'C09J': 3633, 'B41M': 3832, 'G06Q': 760, 'E05F': 718, 'E04H': 596, 'F16B': 2418, 'A61J': 1275, 'B30B': 1032, 'B67C': 235, 'E01B': 532, 'H01R': 9009, 'H01G': 895, 'H02M': 1659, 'A61L': 4247, 'F41G': 233, 'F42B': 552, 'D06P': 1649, 'B23C': 298, 'H03M': 1968, 'C23F': 646, 'C23C': 5087, 'H01S': 3785, 'G01Q': 74, 'B60C': 1841, 'C09B': 2422, 'C09C': 1002, 'H04R': 1175, 'H04L': 7619, 'B21D': 1975, 'B31D': 103, 'E04C': 870, 'A23J': 376, 'B60K': 1672, 'B60W': 970, 'H04J': 1952, 'B02C': 963, 'B04C': 217, 'G01C': 1099, 'F23G': 502, 'F24H': 504, 'A47G': 500, 'B44D': 116, 'G09F': 1414, 'F02K': 333, 'C10B': 323, 'C12C': 112, 'G02C': 691, 'A01C': 355, 'C05G': 178, 'B60Q': 533, 'G07C': 789, 'G07F': 1687, 'B23Q': 1618, 'B24B': 1337, 'C12R': 1433, 'F02G': 73, 'B09C': 336, 'B09B': 616, 'E04D': 594, 'B60T': 2818, 'D21C': 713, 'B21B': 1379, 'F26B': 988, 'A61N': 1807, 'H05F': 100, 'B63B': 860, 'F16F': 2042, 'C12S': 175, 'G10K': 774, 'C12M': 959, 'A23C': 645, 'G05F': 649, 'H03F': 1368, 'H03G': 788, 'C21D': 1215, 'A01H': 420, 'C08H': 102, 'D04B': 593, 'E02F': 667, 'F04F': 122, 'B21J': 330, 'A63H': 299, 'C21C': 456, 'F27D': 985, 'A21C': 334, 'C25C': 268, 'G03D': 951, 'H02K': 4226, 'A01D': 757, 'A43D': 31, 'F16G': 375, 'H02P': 1179, 'B28D': 315, 'E03F': 375, 'H02B': 477, 'D05B': 214, 'D05C': 90, 'B44C': 397, 'C05D': 56, 'B31B': 446, 'C11C': 122, 'A45D': 825, 'A23G': 1590, 'A23P': 149, 'D03D': 977, 'E01H': 191, 'H03H': 1726, 'F04B': 1666, 'H04H': 496, 'H03L': 915, 'F23L': 258, 'G09B': 730, 'F21S': 419, 'C22B': 1197, 'G10D': 105, 'C06B': 242, 'F24C': 583, 'B07C': 532, 'A46B': 408, 'A46D': 102, 'B25B': 1164, 'B27M': 59, 'E04F': 989, 'B66C': 533, 'B61B': 174, 'F28F': 1145, 'C21B': 349, 'F27B': 736, 'F28D': 823, 'G01T': 463, 'D06N': 370, 'D02G': 358, 'B27N': 319, 'B03C': 353, 'B07B': 612, 'C10L': 1796, 'C10M': 2676, 'C10N': 979, 'C07G': 53, 'B08B': 1176, 'C23G': 467, 'C25B': 768, 'F16D': 2426, 'E05G': 123, 'G09C': 159, 'G01V': 913, 'B64G': 285, 'A41G': 20, 'A47J': 1291, 'F23B': 9, 'A62D': 572, 'B23B': 1377, 'B25C': 216, 'B42B': 98, 'B43K': 326, 'B60D': 107, 'B60G': 947, 'G07B': 437, 'D01H': 555, 'E02B': 224, 'E03D': 333, 'E21D': 346, 'F25D': 855, 'A47B': 809, 'G01M': 1280, 'B42D': 457, 'G07D': 833, 'G08G': 587, 'H01T': 379, 'H03J': 263, 'G10L': 1503, 'H04W': 2296, 'A23K': 810, 'A24D': 361, 'A24F': 58, 'A63B': 1349, 'B04B': 601, 'B26B': 493, 'B41D': 17, 'B41N': 484, 'B60H': 551, 'F25B': 1217, 'B60M': 59, 'B60P': 394, 'B41C': 287, 'F01C': 302, 'F16C': 2518, 'B06B': 352, 'A24C': 349, 'A47F': 439, 'D04H': 1414, 'B25H': 168, 'B25J': 833, 'C11B': 422, 'F16N': 218, 'F23N': 445, 'F23M': 112, 'G01J': 1399, 'F42D': 55, 'G01W': 82, 'G04G': 263, 'A41B': 161, 'C40B': 248, 'D21B': 133, 'D21J': 60, 'C07H': 3397, 'F01N': 1961, 'F01B': 214, 'F21V': 1461, 'F41H': 167, 'G12B': 155, 'A63F': 623, 'H01P': 751, 'A23D': 352, 'A47L': 996, 'B22C': 481, 'B66B': 932, 'C05F': 371, 'B25G': 137, 'F16S': 30, 'F24D': 378, 'G06M': 92, 'H05H': 477, 'H01K': 133, 'A62B': 230, 'C01C': 119, 'B26F': 314, 'F01K': 320, 'G08C': 316, 'H03B': 304, 'A23B': 515, 'A47K': 526, 'E05D': 810, 'B64D': 392, 'F24F': 1126, 'B25D': 349, 'B60N': 1073, 'B67D': 658, 'E04G': 696, 'F25J': 437, 'C14C': 209, 'E01C': 589, 'C10J': 342, 'F28C': 63, 'F02P': 924, 'H02N': 201, 'B42C': 185, 'B44F': 162, 'B68B': 17, 'D06Q': 29, 'D06L': 209, 'D06B': 302, 'E21C': 77, 'G21B': 50, 'F17C': 445, 'B21H': 76, 'C22F': 335, 'B61L': 234, 'B63G': 62, 'B64C': 579, 'G21F': 354, 'E01D': 245, 'F24J': 309, 'F42C': 117, 'G06G': 108, 'G06N': 420, 'F16M': 293, 'B23H': 382, 'B62B': 391, 'C01D': 158, 'F28G': 72, 'F41C': 18, 'A23N': 108, 'B24C': 448, 'B27K': 180, 'C08C': 154, 'D02J': 164, 'D01D': 467, 'B27B': 199, 'F22B': 394, 'B21C': 580, 'G21G': 27, 'G21K': 285, 'B42F': 271, 'B62M': 372, 'B03B': 441, 'F16P': 82, 'A61H': 412, 'B27C': 74, 'B61H': 76, 'B60S': 455, 'A44B': 353, 'A63G': 57, 'F41B': 56, 'B23F': 157, 'H04K': 91, 'A42B': 297, 'C10K': 83, 'B43L': 114, 'G10C': 129, 'G10G': 51, 'F15C': 55, 'D03C': 160, 'F17D': 98, 'F23Q': 126, 'F41J': 87, 'A01J': 532, 'C13K': 78, 'A47H': 91, 'E03C': 328, 'F25C': 87, 'D03J': 70, 'F01M': 479, 'G03H': 296, 'F41A': 231, 'B43M': 100, 'B62K': 226, 'A41C': 91, 'A41F': 47, 'D04D': 19, 'G07G': 258, 'B65C': 336, 'B27G': 100, 'C09H': 7, 'D01G': 303, 'A22B': 103, 'A45B': 76, 'D06H': 112, 'G21H': 16, 'A21B': 124, 'A61D': 73, 'F23K': 95, 'A24B': 204, 'D21G': 157, 'B03D': 126, 'G05G': 302, 'F21M': 21, 'F21Q': 14, 'H04S': 278, 'F16T': 34, 'B60F': 28, 'E06C': 83, 'B23G': 37, 'G06E': 58, 'A47D': 88, 'A44C': 139, 'G04B': 338, 'A42C': 34, 'B21L': 17, 'G21D': 84, 'B61G': 39, 'D07B': 165, 'A01P': 256, 'B82B': 34, 'G06C': 1, 'D04C': 50, 'B41K': 119, 'C12G': 120, 'F21L': 56, 'H03D': 352, 'A45C': 296, 'B68G': 43, 'F03C': 31, 'B41B': 27, 'B31F': 170, 'D06J': 5, 'A01L': 34, 'F21K': 25, 'B21F': 221, 'B64F': 116, 'D02H': 63, 'F01P': 272, 'G01H': 173, 'G04F': 84, 'B63C': 183, 'B81B': 116, 'F15D': 68, 'D06G': 15, 'B41L': 248, 'C12H': 96, 'B81C': 108, 'G04C': 154, 'G04D': 1, 'B27L': 30, 'C09G': 68, 'D06C': 205, 'G10H': 231, 'B62L': 116, 'A23F': 119, 'B27D': 36, 'B66D': 169, 'F21P': 4, 'B61C': 80, 'B67B': 142, 'C10C': 106, 'A41H': 34, 'C09F': 33, 'F41F': 72, 'C25F': 91, 'F03D': 87, 'H05G': 135, 'F02N': 175, 'F03B': 93, 'A45F': 74, 'B60V': 48, 'B44B': 47, 'B27F': 66, 'C13F': 58, 'C05C': 40, 'B61J': 7, 'D21D': 159, 'F03G': 73, 'B27H': 4, 'B25F': 102, 'B64B': 38, 'E03B': 137, 'F28B': 18, 'H03C': 114, 'G06J': 28, 'F03H': 26, 'E21F': 31, 'C06D': 90, 'F21Y': 15, 'F22D': 65, 'A63D': 46, 'C13D': 41, 'G10F': 9, 'F24B': 39, 'F21W': 16, 'F23H': 64, 'B31C': 28, 'C13G': 5, 'D01B': 5, 'C23D': 40, 'A63K': 4, 'C05B': 13, 'F22G': 11, 'C06C': 24, 'B02B': 49, 'C14B': 13, 'C10H': 29, 'C12F': 8, 'B61K': 14, 'C10F': 10, 'H05C': 5, 'C06F': 19, 'A63J': 11, 'D01C': 14, 'C13J': 14, 'B41G': 5, 'B62C': 5, 'B29J': 1, 'G09D': 2, 'C12J': 10, 'D04G': 5}
Average number of subclasses per patents: 2.0736938450070297
Number of patents containing groups: 105979
Average number of groups per patents: 2.977448362411421
Number of patents containing subgroups: 105979
Average number of subgroups per patents: 4.2434538918087545
-----------------------------------------------------------------------------------------
******************----STATS of title, abstract, claims, description----******************
-----------------------------------------------------------------------------------------
Number of patents not containining Title: 415
Number of patents not containining ipc-codes: 108
Number of patents containining abstract: 39314
Number of patents containining description: 74491
Number of patents containining claims: 74488
Number of patents containining all previous: 37895
Number of patents containing abstract and claims: 37895
Number of patents containing description and claims: 74488
Number of patents containing abstract and description: 37898
Number of patents containing abstract in more than 1 language: 12532
Number of patents containing description in more than 1 language: 0
Number of patents containing claims in more than 1 language: 109236
Number of patents where main language is English: 73865
Number of patents where main language is German: 23851
Number of patents where main language is French: 7783
Number of English patents containing abstract in non-English: 199
Number of English patents containing description in non-English: 26
Number of English patents containing claims in non-English: 48589
Number of non-english patents containing abstract in English: 12373
Number of non-english patents containing description in English: 115
Number of non-english patents containing claims in English: 12289
-------------------------------------------------------------------------------------------
******************----STATS of words in Abstract, Description, Claims----******************
-------------------------------------------------------------------------------------------
Min number of words in abstract: 5
Max number of words in abstract: 1015
Average number of words in abstract: 123.6688190281606
Min number of words in Description: 139
Max number of words in Description: 145754
Average number of words in Description: 4630.401202829872
Min number of words in Claims: 0
Max number of words in Claims: 40337

-------------------------------------------------------------------------------------------------------------------------------------
************************************************* ΠΡΟΣΟΧΗ *************************************************
-------------------------------------------------------------------------------------------------------------------------------------
Για την σωστή εκτέλεση του script, θα πρέπει να αλλαχτεί το συγκεκριμένο κομμάτι κώδικα με το σωστό path που έχει ο καθένας
τα έγγραφα του.

	- dir = 'patents/'



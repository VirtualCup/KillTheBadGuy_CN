from UnityText import UnityText;
from UnityTk2dFontData import UnityTk2dFontData;
from StringHelper import StringHelper;
from xml.dom.minidom import parseString
import os;
import csv;
import sys;

reload(sys);
sys.setdefaultencoding('utf-8');

def save_to_csv():
	utxt = UnityText("OriginalFile/unnamed asset-resources.assets-1235.dat");
	f = open("localization.csv", "wb");
	csv_writer = csv.writer(f);
	udom = parseString(utxt.get_txt().decode("utf-8").encode("utf-16"));
	root = udom.documentElement;
	rows = root.getElementsByTagName("Text");
	for row in rows:
		id = row.getAttribute("id");
		txt = row.getAttribute("text");
		csv_writer.writerow([txt, "", id]);
	f.close();

def csv_to_raw():
	f = open("localization.new.csv", "rb");
	csv_reader = csv.reader(f);
	dicts = {};
	for row in csv_reader:
		id = row[2];
		cntxt = row[1];
		dicts[id] = cntxt;
	f.close();

	utxt = UnityText("OriginalFile/unnamed asset-resources.assets-1235.dat");
	udom = parseString(utxt.get_txt().decode("utf-8").encode("utf-16"));
	elms = udom.documentElement.getElementsByTagName("Text");
	for elm in elms:
		id = elm.getAttribute("id").encode("utf-8");
		elm.setAttribute("text", dicts[id]);
	
	xmlstr = udom.toxml("utf-16");
	utxt.set_txt(xmlstr.decode("utf-16").encode("utf-8"));
	utxt.save_to_raw("KillTheBadGuy/unnamed asset-resources.assets-1235.dat");

def gen_font_image(bmfc_filepath, output_filepath):
	# Can't add " ", make sure the path have no space.
	bmfont_tool_path = "E:\\BMFont\\bmfont.com";
	text_file_path = "\"Font\\textmin.txt\"";
	bmfc_filepath = "\"" + bmfc_filepath.replace("/", "\\") + "\"";
	output_filepath = "\"" + output_filepath.replace("/", "\\") + "\"";
	commandstr = " ".join((bmfont_tool_path , "-c" ,bmfc_filepath, "-o", output_filepath, "-t" ,text_file_path));
	os.system(commandstr.encode('mbcs'));
	
# Gen text raw
csv_to_raw();

# Font gen
## min text
sh = StringHelper();
sh.add_file_text("localization.new.csv");
sh.add_western();
f = open("Font/textmin.txt", "wb");
f.write(sh.get_chars().decode("utf-8").encode("utf-8-sig"));
f.close();

## gen font
gen_font_image("Font/ArialSmallnoStroke_0-sharedassets0.assets-24.bmfc", "Font/ArialSmallnoStroke_0-sharedassets0.assets-24.fnt");
fontdata = UnityTk2dFontData("OriginalFile/unnamed asset-sharedassets0.assets-1733.dat");
fontdata.read_from_bmfont("Font/ArialSmallnoStroke_0-sharedassets0.assets-24.fnt");
fontdata.save_to_raw("KillTheBadGuy/unnamed asset-sharedassets0.assets-1733.dat");

gen_font_image("Font/ImpactBig_0-sharedassets0.assets-27.bmfc", "Font/ImpactBig_0-sharedassets0.assets-27.fnt");
fontdata = UnityTk2dFontData("OriginalFile/unnamed asset-sharedassets0.assets-1734.dat");
fontdata.read_from_bmfont("Font/ImpactBig_0-sharedassets0.assets-27.fnt");
fontdata.save_to_raw("KillTheBadGuy/unnamed asset-sharedassets0.assets-1734.dat");

gen_font_image("Font/ImpactMedium_0-sharedassets0.assets-25.bmfc", "Font/ImpactMedium_0-sharedassets0.assets-25.fnt");
fontdata = UnityTk2dFontData("OriginalFile/unnamed asset-sharedassets0.assets-1735.dat");
fontdata.read_from_bmfont("Font/ImpactMedium_0-sharedassets0.assets-25.fnt");
fontdata.save_to_raw("KillTheBadGuy/unnamed asset-sharedassets0.assets-1735.dat");

gen_font_image("Font/ImpactSmall_0-sharedassets0.assets-15.bmfc", "Font/ImpactSmall_0-sharedassets0.assets-15.fnt");
fontdata = UnityTk2dFontData("OriginalFile/unnamed asset-sharedassets0.assets-1739.dat");
fontdata.read_from_bmfont("Font/ImpactSmall_0-sharedassets0.assets-15.fnt");
fontdata.save_to_raw("KillTheBadGuy/unnamed asset-sharedassets0.assets-1739.dat");

gen_font_image("Font/ImpactRedWhiteBig_0-sharedassets0.assets-23.bmfc", "Font/ImpactRedWhiteBig_0-sharedassets0.assets-23.fnt");
fontdata = UnityTk2dFontData("OriginalFile/unnamed asset-sharedassets0.assets-1736.dat");
fontdata.read_from_bmfont("Font/ImpactRedWhiteBig_0-sharedassets0.assets-23.fnt");
fontdata.save_to_raw("KillTheBadGuy/unnamed asset-sharedassets0.assets-1736.dat");

gen_font_image("Font/ImpactRedWhiteMedium_0-sharedassets0.assets-26.bmfc", "Font/ImpactRedWhiteMedium_0-sharedassets0.assets-26.fnt");
fontdata = UnityTk2dFontData("OriginalFile/unnamed asset-sharedassets0.assets-1737.dat");
fontdata.read_from_bmfont("Font/ImpactRedWhiteMedium_0-sharedassets0.assets-26.fnt");
fontdata.save_to_raw("KillTheBadGuy/unnamed asset-sharedassets0.assets-1737.dat");

gen_font_image("Font/ImpactRedWhiteSmall_0-sharedassets0.assets-17.bmfc", "Font/ImpactRedWhiteSmall_0-sharedassets0.assets-17.fnt");
fontdata = UnityTk2dFontData("OriginalFile/unnamed asset-sharedassets0.assets-1738.dat");
fontdata.read_from_bmfont("Font/ImpactRedWhiteSmall_0-sharedassets0.assets-17.fnt");
fontdata.save_to_raw("KillTheBadGuy/unnamed asset-sharedassets0.assets-1738.dat");

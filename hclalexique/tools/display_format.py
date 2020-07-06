
format_table={
"TEXT":
    {
    "table":"",
    "/table":"",
    "tr":"",
    "/tr":"\n",
    "td":"",
    "/td":"\t",
    },
"CSV":
    {
    "table":"",
    "/table":"",
    "tr":"",
    "/tr":"\n",
    "td":"",
    "/td":"\t",
    },
"HTML":
    {
    "table":"<html> <body dir='rtl'><table>",
    "/table":"</table></body></html>",
    "tr":"<tr>",
    "/tr":"</tr>",
    "td":"<td>",
    "/td":"</td>",
    },
"XML":
    {

    "table":"<?xml encoding='utf-8'><lexique>",
    "/table":"</lexique></xml>",
    "tr":"<term>",
    "/tr":"</term>",
    "td":"<language>",
    "/td":"</language>",
    },
}
def display_format(table,formatting):
    if not format_table.has_key(formatting):
        frmatting="TEXT";
    start_tag=format_table[formatting]["table"];
    end_tag=format_table[formatting]["/table"];
    start_line_tag=format_table[formatting]["tr"];
    end_line_tag=format_table[formatting]["/tr"];
    start_data_tag=format_table[formatting]["td"];
    end_data_tag=format_table[formatting]["/td"];
    text=""
    text+=start_tag;
    for i in range(len(table)):
        text+=start_line_tag;
        for j in range(len(table[i])):
            text+=start_data_tag;
            text+=table[i][j];
            text+=end_data_tag;
        text+=end_line_tag;
    text+=end_tag;
    return text;
table={
0:{0:'A',1:'B',2:'C'},
1:{0:'X',1:'Y',2:'Z'},
2:{0:'O',1:'I',2:'U'},
}
print display_format(table,"TEXT");
print "-------------------------"
print display_format(table,"XML");
print "-------------------------"
print display_format(table,"HTML");
print "-------------------------"
print display_format(table,"CSV");
